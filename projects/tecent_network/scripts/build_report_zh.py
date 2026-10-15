#!/usr/bin/env python3
"""Build a separate, offline Chinese edition without changing source metadata or English output."""
from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess

import matplotlib
from matplotlib import font_manager
from matplotlib.text import Text

import build_report as br

ROOT, OUT = br.ROOT, br.OUT
FIGURES = OUT / "report_figures_zh"
TOPICS = ["数据中心网络与 AI 基础设施", "云网关与硬件卸载", "交互媒体与体验质量（QoE）", "广域网与光系统", "网络测量与运维", "安全与隐私", "云资源优化（边界）"]
INSTITUTIONS = {
    "Tsinghua University": "清华大学", "Nanjing University": "南京大学", "University of California, Santa Barbara": "加州大学圣巴巴拉分校",
    "Peng Cheng Laboratory": "鹏城实验室", "Wuhan University": "武汉大学", "City University of Hong Kong": "香港城市大学",
    "Nanjing University of Science and Technology": "南京理工大学", "Zhejiang University": "浙江大学", "Beijing University of Posts and Telecommunications": "北京邮电大学",
    "Zhongguancun Laboratory": "中关村实验室", "Massachusetts Institute of Technology": "麻省理工学院", "University at Buffalo": "布法罗大学",
    "Quancheng Laboratory": "泉城实验室", "Northwestern University": "美国西北大学", "King Abdullah University of Science and Technology": "阿卜杜拉国王科技大学",
    "Peking University": "北京大学", "Xi'an Jiaotong University": "西安交通大学", "Hong Kong University of Science and Technology": "香港科技大学",
    "University of Texas at Austin": "得克萨斯大学奥斯汀分校", "Columbia University": "哥伦比亚大学", "Fudan University": "复旦大学",
    "University of Chicago": "芝加哥大学", "University of Michigan": "密歇根大学", "Harvard University": "哈佛大学",
    "Politecnico di Milano": "米兰理工大学", "Queen Mary University of London": "伦敦玛丽女王大学", "Xiamen University": "厦门大学",
    "Hong Kong Polytechnic University": "香港理工大学", "National University of Singapore": "新加坡国立大学",
    "Computer Network Information Center, Chinese Academy of Sciences": "中国科学院计算机网络信息中心", "Chinese University of Hong Kong, Shenzhen": "香港中文大学（深圳）",
    "University of Chinese Academy of Sciences": "中国科学院大学", "Shanghai Jiao Tong University": "上海交通大学", "University of Science and Technology of China": "中国科学技术大学",
    # The English affiliation does not establish an unambiguous official Chinese entity.
    "Institute of Artificial Intelligence, China": "Institute of Artificial Intelligence, China（机构中文名待核实）", "Tencent": "腾讯"
}
LOCATIONS = {"China": "中国", "Mainland China": "中国内地", "Hong Kong": "中国香港", "United States": "美国", "Singapore": "新加坡", "Saudi Arabia": "沙特阿拉伯", "Italy": "意大利", "United Kingdom": "英国"}
DEPLOYMENTS = {"production_reported": "作者报告生产部署", "research_tool": "研究工具", "prototype_evaluation": "原型评估", "production_level_prototype": "生产级原型", "production_use_case": "生产用例", "testbed_and_simulation": "测试床与仿真", "simulation_and_hardware_experiments": "仿真与硬件实验", "cluster_evaluation": "集群评估", "experimental_evaluation": "实验评估", "system_evaluation": "系统评估"}
TAGS = {"AI workload": "AI 负载", "Internet measurement": "互联网测量", "learning-assisted control": "学习辅助控制", "disaggregation": "解耦", "programmability": "可编程性", "production operations": "生产运维", "telemetry": "遥测", "optical": "光网络", "resource efficiency": "资源效率", "privacy": "隐私", "trusted hardware": "可信硬件", "cloud gaming": "云游戏", "application-transport co-design": "应用与传输协同设计", "reliability": "可靠性", "multipath": "多路径", "wireless": "无线接入", "loss recovery": "丢包恢复", "congestion control": "拥塞控制", "traffic engineering": "流量工程", "data analytics": "数据分析", "routing": "路由", "network architecture": "网络架构", "emulation": "仿真与回放", "last mile": "最后一公里", "security": "安全", "GPU communication": "GPU 通信", "cloud scheduling": "云调度"}
FIRST_CLASSES = {"Dual Tencent + academic/research": "腾讯与高校／研究机构双重署名", "Academic/research without Tencent": "高校／研究机构署名，无腾讯署名", "Tencent without academic/research": "腾讯署名，无高校／研究机构署名", "Explicit unaffiliated / other": "明确无机构／其他"}
SOURCE_STATUS = {"publisher_address_reviewed": "已核查出版商地址", "official_location_page_reviewed": "已核查机构位置页", "official_location_verified_web_primary": "经网页核实机构一手地址", "official_page_empty_or_challenge": "机构页为空／有访问挑战，位置暂定", "country_only_in_affiliation_city_unresolved": "仅确认国家，城市未确定", "official_location_reference_not_cached": "机构位置参考页未缓存", "official_location_fetch_failed": "机构页获取失败"}
CHART_TEXT = {
    "Papers · one primary topic per paper": "论文数 · 每篇只分配一个主主题", "primary papers": "篇正式论文", "none\nobserved": "未观察到",
    "Observed papers": "观察到的论文数", "Within-year share (%)": "当年主题占比（%）", "Publication year · *2026 dated corpus; no annualization": "发表年份 · *2026 为截至分析日期的样本，不作年化",
    "Academic/research institution represented": "有高校／研究机构署名", "Tencent-only": "仅腾讯署名", "Paper count · dual affiliations count as institutional presence": "论文数 · 双重署名也计入机构参与",
    "Full paper–institution counts": "论文—机构完整计数", "DCN / AI": "数据中心／AI", "Gateways": "云网关", "QoE": "体验质量", "WAN": "广域网", "Operations": "运维", "Security": "安全", "Resources": "资源",
    "Longitude": "经度", "Latitude": "纬度", "Global institutional anchors": "全球机构城市锚点", "Mainland China / Hong Kong detail": "中国内地与香港局部",
    "Beijing": "北京", "Nanjing": "南京", "Shanghai": "上海", "Shenzhen": "深圳", "Xi'an": "西安", "Wuhan": "武汉", "Hangzhou": "杭州", "Xiamen": "厦门", "Jinan": "济南", "Hefei": "合肥",
    "1 institution": "1 家机构", "3 institutions": "3 家机构", "6 institutions": "6 家机构", "Previously observed institution": "此前已出现的机构", "First observed in this corpus": "在本样本中首次出现", "Distinct institutions represented that year": "当年出现的不同机构数", "Papers with ≥1 institution in location\nOverlapping counts, not a partition": "含当地至少一家机构的论文数\n各地计数可重叠，不构成占比分割",
    "Workloads & experience": "负载与体验", "Control & reliability": "控制与可靠性", "Offload & transport": "卸载与传输", "Physical bottlenecks": "物理瓶颈", "Observe, replay, diagnose": "观察、回放、诊断",
    "AFR / LADR · interactive QoE    |    SwiftEP / Holmes · AI efficiency": "AFR / LADR · 交互体验    |    SwiftEP / Holmes · AI 效率",
    "OpTel / FlexWAN · optics    |    BLADE · Wi-Fi contention": "OpTel / FlexWAN · 光网络    |    BLADE · Wi-Fi 竞争"
}


