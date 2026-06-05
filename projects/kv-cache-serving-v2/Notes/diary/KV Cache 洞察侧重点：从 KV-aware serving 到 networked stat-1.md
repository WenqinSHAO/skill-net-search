# KV Cache 洞察侧重点：从 KV-aware serving 到 networked state plane

版本：v0.1｜用途：可阅读 PPT / slides 内容底板｜输出形式：Markdown

## 0. 一句话主张

**Take-away.** 我们不再补写一篇 KVCache 分类综述，而是聚焦 KV state plane 的网络化：当 KV 从 engine-internal tensor 变成可寻址、可路由、可传输、可治理的状态对象后，系统要在 `route request to state`、`move state to request`、`compute near state`、`compress state`、`fallback recompute` 之间做实时选择。

% WQ: “KV state plane 的网络化”这个statement太强，而且并不是现实。现实是KV cache serving是一个系统性的事情，很多先有的工作发生在对LLM inference serving软件层面的补充，分布是存储系统上，并不是一个网络有太多接入面的事情。要更中性第去表述。用网络的控制面去介入KV routing，KV cache aware routing只是一个很局部的提议，而不是全景或是我们这篇洞察得出的唯一结论。

这个定位与已有全景综述互补。MiracleFarms 的 KVCache wiki 已经把系统维度、部署维度、工作负载维度和未来方向铺开；我们的差异化应放在网络、控制面、CXL / NDP active memory、以及 agentic workload 下的 KV 状态服务接口。参见 [R1]-[R6]。

```text
KV reuse value ~= p_hit * C_saved
                 - C_store
                 - p_fetch * C_transfer
                 - p_miss * C_fallback
                 - C_control
                 - C_quality
```

网络与器件的价值不是抽象地“更快”，而是让复用收益不被搬运、拷贝、等待、错路由和错误复用吃掉。

## 1. Slides 阅读路径

| Slide | 主题 | 核心信息 | 可视化/材料 |
|---:|---|---|---|
| 1 | Thesis | KV 正在从本地缓存变成 networked state plane。 | 一句话主张 + 公式 |
| 2 | 全景 stack | 已有 stack 图定义 L1-L7 接口。 | llm_serving_stack.png |
| 3 | Request journey | 一次请求如何触发 lookup、compatibility check、route/fetch/recompute、handoff、publish。 | llm_serving_journey.png |
| 4 | Workload radius | 不同 workload 的 KV 复用半径不同，不能用同一种网络/内存策略覆盖。 | 工作负载半径表 |
| 5 | Workload future | Agent、multimodal、reasoning、user private KV 改写典型请求假设。 | 趋势矩阵 |
| 6 | 四个深入点 | A/B/C/D 分别对应 transport、routing/control、active memory、agentic state service。 | 四象限 |
| 7 | A: gap | KV 传输需要 typed object + memory descriptor + completion semantics；传统 byte stream 不够。 | gap 图 |
| 8 | A: current work | Mooncake TE、Dynamo/NIXL、GDS 正在填平 application need 与 substrate 能力的 gap。 | transport ladder |
| 9 | B: current routing | 现在的核心矛盾是 cache affinity vs load balance，不是“网络要不要接管”。 | 当前 routing 表 |
| 10 | B: unmet needs | router 需要新接口：block index、tier location、queue/KV util、path telemetry、tenant policy。 | control API |
| 11 | C: active memory | NDP/CXL/RPU 是计算移位；当 decode IO-bound 时，目标是少搬 KV，而非省 GPU 算力。 | maturity ladder |
| 12 | C: trade-off | active memory 要按 workload 验证 bytes avoided 是否大于同步、编程和质量成本。 | break-even rule |
| 13 | D: agentic state | Agent 不是更长 prompt，而是 task/workflow/state graph。 | agent pattern 表 |
| 14 | D: forward work | KVFlow、Tokencake、Agentix、TokenDance、KVCOMM、Q-KVComm 是早期信号。 | opportunity map |
| 15 | 行动项 | 形成 workload-radius benchmark、KV object ABI、transfer/control prototype、active memory experiment。 | action agenda |

## 2. 全景：已有 stack 与 request journey

