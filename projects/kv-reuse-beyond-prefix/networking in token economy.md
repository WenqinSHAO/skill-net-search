# Token 经济学里，网络的一席之地

Model as a Service 正在进入更接近云计算的竞争状态：模型能力会扩散，开源模型会被多家同时服务，API 层面的差异化会逐渐落到单位 token 成本、TTFT、TPOT 和稳定性上。即使一家厂商有自研模型优势，serving margin 仍然取决于token成本。

KV reuse的帐大致可以算成KV的复用率/价值减去其传输，存储和额外调度的成本。

```text
net_value ~= p_hit * C_saved
            - C_store
            - p_fetch * C_transfer
            - p_miss * C_fallback
            - C_control
            - C_quality
```

这里短期变化最大的不是某个单点优化，而是两个系统性变量。

第一，agent 应用与 context engineering 正在抬高 `p_hit` 和 `C_saved`。传统 prefix caching 依赖相同前缀；agent workload 里更常见的是稳定但分散的上下文：system prompt、tool schema、skill定义的工作流，中间 plan，等。它们未必构成完整前缀，却经常重复出现，本身就具有高cache价值。命中率提高，单次命中省下的 prefill 也更大，因为 agent trace 往往更长，且同一段上下文可能被多个后续调用消费。

```text
agent/context engineering
        |
        v
stable segment 更清楚
(system prompt / schema / doc / plan / memory)
        |
        +--> p_hit 上升
        +--> C_saved 上升
        +--> C_control 下降一部分：少靠盲目相似度搜索
```

第二，serving 软件正在降低 `C_store`、`C_transfer` 和 `C_control`。比如Mooncake已经支持在GPU HBM、CPU DRAM、SSD、远端存储上调度KV。

```text
local KV              external KV layer             KV state plane
---------             -----------------             -----------------------
vLLM block/page  -->   LMCache / HCache      -->     router + metadata
GPU-local mgmt         engine 外复用                 tiered store + transfer
C_control↓             C_store 可分层                C_transfer 可优化
```

网络社区也已经开始尝试进一步降低C_transfer。今年3月IETF/IRTF 讨论有“KV-centric networking at scale”的提案。曾经的ICN领军人物Zhang LiXia老师试图把In-network cache的概念用于KV serving。

网络在这里的入口，首先是命名与定位/routing。KV block 如果只是某个进程里的匿名 tensor，网络只能搬字节；如果它带有 model id、tokenizer、layer/head layout、RoPE offset、等元数据，调度器和数据面就能判断：请求应该送到状态附近，还是状态应该搬到请求附近；应该走 HBM、DRAM、NVMe，还是远端存储；应该直接复用，还是选择性重算。IPv6和SRv6可能都会有用武之地。

```text
KV object metadata
--------------------------------------------------
model / tokenizer / layer layout / block size
position / RoPE offset / dtype / compression
tenant / TTL / provenance / reuse confidence
--------------------------------------------------
        |
        +--> route request to KV
        +--> move KV to request
        +--> recompute only repair part
        +--> reject unsafe reuse
```

第一个已经发生的例子是 **route-to-state**。llm-d 的 precise prefix-cache-aware routing 不再按粗粒度请求流量猜测 locality。每个 vLLM pod 通过 ZMQ 发布 KV-cache events，scheduler 建立以 block hash 为键的索引，并按 incoming request prefix 已经驻留在候选 pod 上的比例打分；同时再结合 queue size 和 KV utilization 做 load-aware 平衡。这样做的收益是：请求被送到已有 prefix/KV 的实例，避免跨节点 fetch，也避免重新 prefill。这里网络接口减少 data movement 的方式不是优化一次 transfer，而是让 transfer 根本不发生。([llm-d][1])

```text
request prefix
     |
     v
scheduler 查询 per-pod KV block index
     |
     +--> pod A: 20% resident
     +--> pod B: 85% resident  ---> route to B
     +--> pod C: overloaded
```