def esc(value):
    return html.escape(str(value), quote=True)


def read_json(name):
    return json.loads((ROOT / "data" / name).read_text())


def inst(name):
    return INSTITUTIONS.get(name, name)


def localize_figures(results, papers, topics, world):
    """Use identical plot calculations; localize text before embedding font outlines."""
    font_path=subprocess.check_output(["fc-match","-f","%{file}","Noto Sans CJK SC"],text=True).strip()
    font_manager.fontManager.addfont(font_path)
    font_family=font_manager.FontProperties(fname=font_path).get_name()
    old_save, old_short = br.save_figure, br.short_institution
    translations = {**CHART_TEXT, **LOCATIONS}
    translations.update({meta["label"]: zh for meta, zh in zip(topics.values(), TOPICS)})
    translations.update({old_short(k): v for k, v in INSTITUTIONS.items()})
    translations.update({k: v for k, v in INSTITUTIONS.items()})
    original_figures = br.FIGURES
    br.FIGURES = FIGURES
    def save_localized(fig, name):
        # Axis ticks are regenerated by their formatter during draw; translating
        # only their Text objects would be silently undone by tight_layout/savefig.
        for ax in fig.axes:
            for axis in ["x", "y"]:
                labels=getattr(ax,f"get_{axis}ticklabels")()
                original=[label.get_text() for label in labels]
                localized=[translations.get(text,text) for text in original]
                if localized != original:
                    getattr(ax,f"set_{axis}ticks")(getattr(ax,f"get_{axis}ticks")(),localized)
        for item in fig.findobj(Text):
            text = item.get_text()
            item.set_text(translations.get(text, text))
            item.set_fontfamily(font_family)
        # Recalculate bounds with Chinese labels, avoiding clipping from English metrics.
        if name != "technology_stack":
            fig.tight_layout()
        old_save(fig, name)
    try:
        br.save_figure = save_localized
        with matplotlib.rc_context({"font.family": font_family, "svg.fonttype": "path"}):
            br.plots(results, papers, topics, world)
    finally:
        br.save_figure, br.short_institution, br.FIGURES = old_save, old_short, original_figures