**Take-away.** 先从全局系统接口出发，再讨论网络或器件。KV-aware serving stack 的关键不是某个 kernel，而是应用、路由、metadata、reuse engine、KV service、engine、memory/transport 七层之间的契约。

### 2.1 Stack 的读法

观察：L1 应用/Agent runtime 暴露 stable segment、workflow graph、tool stall、privacy label；L2 router/scheduler 在 cache affinity、load balance、SLO、admission 之间取舍；L3 metadata plane 判断 model/tokenizer/RoPE/dtype/tenant/TTL/provenance 是否兼容；L4 reuse engine 决定 prefix hit、chunk reuse、semantic match、repair；L5 external KV service 负责 tiered store 和 transfer orchestration；L6/L7 是 engine 和 model/memory/transport。

趋势：KV 从 L6 engine-local layout 向 L2-L5 的 control/data plane 上移。这个过程让网络、存储和安全都进入 serving critical path。

最新工作回应：vLLM/SGLang 解决 local/radix reuse；LMCache/Mooncake Store 把 KV 外置；Mooncake TE/NIXL/GDS 解决 transfer path；llm-d/DualMap 解决 cache-aware routing；KVShare/SemShareKV/DroidSpeak/Q-KVComm 扩大 reuse contract。

机会：把这些分散接口收敛成可观察、可编排的 KV object ABI：object identity、compatibility metadata、memory descriptor、path class、completion semantics、telemetry span、tenant guardrail。

### 2.2 Request journey 的读法

```text
API request
  -> context plan: stable / dynamic / private / reusable
  -> tokenize + segment + hash
  -> metadata lookup + compatibility check
  -> route-to-state OR fetch state OR prefill missing part
  -> allocate decode pages + handoff KV
  -> decode loop consumes live KV, appends new KV
  -> publish cache events, telemetry, tiering decision
```

网络的入口不是“替模型推理”，而是优化这条 journey 里四类动作：避免 fetch、低拷贝 transfer、批量化碎片 KV movement、向 scheduler 暴露路径与缓存状态。

## 3. Workload：KV 复用半径与未来演进

**Take-away.** KV 策略必须先回答 workload 的 reuse radius。Live decode KV 往往应留在 GPU / NVLink / same-node 半径；prefill handoff 可以跨节点或 rack，因为prefill和decoding在AI infra层面已经有了分化，所以很可能是两个不同的Scale-UP域，attention 和 FFN部分还有可能进一步分化；document / workspace / enterprise memory 可以进入 cluster KV pool；用户私有 KV 和冷文档可以进入更长寿命的 distributed store。

MiracleFarms 把 workload 画像压成四个变量：prefix 复用度、上下文长度、decode 长度、并发模式；五类典型负载在这四个变量上差异很大 [R2]。

| Workload | KV 状态形态 | 合理 reuse / movement radius | 系统影响 | 未来机会 |
|---|---|---|---|---|
| 多轮 Chat | session history + stable system prompt | session / pod / small replica group | session affinity、L2 swap、prefix cache | 用户级 KV 粘性、per-user quota、删除/审计 |
| Agent workflow | tool schema、plan、sub-agent branches、shared task state | workflow / rack / cluster KV pool | task-level scheduling、tool-stall offload、future-use prefetch | Agent cache plan ABI、workflow-aware TTL、KV collectives |
| Coding / long context | repo files、workspace、long stable documents | workspace / local NVMe / cluster store | persistent prefix cache、SP/CP、KV quantization | workspace KV service、incremental file-diff KV |
| RAG / enterprise docs | shared document chunks + dynamic query tail | tenant / document collection / ToR or cluster cache | position-independent chunk reuse、tenant-aware routing | document KV registry、policy-aware reuse |
| Reasoning / Long CoT | short prompt + very long generated KV | HBM / DRAM / same decode pool; avoid WAN per-token path | TPOT dominates、large batch decode pool、swap not recompute | aggressive retention/quantization、preemption redesign |
| Multimodal | image/video/audio token KV, often object-level stable | media object / edge cache / cold store before prefill | video KV explosion、temporal redundancy、cross-request image reuse | modality-specific KV ABI、video sparse KV |
| Multi-model / Multi-LoRA agents | shared backbone state + model/adapter-specific deltas | model family / adapter pool / cluster | compatibility control、selective recomputation | base+delta KV, cross-model state registry |

