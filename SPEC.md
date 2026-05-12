# Net-Research SPEC

> 本文档定义共享论文数据库的契约，以及后续 importer / validator 必须保证的基本不变量。
> 它不规定复杂项目 schema；项目层保持轻量，由 `SKILL.md` 约束其工作流和边界。

版本：2.0  
更新日期：2026-05-10

---

## 1. Scope of This SPEC

本 SPEC 只约束**共享层**：

- `papers/`
- `index/all_papers.json`

不约束复杂的项目分析格式；项目层的结构与写作方式由 `SKILL.md` 定义。

---

## 2. Shared-Layer Invariants

共享层必须满足以下不变量：

1. 每篇 canonical 论文有且只有一个 `id`
2. `index/all_papers.json` 中每条记录都应对应一个真实存在的 paper file
3. paper file 的路径必须与索引中的 `file` 字段一致
4. 同一论文不应在索引中出现多个 canonical 记录
5. 共享层内容只保存稳定事实与中性摘要，不保存项目判断
6. 路径统一使用 POSIX 风格分隔符 `/`

这些不变量是未来 validator 需要检查、importer 需要维护的基础。

---

## 3. Repository Layout

```text
{workspace}/
├── index/
│   └── all_papers.json
├── papers/
│   └── {venue}/{year}/{id}-{slug}.md
└── projects/
    └── {project-name}/...
```

这里只有 `index/all_papers.json` 是共享层索引。

不维护派生索引，例如：

- `by_topic.json`
- `by_year.json`
- `by_conference.json`

按 topic / venue / year 的查询统一通过过滤 `all_papers.json` 完成。

---

## 4. Shared Paper Markdown Format

存储路径：

`papers/{venue_lower}/{year}/{id}-{slug}.md`

每篇论文文件使用 YAML frontmatter。

### 4.1 Frontmatter schema

```yaml
---
id: nsdi26-001
title: "Paper Title"
conference: "NSDI 2026"
date: "2026-03"
authors:
  - name: "Author Name"
    affiliation: "Institution"
    is_industry: true
topics:
  - LLM Serving
  - Distributed Systems
tags:
  - llm-serving
  - distributed-systems
arxiv: "2503.12345"
url: "https://..."
status: analyzed
---
```

### 4.2 Body expectations

共享层正文推荐包含：

```markdown
# Paper Title

## 摘要

## Problem

## Method

## Evaluation

## Limitations
```

允许信息不完整，但内容必须保持中性、可复用。

**禁止写入**：

- “这篇论文适合项目 X”
- “相比项目里其他论文更重要”
- 针对某个项目的纳入理由

---

## 5. Field Definitions

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | canonical paper ID |
| `title` | string | ✅ | 论文标题 |
| `conference` | string | ✅ | 规范化 venue 名称，如 `NSDI 2026` |
| `date` | string | ✅ | `YYYY-MM` |
| `authors` | list | ✅ | 每项含 `name`、`affiliation`、`is_industry` |
| `topics` | list | ✅ | 受控 topic 标签列表 |
| `tags` | list | ✅ | 小写短横线标签 |
| `arxiv` | string | ❌ | arXiv ID；无则空字符串 |
| `url` | string | ✅ | 官方或主要来源 URL |
| `status` | string | ✅ | `new` / `analyzed` / `archived` |

### 5.1 Status meanings

- `new`：已建记录，但摘要/结构化内容仍明显不完整
- `analyzed`：已有 abstract，且共享层摘要达到可复用水平
- `archived`：保留记录，但不再是活跃关注对象

---

## 6. Canonical ID and Path Rules

### 6.1 ID format

格式：

`{venue_lower}{year_last2}-{sequence:03d}`

示例：

- `nsdi26-001`
- `sigcomm25-003`
- `arxiv26-014`

### 6.2 Venue abbreviation set

当前支持：

- `nsdi`
- `sigcomm`
- `osdi`
- `conext`
- `imc`
- `atc`
- `eurosys`
- `fast`
- `sosp`
- `isca`
- `iclr`
- `icml`
- `neurips`
- `arxiv`

### 6.3 File path

文件路径格式：

`papers/{venue_lower}/{year}/{id}-{slug}.md`

其中：

- `{year}` 为四位年份目录
- `slug` 来自标题的规范化文件名

索引中的 `file` 字段必须使用相同路径，并统一为 `/` 分隔。

---

## 7. Topic Vocabulary

topics 应使用受控词表，当前以高层标签为主：

- `LLM Serving`
- `LLM Training`
- `AI Observability`
- `AI DCN`
- `Network Measurement`
- `Network Monitoring`
- `Network Security`
- `Distributed Systems`
- `Consensus`
- `Replication`
- `Congestion Control`
- `Transport Protocol`
- `Routing`
- `Edge Computing`
- `CDN`
- `Caching`
- `SDN`
- `NFV`
- `Network Programmability`
- `Wireless`
- `Mobile`
- `IoT`
- `Datacenter Networking`
- `Cloud Computing`
- `Machine Learning for Networks`
- `Learning-based Systems`

规则：

1. `topics` 用于较稳定的检索和聚类，应该克制
2. 不要把每个项目私有分类都写进 `topics`
3. 如果当前词表不足，先在项目层讨论，再决定是否扩展共享词表

