# C1 翻译质量抽检报告（自动生成）

> 生成脚本：`pipeline/05_qa.py`　｜　扫描目录：`C1/翻译/`　｜　译稿数：**33**

本报告只做**信号提示**，不自动判合格；`⚠` 项需人工确认。

## 1. 覆盖度

- 清单中可译条目：**33** 篇
- 已产出译稿：**33** 篇
- **覆盖率：100.0%**（验收要求 ≥ 80%）

✅ 清单内所有可译条目均已产出译稿。

## 2. 禁用译法扫描

✅ 未命中任何禁用译法（术语一致性检查通过）。

## 3. 结构完整性（实质小节数比对）

> 只统计**后面跟着正文**的小节标题；站点导航标题（Related posts / Company 等）已排除，
> 否则会误判成漏译。详见脚本顶部说明。

| 文件 | 原文实质小节 | 译文小节 | 比例 |
|---|---|---|---|
| 01-代码评审去做就对了.md | 7 | 0 | 0.00 ⚠ |

## 4. 篇幅抽查

下限 = 原文词数 × 0.75（低于此值疑似漏译）。

✅ 全部 33 篇译稿篇幅均在阈值之上（漏译风险低）。

## 5. 术语表待回填

译者在正文里标记了 **205** 个 glossary 未覆盖的新词（已去重）：