% WQ: 我觉得上面的分类有点太细了，Agent workflow 和 Coding 和 Reasoning是不是应该和起来；还有RAG本就是 Agent workflow的一部分；要看看那其他workload，比如Generative recommendation，文本的结构抽取等，有别于通用Agent的，或在那个基础上特化的；多模态有点太粗糙了，现在用于影视生产的工作流很多，是个什么样子，哪些素材是要大量复用的，对KV cache是个什么要求？

未来演进的关键是三条线：Agent 把 KV 从线性 session 变成 task/workflow 树；reasoning 把瓶颈从 TTFT 推向 long-decode TPOT；用户私有 KV 把 cache 变成数据资产，带来隔离、配额、计费和生命周期管理 [R4]。

```text
KV reuse radius rule of thumb

live decode token path       -> HBM / NVLink / same node
prefill-to-decode handoff    -> same rack / cluster, direct memory path
warm prefix / doc / workspace -> rack or cluster KV pool
cold document / user memory   -> distributed store, fetched before prefill
cross-region reuse            -> only for high-value long context, not token-by-token decode
```

## 4. 我们要深入的四个点

**Take-away.** 四个深入点不是并列技术清单，而是从同一个系统问题分解出来：当 KV 成为可寻址状态，系统如何选择 locality、movement、computation placement、workflow-level sharing。

| 深入点 | 系统问题 | 为什么现在重要 | 产出形式 |
|---|---|---|---|
| A. KV-aware multi-substrate transport | 应用层 KV movement 需要 typed object / scatter-gather / direct memory / completion semantics，传统网络只给 byte stream。 | Mooncake TE、NIXL、GDS、TensorRT-LLM disaggregated serving 已经把这个 gap 产品化。 | 介绍性 + 架构图 + transfer plan model |
| B. KV routing and control interface | 分布式 serving 要在 cache hit、load、SLO、tenant fairness、stale index 之间取舍。 | llm-d、SGLang Router、Mooncake scheduler、DualMap 说明 router 已成为 KV control point。 | 需求分析 + 最小接口草案 |
| C. Active KV memory with CXL/NDP/RPU | 当 KV 读写/传输成为瓶颈，计算可以向内存侧移动，以少搬数据为目标。 | CXL pool、Beluga、TraCT、CXL-NDP、CXL-RPU/PNM 给出从成熟到激进的路线。 | maturity ladder + workload trade-off |
| D. Agentic KV state service | Agent 把 KV 从 request-local cache 变成 workflow state、shared memory、collective state、甚至通信对象。 | KVFlow、Tokencake、Agentix、TokenDance、KVCOMM、Q-KVComm 已经出现早期形态。 | workload pattern -> opportunity map |

## 5. A. KV-aware multi-substrate transport

**Take-away.** KV transfer 不是普通 RPC。它是带模型语义、位置语义和内存布局语义的状态移动；方向相对确定：需要 unified transfer abstraction，把碎片化 KV page 编译成跨 NVLink / RDMA / TCP / CXL / NVMe-oF / GDS 的 transfer plan。

### 5.1 观察：应用层需求与网络能力有 gap

KV movement 的应用层需求包括：

- 传输对象不是 byte stream，而是 layer/head/page/token-range 组成的 typed KV block。
- 目标通常不是“远端进程收到消息”，而是“写入 decode worker 已分配的 GPU memory page”。
- 传输要与 prefill/decode SLO、continuous batching、GPU forward、eviction/prefetch overlap。
- KV 可能在 HBM、CPU DRAM、NVMe、NVMe-oF、remote DRAM、object store 之间流动。
- 正确性依赖 model id、tokenizer、RoPE offset、layout、dtype、quantization、tenant、TTL。

传统网络/存储接口通常只暴露连接、byte stream、block device 或 RPC completion；它们不理解 KV object identity、memory descriptor、tier cost、reuse confidence、cache invalidation。