第二个例子是 **phase-disaggregation 的 direct memory path**。prefill 和 decode 的资源形态不同：prefill 偏 compute-bound，decode 偏 memory-bound。Dynamo/SGLang disaggregation 的流程里，decode worker 先分配接收 KV 的 GPU memory page，并把 RDMA connection information 和 base GPU memory pointer 注册给 prefill worker；prefill 完成 prompt processing 后，通过 RDMA 直接把 KV 写入 decode 的 GPU memory，decode 侧轮询完成并继续生成 token。文档明确把它描述为 zero-copy GPU-to-GPU transfer，CPU 只少量参与，RDMA connection 一次建立、请求间复用。([NVIDIA Docs][2])

这类接口减少的是整条搬运链路：

```text
低效路径:
prefill GPU -> host DRAM -> network -> host DRAM -> decode GPU

direct path:
prefill GPU -> RDMA/NIXL/Mooncake -> decode GPU
```

Dynamo 的设计文档还强调，高性能 disaggregation 的关键是 efficient KV transfer；NIXL 可以把 KV 从 prefill engine 的 VRAM 直接传到 decode engine 的 VRAM，且 transfer non-blocking，GPU forward pass 可以继续处理其他请求。PrefillRouter 负责选择 prefill worker、注入 transfer metadata、把请求路由到 decode worker，再由 decode worker 用这些 metadata 协调直接传输。([NVIDIA Docs][3]) 这说明网络接口已经不只是“RPC 调用”，而是 serving scheduler、memory descriptor、transport backend 共同定义的状态交接协议。

第三个例子是 **unified transfer abstraction**。Mooncake Transfer Engine 把数据移动抽象成两个核心对象：Segment 与 BatchTransfer。Segment 表示可远程读写的连续地址空间，可以是 DRAM/VRAM 这类 RAM Segment，也可以是 NVMe-oF 提供的持久化 Segment；BatchTransfer 负责在一组不连续地址空间之间做双向 read/write，同步形式类似更灵活的异步 AllScatter/AllGather。它支持 TCP、RDMA、EFA、NVMe-oF、NVLink、IntraNodeNvlink、HIP 等 backend，并能让 DRAM/VRAM/NVMe-oF 之间的读写走不同路径。([kvcache-ai.github.io][4])

这类 abstraction 对 KV 很关键，因为 KV block 天然碎片化：不同 layer、不同 head、不同 token range、不同 cache page 可能分散在多个地址区间。没有 batch/scatter-gather 接口，上层会把大量小块搬运变成大量小 RPC 或小 memcpy；有了 BatchTransfer，runtime 可以把碎片化 KV movement 合并成更大的传输计划，再由底层按 topology 和 transport 选择路径。Mooncake 文档还提到 topology-aware path selection：多 socket、多 GPU、多 RDMA NIC 的服务器里，任意 NIC 都能传不等于每条路径都好，UPI 或 PCIe switch 可能成为瓶颈；传输层需要感知拓扑。([kvcache-ai.github.io][4])

```text
KV blocks:
[L0,H0,page3] [L4,H2,page9] [L8,H1,page1] ...

without batching:
many small copies / RPCs / syncs

with BatchTransfer:
one transfer plan
  -> RDMA path for remote DRAM/VRAM
  -> NVLink path for intra-node GPU
  -> NVMe-oF/cuFile path for storage tier
  -> topology-aware NIC choice
```

第四个例子是 **storage-to-GPU bypass**。GPUDirect Storage 的原则非常适合解释 KV tiering 的网络/存储机会：数据从本地或远端 storage 直接 DMA 到 GPU memory，避免 CPU bounce buffer。NVIDIA 文档说明，GDS 的 direct DMA path 可以提高带宽、降低延迟、降低 CPU/GPU utilization load；bounce buffer 路径需要先把数据 copy 到 CPU 临时缓冲，再 copy 到目标设备，而 direct path 只有一次 source-to-target copy。([NVIDIA Docs][5])