---

## 8. Filter Record Format

在外部检索后、写入共享层前，统一使用如下中间格式：

```json
{
  "raw_title": "DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants",
  "raw_authors": "Alice Smith; Bob Jones",
  "conference": "NSDI",
  "year": 2026,
  "url": "https://...",
  "arxiv_id": "2411.02820",
  "abstract": "Full abstract text...",
  "topics_raw": ["LLM Serving", "Distributed Systems"],
  "is_industry": true
}
```

### 8.1 Minimum viable input

至少应具备以下之一：

- `url`
- `arxiv_id`

并且必须有：

- `raw_title`
- `conference`
- `year`

### 8.2 Interpretation rules

- `abstract` 为空时，可先创建最小记录
- `topics_raw` 是原始候选标签，不等于最终 `topics`
- `is_industry` 可作为粗粒度补充信息，但不替代作者 affiliation 解析

---

## 9. Deduplication Rules

去重是 importer 的核心职责。

### Layer 1: External identifier match

若 `arxiv_id` 一致，则优先视为同一论文。

后续可扩展到：

- DOI
- OpenReview ID

### Layer 2: Venue + year + normalized title exact match

若以下同时满足，则视为同一论文：

- venue 一致
- year 一致
- 规范化 title 一致

### Layer 3: High-confidence fuzzy title match

若以下同时满足，可视为同一论文，但应留下 warning：

- venue 一致
- 年份差不超过 1
- title 相似度超过阈值

### Deduplication principle

目标不是“尽量合并”，而是“只在高置信度时合并”。  
不确定时宁可提示人工确认，也不要悄悄污染 canonical 记录。

---

## 10. Merge Rules

当确认是同一论文时：

1. 保留已有 canonical `id`
2. 保留更可信的 `conference` / `url`
3. 优先保留更完整的 `authors`
4. 保留更完整的 `abstract`
5. 合并 `topics`，但最终结果必须仍符合受控词表原则
6. 不得因为一次 merge 改写出新的错误路径或 duplicate record

特别注意：

- merge 更新的是**canonical record**
- 不是“在当前 venue/year 目录再写一个副本”

---

## 11. Index Format

`index/all_papers.json` 格式：

```json
{
  "last_updated": "2026-05-10",
  "total_count": 123,
  "papers": [
    {
      "id": "nsdi26-001",
      "title": "Paper Title",
      "conference": "NSDI 2026",
      "date": "2026-03",
      "topics": ["LLM Serving"],
      "abstract": "Abstract...",
      "is_industry": true,
      "file": "papers/nsdi/2026/nsdi26-001-paper-title.md"
    }
  ]
}
```

约束：

1. `total_count == len(papers)`
2. `id` 唯一
3. `file` 唯一指向 canonical paper file
4. `file` 路径必须可解析到真实文件

---

## 12. Slugify Rules

`slug` 用于生成安全文件名。

规范：

1. Unicode NFC 归一化
2. 转为 ASCII；无法保留的字符删除
3. 去掉非字母数字字符
4. 空格和重复连字符压成单个 `-`
5. 截断到合理长度
6. 若结果为空，使用稳定 hash fallback

目标是：

- 稳定
- 可读
- 跨平台安全

---

## 13. Validator Expectations

后续 validator 至少应检查：

1. `all_papers.json` JSON 结构是否合法
2. `total_count` 是否正确
3. 是否存在 duplicate IDs
4. `file` 是否存在
5. `file` 路径分隔符是否统一
6. frontmatter 是否齐全
7. `conference`、`date`、`status` 是否符合规范
8. `topics` 是否偏离受控词表
9. 索引记录与文件 frontmatter 是否冲突

validator 的职责是暴露 repo 状态，不替代人工判断研究质量。

---

## 14. Importer Expectations

后续 importer 应是一个**机械、可复用、尽量窄职责**的工具。

它负责：

1. 接受 filter records
2. 规范化字段
3. 去重
4. 写入 / 更新 canonical paper file
5. 更新 `all_papers.json`

它不负责：

1. 生成项目洞察
2. 推断某篇论文是否值得纳入某个项目
3. 自动写 cross-paper synthesis

---

## 15. Project-Layer Boundary

项目层内容不由 importer 管理。

像下面这些内容应只存在于 `projects/{name}/`：

- 为什么纳入这篇论文
- 它在项目中的角色
- 与其他项目论文的比较
- 时间线、分类法、研究空白

如果某信息离开项目语境仍成立，它才有资格进入共享层。

---

*Last updated: 2026-05-10*

## 七、文件路径速查

| 内容 | 路径 |
|------|------|
| 公共论文正文 | `papers/{conference}/{year}/{id}-{slug}.md` |
| 公共索引（唯一） | `index/all_papers.json` |
| 项目配置 | `projects/{name}/config.json` |
| 项目聚合数据 | `projects/{name}/summary.json` |
| 项目洞察（人工） | `projects/{name}/insights/*.md` |
| 项目洞察（汇总） | `projects/{name}/insights/state.md` |
| 项目报告 | `projects/{name}/reports/*.md` |
| 导入脚本 | `scripts/import_conference.py` |

---

*本文档为 net-research skill 的核心契约，所有脚本和 AI 执行步骤必须遵守。*