```text
application need
  KV object + page list + target memory descriptor + SLO + compatibility

network/storage substrate
  byte stream / RDMA queue pair / file / block device / object

gap
  scatter-gather plan, zero-copy path, topology-aware choice, completion semantics, telemetry
```

### 5.2 趋势：transfer engine 从“调用网络”变成“编排状态移动”

Mooncake Transfer Engine 的 Segment / BatchTransfer 抽象是当前最清楚的方向之一。Segment 把 DRAM/VRAM/NVMe-oF 等连续地址空间抽象成可远程读写对象；BatchTransfer 把一组不连续源/目的地址编译成批量 read/write；底层可以选择 TCP、RDMA、GPUDirect RDMA、NVMe-oF 等路径 [R7][R8]。Dynamo/NIXL 则把 prefill engine 的 VRAM 直接传到 decode engine 的 VRAM，并且 transfer non-blocking [R9]。GDS 把 storage 到 GPU 的路径绕开 CPU bounce buffer [R11]。

### 5.3 最新工作如何回应

| 工作 | 回应的 gap | 系统意义 |
|---|---|---|
| CacheGen | KV 作为 network payload 过大，带宽受限。 | 压缩/streaming 让跨网络复用有可行性。 |
| Mooncake TE | 多 tier、多 backend、多碎片 KV movement 难以由上层手写。 | Segment + BatchTransfer 把 KV movement 变成 transfer plan。 |
| Dynamo / NIXL | PD handoff 不应经过 CPU bounce path。 | prefill VRAM -> decode VRAM direct, non-blocking transfer。 |
| GDS / cuFile | 低层存储便宜但恢复路径可能拖垮 CPU/PCIe。 | storage -> GPU direct DMA，降低 copies 和 jitter。 |
| TensorRT-LLM disaggregated serving | layout mismatch、backend 多样、全局 request id / metadata。 | 说明 transfer path 已进入 engine-level contract。 |

### 5.4 机会

- **KV transfer compiler**：输入 KV block list、memory descriptors、topology、SLO、tier pressure；输出 batched transfer plan。
- **Topology-aware path selection**：在多 socket、多 GPU、多 RDMA NIC、多 PCIe switch 中选择路径，不假设“任意 NIC 都一样”。
- **Multi-substrate striping / fallback**：对 large KV object 在 RDMA、CXL、NVMe-oF、TCP 中分层和容错。
- **Transfer telemetry ABI**：每次 KV fetch/handoff 形成 span，反馈到 routing/admission。
- **跨 scale-up / scale-out bridge**：在线 decode KV 尽量不跨远端；prefill handoff、warm prefix、document KV、agent shared state 可跨 node/rack/cluster。

## 6. B. KV routing and control interface

**Take-away.** 不能一开始就说“网络控制面参与 KV routing”。更稳妥的论证是：当前 route-to-state 已经发生；它的核心矛盾是 cache affinity vs load balance；现有接口无法充分表达 freshness、tier、path、tenant、future reuse；网络与传输控制面可以提供状态可见性和路径执行能力，但不应替代 serving scheduler 的语义决策。

### 6.1 观察：现在怎么做

当前 KV-aware routing 大致分四层：

1. **Random / round-robin**：负载平均，但 distributed prefix hit 被打散。
2. **Session affinity / consistent hash**：保留局部性，但热门 prefix 或长 session 会形成热点。
3. **Prefix-tree / token-level routing**：router 维护 prefix tree 或 block hash，向已有 KV 的副本路由。
4. **Precise per-pod KV index**：llm-d 让 vLLM pod 发布 KV-cache events，scheduler 以 block hash 建索引，并按 incoming prefix 的 resident fraction 评分，同时结合 load-aware stack [R10]。

MiracleFarms routing 章节把这个问题概括成：多副本部署里，路由不再只是 LB，而是最大化 prefix hit 与避免热点之间的折中 [R5]。

### 6.2 需求：什么还没被满足

