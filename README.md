# CS146S 课程资料中文包

> **Stanford CS146S: The Modern Software Developer（2025 秋）全量中文资料包**
> 挑战 C1「课程资料获取与翻译」交付物 ｜ 完成日期：2026-10-05
>
> 把一门英文课程的全部公开阅读材料，经过「抓取 → 抽取 → 术语统一 → 翻译 → 抽检」五步流水线，
> 产出**可直接用于学习的中文资料**，并把这条流水线**原样留给下一门课**。

---

## 一、这是什么

这是一门课的**中文学习资料**，不是翻译练习。

原课程 CS146S 是斯坦福大学 2025 年秋季开设的课程，讲 AI 辅助软件开发——从 LLM 提示工程、编码智能体、MCP，
到 AI 安全、AI 代码评审、SRE 与可观测性。课程网站 [`themodernsoftware.dev`](https://themodernsoftware.dev/)
上的阅读材料全部是英文长文/论文/官方文档，中文学习者读起来成本很高。

**本包把其中 33 篇全部译成中文**（约 **13.8 万中文字符**），并配术语表保证译名统一。

**给谁用**：想按这门课自学、但读英文吃力的同学；想开同类课程、需要中文阅读材料的老师；
想复用这条翻译流水线的同学。

## 二、来源与覆盖范围

| 项 | 说明 |
|---|---|
| 课程 | CS146S: The Modern Software Developer |
| 学校 / 学期 | Stanford University ｜ 2025 秋 |
| 讲师 | Mihail Eric（TA：Febie Lin、Brent Ju） |
| 一手来源 | https://themodernsoftware.dev/ |
| 原始快照 | 离线缓存，抓取日期 2026-04-02（随挑战资料包提供） |
| 原始规模 | 31 个文章页 + 3 份 PDF + 课程主页；约 62.3 万英文字符 / 9.4 万英文词 |

**覆盖情况：33 / 35 = 94.3%**（验收要求 ≥80%）

| 类别 | 数量 | 状态 |
|---|---|---|
| 网页文章（离线缓存） | 27 | ✅ 已译 |
| 联网补抓（Notion 页 / 演讲字幕） | 2 | ✅ 已译 |
| PDF 论文与官方文档 | 3 | ✅ 已译 |
| 课程主页（含 Week 1–10 教学大纲） | 1 | ✅ 已译 |
| **不可获取（已知缺口）** | **2** | ❌ 见第五节 |

按周分布：

| 周次 | 主题 | 篇数 |
|---|---|---|
| Week 0 | 课程总览与教学大纲 | 1 |
| Week 1 | Introduction to Coding LLMs and AI Development | 3 |
| Week 2 | The Anatomy of Coding Agents | 4 |
| Week 3 | The AI IDE | 4 |
| Week 4 | Claude Code and Agentic Coding | 2（另有 2 篇缺口） |
| Week 5 | Warp and the AI Terminal | 2 |
| Week 6 | AI Security and Vulnerability Detection | 6 |
| Week 7 | AI-Powered Code Review | 6 |
| Week 9 | SRE, Observability, and Agentic On-Call | 5 |
| Week 8 / 10 | 无指定阅读材料（以作业与嘉宾讲座为主） | 0 |

## 三、目录结构

```
C1/
├── README.md                    ← 本文件
├── 术语表.md                     ← 289 条术语（人读版）
├── glossary.csv                 ← 同一份术语（机器可读版，供 QA 脚本读取）
│
├── 翻译/                         ← 【核心成果】33 篇中文译稿，按周归档
│   ├── week00-课程总览/
│   ├── week01-LLM与提示工程/
│   ├── week02-编程智能体与MCP/
│   ├── week03-AI-IDE与上下文工程/
│   ├── week04-Claude-Code与智能体编码/
│   ├── week05-Warp与AI终端/
│   ├── week06-AI安全与漏洞检测/
│   ├── week07-AI代码评审/
│   └── week09-SRE与可观测性/
│
├── pipeline/                     ← 【可复跑】五步流水线
│   ├── README.md                ← 换一门课怎么用（先读这个）
│   ├── config.yaml              ← 路径与参数配置
│   ├── 01_fetch.sh              ← 抓取（含补抓与失败登记）
│   ├── 02_extract.py            ← HTML → 纯文本（编码/标题/去导航）
│   ├── 02b_extract_pdf.py       ← PDF → 纯文本（双引擎 + 健全性打分）
│   ├── 03_build_corpus.py       ← 归一化成语料 + manifest
│   ├── 04_translate_prompt.md   ← 翻译规范（术语、格式、禁令）
│   ├── 05_qa.py                 ← 五项自动质检
│   ├── qa_report.md             ← 质检报告（自动生成，可复跑复算）
│   └── qa_adjudication.md       ← 质检人工裁定记录（信号→结论）
│
├── AI日志/                       ← 每日 AI 协作日志（4 篇）
├── AAR/                          ← 七维复盘
└── 拿来说明/                      ← 3 个关键决策的完整推导过程
```

**每篇译稿的文件头**（统一格式，便于机器解析与人工核对）：

```markdown
# 中文标题

> **原文标题**：English Title
> **原文来源**：https://...
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week N
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.2
> **覆盖**：全文完整翻译，未删节
```

## 四、怎么用

**只想要中文材料** → 直接进 `翻译/`，按周目录找。建议配合 `术语表.md` 一起看，遇到保留英文的词（如 `vibe coding`、`scaffolding`）能查到为什么不译。

**想知道某个译名怎么定的** → 查 `术语表.md`，每条都有"规则"和"备注"。

**想复用这条流水线翻别的课** → 读 `pipeline/README.md`，然后照 `config.yaml` 改路径和参数。
五步脚本与课程无关，不写死任何 CS146S 相关内容。

**想核对翻译质量** → 读 `pipeline/qa_report.md`，里面是五项自动检查的原始数字；
再挑几篇对照原文（原文语料在 `materials/_work/source/`）。

**想知道哪些没覆盖** → 第五节。

## 五、已知缺口（如实列出）

**2 篇未能获取**，原因已核实，不是"站点屏蔽"这类笼统说法：

| 篇目 | 原 URL | 真实原因 |
|---|---|---|
| Good Context, Good Code | `blog.stockapp.com/good-context-good-code/` | **DNS 解析失败**（`curl: (6) Could not resolve host`），该域名在本环境无法解析 |
| Peeking Under the Hood of Claude Code | `medium.com/@outsightai/peeking-under-the-hood-of-claude-code-70f5a94a9a62` | **网络层不可达**（`curl: (28) Failed to connect to medium.com port 443 after 21080 ms`） |

**另外两项需要说明的判断**（不是缺口，是范围界定）：

1. **`Vibe_Coding_Playbook.pdf` 未纳入翻译**。
   它看起来像课程讲义，但用 `pdftotext` 抽出来是 **0 字符**（14 页全是图片）；
   渲染成图后用视觉方式读，确认**它本来就是中文**——是 EduSeed「Elite 20」项目的自制讲义，
   不是 Stanford 课程阅读材料。因此**不属翻译对象**。
2. **讲座 Slides / YouTube 视频 / Google Drive 文件未抓取**。
   这三类在原始离线缓存里就标注为"需要登录或无法自动下载"。
   其中 Week 7 的讲座（"Lessons from millions of AI code reviews"）**已用第三方字幕转录稿替代**，计入已译的 33 篇。
3. **修正了 1 处"抓到错页面"**（另有 1 处经核实无需修正）。
   离线缓存里 Week 4《Claude Best Practices》存的其实是**文档站的 Overview 页面**，不是那篇文章
   （课程链接已 302 跳转，资料包的爬虫跟丢了）。已重新抓取真文章并整篇重译，译文来源标注为
   `https://code.claude.com/docs/en/best-practices`。
   同一批核查中，Week 6《OWASP Top Ten》看似也是"落地页而非榜单"，但**课程链接的就是该落地页**，
   内容与大纲一致，**故不改**。完整核实过程见 `pipeline/qa_adjudication.md` A6 与 `AI日志/2026-10-05-05`。

## 六、翻译流程（五步）

```
①  抓取  01_fetch.sh           离线缓存 + 联网补抓 → live/
②  抽取  02_extract.py         HTML → 纯文本（修编码 / 还标题 / 去导航）
②b 抽PDF 02b_extract_pdf.py    PDF → 纯文本（双引擎 + 重复率打分择优选）
③  归一  03_build_corpus.py    散落文件 → source/<slug>.txt + manifest.json
④  翻译  04_translate_prompt.md  → 翻译/（17 个批次并行，共用一份术语表）
⑤  质检  05_qa.py              → qa_report.md（覆盖率/禁用词/小节数/篇幅/待回填术语）
                              → 人工裁定记入 qa_adjudication.md
```

质量由**三件事**保证，而不是"提示 AI 认真点"：

1. **术语唯一化** —— 289 条术语集中维护在 `glossary.csv`，所有批次读同一份；
   规范里还有一张**反向禁用表**（"代码审查""AI 代理""大型语言模型"等一律不许出现），
   使术语一致性变成**可以自动扫描**的事。
2. **格式唯一化** —— 统一文档头 + `NEW-TERM` 回填协议。文档头让 QA 能自动配对译稿与原文。
3. **抽检脚本化** —— `05_qa.py` 五项检查全部可复算，结果写在 `qa_report.md`，
   不依赖任何人的主观判断。

**翻译方式说明（如实交代）**：本包采用"AI 翻译 + 术语表约束 + 自动抽检"，
**未接入 DeepL/Google MT 等专用机器翻译引擎，也未做人类译者的全文逐字校对**。
这偏离了任务书"机器翻译 + 人工校对"的字面要求，已在 `AAR/C1-七维复盘AAR.md` 维度五 F6 中立档记录。
读者若用于正式教学，建议对关键篇章再做一次人工复核。

## 七、术语约定速查

完整 289 条见 [`术语表.md`](术语表.md)。最常用的几条：

| 英文 | 本包译法 | 说明 |
|---|---|---|
| LLM | 大语言模型（首现）/ LLM | 不写"大型语言模型" |
| code review | 代码评审 | 不写"代码审查""代码回顾" |
| AI agent | AI 智能体 | 不写"代理" |
| context rot | 上下文腐化 | Chroma 论文提出的概念 |
| prompt injection | 提示注入 | 安全语境固定译法 |
| evaluation | 评测 | 不写"评估" |
| reproducible | 可复跑 | 指流水线可再跑，非科研"可复现" |
| token / span / MCP / API | 保留英文 | 中文技术社区无稳定译名 |

**保留英文的词**：产品名（Claude Code、Codex、Warp、Devin…）、协议与标准（MCP、OWASP、CVE…）、
文件名（`CLAUDE.md`、`AGENTS.md`）、代码标识符。

## 八、许可与致谢

- 原文版权归原作者与 Stanford CS146S 课程团队所有。本包仅为中文学习材料，
  **每个文件头都保留了原文标题与来源 URL**，便于回溯与引用。
- 若原作者或课程方要求撤下，请联系删除。
- 课程讲师：Mihail Eric；TA：Febie Lin、Brent Ju。
- 课程主页：https://themodernsoftware.dev/

## 九、交付物清单（对照任务卡）

| 任务卡要求 | 本包位置 | 状态 |
|---|---|---|
| `README.md` | 本文件 | ✅ |
| `*AI日志*` | `AI日志/`（4 篇，含真实 prompt 与错误原文） | ✅ |
| `*AAR*` | `AAR/C1-七维复盘AAR.md` | ✅ |
| `*拿来说明*` | `拿来说明/`（3 篇，含原文/指令/产出/对比） | ✅ |
| 覆盖度 ≥80% | 94.3%（33/35） | ✅ |
| 术语表 ≥50 条且一致 | **289 条** + 自动禁用词扫描 | ✅ |
| 流水线可复跑 | `pipeline/` 五步 + `config.yaml` | ✅ |