def render(results, papers, topics, content, english_content, names, author_rows):
    by_short = {p["short"]: p for p in papers}
    def person(name):
        return f'{names[name]["zh"]}（{name}）' if name in names else name
    def cite(short):
        p = by_short[short]
        return f'<a class="paper-ref" href="#paper-{p["paper_id"]}">{esc(short)} {p["year"]}</a>'
    def figures(name, title, caption):
        old = br.FIGURES
        try:
            br.FIGURES = FIGURES
            return br.figure(name, title, caption).replace("Scroll the figure horizontally on a narrow screen.", "窄屏可横向滚动查看完整图表。")
        finally:
            br.FIGURES = old
    def table(headers, rows):
        return br.table(headers, rows)
    topic_label = {key: zh for key, zh in zip(topics, TOPICS)}
    nav = [("overview", "研究概览"), ("topics", "主题与时间演进"), ("connections", "合作网络与地理分布"), ("deepdives", "分主题深入分析"), ("outlook", "潜在优势与待解问题"), ("methods", "方法与局限"), ("evidence", "逐篇论文证据"), ("verified-names", "中文姓名核验")]
    body = f'<header class="hero"><div class="eyebrow">研究版图 / 2019—2026 / 中文版</div><h1>{esc(content["title"])}</h1><p class="subtitle">{esc(content["subtitle"])}</p><div class="hero-meta">分析快照：2026 年 10 月 15 日 ／ 元数据核查：2026 年 10 月 14 日<br>NSDI · SIGCOMM · CoNEXT/PACMNET · IMC · HotNets<br><a href="tencent_networking_report.html" lang="en">Read the English edition ↗</a></div></header>'
    body += '<div class="report-shell"><nav aria-label="报告章节"><div class="nav-title">本报告</div>' + ''.join(f'<a href="#{key}">{label}</a>' for key,label in nav) + '<a href="tencent_networking_metadata.xlsx">元数据工作簿 ↗</a><a href="../ANALYSIS_PLAN.md">分析计划 ↗</a></nav><main id="main">'
    body += '<section id="overview"><div class="section-number">01 / 研究概览</div><h2>围绕生产运营瓶颈形成的系统研究版图</h2><div class="stats">'
    for value, label in [(32,"篇经核查的正式论文"),(35,"家高校／研究机构"),("31/32","论文有学术机构共同署名"),(5,"篇明确涉及 AI 负载")]:
        body += f'<div><strong>{value}</strong><span>{label}</span></div>'
    body += '</div><p class="lead">贯穿这些工作的不是某个单一协议，而是反复将生产瓶颈转化为更可编程、可测量、资源更高效的系统：从云网关和光骨干网，到交互视频与 AI 基础设施。</p><div class="callout"><strong>首先读对统计分母。</strong>这是用户逐项核查的选定论文样本，不是腾讯全部网络研究。32 篇中含 1 篇云资源边界论文；网络核心敏感性口径为 31 篇。2 篇海报不计入核心统计。2019／2020 年未观察到论文不等于确定零产出；2026 年是截至分析日期的样本，不是完整全年总量。</div>'
    body += '<div class="insight-grid"><article><h3>学术机构参与是常态</h3><p>96.9% 的论文列有高校／研究机构。只有 ' + cite("LADR") + ' 全部作者署名腾讯。这描述的是公开论文署名，不是腾讯内部研发中校企合作的占比。</p></article><article><h3>AI 以全栈问题的形式出现</h3><p>' + '、'.join(cite(s) for s in ["Holmes","Astral","SwiftEP","DistDPU","Pegasus"]) + ' 分别连接可观测性、通信、虚拟化与物理设施。通用数据中心论文不自动计为 AI。</p></article><article><h3>潜在运营优势，不是已证实的壁垒</h3><p>成本、时延与可靠性改进提示了可能的竞争机制，但样本并未证明市场份额、因果营收收益，或经独立审计的领先优势。</p></article></div></section>'
    body += '<section id="topics"><div class="section-number">02 / 研究主题</div><h2>广泛的系统研究，近期叠加 AI 基础设施层</h2>'
    body += figures("topic_partition", "主题分布：32 篇论文，每篇一个主主题", "未四舍五入前合计 100%；技术／负载标签可重叠，另行呈现。灰色类别 Hestia 是唯一边界论文。")
    body += table(["主主题","论文数","占比／32","网络核心口径／31","高校／研究机构参与","仅腾讯"], [[esc(topic_label[r["topic"]]),r["papers"],br.percent(r["share_percent"]),f'{r["networking_core_papers"]} · {br.percent(r["networking_core_share_percent"])}',r["academic_research_collaboration"],r["tencent_only"]] for r in results["topic_partition"]])
    body += figures("topic_evolution", "发表年份：数量与主题构成", "发表年份不是项目启动或部署年份。近期数量更多也可能受披露及会议时间影响；不推算增长率，不对 2026 年作全年预测。")
    body += '<p><strong>AI 占比不是逐年单调上升。</strong>明确 AI 负载论文在 2024 年为 0／5、2025 年为 2／5、2026 年为 3／14。Turbo 是数据分析通信研究，P-ECMP 与 Harp 是通用数据中心研究；保持区分可避免夸大 AI 数量。</p>'
    body += figures("collaboration_types", "学术合作与仅腾讯署名论文", "学术／研究机构参与包括双重署名和研究实验室。此样本没有仅与其他企业合作而无学术机构的正式论文。“仅腾讯”是署名分类，不代表未使用外部思想或工具。")
    tags = sorted(results["secondary_tags"], key=lambda r:-r["papers"])[:12]
    body += '<details><summary>可重叠的技术／负载标签及计数规则</summary>' + table(["辅助标签","论文数","占比／32"],[[esc(TAGS.get(r["tag"],r["tag"])),r["papers"],br.percent(r["share_percent"])] for r in tags]) + '<p>这些占比不能相加。主主题是根据完整已采集摘要作出的分析判断，不是只按题目关键词生成。</p></details></section>'
    body += '<section id="connections"><div class="section-number">03 / 合作网络</div><h2>以中国为中心、具有持续国际连接的合作网络</h2>'
    body += figures("partner_matrix", "合作机构频次与主题跨度：前 15 家", "每个论文—机构组合计一次，不受作者数量或双重署名行数影响。排名为完整计数；分数计数见后表和 CSV。共同署名不等于合同或经费关系。")
    body += figures("partner_geography", "论文署名机构的地理分布", "气泡面积表示近似城市锚点上的机构数，不是论文数；相近锚点可能重叠。1 家仅知国家的机构不绘点。南理工机构页为空，城市锚点仍为暂定。清华、中科大以母机构城市代表多个校区。底图为公有领域 Natural Earth；不映射作者国籍或迁移。")
    body += figures("geography_evolution", "样本中的机构足迹如何演变", "“首次出现”指在本样本中首次署名，不是现实合作开始。各国家论文数可以重叠；香港在地理数据中作为中国的独立地区，不单列为国家。")
    body += '<p><strong>20／32 篇论文</strong>至少有一家位于中国以外的机构。这是共同署名的地理足迹，不是研究人员国籍。重复机构组合也可能跟随某个研究者而变化，仅凭此数据无法区分。</p><p><strong>主要持续节点是清华大学（19 篇）、北京大学（7 篇）、密歇根大学（7 篇）。</strong>欧洲连接来自 Astral 一篇（米兰理工、伦敦玛丽女王）；新加坡国立出现在 2026 年的 5 篇论文中，但这不证明合作始于该年。</p><h3>研究者群组：分析视角，不是正式组织</h3><p>以下为分析者整理、可以重叠的主题群组。括号为姓名字符串在样本论文中的出现次数，不代表已经全局消歧的个人身份。</p><div class="cohorts">'
    for original, translated in zip(english_content["cohorts"],content["cohorts"]):
        roster = [f'{esc(person(name))} <span class="muted">({len({a["paper_id"] for a in author_rows if a["author_name"] == name})})</span>' for name in original["people"]]
        body += f'<article><h4>{esc(translated[0])}</h4><p>{esc(translated[1])}</p><p class="roster">'+' · '.join(roster)+'</p><p>'+' '.join(cite(s) for s in original["papers"])+'</p></article>'
    body += '</div><h3>学术伙伴的角色：证据能说明到哪一步？</h3><p>机构署名能明确证明共同作者关系，但不足以确定任务归属。PDF 首页提供少量更具体的证据：实习、双重署名、共同贡献及通讯作者。这支持实际参与及共同获得署名认可，不支持笼统的“高校做理论、腾讯做工程”叙事。</p>'
    claims = ["复旦署名的 Zhiyi Yao 与 Chao Peng 在腾讯实习期间完成工作；Xuya Jia 与 Zhiyi Yao 标为共同贡献。", "Zhiyi Yao、Pengbo Hu、Congcong Miao 标为共同贡献；徐跃东（Yuedong Xu）明确为通讯作者；前两位同时署名复旦与腾讯。", "腾讯署名的 Congcong Miao 与西北大学署名的肖蕴明（Yunming Xiao）明确标为共同贡献。", "腾讯署名的 Yadong Liu 与密歇根大学署名的肖蕴明（Yunming Xiao）标为共同贡献。", "腾讯署名的 Congcong Miao 与北大署名的 Yuejie Wang 标为共同贡献。", "密歇根大学署名的 Shihan Lin 与腾讯署名的 Shunqiao Jiang 标为共同贡献。"]
    roles = read_json("analysis_role_evidence.json")["checks"]
    body += table(["论文","明确署名的关系","证据"], [[cite(r["paper"]),esc(claim),f'<a href="{esc(r["source_url"])}">PDF ↗</a> · 作者上标及贡献脚注'] for r,claim in zip(roles,claims)])
    body += '<details><summary>第一作者机构结构：位置不等于领导权</summary>' + table(["第一作者机构类别","论文数"],[[esc(FIRST_CLASSES[k]),v] for k,v in results["first_author_classes"].items()]) + '<p>类别互斥，共覆盖 32 个第一作者位置；共同贡献和通讯作者可能与第一署名位置不同。</p></details><h3>观察到的机构组合，不是职业履历</h3>'
    trajectory = []
    for name in ["Congcong Miao","Yunming Xiao","Zili Meng","Heng Yu"]:
        years=[]
        for year in range(2021,2027):
            affiliated=sorted({a["institution"] for a in author_rows if a["author_name"]==name and a["year"]==year and a["institution"]})
            if affiliated: years.append(f'<strong>{year}</strong>：'+esc('、'.join(inst(i) for i in affiliated)))
        trajectory.append([esc(person(name)),'<br>'.join(years)])
    body += table(["重复姓名","本样本论文中出现的署名机构"],trajectory) + '<p class="small">同一年可能出现不同组合、双重任职或日程来源差异。不能由此确定迁移日期、雇佣关系，或机构变化后不再与腾讯合作。</p>'
    body += '<details><summary>全部高校／研究机构、地理证据及分数计数</summary>'+table(["机构","地区","论文数","分数贡献","观察年份","位置来源"],[[esc(inst(r["institution"])),esc(LOCATIONS.get(r["region"],r["region"])),r["paper_count"],f'{r["fractional_paper_credit"]:.2f}',f'{r["first_observed_year"]}—{r["last_observed_year"]}',f'<a href="{esc(r["source_url"])}">来源 ↗</a> · {esc(SOURCE_STATUS.get(r["source_status"],r["source_status"]))}'] for r in results["partners"]])+'</details></section>'
    body += '<section id="deepdives"><div class="section-number">04 / 分主题深入分析</div><h2>跟随瓶颈迁移，再追问它改变了什么</h2>'
    body += figures("technology_stack", "技术栈视角：分析性归纳", "各行按机制作用位置分组。水平接近及垂直排列不证明生产集成、直接依赖或共用代码库；有些论文跨层。此图不是腾讯官方架构。")
    for original,dive in zip(english_content["deepdives"],content["deepdives"]):
        key=original["topic"]; row=next(r for r in results["topic_partition"] if r["topic"]==key)
        body += f'<article class="deepdive" id="topic-{key}" style="--topic-color:{topics[key]["color"]}"><div class="topic-kicker">{row["papers"]} 篇 · 占样本 {br.percent(row["share_percent"])}</div><h3>{esc(dive["heading"])}</h3><p class="thesis">{esc(dive["thesis"])}</p>'
        for sequence in original["sequences"]:
            body += '<div class="paper-sequence">'+'<span class="arrow" aria-hidden="true">→</span>'.join(cite(s) for s in sequence)+'</div>'
        body += '<div class="two-col"><div><h4>学术连接及可证实的角色</h4><p>'+esc(dive["partners"])+'</p><h4>潜在运营价值</h4><p>'+esc(dive["leverage"])+'</p></div><div><h4>证据尚不能证明什么</h4><p>'+esc(dive["limits"])+'</p><h4>下一步研究问题 <span class="badge hypothesis">假设</span></h4><p>'+esc(dive["future"])+'</p></div></div>'
        body += '<details><summary>论文机制与评估设置：完整结果见附录</summary>'+table(["论文","机制","证据场景"],[[cite(p["short"]),esc(p["zh"][0]),esc(DEPLOYMENTS[p["deployment"]])] for p in papers if p["topic"]==key])+'</details></article>'
    body += '</section><section id="outlook"><div class="section-number">05 / 启示与下一步调查</div><h2>潜在优势：持续的运营学习闭环</h2><p class="lead">更稳妥的归纳是一种能力模式：接触生产环境，发现瓶颈；通过系统研究提出更可编程或更高效的抽象；测量和部署反馈到下一轮迭代。论文支持这个模式的部分环节，但未测出因果竞争壁垒。</p><div class="insight-grid"><article><h3>成本／有效工作</h3><p>光容量、普通 DDR、硬件化管理及 GPU 数据搬运都在减少超额配置。须说明具体分母，不能将不同节省比例相乘。</p></article><article><h3>体验／韧性</h3><p>客户端队列、丢包来源、路径故障和光层劣化需要不同控制闭环。时延或检测改善不直接证明留存提升或避免的经济损失。</p></article><article><h3>迭代速度</h3><p>追踪与仿真可能减少理解异构生产栈的成本。这是潜在组织能力，不是用论文数量测出的工程生产率。</p></article></div>'
    body += table(["待解问题","仍然未知","下一步调查"],[[esc(x) for x in row] for row in content["open_questions"]])+'</section>'
    body += '<section id="methods"><div class="section-number">06 / 方法与边界</div><h2>统计了什么，以及没有推断什么</h2><ol>'
    methods = [
        ("范围", "来自五个会议范围的 32 篇正式论文，发表时间为 2019—2026 年。31 篇属于网络核心，Hestia 保留为边界候选；另 2 篇海报在工作簿中单列。"),
        ("分类", "每篇一个主主题，技术／负载标签可重叠。分类是基于完整摘要的分析判断，不是出版商关键词或推测的公司优先级。"),
        ("共同署名", "每篇内对机构去重，不重复累计作者和双重署名行。高校与研究机构合并展示，但企业和明确无机构作者不重标为高校。"),
        ("完整与分数计数", "每个论文—学术机构连接完整权重为 1；有 k 家学术伙伴的论文，每家分得 1/k。仅腾讯论文没有学术连接，因此分数贡献合计为 31，不是 32。不按引用加权。"),
        ("身份与角色", "保留作者顺序。重复名字不证明个人身份、领导权、经费或智力／工程分工。中文版仅对经一手来源核实的作者增加中文名，并保留英文名，不覆盖原始元数据。"),
        ("地理", "使用发表时署名机构，并以出版商或官方机构地址支持。坐标为近似城市锚点；母机构归并隐藏校区细节。一家机构城市未确定。地理位置不代表国籍。"),
        ("结果", "指标由作者报告，未独立复现实验。生产、原型、仿真及实验目标分别标注，不将不同基线、负载或资源结果合成通用分数。"),
        ("证据质量", "27 篇正式论文的作者映射经 PDF 核查，5 篇经出版商存档核查；32 篇均有完整、可溯源摘要。五篇缺失最终 PDF 的实现／角色结论仍受限；Dorado、Holmes 的来源差异保留记录。")]
    body += ''.join(f'<li><strong>{title}。</strong>{text}</li>' for title,text in methods)+'</ol><h3>敏感性与审计轨迹</h3><p>移除 Hestia 后剩 31 篇，并移除唯一的中科大连接。若以最终会议日程替代 Dorado 的三处有冲突的出版商映射，该篇的国科大连接将改为中关村实验室，Heng Yu 的机构由清华改为中关村；其他作者仍保留清华。这影响机构归属，不影响论文总量或中国／国际足迹。</p><p class="small">规范化修正：“School of Computer Science and Technology”是中科大署名内部院系，不是独立机构。香港城大、香港大学、香港中文大学及港中大（深圳）不合并。大学／实验室联合署名保留在原始元数据中。</p><div class="downloads"><a href="tencent_networking_metadata.xlsx">精简元数据工作簿</a><a href="tencent_networking_publications.xlsx">完整审计工作簿</a><a href="analysis_topic_partition.csv">主题图表数据</a><a href="analysis_partners.csv">机构／地理数据</a><a href="analysis_paper_evidence.csv">英文原始论文注释</a><a href="../data/analysis_results.json">完整聚合结果 JSON</a></div></section>'
    body += '<section id="evidence"><div class="section-number">07 / 逐篇证据</div><h2>检查叙事背后的每篇论文</h2><p>支持题目、年份、主题、中英文作者姓名和机构搜索。每张卡片区分作者报告结果与分析解读；论文标题和系统名保留英文方便检索。原始英文注释及元数据疑点也可展开核对。</p><label for="paper-search">搜索 32 篇论文证据附录</label><input id="paper-search" type="search" placeholder="例如：MoE、2026、清华、孟子立、云游戏……"><p id="search-count" aria-live="polite">显示 32 篇论文</p><div class="paper-cards">'
    for p in papers:
        author_names = p["authors_ordered"].split("; ")
        displayed = '；'.join(person(a) for a in author_names)
        affiliations = '；'.join(inst(i) for i in p["partners"])
        search = ' '.join([p["title"],str(p["year"]),p["short"],topic_label[p["topic"]],topics[p["topic"]]["label"],displayed,p["authors_ordered"],affiliations,'; '.join(p["partners"]),' '.join(TAGS.get(t,t) for t in p["tags"]),' '.join(p["tags"])])
        body += f'<article class="paper-card" id="paper-{p["paper_id"]}" data-search="{esc(search.casefold())}"><div class="paper-card-meta">{esc(p["venue"])} {p["year"]} · {esc(topic_label[p["topic"]])}</div><h3 lang="en">{esc(p["title"])}</h3>'
        for label,value in zip(["机制","作者报告结果","评估语境","分析解读"],p["zh"]):
            body += f'<p><strong>{label}。</strong>{esc(value)}</p>'
        status={"pdf_verified":"经 PDF 核查","publisher_deposit_verified":"经出版商记录核查"}[p["affiliation_status"]]
        body += f'<p class="small"><strong>高校／研究机构：</strong>{esc(affiliations or "未列出（仅腾讯）")}</p><p class="small"><strong>其他企业：</strong>{esc("；".join(inst(i) for i in p["industry_partners"]) or "未列出")}</p><details><summary>有序作者名单、核查状态与原始元数据疑点</summary><p class="small">{esc(displayed)}</p><p class="small">机构核查状态：{status}。以下原始疑点按英文保留，以避免翻译改变来源差异的含义。</p><p class="small" lang="en">{esc(p["metadata_notes"]) if p["metadata_notes"] else "未记录额外来源差异。"}</p></details><details><summary>核对英文原始分析注释</summary><div lang="en">'
        for label,key in [("Mechanism","mechanism"),("Reported result","result"),("Evaluation context","evaluation"),("Analyst interpretation","implication")]:
            body += f'<p><strong>{label}.</strong> {esc(p[key])}</p>'
        body += f'</div></details><div class="paper-links"><a href="{esc(p["paper_url"])}">论文／DOI ↗</a><a href="{esc(p["abstract_source"])}">结果来源 ↗</a>'
        if p["pdf_url"]: body += f'<a href="{esc(p["pdf_url"])}">PDF 链接 ↗</a>'
        body += f'<span class="badge">{esc(DEPLOYMENTS[p["deployment"]])}</span></div></article>'
    body += '</div></section><section id="verified-names"><div class="section-number">08 / 中文姓名核验</div><h2>只使用已确认的中文名</h2><p>以下 8 位作者的中文名已通过本人／机构一手来源核实，结合署名机构、邮箱或同篇论文确认对应关系。中文仅用于本项目展示，不回填历史任职，也不将其他同名者自动合并。未确认的作者保留英文；例如 Congcong Miao 的检索出现其他领域同名者，故不猜写中文。</p>'
    body += table(["英文署名","已核实中文名","一手来源","核验依据"],[[esc(name),esc(record["zh"]),f'<a href="{esc(record["source_url"])}">本人／机构主页 ↗</a>'+ (f' · <a href="{esc(record["secondary_source_url"])}">交叉来源 ↗</a>' if record.get("secondary_source_url") else ''),esc(record["evidence"])] for name,record in names.items()])
    body += '</section><footer>师爷编制 · 项目分析，非腾讯官方声明。基于核查元数据与可审计注释。图表嵌入中文字体轮廓，离线无需外部 JavaScript、字体下载或图表服务。Natural Earth 底图为公有领域。中文版保留英文原版与原始元数据。</footer></main></div>'
    css=(ROOT/"scripts/report_style.css").read_text()+'''body{font-family:"Noto Sans CJK SC","Microsoft YaHei","PingFang SC",sans-serif;line-height:1.85}h1,h2,h3,h4{font-family:inherit;line-height:1.4;letter-spacing:0}h1{max-width:16em}h2{max-width:28em}.hero .subtitle{max-width:42em}.hero a{color:#a4d9d0}.roster{line-height:2}.stats span{line-height:1.6}.paper-card h3{font-family:system-ui,sans-serif}.badge{white-space:normal}nav a{line-height:1.5}'''
    script="""const search=document.querySelector('#paper-search');const cards=[...document.querySelectorAll('.paper-card')];const count=()=>{document.querySelector('#search-count').textContent='显示 '+cards.filter(c=>!c.hidden).length+' 篇论文';};search.addEventListener('input',()=>{const q=search.value.toLocaleLowerCase().trim();cards.forEach(c=>c.hidden=!c.dataset.search.includes(q));count();});document.querySelectorAll('a[href^="#paper-"]').forEach(a=>a.addEventListener('click',()=>{search.value='';cards.forEach(c=>c.hidden=false);count();}));"""
    return f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="腾讯网络研究主题、演进与学术合作网络的证据驱动分析（2019—2026）。"><title>{esc(content["title"])}</title><style>{css}</style></head><body><a class="skip-link" href="#main">跳转至报告</a>{body}<script>{script}</script></body></html>'


def main():
    english_path=OUT/"tencent_networking_report.html"
    before=hashlib.sha256(english_path.read_bytes()).hexdigest()
    tables,topics,english_content,geography,papers=br.load_inputs()
    results=read_json("analysis_results.json")
    translations=read_json("analysis_papers_zh.json")
    names=read_json("author_names_zh.json")["names"]
    assert set(translations)-{"_schema"} == {p["short"] for p in papers}
    for p in papers:
        p["zh"]=translations[p["short"]]
        assert len(p["zh"])==4
    # Read the exact cached map used by the English report; never fetch or mutate sources.
    world=json.loads((ROOT/results["map_source"]["cache_file"]).read_bytes())
    localize_figures(results,papers,topics,world)
    report=render(results,papers,topics,read_json("report_content_zh.json"),english_content,names,tables["Author_Affiliations"])
    target=OUT/"tencent_networking_report_zh.html"
    target.write_text(report,encoding="utf-8")
    assert hashlib.sha256(english_path.read_bytes()).hexdigest()==before
    print(json.dumps({"report":str(target.relative_to(ROOT)),"papers":len(papers),"figures":7,"verified_chinese_names":len(names),"english_unchanged_sha256":before},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