| 未满足需求 | 为什么普通 LB 不够 | 需要的新状态 |
|---|---|---|
| hit-rate vs load 的连续权衡 | 请求不能只看目标 pod 是否有 cache，也要看队列、KV util、SLO。 | resident block fraction, queue length, KV occupancy, decode backlog |
| index freshness | KV cache events 可能滞后；错路由可能比重算更差。 | event timestamp, confidence, invalidation epoch |
| tier-aware decision | HBM hit、DRAM hit、NVMe hit、remote hit 不是同一种 hit。 | tier location, estimated restore latency, path class |
| tenant fairness / isolation | 共享 cache 池会让大租户挤占小租户或泄露状态。 | tenant quota, sharing policy, provenance |
| route vs fetch vs recompute | 有 cache 不一定 route；远端 fetch 或局部 recompute 可能更便宜。 | transfer estimate, recompute estimate, quality/fallback policy |
| hot prefix replication | 热门 system prompt 会把所有请求吸到少数副本。 | hotness counters, replication budget, admission trigger |

### 6.3 网络/控制面能做什么

网络的定位应是 **KV-aware control substrate**，而不是“网络替代 scheduler”。它可以提供：

- **KV location visibility**：把 object/block location、tier、freshness、path availability 暴露给 scheduler。
- **Path actuation**：按 policy 选择 RDMA/NVMe-oF/CXL/TCP/GDS backend，建立或复用 memory registration。
- **Telemetry**：per-object/per-flow/per-transfer latency、congestion、queue、drop、retry。
- **In-network or near-ToR metadata service**：做 lookup、admission、replication hint、tenant guardrail；不是把完整 KV tensor 塞进交换芯片 SRAM。
- **Completion semantics**：让 decode engine 知道哪些 pages 已安全到达，可以开始消费。

### 6.4 最小控制接口草案

```text
App/runtime -> serving control
  stable_segments, dynamic_tail, privacy_label, SLO, future_reuse_hint

Engine/KV service -> router
  block_hash, model_id, layer_layout, tier_location, resident_fraction,
  queue_length, KV_utilization, eviction_pressure, timestamp

Network/transport -> router
  path_class, available_bandwidth, latency_estimate, registration_state,
  completion_mode, congestion_signal

Router -> action
  route_to_state | fetch_state | replicate_hot_prefix | admit_prefill | recompute | reject_reuse
```

机会：把 llm-d 的 precise routing、Mooncake 的 global cache/scheduler、Dynamo/NIXL 的 memory descriptor 和 OpenTelemetry 式 KV trace 收敛成一个可测试的 routing/control benchmark。

## 7. C. Active KV memory with CXL / NDP / RPU

**Take-away.** CXL/NDP/RPU 的本质不是“把 GPU 计算 offload 到别处”这么简单，而是把一部分计算移到数据旁边。如果 decode 或 long-context retrieval 的瓶颈是 KV IO / bandwidth / restore path，那么 near-memory compute 的主要收益是减少被搬运的 bytes 和同步等待，而不是节省 GPU FLOPS。

### 7.1 观察：先问瓶颈在哪里

| 场景 | 主要瓶颈 | Active memory 是否有意义 |
|---|---|---|
| 短 chat + 小 context | prefill/queue/服务端 overhead | 弱；HBM 内本地执行更直接。 |
| 长 context + offload | 从 DRAM/NVMe/CXL 取回 KV 的带宽和延迟 | 强；token/page selection、compression、prefetch 可减少移动。 |
| reasoning long decode | TPOT、长寿命 KV、抢占/恢复成本 | 中到强；目标是保留/压缩/选择长期 KV，不是加速一次 GEMM。 |
| video / multimodal KV | token 爆炸、时间冗余、对象级复用 | 强；近数据压缩与关键帧选择有空间。 |
| cross-node PD handoff | KV transfer latency / network contention | 中；CXL rack-scale pool 可替代一部分 RDMA hop，但受域范围限制。 |

### 7.2 成熟度阶梯：从保守到激进

