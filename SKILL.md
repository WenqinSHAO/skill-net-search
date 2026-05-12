---
name: net-research
description: >
  This skill is used to search, curate, and analyze academic papers for ongoing
  research projects. It maintains a shared local paper database and helps grow
  project-specific insight spaces through per-paper notes and cross-paper
  synthesis. Triggers include: "搜索某方向论文"、"整理一个研究项目"、
  "补充论文数据库"、"做跨论文分析"、"写 insight report" 等。
---

# Net-Research

## Skill Goal

本技能服务两个层次的工作：

1. **共享层（shared layer）**：维护一个可信、可复用、可持续扩充的本地论文数据库。
2. **项目层（project layer）**：围绕某个明确的研究目标，逐步形成论文范围、单篇解读和跨论文洞察。

核心原则不是“一次性生成完整报告”，而是让项目随着使用自然沉淀。

---

## Core Contract

### 1. Shared layer stores facts

共享层位于：

- `papers/`
- `index/`

这里只保存**稳定事实**：

- 论文元数据
- 论文来源链接
- abstract
- 中性、可复用的结构化摘要

**不得写入**：

- 面向某个项目的选题理由
- 与其他论文的比较性判断
- “这篇论文为什么对项目 X 重要”这类项目上下文

### 2. Project layer stores interpretation

项目层位于：

- `projects/{project-name}/`

这里保存**项目相关解释**：

- 项目意图与边界
- 关心哪些论文，以及为什么关心
- 每篇论文与本项目的关系
- 跨论文比较、分类、演进脉络、研究空白

### 3. Shared papers are canonical, projects are disposable

共享层应长期稳定积累；项目层可以重写、重组、重新开题。

如果项目结构已经混乱，优先保留有价值的论文范围和洞察，再在新的项目空间中重建，而不是强行在旧结构上修补。

---

## Repository Shape

最小结构如下：

```text
{workspace}/
├── SKILL.md
├── SPEC.md
├── index/
│   └── all_papers.json
├── papers/
│   └── {venue}/{year}/{id}-{slug}.md
├── projects/
│   └── {project-name}/
│       ├── README.md
│       ├── papers/
│       │   └── {paper-id}.md
│       └── synthesis/
│           ├── overview.md
│           ├── timeline.md
│           └── comparative.md
└── scripts/
    └── import_conference.py
```

说明：

- `README.md`：项目 scope、intent、纳入论文列表及纳入理由
- `papers/{paper-id}.md`：该论文在**本项目语境**下的解读
- `synthesis/*.md`：跨论文分析，从不同角度逐步展开

> 不要求一开始就有复杂 schema、summary、dashboard。项目结构应尽量轻量。

---

## Shared Paper Record

共享层单篇论文应该回答这些问题：

- 这篇论文是什么？
- 它解决什么问题？
- 方法是什么？
- 评估结果怎样？
- 局限性是什么？

这些内容应该尽量保持**中性、可复用、与具体项目无关**。

推荐结构：

```markdown
# Paper Title

## 摘要

## Problem

## Method

## Evaluation

## Limitations
```

如果信息不足，可以先保留最小记录，但不要用项目判断去填充共享层。

---

## Project Workflow

### Workflow 1: Import or update shared papers

触发示例：

- “抓取 NSDI 2026 论文”
- “补充 KV cache 相关论文到数据库”
- “把这批论文入库”

步骤：

1. 先读取 `SPEC.md`
2. 明确本次要导入的是：
   - 某个 venue/year 的全量论文
   - 某个方向的候选论文
   - 某个用户提供列表
3. 收集原始事实：
   - 标题
   - authors
   - venue/year
   - official URL
   - arXiv / OpenReview / DOI 等可用标识
   - abstract
4. 执行去重与 canonicalization
5. 写入 `papers/` 与 `index/all_papers.json`

此工作流只负责共享层，不负责生成项目判断。

### Workflow 2: Start or refine a project

触发示例：

- “做一个 KV cache serving 项目”
- “整理这个方向的 project space”
- “为这个 topic 建一个研究项目”

步骤：

1. 在 `projects/{name}/README.md` 中写清：
   - 项目要回答什么问题
   - 关心什么，不关心什么
   - 当前纳入哪些论文
   - 每篇论文为什么纳入
2. 不要求一开始就完美；先形成可工作的 paper scope
3. 若已有旧项目，优先抽取其中真正有价值的部分：
   - paper list
   - scope 边界
   - 初步分类想法

### Workflow 3: Per-paper project analysis

触发示例：

- “逐篇分析这个项目里的论文”
- “写 Sim-LLM 在这个项目里的意义”

步骤：

1. 先确认该论文已经在共享层存在
2. 在 `projects/{name}/papers/{paper-id}.md` 写项目语境下的解读
3. 每篇项目笔记至少回答：
   - 为什么与本项目相关
   - 它在本项目里属于哪类方法
   - 与项目中哪些论文最可比较
   - 它的局限或未解决问题是什么

### Workflow 4: Cross-paper synthesis

触发示例：

- “做 cross-paper analysis”
- “整理 timeline”
- “比较不同 approach”

步骤：

1. 基于项目已纳入论文，而不是基于模糊 topic 自动发挥
2. 分别维护：
   - `synthesis/overview.md`
   - `synthesis/timeline.md`
   - `synthesis/comparative.md`
3. 重点输出：
   - 这个方向的总体图景
   - 关键时间线与技术演进
   - 不同方法如何解决相似目标
   - 重要 tradeoff、冲突、空白

> 项目的高质量输出，应该是前面 paper curation 和 per-paper analysis 的自然结果。

---

## Project README Expectations

`projects/{name}/README.md` 应是项目的主入口。

至少应包含：

1. **Intent**
   - 这个项目试图理解什么问题

2. **Scope**
   - 包含什么
   - 不包含什么

3. **Paper Set**
   - 当前纳入论文列表
   - 每篇纳入理由

4. **Open Ends**
   - 还缺哪些论文
   - 哪些边界论文待确认

这比过早引入复杂配置文件更重要。

---

## Search Guidance

优先来源：

- 会议官方 accepted papers / program 页面
- arXiv
- OpenReview
- 官方 PDF / DOI 页面

搜索时应尽量保留“来源路径”概念，即清楚知道一篇论文是：

- 用户显式提供
- 本地数据库已有
- 本次外部检索补充得到

---

## What The Skill Should Produce Over Time

持续使用后，理想产物是：

1. 一个更完整、更可信的共享数据库
2. 若干个有明确 scope 的项目空间
3. 每个项目下：
   - 明确的论文集合与纳入理由
   - 单篇项目笔记
   - 跨论文综合分析

换句话说，项目质量不是靠单次 prompt 堆出来，而是靠多次使用后逐步沉淀出来。

---

## Non-Goals

本技能当前不追求：

- 复杂项目 schema
- 过早自动生成 summary dashboard
- 在没有明确项目范围时直接生成大而全报告
- 把项目判断回写到共享层

---

## Operational Notes

每次执行前都先读 `SPEC.md`。

`SPEC.md` 负责定义：

- 共享层的 canonical 数据结构
- 去重规则
- importer/validator 未来需要保障的 invariant

本 `SKILL.md` 负责定义：

- 整体工作流
- shared vs project 的边界
- 项目如何自然演化

---

*Last updated: 2026-05-10*
