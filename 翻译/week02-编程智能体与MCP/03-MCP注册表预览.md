# MCP 注册表预览

> **原文标题**：MCP Registry Preview
> **原文来源**：https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week 2
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.3
> **覆盖**：全文完整翻译，未删节

---

今天，我们推出模型上下文协议（MCP）注册表——一个面向公开可用 MCP 服务器的开放目录与 API，用于改善可发现性与实现。通过标准化服务器的分发与发现方式，我们扩大了它们的覆盖范围，同时让客户端更容易建立连接。

MCP 注册表现已开放预览。要开始使用：

- 按照《向 MCP 注册表添加服务器》指南添加你的服务器（面向服务器维护者）
- 按照《访问 MCP 注册表数据》指南访问服务器数据（面向客户端维护者）

## MCP 服务器的单一权威来源

2025 年 3 月，我们曾分享过，我们想为 MCP 生态构建一个中心注册表。今天我们宣布，我们已上线 https://registry.modelcontextprotocol.io，作为官方的 MCP 注册表。作为 MCP 项目的一部分，MCP 注册表以及一份上位 OpenAPI 规范都是开源的——任何人都可以据此构建兼容的子注册表。

我们的目标是标准化服务器的分发与发现方式，提供一个子注册表可以基于其构建的单一权威来源。反过来，这会扩大服务器的覆盖范围，帮助客户端在 MCP 生态中更容易地找到服务器。

### 公共与私有子注册表

在构建中心注册表时，对我们来说很重要的是，不要削弱社区和公司已经构建的现有注册表。MCP 注册表充当公开可用 MCP 服务器的单一权威来源，各组织可以选择按自定义标准创建子注册表。例如：

公共子注册表——比如与各个 MCP 客户端绑定的、有主见的「MCP 应用市场」——可以自由地增补和增强它们从上游 MCP 注册表引入的数据。每一种 MCP 终端用户画像的需求都不同，以有主见的方式恰当服务自己的终端用户，是 MCP 客户端应用市场分内的事。

私有子注册表会存在于对隐私和安全有严格要求的企业内部，但 MCP 注册表为这些企业提供了一个可以基于其构建的单一上游数据源。至少，我们希望能与这些私有实现共享 API schema，这样相关的 SDK 和工具就能在整个生态中共享。

在两种情况下，MCP 注册表都是起点——它是那个集中的位置，MCP 服务器维护者在此发布和维护自己申报的信息，供下游消费者加工并交付给各自的终端用户。

### 社区驱动的审核机制

MCP 注册表是一个官方 MCP 项目，由注册表工作组维护，采用宽松许可证。社区成员可以提交 issue 来举报违反 MCP 审核准则的服务器——例如包含垃圾信息、恶意代码，或者冒充合法服务的服务器。注册表维护者随后可以将这些条目列入拒绝名单（denylist），并追溯性地将其从公开访问中移除。

## 快速上手

要开始使用：

- 按照《向 MCP 注册表添加服务器》指南添加你的服务器（面向服务器维护者）
- 按照《访问 MCP 注册表数据》指南访问服务器数据（面向客户端维护者）

MCP 注册表的这次预览旨在帮助我们在正式可用之前改进用户体验，它不提供数据持久性保证或其他担保。我们建议 MCP 采用者密切关注开发进展，因为在注册表正式可用之前可能会出现破坏性变更。

随着我们继续开发注册表，我们鼓励大家在 modelcontextprotocol/registry GitHub 仓库上反馈和贡献：欢迎参与 Discussion（讨论）、提交 Issue 和拉取请求（PR）。

## 感谢 MCP 社区

MCP 注册表从一开始就是协作的成果，我们非常感谢广大开发者社区的热情与支持。

2025 年 2 月，它从一个草根项目开始，当时 MCP 的创造者 David Soria Parra 和 Justin Spahr-Summers 邀请 PulseMCP 和 Goose 团队帮助构建一个中心化的社区注册表。来自 PulseMCP 的注册表维护者 Tadas Antanavicius 与来自 Block 的 Alex Hancock 合作，牵头了最初的工作。很快，GitHub 的 MCP 负责人、注册表维护者 Toby Padilla 也加入进来；更近一些时候，来自 Anthropic 的 Adam Jones 作为注册表维护者加入，推动项目走向今天的发布。MCP 注册表开发工作的最初公告列出了来自至少 9 家不同公司的 16 位贡献者。

还有许多人为让这个项目落地做出了关键贡献：来自 Stacklok 的 Radoslav Dimitrov、来自 GitHub 的 Avinash Sridhar、来自 VS Code 的 Connor Peet、来自 NuGet 的 Joel Verhagen、来自 Last9 的 Preeti Dewani、来自 Microsoft 的 Avish Porwal、Jonathan Hefner，以及许多提供了代码评审和开发支持的 Anthropic 与 GitHub 员工。我们也感谢注册表贡献者名单上的每一位，以及参与讨论和 issue 的人。

我们深深感谢每一位为这一基础性开源基础设施投入的人。我们正在一起帮助全世界的开发者和组织构建更可靠、具备上下文感知的 AI 应用。谨代表 MCP 社区，谢谢大家。

<!-- NEW-TERM: source of truth | 单一权威来源 -->
<!-- NEW-TERM: sub-registry | 子注册表 -->
<!-- NEW-TERM: denylist | 拒绝名单 -->
<!-- NEW-TERM: opinionated | 有主见的 -->