| 阶段 | 形态 | 代表工作/信号 | 系统含义 |
|---:|---|---|---|
| 0 | Passive tiering: HBM / DRAM / NVMe / remote store | vLLM offload, LMCache, Mooncake Store, HiFC | 先把 KV 放得下，问题是 restore path。 |
| 1 | Direct path / zero-copy transfer | NIXL, GPUDirect RDMA, GDS, Mooncake TE | 减少 CPU bounce 和拷贝链路。 |
| 2 | CXL shared memory capacity pool | Beluga, TraCT, CXL storage explorations | 用 memory semantics 降低 RDMA pool 的协议和同步成本 [R14][R15]。 |
| 3 | Transparent in-device compression / bit-plane layout | CXL-NDP | 不改应用接口，提升有效 CXL bandwidth [R16]。 |
| 4 | Token/page selection near memory | zettA CXL-RPU, CXL-PNM | 在 CXL memory module/PNM 内做选择，减少召回到 GPU 的 KV pages [R17][R18]。 |
| 5 | Full near-data attention / active KV appliance | 更激进研究方向 | 只有在数据搬运节省显著大于同步/编程成本时成立。 |

### 7.3 Trade-off

```text
active_memory_value ~= bytes_not_moved * path_cost
                      - near_memory_compute_latency
                      - synchronization_consistency_cost
                      - precision_or_quality_risk
                      - programmability_debug_cost
                      - deployment_capex_and_operational_risk
```

如果 workload 的 bottleneck 是 GPU matrix compute，NDP/RPU 未必有效；如果 bottleneck 是 KV restore bandwidth、PCIe、RDMA hop、NVMe bounce、长 decode 的 KV 读放大，那么 active memory 才是系统级优化。

机会：

- **Selection-in-memory**：在 CXL/RPU 做 token/page selection，只把有效 KV pages 搬到 GPU。
- **Compression-in-memory**：在 device-side 做 bit-plane / lossless / low-bit decode，减少 CXL/DRAM bytes。
- **Prefetch-in-memory**：根据 decode progress 或 workflow graph 提前准备 hot pages。
- **CXL + network node 结合**：ToR-attached CXL memory service 既是 memory tier，也是 placement / telemetry endpoint。
- **Benchmark**：必须按 workload 分组评估；不能只报 microbenchmark bandwidth。

## 8. D. Agentic KV state service（名字暂定）

**Take-away.** “Agentic KV collectives” 是一个重要机制，但题目可以更宽：Agentic KV state service。Agent 服务会把 KV 从 request-local cache 推向 workflow-scoped、tenant-scoped、user-scoped、model-family-scoped 的状态服务。Collective sharing、workflow-aware eviction、tool-stall offload、cross-context correction、representation exchange 都是这个服务里的机制。

% WQ: 其实是Agentic App的构成和框架与KV cache serving之间的一个协同关系，应用设计的时候要考虑到复用的模式，KV cache serving提供相应的适配和接口

### 8.1 观察：Agent 应用的 KV 特点

| Agent 场景 | KV 特点 | 系统需求 |
|---|---|---|
| 超高吞吐简单 Agent | 大量重复 system prompt、tool schema、skill/workflow definition；decode 可能短。 | 强 prefix/radix reuse、cache-aware routing、批量化 prefill。 |
| 多 Agent 集群化作业 | 多 agent 同步 round、all-gather shared output、fork/merge 分支。 | collective KV sharing、diff-aware storage、round-aware prompt interface。 |
| 企业 Agent / 文档与记忆共享 | 组织知识库、权限标签、用户私有 memory、跨 session 长寿命。 | tenant/user-scoped KV、policy-aware reuse、quota/billing/lifecycle。 |
| Coding / research Agent | workspace 文件稳定，工具调用频繁，长任务持续数小时。 | workspace KV service、tool-stall offload、incremental file diff。 |
| Reasoning Agent | long decode、低 prefix reuse、高 TPOT 压力。 | dedicated decode pool、aggressive retention/quantization、swap-not-recompute。 |
| Multi-model / Multi-LoRA Agent | 共享 backbone，但 adapter / fine-tune 不同；同一上下文被多个角色消费。 | base+delta KV、selective recompute、compatibility ABI。 |

% WQ: 超高吞吐简单 Agent， 不一定是简单Agent，如果claude code用claude自己的模型和AI Infra，比用DeepSeek这样的第三方LLM API，推理吞吐高十倍，那用户可能愿意用超过十倍的钱去购买这样的服务，形成溢价，Agent越是复杂交互越是多，收益反而越明显；coding 和 reasoning似乎没有必要拆开来，感觉和之前的## 3. Workload：KV 复用半径与未来演进有点重复的感觉。另外可以考虑一下，把文档预计算成KV的服务来加速推理或是提高推理质量，KG2KV等