| 出现在 | NEW-TERM |
|---|---|
| 01-CS146S课程总览与教学大纲.md | `playground | 练习场 | 出现于第 1 周作业「LLM 提示词练习场（Playground）」` |
| 02-OpenAI如何使用Codex.md | `hot path | 热路径` |
| 02-OpenAI如何使用Codex.md | `boilerplate | 样板代码` |
| 02-OpenAI如何使用Codex.md | `cold-start problem | 冷启动问题` |
| 02-OpenAI如何使用Codex.md | `drive-by fix | 顺手修复` |
| 02-OpenAI如何使用Codex.md | `mono-repo | 单体仓库` |
| 02-OpenAI如何使用Codex.md | `property-based test | 基于性质的测试` |
| 02-OpenAI如何使用Codex.md | `triage | 分诊` |
| 01-模型上下文协议MCP简介.md | `host application | 宿主应用` |
| 01-模型上下文协议MCP简介.md | `Dynamic Client Registration (DCR) | 动态客户端注册（DCR）` |
| 02-远程MCP服务器认证.md | `elicitation | 服务端向用户征询补充信息（暂保留英文 elicitation）` |
| 02-远程MCP服务器认证.md | `Streamable HTTP transport | Streamable HTTP 传输方式` |
| 03-MCP注册表预览.md | `source of truth | 单一权威来源` |
| 03-MCP注册表预览.md | `sub-registry | 子注册表` |
| 03-MCP注册表预览.md | `denylist | 拒绝名单` |
| 03-MCP注册表预览.md | `opinionated | 有主见的` |
| 04-API并不是好的MCP工具.md | `tool chaining | 工具链式调用` |
| 01-规格是新的源代码.md | `PM | 产品经理 | 出现于第 1 段` |
| 01-规格是新的源代码.md | `MVP | 最小可行产品 | 出现于「等等，原型不是已经把规格杀死了吗？」第 1 段` |
| 01-规格是新的源代码.md | `object code | 目标代码 | 出现于「规格——新的源代码」第 1 段` |
| 01-规格是新的源代码.md | `wireframe | 线框图 | 出现于「等等，原型不是已经把规格杀死了吗？」第 1 段` |
| 01-规格是新的源代码.md | `landing page | 落地页 | 出现于「规格驱动开发的实战」第 3 段` |
| 01-规格是新的源代码.md | `IDE | 集成开发环境 | 出现于「规格驱动开发的实战」配置清单` |
| 01-规格是新的源代码.md | `ticket | 工单 | 出现于「规格驱动开发的实战」配置清单` |
| 01-规格是新的源代码.md | `lossy projection | 有损投影 | 出现于「规格——新的源代码」第 7 段` |
| 02-长上下文为何失效.md | `context poisoning | 上下文毒化 | 出现于「上下文失效」列表第 1 项` |
| 02-长上下文为何失效.md | `context distraction | 上下文干扰 | 出现于「上下文失效」列表第 2 项` |
| 02-长上下文为何失效.md | `context confusion | 上下文混淆 | 出现于「上下文失效」列表第 3 项` |
| 02-长上下文为何失效.md | `context clash | 上下文冲突 | 出现于「上下文失效」列表第 4 项` |
| 02-长上下文为何失效.md | `leaderboard | 排行榜 | 出现于「上下文混淆」第 3 段` |
| 02-长上下文为何失效.md | `summarization | 摘要 | 出现于「上下文干扰」第 5 段` |
| 02-长上下文为何失效.md | `fact retrieval | 事实检索 | 出现于「上下文干扰」第 5 段` |
| 02-长上下文为何失效.md | `context quarantine | 上下文隔离区 | 出现于倒数第 3 段` |
| 02-长上下文为何失效.md | `frontier model | 前沿模型 | 出现于正文第 1 段` |
| 02-长上下文为何失效.md | `reasoning model | 推理模型 | 出现于「上下文混淆」第 5 段` |
| 02-长上下文为何失效.md | `quantized | 量化 | 出现于「上下文混淆」第 4 段` |
| 02-长上下文为何失效.md | `shard | 分片 | 出现于「上下文冲突」第 3 段` |
| 03-Devin编程智能体入门101.md | `playbook | playbook | 出现于「自动化工作流」小节脚注 2` |
| 03-Devin编程智能体入门101.md | `bisect | 二分定位 | 出现于「把你的杂活交出去」小节` |
| 03-Devin编程智能体入门101.md | `feature flag | 功能开关 | 出现于「为最重复的工作创建快捷方式」小节` |
| 03-Devin编程智能体入门101.md | `staging environment | 预发布环境 | 出现于「给它一个开发 / 预发布环境」小节标题` |
| 04-为智能体编写有效的工具.md | `affordance | 可供性 | 出现于「为智能体选择合适的工具」第 2 段` |
| 04-为智能体编写有效的工具.md | `namespacing | 命名空间 | 出现于「如何编写工具」开头的列表、「为工具分命名空间」小节` |
| 04-为智能体编写有效的工具.md | `transcript | 对话记录 | 出现于「分析结果」第 2 段` |
| 04-为智能体编写有效的工具.md | `held-out test set | 留出测试集 | 出现于「分析结果」上游图片说明、「与智能体协作」第 3 段` |
| 04-为智能体编写有效的工具.md | `verifier | 验证器 | 出现于「生成评测任务」末段` |
| 04-为智能体编写有效的工具.md | `interleaved thinking | 交错思考 | 出现于「运行评测」第 4 段` |
| 04-为智能体编写有效的工具.md | `agentic loop | 智能体循环 | 出现于「运行评测」第 1 段` |
| 04-为智能体编写有效的工具.md | `tool annotations | 工具注解 | 出现于「对工具描述做提示工程」末段` |
| 01-Anthropic如何使用Claude-Code.md | `inference | 推理 | 出现于目录及第 4 节标题，首现作「推理（inference）」` |
| 01-Anthropic如何使用Claude-Code.md | `runbook | 运行手册 | 出现于第 3 节「文档综合与运行手册」` |
| 01-Anthropic如何使用Claude-Code.md | `monorepo | 单体仓库 | 出现于第 2 节「探索代码库」、第 3 节建议` |
| 01-Anthropic如何使用Claude-Code.md | `dogfooding | 吃自家狗粮 | 出现于第 6 节「通过吃自家狗粮（dogfooding）测试模型迭代」` |
| 01-Anthropic如何使用Claude-Code.md | `stack trace | 堆栈跟踪 | 出现于第 3 节「复杂的基础设施调试」` |
| 01-Anthropic如何使用Claude-Code.md | `checkpoint | 检查点 | 出现于第 2 节、第 9 节` |
| 01-Anthropic如何使用Claude-Code.md | `RL | 强化学习 | 出现于目录及第 9 节标题` |
| 01-Anthropic如何使用Claude-Code.md | `phone tree | 电话树 | 出现于第 10 节「法务部门工作流自动化」` |
| 01-Anthropic如何使用Claude-Code.md | `time-to-resolution | 解决时间 | 出现于第 3 节「复杂的基础设施调试」及团队影响` |
| 01-Anthropic如何使用Claude-Code.md | `weight transfer | 权重传输 | 出现于第 9 节标题段及用例` |
| 01-Anthropic如何使用Claude-Code.md | `call stack | 调用栈 | 出现于第 9 节「理解代码库与分析调用栈」` |
| 01-Anthropic如何使用Claude-Code.md | `slot machine | 老虎机 | 出现于第 5 节「处理重复性的重构任务」与建议` |
| 01-Anthropic如何使用Claude-Code.md | `creative | 创意 | 出现于第 7 节 Google Ads 相关用例与团队影响` |
| 01-Anthropic如何使用Claude-Code.md | `performance marketing | 效果营销 | 出现于第 7 节首段` |
| 01-Anthropic如何使用Claude-Code.md | `ROI | 投资回报率 | 出现于第 7 节「用于广告系列分析的 Meta Ads MCP 服务器」，原文直接用缩写 ROI` |
| 01-Anthropic如何使用Claude-Code.md | `edge case | 边缘用例 | 出现于第 4、8 节` |
| 01-Anthropic如何使用Claude-Code.md | `state management | 状态管理 | 出现于第 8 节「前端打磨与状态管理改动」` |
| 01-Anthropic如何使用Claude-Code.md | `GA launch | GA 发布 | 出现于第 8 节团队影响「周期从数周变成数小时」，GA = general availability` |
| 02-Claude-Code最佳实践.md | `classifier model | 分类器模型` |
| 02-Claude-Code最佳实践.md | `fixture | 基准文件（fixture）` |
| 02-Claude-Code最佳实践.md | `finding | 发现（finding）` |
| 02-Claude-Code最佳实践.md | `worktree | worktree（工作树，保留英文）` |
| 02-Claude-Code最佳实践.md | `fan-out | 扇出（fan-out）` |
| 01-Warp与Claude-Code对比.md | `Agentic Development Environment | 智能体化开发环境` |
| 01-Warp与Claude-Code对比.md | `orchestration platform | 编排平台` |
| 01-Warp与Claude-Code对比.md | `Agent Modality | 智能体模态` |
| 01-Warp与Claude-Code对比.md | `webhook | webhook` |
| 01-Warp与Claude-Code对比.md | `Zero Data Retention | 零数据保留` |
| 02-Warp如何用Warp构建Warp.md | `one-shot | 一次性完成` |
| 02-Warp如何用Warp构建Warp.md | `anti-pattern | 反模式` |
| 02-Warp如何用Warp构建Warp.md | `panic | panic` |
| 01-SAST与DAST.md | `RASP (Runtime Application Self-Protection) | 运行时应用自我保护 | 出现于「用 RASP 作为 SAST 和 DAST 的替代方案」` |
| 01-SAST与DAST.md | `false positive | 误报 | 出现于「SAST 与 DAST：关键区别」对照表` |
| 01-SAST与DAST.md | `false negative | 漏报 | 出现于「SAST 与 DAST：关键区别」对照表` |
| 01-SAST与DAST.md | `path traversal | 路径遍历 | 出现于「什么时候用 SAST」` |
| 01-SAST与DAST.md | `IAST | IAST（交互式应用安全测试，Interactive Application Security Testing）| 出现于「采用混合方案」` |
| 01-SAST与DAST.md | `false positive rate | 误报率 | 出现于「使用 DAST 工具时的性能考量」` |
| 02-通过提示注入实现Copilot远程代码执行.md | `YOLO mode | YOLO 模式 | 出现于「YOLO 模式」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `proof-of-concept | 概念验证 | 出现于「攻击链解析」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `payload | payload（载荷） | 出现于「攻击链解析」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `conditional prompt injection | 条件提示注入 | 出现于「攻击链解析」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `botnet | 僵尸网络 | 出现于「把工作站加入僵尸网络」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `ZombAI | ZombAI（僵尸 AI） | 出现于「把工作站加入僵尸网络」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `command and control server | 命令与控制服务器 | 出现于「把工作站加入僵尸网络」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `info stealer | 信息窃取程序 | 出现于「把工作站加入僵尸网络」小节` |
| 02-通过提示注入实现Copilot远程代码执行.md | `Patch Tuesday | 补丁星期二 | 出现于「负责任披露」小节` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `compaction | 压缩 | 出现于「同样的代码、同样的 AI，每次却报出不同的 bug」` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `taint tracking | 污点追踪 | 出现于 TL;DR 第 3 段` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `inter-procedural taint flow | 过程间污点流 | 出现于「回答我们的问题」` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `true positive rate | 真阳率 | 出现于 TL;DR 第 2 段` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `SARIF | SARIF（静态分析结果交换格式） | 出现于「本文的范围」` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `ASPM | ASPM（应用安全态势管理，Application Security Posture Management） | 出现于「同样的代码、同样的 AI」小节` |
| 03-用Claude-Code与Codex发现现代Web应用漏洞.md | `guardrails | 护栏 | 出现于「我们的发现」小节` |
| 04-AI智能体来了威胁也来了.md | `agentic application | 智能体化的应用 | 出现于「执行摘要」第 1 段` |
| 04-AI智能体来了威胁也来了.md | `defense-in-depth | 纵深防御 | 出现于「执行摘要·关键发现」末条` |
| 04-AI智能体来了威胁也来了.md | `prompt hardening | 提示词加固 | 出现于「执行摘要·关键发现」第 1 条` |
| 04-AI智能体来了威胁也来了.md | `content filtering | 内容过滤 | 出现于「执行摘要·关键发现」第 2 条` |
| 04-AI智能体来了威胁也来了.md | `tool input sanitization | 工具输入清洗 | 出现于「执行摘要·关键发现」第 3 条` |
| 04-AI智能体来了威胁也来了.md | `tool vulnerability scanning | 工具漏洞扫描 | 出现于「防护与缓解措施·工具漏洞扫描」` |
| 04-AI智能体来了威胁也来了.md | `code executor sandboxing | 代码执行器沙箱化 | 出现于「防护与缓解措施·代码执行器沙箱化」` |
| 04-AI智能体来了威胁也来了.md | `code interpreter | 代码解释器 | 出现于「AI 智能体模拟攻击」股票智能体` |
| 04-AI智能体来了威胁也来了.md | `tool schema | 工具模式 | 出现于「执行摘要·关键发现」第 1 条` |
| 04-AI智能体来了威胁也来了.md | `tool misuse | 工具滥用 | 出现于「AI 智能体的安全风险」列表第 2 项` |
| 04-AI智能体来了威胁也来了.md | `intent breaking and goal manipulation | 意图破坏与目标操纵 | 出现于「AI 智能体的安全风险」列表第 3 项` |
| 04-AI智能体来了威胁也来了.md | `identity spoofing and impersonation | 身份伪造与冒充 | 出现于「AI 智能体的安全风险」列表第 4 项` |
| 04-AI智能体来了威胁也来了.md | `agent communication poisoning | 智能体通信投毒 | 出现于「AI 智能体的安全风险」列表第 6 项` |
| 04-AI智能体来了威胁也来了.md | `resource overload | 资源过载 | 出现于「AI 智能体的安全风险」列表第 7 项` |
| 04-AI智能体来了威胁也来了.md | `agent hijacking | 智能体劫持 | 出现于「AI 智能体的安全风险」列表第 3 项` |
| 04-AI智能体来了威胁也来了.md | `orchestration agent | 编排智能体 | 出现于「AI 智能体模拟攻击」` |
| 04-AI智能体来了威胁也来了.md | `mounted volume | 挂载卷 | 出现于「通过挂载卷外泄敏感数据」` |
| 04-AI智能体来了威胁也来了.md | `least-privilege | 最小特权 | 出现于「执行摘要·关键发现」第 4 条` |
| 04-AI智能体来了威胁也来了.md | `syscall filtering | 系统调用过滤 | 出现于「执行摘要·关键发现」第 4 条` |
| 04-AI智能体来了威胁也来了.md | `data loss prevention (DLP) | 数据防泄漏 | 出现于「执行摘要·关键发现」第 5 条` |
| 04-AI智能体来了威胁也来了.md | `privilege escalation | 权限提升 | 出现于「执行摘要·关键发现」第 5 条` |
| 04-AI智能体来了威胁也来了.md | `lateral movement | 横向移动 | 出现于「代码执行器沙箱化」` |
| 04-AI智能体来了威胁也来了.md | `cryptojacking | 加密货币劫持挖矿 | 出现于「代码执行器沙箱化」最后一条` |
| 04-AI智能体来了威胁也来了.md | `arbitrary code execution | 任意代码执行 | 出现于「执行摘要·关键发现」第 4 条` |
| 04-AI智能体来了威胁也来了.md | `server-side request forgery (SSRF) | 服务端请求伪造 | 出现于「获得对内部网络的未授权访问·目标」` |
| 04-AI智能体来了威胁也来了.md | `metadata service | 元数据服务 | 出现于「通过元数据服务外泄服务账户访问令牌」` |
| 04-AI智能体来了威胁也来了.md | `service account | 服务账户 | 出现于「通过元数据服务外泄服务账户访问令牌」` |
| 04-AI智能体来了威胁也来了.md | `broken object-level authorization (BOLA) | 对象级授权失效 | 出现于表 1` |
| 04-AI智能体来了威胁也来了.md | `shadow AI | 影子 AI | 出现于「执行摘要」AI Access Security 段` |
| 05-OWASP-Top-10.md | `bug bounty | 漏洞赏金 | 出现于「目标」小节` |
| 05-OWASP-Top-10.md | `normalization | 归一化 | 出现于「目标」「流程」小节` |
| 05-OWASP-Top-10.md | `CWE | CWE | 出现于「数据结构」小节，保留英文缩写` |
| 05-OWASP-Top-10.md | `CWSS | CWSS | 出现于「流程」小节，保留英文缩写` |
| 05-OWASP-Top-10.md | `HaT | HaT | 出现于「注意」小节，保留英文缩写` |
| 05-OWASP-Top-10.md | `TaH | TaH | 出现于「注意」小节，保留英文缩写` |
| 05-OWASP-Top-10.md | `incidence rate | 发生率 | 出现于「流程」小节` |
| 06-上下文腐化.md | `haystack | 干草堆 | 首现于「大海捞针（NIAH）」说明段` |
| 06-上下文腐化.md | `needle | 针 | 首现于「大海捞针（NIAH）」说明段` |
| 06-上下文腐化.md | `LLM judge | LLM 裁判 | 首现于「细节」小节` |
| 06-上下文腐化.md | `abstention | 拒绝作答 | 首现于「干扰项的影响 · 结果」小节` |
| 06-上下文腐化.md | `cosine similarity | 余弦相似度 | 首现于「针—问题相似度」小节` |
| 06-上下文腐化.md | `normalized Levenshtein distance | 归一化 Levenshtein 距离 | 首现于「重复词 · 实验」小节` |
| 06-上下文腐化.md | `autoregressive | 自回归 | 首现于「重复词」小节` |
| 06-上下文腐化.md | `interpretability | 可解释性 | 首现于「干草堆结构 · 结果」小节` |
| 06-上下文腐化.md | `reranker | 重排序器 | 首现于「针—问题相似度 · 实验」小节` |
| 06-上下文腐化.md | `maximal marginal relevance | 最大边际相关 | 首现于「针—问题相似度 · 实验」小节` |
| 01-代码评审去做就对了.md | `peer review | 同行评审 | 出现于第 1 段` |
| 01-代码评审去做就对了.md | `walkthrough | 走查 | 出现于第 1 段引用块` |
| 01-代码评审去做就对了.md | `peer desk check | 同行桌面检查 | 出现于第 1 段引用块` |
| 01-代码评审去做就对了.md | `inspection | 检查 | 出现于第 1 段引用块` |
| 02-如何高效地评审代码.md | `staff engineer | 资深工程师` |
| 02-如何高效地评审代码.md | `code owner | 代码负责人` |
| 02-如何高效地评审代码.md | `first responder | 第一响应人` |
| 02-如何高效地评审代码.md | `notification fatigue | 通知疲劳` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `readability | 可读性 | Google 内部的形式化最佳实践机制名，全文首现处保留英文 readability` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `useful ratio | 有用率 | 第 4 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `shepherding | 全程照看 | 第 2.1 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `best practice | 最佳实践 | 全文` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `ground truth | 人工标注基准 | 第 3.3.1 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `intrinsic evaluation | 内在评测 | 第 3.3 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `extrinsic evaluation | 外部评测 | 第 6 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `beam search | 束搜索 | 第 4.1.2 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `readability mentor | readability 导师 | 第 2.2 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `teamfooding | 团队内测 | 第 4 节` |
| 03-现代代码评审中AI辅助的编码实践评估.md | `comment resolution rate | 评论解决率 | 第 5.1 节` |
| 04-AI代码评审最佳实践.md | `acceptance criteria | 验收标准 | 出现于「1. 明确预期」第 3 条` |
| 04-AI代码评审最佳实践.md | `N+1 query | N+1 查询 | 出现于「6. 性能优化」第 1 条` |
| 04-AI代码评审最佳实践.md | `on-premises | 本地部署 | 出现于常见问题第 5 条` |
| 05-软件团队的代码评审要点.md | `hierarchy of needs | 需求层次 | 出现于正文第 4 段` |
| 05-软件团队的代码评审要点.md | `mental model | 心智模型 | 出现于「让团队成员保持同步」第 1 段` |
| 05-软件团队的代码评审要点.md | `changeset | 改动集 | 出现于「发送拉取请求」第 6 段` |
| 05-软件团队的代码评审要点.md | `interface boundary | 接口边界 | 出现于「评审者：如何给出建设性反馈」第 9 段` |
| 05-软件团队的代码评审要点.md | `off-by-one | 差一 | 出现于「发送拉取请求」改进例子的改动摘要` |
| 05-软件团队的代码评审要点.md | `nitpick | 挑刺 | 出现于「提交一个好的拉取请求」第 3 段` |
| 06-数百万次AI代码评审的经验.md | `tribal knowledge | 部落知识` |
| 06-数百万次AI代码评审的经验.md | `fix forward | 向前修复` |
| 01-站点可靠性工程SRE导论.md | `sysadmin | 系统管理员` |
| 01-站点可靠性工程SRE导论.md | `pager | 值班手机` |
| 01-站点可靠性工程SRE导论.md | `Wheel of Misfortune | 厄运轮盘` |
| 01-站点可靠性工程SRE导论.md | `MTTF (mean time to failure) | 平均无故障时间` |
| 01-站点可靠性工程SRE导论.md | `phased rollout | 分阶段发布` |
| 01-站点可靠性工程SRE导论.md | `provisioning | 资源供给` |
| 01-站点可靠性工程SRE导论.md | `utilization | 利用率` |
| 01-站点可靠性工程SRE导论.md | `organic growth / inorganic growth | 自然增长 / 非自然增长` |
| 01-站点可靠性工程SRE导论.md | `blame-free postmortem culture | 无指责的事故复盘文化` |
| 01-站点可靠性工程SRE导论.md | `change gate | 变更关卡` |
| 01-站点可靠性工程SRE导论.md | `sharding | 分片` |
| 02-你应该知道的可观测性基础.md | `instrumentation | 插桩 | 出现于「OpenTelemetry：行业标准」一节` |
| 02-你应该知道的可观测性基础.md | `exemplar | 范例追踪链 | 出现于「追踪链、指标与日志之间的关联」一节` |
| 02-你应该知道的可观测性基础.md | `baggage | baggage | 出现于「错误处理与异常追踪」一节` |
| 02-你应该知道的可观测性基础.md | `high-cardinality | 高基数 | 出现于「追踪工具箱」一节` |
| 03-用AI排查Kubernetes故障.md | `noisy neighbor | 吵闹邻居 | 出现于第 2 段` |
| 05-多智能体系统在AI原生工程中的作用.md | `AI-native | AI 原生` |
| 05-多智能体系统在AI原生工程中的作用.md | `irreducible interdependence | 不可约的相互依赖` |
| 05-多智能体系统在AI原生工程中的作用.md | `orchestration | 编排` |
| 05-多智能体系统在AI原生工程中的作用.md | `stateful agent | 有状态的智能体` |
| 05-多智能体系统在AI原生工程中的作用.md | `coordination protocol | 协调协议` |
| 05-多智能体系统在AI原生工程中的作用.md | `race condition | 竞态条件` |
| 05-多智能体系统在AI原生工程中的作用.md | `deadlock | 死锁` |
| 05-多智能体系统在AI原生工程中的作用.md | `directed acyclic graph | 有向无环图` |
| 05-多智能体系统在AI原生工程中的作用.md | `connection pool | 连接池` |
| 05-多智能体系统在AI原生工程中的作用.md | `auto-scaling | 自动扩缩容` |
| 05-多智能体系统在AI原生工程中的作用.md | `incident lifecycle | 事故生命周期` |