这对 KV serving 的意义是：当 KV 被放到 SSD、NVMe-oF 或远端存储层时，存储本身便宜不等于系统便宜；真正决定收益的是 restore path 是否会把 CPU memory、PCIe、NIC、GPU synchronization 全部拖进关键路径。HiFC 这类 flash-based KV tier、Mooncake 的 NVMe-oF Segment、GDS/cuFile 这类 direct path，都在回答同一个问题：低层存储能不能用足容量优势，同时不让 transfer cost 抵消 saved prefill。Mooncake Transfer Engine 也明确支持 NVMe-oF 到 DRAM/VRAM 的直接传输，绕过 CPU，实现 zero-copy。([kvcache-ai.github.io][4])

```text
cheap storage alone:
SSD/NVMe -> CPU bounce -> GPU
          latency + jitter + CPU bandwidth

KV-aware storage path:
SSD/NVMe-oF -> DMA/cuFile/RDMA -> GPU/DRAM target
              fewer copies + explicit placement
```

第五个机会是 **placement 与 in-network cache 的结合**。IRTF/ICN 视角值得放在这里：KV 的命名、寻址、信任和 delegation 做好以后，cache placement 不必完全由中心化 scheduler 预先规划。请求携带对某类 KV object 的需求，网络/边缘 cache/ToR-attached storage service 可以根据名称、热度、tenant policy 和 locality 做 request-driven placement。这里的“in-network cache”更像 ToR 附近的 memory/storage service 加上一套网络可见接口，而不是把完整 KV tensor 塞进交换芯片 SRAM。交换机或 DPU 更适合做 metadata lookup、routing hint、admission、telemetry、copy avoidance、RDMA/NVMe-oF path coordination。

```text
request: need KV(name=X, model=M, tenant=T)
        |
        v
network-visible KV index / cache service
        |
        +--> hit near ToR: serve locally
        +--> hit remote rack: route/fetch by policy
        +--> miss: recompute and publish metadata
```

这正是 networking systems 熟悉的地盘：FastClick/VPP 式的数据面流水线、RDMA memory registration、zero-copy buffer management、multi-path transport、topology-aware scheduling、NIC/DPU offload、per-flow/per-object telemetry。KV serving 给这些技术一个新的对象模型：packet 之外，还有 KV block、segment、cache page、transfer batch、reuse metadata。网络协议如果只暴露 byte stream，serving 层只能在应用里反复 copy 和重试；协议如果暴露 memory region、object identity、placement hint 和 completion semantics，runtime 就能把 KV movement 编排成可优化的数据面。

最终的定位可以更直接地写成：Token 经济学里的网络价值，是把 KV 从“可搬运的字节”升级成“可寻址的KV block”。route-to-state 降低 `p_fetch`，direct memory path 降低 `C_transfer`，batch transfer 降低碎片化搬运的 `C_control`，storage bypass 降低从低吞吐/低层存储恢复时的 copy 和 jitter，naming/addressing 让 placement 可以从静态规划走向 request-driven。KV reuse 的收益来自少算；网络系统的任务，是让少算之后的收益不被多搬、多拷贝、多等待挥霍掉。

[1]: https://llm-d.ai/docs/guide/Installation/precise-prefix-cache-aware?utm_source=chatgpt.com "Precise Prefix Cache Aware Routing | llm-d"
[2]: https://docs.nvidia.com/dynamo/dev/backends/sg-lang/disaggregation?utm_source=chatgpt.com "Disaggregation | NVIDIA Dynamo Documentation"
[3]: https://docs.nvidia.com/dynamo/design-docs/disaggregated-serving?utm_source=chatgpt.com "Disaggregated Serving | NVIDIA Dynamo Documentation"
[4]: https://kvcache-ai.github.io/Mooncake/design/transfer-engine/index.html?utm_source=chatgpt.com "Transfer Engine — Mooncake"
[5]: https://docs.nvidia.com/gpudirect-storage/design-guide/?utm_source=chatgpt.com "1. Design Guide — GPUDirect Storage Design Guide"