### 8.2 趋势：从 request scheduling 到 workflow/state scheduling

MiracleFarms future workload 页面指出，Agent 把请求假设从独立 request-response 改写成持续数分钟到数小时的 task；KV 从秒级线性结构变成分钟/小时级树状结构；调度单元从 batch 变成 task/workflow [R4]。这与 Agentix 把 agentic program 抽象成动态 DAG 的方向一致 [R22]。

### 8.3 最新工作如何回应

| 工作 | 观察到的 agentic KV 问题 | 回应方式 |
|---|---|---|
| KVFlow | LRU 不理解未来 agent step，常在复用前驱逐。 | Agent Step Graph + steps-to-execution + overlapped prefetch [R20]。 |
| Tokencake | tool call stall 让 KV 占着 GPU memory 但不被使用；关键 agent 又会被挤掉。 | Space Scheduler + Time Scheduler，把 stalled time 纳入 KV 管理 [R21]。 |
| Agentix / Autellix | serving 系统忽略 agent program/call 之间依赖。 | 把 agentic program 作为 DAG 调度，利用依赖与统计信息 [R22]。 |
| TokenDance | 多 agent synchronized rounds 产生 All-Gather 式 shared output KV redundancy。 | collective KV sharing + diff-aware storage；共享 block 成本按 round 支付一次 [R19]。 |
| KVCOMM | 共享内容在不同 agent prefix 下有 offset variance。 | anchors 估计/修正 shared content 的 KV offset [R23]。 |
| DroidSpeak / LRAgent | 多模型/多 LoRA 角色重复处理相同上下文。 | selective recompute 或 base+delta KV sharing [R25][R26]。 |
| Q-KVComm | Agent 互传 raw text 会让接收方重算内部表示。 | 传输 compressed KV representation，探索 communication-layer reuse [R24]。 |

### 8.4 机会

- **Agent cache plan ABI**：agent runtime 输出 stable/private/shared/dynamic segments、tool-stall window、future reuse hint、approximation tolerance。
- **Workflow-scoped KV service**：KV 的生命周期跟 task graph，而不是单次 request。
- **KV collectives**：broadcast、all-gather、fork、merge、reduce-diff 等 agent-native KV operations。
- **Enterprise memory service**：组织文档、用户私有记忆、权限与计费绑定到 KV object policy。
- **Cross-model compatibility registry**：记录哪些模型/LoRA/adapter 可以 exact reuse、approximate reuse、selective recompute 或禁止 reuse。
- **Agent benchmark**：不能只测 single-agent latency；要测 task-level goodput、KV occupancy over time、tool-stall utilization、policy violation。

## 9. 总结：趋势与行动项

**Take-away.** 下一阶段值得把握的机会，不是再整理“KVCache 有哪些算法”，而是把 KV 作为状态服务来定义可落地的接口、benchmark、prototype。

### 9.1 趋势判断

1. **KV object ABI 会成为关键接口。** 没有 model/layout/position/dtype/tenant/provenance，跨引擎、跨节点、跨模型 reuse 都会脆弱。
2. **Workload radius 决定系统半径。** 短 chat、long context、reasoning、agent、RAG、multimodal 对 KV locality 的要求不同。
3. **Transport 会从 backend selection 走向 transfer planning。** KV fragments 需要被编译成 batched movement plan。
4. **Routing 会从 load balancer 变成 state-aware scheduler client。** 但语义决策仍要由 serving control plane 主导。
5. **CXL/NDP/RPU 的价值在少搬数据。** 先用 workload 证明 IO-bound，再决定 offload 什么计算。
6. **Agent 会推动 KV 从 cache 变成 state service。** Workflow、tenant、user、model-family 都会成为 KV 生命周期边界。

### 9.2 建议行动