## 6. 逐篇明细

| 译稿 | 中文字符 | 原文词数 | 原文实质小节 | 译文小节 |
|---|---|---|---|---|
| C1/翻译/week00-课程总览/01-CS146S课程总览与教学大纲.md | 1,847 | 1,216 | 13 | 63 |
| C1/翻译/week01-LLM与提示工程/01-什么是提示工程.md | 5,549 | 3,558 | 24 | 36 |
| C1/翻译/week01-LLM与提示工程/03-提示工程指南-核心技术.md | 161 | 82 | 0 | 0 |
| C1/翻译/week01-LLM与提示工程/02-OpenAI如何使用Codex.md | 3,346 | 2,024 | 0 | 18 |
| C1/翻译/week02-编程智能体与MCP/01-模型上下文协议MCP简介.md | 7,122 | 4,846 | 14 | 15 |
| C1/翻译/week02-编程智能体与MCP/02-远程MCP服务器认证.md | 2,204 | 1,905 | 12 | 13 |
| C1/翻译/week02-编程智能体与MCP/03-MCP注册表预览.md | 1,349 | 811 | 2 | 5 |
| C1/翻译/week02-编程智能体与MCP/04-API并不是好的MCP工具.md | 1,062 | 784 | 5 | 5 |
| C1/翻译/week03-AI-IDE与上下文工程/01-规格是新的源代码.md | 3,275 | 1,950 | 6 | 7 |
| C1/翻译/week03-AI-IDE与上下文工程/02-长上下文为何失效.md | 2,929 | 1,602 | 6 | 6 |
| C1/翻译/week03-AI-IDE与上下文工程/03-Devin编程智能体入门101.md | 5,647 | 3,460 | 43 | 59 |
| C1/翻译/week03-AI-IDE与上下文工程/04-为智能体编写有效的工具.md | 5,538 | 3,332 | 12 | 13 |
| C1/翻译/week04-Claude-Code与智能体编码/01-Anthropic如何使用Claude-Code.md | 9,113 | 10,603 | 0 | 42 |
| C1/翻译/week04-Claude-Code与智能体编码/02-Claude-Code最佳实践.md | 7,602 | 5,191 | 29 | 31 |
| C1/翻译/week05-Warp与AI终端/01-Warp与Claude-Code对比.md | 1,086 | 604 | 7 | 8 |
| C1/翻译/week05-Warp与AI终端/02-Warp如何用Warp构建Warp.md | 1,760 | 1,187 | 0 | 13 |
| C1/翻译/week06-AI安全与漏洞检测/01-SAST与DAST.md | 4,806 | 3,041 | 24 | 24 |
| C1/翻译/week06-AI安全与漏洞检测/02-通过提示注入实现Copilot远程代码执行.md | 2,092 | 1,219 | 10 | 13 |
| C1/翻译/week06-AI安全与漏洞检测/03-用Claude-Code与Codex发现现代Web应用漏洞.md | 5,136 | 3,623 | 13 | 13 |
| C1/翻译/week06-AI安全与漏洞检测/04-AI智能体来了威胁也来了.md | 9,319 | 7,308 | 41 | 50 |
| C1/翻译/week06-AI安全与漏洞检测/05-OWASP-Top-10.md | 2,130 | 2,527 | 15 | 25 |
| C1/翻译/week06-AI安全与漏洞检测/06-上下文腐化.md | 12,443 | 7,584 | 22 | 42 |
| C1/翻译/week07-AI代码评审/01-代码评审去做就对了.md | 897 | 959 | 7 | 0 |
| C1/翻译/week07-AI代码评审/02-如何高效地评审代码.md | 5,109 | 3,391 | 15 | 17 |
| C1/翻译/week07-AI代码评审/03-现代代码评审中AI辅助的编码实践评估.md | 10,870 | 7,879 | 0 | 34 |
| C1/翻译/week07-AI代码评审/04-AI代码评审最佳实践.md | 3,254 | 2,024 | 27 | 31 |
| C1/翻译/week07-AI代码评审/05-软件团队的代码评审要点.md | 3,379 | 2,063 | 6 | 6 |
| C1/翻译/week07-AI代码评审/06-数百万次AI代码评审的经验.md | 3,156 | 2,737 | 0 | 7 |
| C1/翻译/week09-SRE与可观测性/01-站点可靠性工程SRE导论.md | 6,178 | 4,098 | 10 | 13 |
| C1/翻译/week09-SRE与可观测性/02-你应该知道的可观测性基础.md | 2,761 | 1,854 | 23 | 27 |
| C1/翻译/week09-SRE与可观测性/03-用AI排查Kubernetes故障.md | 2,200 | 1,412 | 7 | 16 |
| C1/翻译/week09-SRE与可观测性/04-智能体AI在值班工程中的价值.md | 1,475 | 986 | 4 | 11 |
| C1/翻译/week09-SRE与可观测性/05-多智能体系统在AI原生工程中的作用.md | 3,488 | 2,039 | 9 | 7 |