| 行动 | 目标产物 | 判断标准 |
|---|---|---|
| 定义 workload-radius benchmark | 按 chat / agent / coding / RAG / reasoning / multimodal 分组的 KV trace schema | 每类 workload 能明确合理 KV 半径和关键指标。 |
| 起草 KV object ABI v0 | metadata + memory descriptor + policy + telemetry 字段 | 能支持 route/fetch/recompute/reject 四类动作。 |
| 构建 transfer-plan model | KV block list -> substrate/path plan 的模型或模拟器 | 能解释 Mooncake TE/NIXL/GDS 组合下何时受益。 |
| 路由控制原型 | 基于 llm-d/Mooncake-style event index 的 route-to-state simulator | 能量化 hit-rate、hotspot、load、SLO trade-off。 |
| Active memory 实验设计 | CXL/NDP/RPU maturity ladder + workload fit matrix | 能避免“为了 offload 而 offload”的错误叙事。 |
| Agentic KV state service 草案 | cache plan ABI + workflow-scoped KV lifecycle + collectives | 能覆盖 TokenDance/KVFlow/Tokencake/Agentix 等信号。 |

## 10. References for follow-up reading

- [R1] MiracleFarms KVCache future overview. https://miraclefarms.github.io/wiki/kvcache/future/
- [R2] MiracleFarms KVCache workload overview. https://miraclefarms.github.io/wiki/kvcache/workloads/
- [R3] MiracleFarms KVCache future system. https://miraclefarms.github.io/wiki/kvcache/future-system/
- [R4] MiracleFarms KVCache future workload evolution. https://miraclefarms.github.io/wiki/kvcache/future-workloads/
- [R5] MiracleFarms KVCache routing and affinity. https://miraclefarms.github.io/wiki/kvcache/routing/
- [R6] MiracleFarms KVCache storage hierarchy. https://miraclefarms.github.io/wiki/kvcache/storage-hierarchy/
- [R7] Mooncake Transfer Engine documentation. https://kvcache-ai.github.io/Mooncake/design/transfer-engine/index.html
- [R8] Mooncake GitHub overview. https://github.com/kvcache-ai/Mooncake
- [R9] NVIDIA Dynamo disaggregated serving documentation. https://docs.dynamo.nvidia.com/dynamo/design-docs/disaggregated-serving
- [R10] llm-d precise prefix-cache aware routing guide. https://github.com/llm-d/llm-d/tree/main/guides/precise-prefix-cache-aware
- [R11] NVIDIA GPUDirect Storage technical blog. https://developer.nvidia.com/blog/gpudirect-storage/
- [R12] KVCache Cache in the Wild. https://arxiv.org/abs/2506.02634
- [R13] ServeGen workload characterization. https://arxiv.org/abs/2505.09999
- [R14] Beluga: CXL-based KVCache management. https://arxiv.org/abs/2511.20172
- [R15] TraCT: CXL shared memory KV cache at rack-scale. https://arxiv.org/abs/2512.18194
- [R16] CXL-NDP for LLM inference. https://arxiv.org/html/2509.03377v1
- [R17] zettA.AI zettEngine CXL-RPU pitch deck. https://zettai.us/ZettEngine_CXL_PitchDeck_v1.pdf
- [R18] CXL-enabled PNM for 1M-token LLM inference. https://arxiv.org/abs/2511.00321
- [R19] TokenDance: collective KV sharing for multi-agent serving. https://arxiv.org/abs/2604.03143
- [R20] KVFlow: workflow-aware prefix caching. https://arxiv.org/abs/2507.07400
- [R21] Tokencake: KV-centric multi-agent serving. https://arxiv.org/abs/2510.18586
- [R22] Agentix / Autellix: serving LLM agents as programs. https://arxiv.org/abs/2502.13965
- [R23] KVCOMM: cross-context KV-cache communication. https://arxiv.org/abs/2510.12872
- [R24] Q-KVComm: adaptive KV-cache compression for multi-agent communication. https://arxiv.org/abs/2512.17914
- [R25] DroidSpeak: KV cache sharing across fine-tuned variants. https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/
- [R26] LRAgent: KV cache sharing for multi-LoRA agents. https://arxiv.org/abs/2602.01053
- [R27] TensorRT-LLM disaggregated serving documentation. https://nvidia.github.io/TensorRT-LLM/advanced/disaggregated-service.html
- [R28] CacheGen: KV cache compression and streaming. https://arxiv.org/abs/2310.07240