# Claude Code 最佳实践

> **原文标题**：Best practices for Claude Code
> **原文来源**：https://code.claude.com/docs/en/best-practices
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week 4
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.3
> **覆盖**：全文完整翻译，未删节

---

Claude Code 是一个智能体化的编程环境。它不像聊天机器人那样答完问题就等着，Claude Code 能读你的文件、运行命令、做出修改，自主地把问题一路推进下去，你可以在旁边看着、随时纠偏，也可以干脆走开。这改变了你的工作方式。你不再是先自己写代码、再让 Claude 评审，而是描述你想要什么，由 Claude 想清楚怎么把东西建出来。Claude 会探索、规划、实现。但这种自主性仍然有学习曲线。Claude 在一定的约束下工作，这些约束你需要理解。本指南收录了一些在实践中行之有效的模式，它们来自 Anthropic 内部各团队的经验，也来自在各种代码库、语言和环境中使用 Claude Code 的工程师。智能体循环（agentic loop）如何运作，见《Claude Code 工作原理》。

多数最佳实践都基于同一个约束：Claude 的上下文窗口很快就会被填满，而随着它被填满，性能会下降。

Claude 的上下文窗口装着你的整个对话，包括每一条消息、Claude 读过的每一个文件，以及每一条命令输出。然而，它很快就会被填满。一次调试会话或一次代码库探索，就可能产生并消耗数万个 token。这一点很关键，因为随着上下文被填满，LLM 的性能会下降。当上下文窗口快要满时，Claude 可能开始「忘记」早先的指令，或者犯更多错误。上下文窗口是最重要的资源，必须管理好。

想看看会话在实践中是怎么被填满的，可以看一段交互式演示：启动时会加载什么，每读一次文件要花多少代价。用**自定义状态栏**持续跟踪上下文用量；关于减少 token 用量的策略，见《减少 token 用量》。

## 给 Claude 一个验证工作的办法

给 Claude 一个它能跑的检查：测试、构建、一张用来做对比的截图。这决定了你是得盯着这场会话，还是可以直接走开。

Claude 会在工作看起来做完时停下。如果没有一个它能跑的检查，「看起来做完了」就是唯一可用的信号，于是你就成了验证回路：每一个错误都要等你去发现。给 Claude 一个能产出通过或失败的东西，这个回路就会自己闭合。Claude 干活、跑检查、读结果，然后不断迭代，直到检查通过。这个检查可以是任何能在对话中返回 Claude 可读信号的东西：一个测试套件、一个构建退出码、一个 linter、一个把输出和基准文件（fixture）做比对的脚本，或者一张与设计稿对比的浏览器截图。在 Claude 自己的检查通过之后，你自己再跑一次 `/verify`，对着正在运行的应用确认这次改动。

| 策略 | 改前 | 改后 |
|---|---|---|
| 提供验证标准 | 「实现一个校验邮箱地址的函数」 | 「写一个 validateEmail 函数。示例测试用例：user@example.com 为 true，invalid 为 false，user@.com 为 false。实现完之后跑测试」 |
| 用肉眼验证 UI 改动 | 「把仪表盘做得好看一点」 | 「[粘贴截图] 实现这个设计。把结果截图并与原图对比。列出差异并逐条修复」 |
| 解决根因，而不是症状 | 「构建失败了」 | 「构建报了这样的错误：[粘贴错误]。修好它，并验证构建成功。解决根因，不要压制错误」 |

一旦这个检查存在了，接下来要决定它对「停止」的把关有多硬：

- **在一个提示词里**：让 Claude 在同一条消息里跑检查并迭代，就像上表那样。
- **跨一次会话**：把检查设为一个 `/goal` 条件。一个独立的评测器会在每一轮之后重新检查它，Claude 会一直干到目标被解决。如果 Claude 停滞了，Claude Code 最终会在目标仍然设定的情况下停止这次运行——见《/goal 的评测如何运作》。
- **作为确定性闸门**：一个 Stop 钩子把你的检查当脚本运行，并在它通过之前阻止这一轮结束。Stop 的输入（Stop input）涵盖了连续阻塞次数的上限。
- **借助第二意见**：一个验证子智能体，或者一个会检查自身发现结果的动态工作流，会让一个全新的模型尝试反驳这个结果，这样干活的智能体就不是给自己打分的那一个。

每一步都是在拿配置成本换注意力成本。提示词版本今天就能在任何任务上生效。`/goal` 版本和 Stop 钩子版本，才是让无人值守的运行也能正确收尾、不用你操心的东西。让 Claude 拿证据说话，而不是嘴上说成功：测试输出、它跑的命令以及返回了什么，或者结果截图。审阅证据比自己重跑一遍验证更快，而且对你没盯着看的会话同样管用。

## 先探索，再规划，最后写代码

把调研和规划与实现分开，避免解决错问题。

让 Claude 直接跳到写代码，可能产出解决错误问题的代码。用计划模式把探索和执行分开。推荐的工作流有四个阶段：

**1 Explore（探索）**

按 Shift+Tab，直到状态栏显示 ⏸ plan mode on，即进入计划模式；或者用 `claude --permission-mode plan` 启动会话。Claude 会读文件、回答问题，但不做修改。

```
claude (plan mode)
read /src/auth and understand how we handle sessions and login. also look at how we manage environment variables for secrets.
```

> 这段提示让 Claude 读懂 `/src/auth` 里会话与登录的处理方式，以及用于密钥的环境变量是怎么管理的。

**2 Plan（规划）**

让 Claude 写出一份详细的实现计划。

```
claude (plan mode)
I want to add Google OAuth. What files need to change? What's the session flow? Create a plan.
```

按 Ctrl+G，在文本编辑器里打开这份计划，在 Claude 继续之前直接编辑。

**3 Implement（实现）**

通过批准计划或按 Shift+Tab 退出计划模式，然后让 Claude 写代码，并对着它的计划做验证。

```
claude
implement the OAuth flow from your plan. write tests for the callback handler, run the test suite and fix any failures.
```

**4 Commit（提交）**

让 Claude 用描述性的提交信息提交，并创建一个 PR。

```
claude
commit with a descriptive message and open a PR
```

计划模式很有用，但也会带来额外开销。对于那些范围清楚、改动很小的任务（比如改个错别字、加一行日志、重命名一个变量），直接让 Claude 做就行。当你对方案没把握时，当这次改动会修改多个文件时，或者当你要改的代码你并不熟悉时，规划最有用。如果你能用一句话把差异（diff）说清楚，就跳过计划。

## 在提示词里提供具体的上下文

指令越精确，需要纠正的次数就越少。

Claude 能推断意图，但读不了你的心。指明确切的文件、说明约束、给出可以参考的示例模式。

| 策略 | 改前 | 改后 |
|---|---|---|
| 限定任务范围。指明哪个文件、什么场景，以及测试偏好。 | 「给 foo.py 加测试」 | 「给 foo.py 写一个测试，覆盖用户已登出这个边界情况。不要用 mock」 |
| 指向信息源。把 Claude 引向能回答问题的源。 | 「ExecutionFactory 的 api 为什么这么怪？」 | 「翻一翻 ExecutionFactory 的 git 历史，总结一下它的 api 是怎么变成今天这样的」 |
| 参考既有模式。把 Claude 指向你代码库里的模式。 | 「加一个日历组件」 | 「看看首页上现有的组件是怎么实现的，理解这些模式。HotDogWidget.php 是个好例子。照着这个模式实现一个新的日历组件，让用户可以选择月份，并前后翻页来选年份。除了代码库已经在用的库之外，不要用别的库，从头写」 |
| 描述症状。给出症状、可能的位置，以及「修好了」是什么样。 | 「修复登录 bug」 | 「用户反馈会话超时后登录失败。检查 src/auth/ 里的认证流程，尤其是 token 刷新。写一个能复现该问题的失败测试，然后修好它」 |

含糊的提示词在你探索、并且承担得起纠偏成本时很有用。像「这个文件你会怎么改进？」这样的提示词，能问出你本来想不到要问的东西。

### 提供丰富的内容

用 @ 引用文件、粘贴截图/图片，或者直接管道传入数据。

你可以用几种方式给 Claude 提供丰富的数据：

- 用 `@` 引用文件，而不是描述代码在哪。Claude 会在回答之前先读这个文件。
- 直接粘贴图片。把图片复制/粘贴或拖放进提示词。
- 给出文档和 API 参考的 URL。用 `/permissions` 把常用域名加入允许清单。
- 用管道传入数据，例如运行 `cat error.log | claude -p "explain this error"` 直接发送文件内容。
- 让 Claude 自己去取需要的东西。让 Claude 用 Bash 命令、MCP 工具或读文件的方式自行拉取上下文。

## 配置你的环境

几个设置步骤就能让 Claude Code 在你所有会话里都明显更有效。扩展功能的完整概览，以及每个功能该在什么时候用，见《扩展 Claude Code》。

### 写一份有效的 CLAUDE.md

运行 `/init`，基于你当前的项目结构生成一份 CLAUDE.md 起始文件，然后再逐步打磨。

CLAUDE.md 是一个特殊文件，Claude 在每次对话开始时都会读它。把 Bash 命令、代码风格和工作流规则写进去。这样 Claude 就获得了光看代码推断不出来的持久上下文。CLAUDE.md 没有规定的格式，但要保持简短、可读。例如：

```
CLAUDE.md

# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

运行 `/context` 确认 Claude 加载了这个文件。CLAUDE.md 每次会话都会加载，所以只放那些广泛适用的内容。对于那些只在某些时候相关的领域知识或工作流，改用技能（skills）。Claude 会按需加载它们，不会把每次对话都撑大。保持简洁。对每一行都问一句：「删掉这行会让 Claude 犯错吗？」如果不会，就删掉。臃肿的 CLAUDE.md 会让 Claude 忽略你真正想说的指令！

| ✅ 该写 | ❌ 不该写 |
|---|---|
| Claude 猜不出来的 Bash 命令 | Claude 读代码就能搞明白的东西 |
| 与默认值不同的代码风格规则 | Claude 已经知道的标准语言惯例 |
| 测试说明和偏好的测试运行器 | 详细的 API 文档（改成给文档链接） |
| 仓库礼仪（分支命名、PR 惯例） | 经常变动的信息 |
| 你项目特有的架构决策 | 长篇解释或教程 |
| 开发环境的怪癖（必需的环境变量） | 逐个文件地描述代码库 |
| 常见的坑或不显然的行为 | 「写干净的代码」这类不言自明的做法 |

如果 Claude 在你已经写了规则的情况下还是一直做你不想要的事，那多半是文件太长了，规则被淹没了。如果 Claude 问你一些 CLAUDE.md 里已经回答过的问题，那可能是措辞有歧义。把 CLAUDE.md 当作代码来对待：出问题时回头审它，定期删减，并通过观察 Claude 的行为是否真的改变来测试改动。对于已提交到仓库的 CLAUDE.md，运行 `/doctor`，Claude 会对它能从代码库推导出来的内容提出删减建议。如果 Claude 一直跳过某一条指令，只给那一行加上「IMPORTANT」这类强调。如果你强调了很多行，那就没有一行是突出的。把 CLAUDE.md 提交进 git，这样团队其他人都能贡献。这个文件的价值会随时间复利增长。CLAUDE.md 文件可以用 `@path/to/import` 语法导入其他文件。导入规则，以及 CLAUDE.md 文件可以放在哪些位置，见《CLAUDE.md 文件》。

### 配置权限

要想少弹提示又不放弃控制权，用 `/permissions` 预先批准你信任的工具，并用 `/sandbox` 让沙箱中的命令无需询问就能运行。想自己批准每一次编辑和命令时，切到 Manual 模式。

在 Claude Code v2.1.283 或更高版本中，auto 模式是交互式终端和 VS Code 会话内置的起始权限模式：由一个独立的分类器模型（classifier model）代替你审阅大多数操作，只拦截看起来有风险的那些，比如权限范围升级、未知的基础设施，或者由敌意内容驱动的操作。在更早的版本上，auto 模式只在 Pro、Max 和 Team 套餐上是内置的起始权限模式。在 Manual 模式下，Claude Code 在可能修改你系统的操作之前会先问你：写文件、Bash 命令、MCP 工具。这样安全，但很烦。到第十次批准时，你已经是在无脑点确认，而不是在审阅。在 Manual 模式下，有两个工具能减少这类打断，它们在 auto 模式下同样适用：

- **权限允许清单**：批准你确知安全的特定工具，比如 `npm run lint` 或 `git commit`
- **沙箱**：启用操作系统级别的隔离，限制文件系统和网络访问，让 Claude 在划定的边界内更自由地工作

更多内容见《权限模式》《权限规则》和《沙箱》。

### 使用 CLI 工具

让 Claude Code 在与外部服务交互时使用 `gh`、`aws`、`gcloud` 和 `sentry-cli` 这类 CLI 工具。

CLI 工具是与外部服务交互最省上下文的方式。如果你用 GitHub，就装上 `gh` CLI。Claude 知道怎么用它来创建 issue、开拉取请求、读评论。没有 `gh` 时，Claude 仍然能用 GitHub API，但未认证的请求经常会撞上速率限制。Claude 也擅长现学它还不认识的 CLI 工具。可以试试这样的提示词：`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### 连接 MCP 服务器

运行 `claude mcp add`，带上服务器名称以及 URL 或命令，就能连接 Notion、Figma 或你的数据库这类外部工具。例如：`claude mcp add --transport http notion https://mcp.notion.com/mcp`。

有了 MCP 服务器，你可以让 Claude 从 issue 跟踪器里实现功能、查询数据库、分析监控数据、集成 Figma 里的设计，以及自动化工作流。

### 设置钩子

对于那些必须每次发生、零例外的动作，用钩子（hooks）。

钩子会在 Claude 工作流的特定时间点自动运行脚本。与 CLAUDE.md 里偏建议性的指令不同，钩子是确定性的，能保证动作一定发生。Claude 可以替你写钩子。可以试试这样的提示词：「写一个在每次编辑文件后运行 eslint 的钩子」或「写一个阻止写入 migrations 目录的钩子」。直接编辑 `.claude/settings.json` 可以手动配置钩子，运行 `/hooks` 可以浏览已经配置了什么。

### 创建技能

在 `.claude/skills/` 里创建 SKILL.md 文件，给 Claude 提供领域知识和可复用的工作流。

技能用你项目、团队或领域特有的信息扩展 Claude 的知识。Claude 会在相关时自动应用它们，你也可以用 `/skill-name` 直接调用。要创建一个技能，就在 `.claude/skills/` 下新建一个目录，里面放一个 SKILL.md：

```
.claude/skills/api-conventions/SKILL.md

---
name: api-conventions
description: REST API design conventions for our services
---

# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

技能还能定义你直接调用的可重复工作流：

```
.claude/skills/fix-issue/SKILL.md

---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

运行 `/fix-issue 1234` 来调用它。对于那些有副作用、你想手动触发的工作流，用 `disable-model-invocation: true`。

### 创建自定义子智能体

在 `.claude/agents/` 里定义专门的助手，Claude 可以把孤立的任务委派给它们。

子智能体在自己的上下文里运行，有自己的允许工具集。对于要读很多文件、或者需要专门关注又不想弄乱主对话的任务，它们很有用。

```
.claude/agents/security-reviewer.md

---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---

You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

明确告诉 Claude 使用子智能体：「用一个子智能体来评审这段代码的安全问题。」

### 安装插件

运行 `/plugin` 浏览插件市场。插件能添加技能、工具和集成，无需配置。

插件把技能、钩子、子智能体和 MCP 服务器打包成一个可安装单元，来自社区和 Anthropic。如果你用的是带类型的语言，装一个代码智能（code intelligence）插件，让 Claude 获得精确的符号导航和编辑之后的自动错误检测。关于在技能、子智能体、钩子和 MCP 之间如何选择，见《扩展 Claude Code》。

## 有效沟通

像问另一位工程师那样向 Claude 提问；对于较大的功能，在开始实现之前，让 Claude 先访谈你并写出一份规格（spec）。

### 提问代码库相关的问题

问 Claude 那些你会问资深工程师的问题。

在熟悉一个新代码库时，用 Claude Code 来学习和探索。你可以问 Claude 那些你本来会问另一位工程师的问题：

- 日志是怎么工作的？
- 我怎么新建一个 API 端点？
- `foo.rs` 第 134 行的 `async move { ... }` 是做什么的？
- `CustomerOnboardingFlowImpl` 处理了哪些边界情况？
- 为什么第 333 行的这段代码调用 `foo()` 而不是 `bar()`？

这样使用 Claude Code 是一种有效的入职工作流，能缩短上手时间，也减轻其他工程师的负担。不需要什么特别的提示技巧：直接问就行。

### 让 Claude 访谈你

对于较大的功能，先让 Claude 访谈你。用一句最简的提示词开头，让 Claude 用 AskUserQuestion 工具来访谈你。

Claude 会问一些你可能还没考虑过的东西，包括技术实现、UI/UX、边界情况和权衡取舍。发送提示词之前，把 `[brief description]` 换成你的功能。

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool. Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered. Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

规格写完之后，开一个全新的会话去执行它。新会话拥有干净的上下文，完全聚焦于实现，而你也有一份写好的规格可以参照。最有用的规格是自包含的：它们点明涉及的文件和接口，说明哪些不在范围内，并以一个端到端验证步骤收尾，证明这个功能确实能用。花在把规格写精确上的时间，比花在盯着实现过程上的时间回报更高。

## 管理你的会话

对话是持久的，也是可回退的。好好利用这一点！

### 尽早、频繁地纠偏

一旦发现 Claude 跑偏，立刻纠正它。

最好的结果来自紧密的反馈回路。尽管 Claude 偶尔能一次就把问题解得很完美，但快速纠正它通常能更快得到更好的方案。

- **Esc**：按 Esc 键让 Claude 停在半个动作上。上下文会保留，所以你可以重新引导它。
- **Esc + Esc 或 `/rewind`**：按两次 Esc 或运行 `/rewind` 打开回退菜单，恢复之前的对话和代码状态，或者从选中的某条消息开始总结。
- **「撤销掉那个」**：让 Claude 回退它的改动。
- **`/clear`**：在不相关的任务之间重置上下文。上下文里塞满无关内容的长会话会降低性能。

如果在一次会话里你为同一个问题纠正 Claude 超过两次，说明上下文里已经塞满了失败的尝试。运行 `/clear`，把你学到的东西揉进一个更具体的提示词里重新开始。一个干净的会话配一个更好的提示词，几乎总是胜过一场积累了无数纠正的长会话。

### 激进地管理上下文

在不相关的任务之间运行 `/clear` 来重置上下文。

当你接近上下文上限时，Claude Code 会自动压缩对话历史，既保留重要的代码和决策，又腾出空间。在长会话中，Claude 的上下文窗口会被无关的对话、文件内容和命令填满。这会降低性能，有时还会让 Claude 分心。

- 在任务之间频繁使用 `/clear`，彻底重置上下文窗口
- 自动压缩被触发时，Claude 会总结最重要的内容，包括代码模式、文件状态和关键决策
- 想要更多控制权，可以运行 `/compact <instructions>`，比如 `/compact Focus on the API changes`
- 只压缩对话的一部分：用 Esc + Esc 或 `/rewind`，选中一条消息检查点，然后选「Summarize from here」（从这里往后总结）或「Summarize up to here」（总结到这里为止）。前者压缩从该点往后的消息，同时让更早的上下文保持原样；后者压缩更早的消息，同时把最近的消息完整保留。见回退菜单的总结选项。
- 在 CLAUDE.md 里用类似这样的指令自定义压缩行为：「压缩时，始终保留完整的已修改文件列表和所有测试命令」，以确保关键上下文能挺过总结
- 对于那些不需要留在上下文里的问题，用 `/btw`。答案永远不会进入对话历史，所以你可以查看一个细节而不让上下文变大。

### 用子智能体做调研

用「use subagents to investigate X」把调研委派出去。它们在独立的上下文里探索，让你主对话保持干净，专注于实现。

既然上下文是你的根本约束，就用子智能体把调研隔在上下文之外。当 Claude 调研一个代码库时，它会读很多文件，这些都会消耗你的上下文。子智能体在独立的上下文窗口里运行，只把摘要汇报回来：

```
Use subagents to investigate how our authentication system handles token refresh, and whether we have any existing OAuth utilities I should reuse.
```

你还可以在 Claude 实现完某个东西之后，用子智能体做验证。见「加一道对抗式评审」。

### 用检查点回退

你发出的每一条开启一轮对话的提示词都会创建一个检查点。你可以把对话、代码或两者都恢复到之前任意一个检查点。

Claude 在每次改动前会自动给文件做快照，这样检查点就能把它们恢复回来。双击 Escape 或运行 `/rewind` 打开回退菜单。你可以只恢复对话、只恢复代码、两者都恢复，或者从选中的某条消息开始总结。细节见《检查点》。你可以不必小心翼翼地规划每一步，而是让 Claude 去试一些有风险的做法。如果不行，回退，再换一种方式。检查点会和对话一起保存，所以你可以关掉终端，之后再恢复会话，仍然能回退。

检查点只跟踪通过 Claude 的文件编辑工具做出的改动。通过 Bash 命令或外部进程做出的改动不会被记录。这不是 git 的替代品。

### 恢复会话

用 `/rename` 给会话命名，把它们当作分支来用：每条工作线都有自己的持久上下文。

Claude Code 会把对话保存在本地，所以当一个任务跨多次坐下来做时，你不必重新解释上下文。运行 `claude --continue` 从上次停下的地方继续，或者运行 `claude --resume` 从列表里挑一个。给会话起描述性的名字，比如 `oauth-migration`，方便以后查找。恢复、分支和命名控制的完整集合见《管理会话》。

## 自动化与规模化

当你能熟练驾驭一个 Claude 之后，用并行会话、非交互模式和扇出（fan-out）模式把产出翻倍。

### 运行非交互模式

在 CI、pre-commit 钩子或脚本里用 `claude -p "prompt"`。加上 `--output-format stream-json --verbose` 可以得到流式 JSON 输出。

用 `claude -p "your prompt"`，你就能非交互地运行 Claude，不需要交互式提示符。除非你传 `--no-session-persistence`，否则这次运行仍然会创建一个可恢复的会话。非交互模式就是你用来把 Claude 集成进 CI 流水线、pre-commit 钩子或任何自动化工作流的方式。输出格式让你能用程序解析结果：纯文本、JSON 或流式 JSON。

```
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json --verbose
```

第一条命令打印纯文本。`json` 格式返回一个带 `result` 字段的 JSON 对象。`stream-json` 格式每行打印一个 JSON 对象，以一个 init 事件开头。

### 运行多个 Claude 会话

并行运行多个 Claude 会话，以加快开发、跑隔离的实验，或者启动复杂的工作流。

按你自己愿意投入多少协调工作，挑选合适的并行方式；当会话之间需要互相传递发现结果时，再加上消息机制：

- **Worktrees**：在隔离的 git 检出里运行各自的 CLI 会话，这样改动不会互相冲突
- **跨会话消息**：让你自己运行的会话之间互相传递发现结果
- **桌面应用**：可视化地管理多个本地会话，可选地让每个会话在自己的 worktree 里
- **在云端使用 Claude Code**：默认在 Anthropic 托管的基础设施上运行会话
- **Agent view**：研究预览。运行 `claude agents` 派发在后台持续运行的会话，并在一个界面里观察它们
- **Agent teams**：实验性功能，默认关闭。自动协调多个会话，共享任务、消息和一个团队负责人

除了并行化工作之外，多个会话还能实现以质量为中心的工作流。新鲜的上下文能改善代码评审，因为 Claude 不会对自己刚写的代码有偏向。例如，用「写手/评审者」模式：

| Session A（写手） | Session B（评审者） |
|---|---|
| 为我们的 API 端点实现一个限流器 | 评审 @src/middleware/rateLimiter.ts 里的限流器实现。找出边界情况、竞态条件，以及与我们既有中间件模式的一致性。 |
| 这是评审反馈：[Session B 的输出]。解决这些问题。 |  |

测试上也可以这么做：让一个 Claude 写测试，另一个 Claude 写代码让测试通过。

### 跨文件扇出

循环遍历任务，为每个任务调用 `claude -p`。用 `--allowedTools` 为批量操作预批准工具。

对于大规模迁移或分析，你可以把工作分发到许多并行的 Claude 调用上。运行 `/batch <instruction>`，让 Claude 把这次改动拆给 5 到 30 个子智能体。每个子智能体在自己的 worktree 里工作。想用你自己的脚本驱动扇出，就循环调用 `claude -p`：

**1 生成任务清单**

让 Claude 把需要迁移的文件列表写到一个文件里，这样下一步的循环就能读到它，提示词类似：`list all 2,000 Python files that need migrating and save the list to files.txt`

**2 写一个脚本遍历这个清单**

```
for file in $(cat files.txt); do
  claude -p "Migrate $file from Python 2 to Python 3. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)" \
    --permission-mode dontAsk
done
```

**3 先在几个文件上测试，再对全部运行**

根据前 2–3 个文件出的问题打磨你的提示词，然后再对全集运行。`--allowedTools` 标志预批准这次迁移需要的工具，`--permission-mode dontAsk` 会拒绝其他任何需要批准的东西——在你无人值守运行时，这一点很重要。

你还可以把 Claude 集成进既有的数据/处理流水线：

```
claude -p "<your prompt>" --output-format json | your_command
```

### 用 auto 模式自主运行

想要不被打断地执行，同时又有后台安全检查，就用 auto 模式。一个分类器模型会在命令运行之前审阅它们，拦下权限范围升级、未知基础设施和由敌意内容驱动的操作，同时让常规工作无需提示地继续。

```
claude --permission-mode auto -p "fix all lint errors"
```

当分类器在带 `-p` 标志的非交互运行中反复拦截操作时，Claude Code 不会停止这次运行。至于实际上会发生什么，以及阈值是多少，见《auto 模式何时回退》。

### 加一道对抗式评审

在把一个任务当作完成之前，让一个子智能体在干净的上下文里评审差异（diff）并报告缺口。

Claude 无人值守工作的时间越长，在你把工作算作完成之前，一道独立检查就越重要。评审者运行在全新的子智能体上下文里，它只看到差异和你给它的标准，看不到产生这次改动的推理过程，所以它会按自己的标准来评估结果。要做正确性检查，就运行内置的 `/code-review` 技能：它会在一个全新的子智能体里评审当前差异中的 bug，并把发现结果返回给会话。想改为拿差异对着你的计划来检查，就自己写评审提示词。点明要检查的工作、用来对照的计划，以及什么算一个发现（finding）：

```
Use a subagent to review the rate limiter diff against PLAN.md. Check that every requirement is implemented, the listed edge cases have tests, and nothing outside the task's scope changed. Report gaps, not style preferences.
```

因为评审者是以子智能体身份运行的，实现会话会直接收到这些缺口，可以修复它们并重新评审，不需要你在窗口之间来回粘贴发现结果。

一个被要求找缺口的评审者通常总能报出一些，哪怕工作本身没问题——因为这就是它被要求做的事。追着每个发现跑会导致过度工程：多余的抽象层、防御性代码，以及为不可能发生的情况写的测试。告诉评审者只标出那些影响正确性或既定需求的缺口，其余的当作可选项。

## 避免常见的失败模式

这些是常见的错误。早点认出它们能省下时间：

- **大杂烩会话。** 你一开始做一个任务，然后问 Claude 一件不相关的事，然后又回到第一个任务。上下文里塞满了无关信息。
  **修法**：在不相关的任务之间 `/clear`。
- **反复纠正。** Claude 做错了，你纠正它，还是错，你又纠正。上下文被失败的尝试污染了。
  **修法**：两次纠正失败之后，`/clear`，把你学到的东西揉进一个更好的初始提示词里。
- **过度写的 CLAUDE.md。** 如果你的 CLAUDE.md 太长，Claude 会忽略掉一半，因为重要的规则淹没在噪声里。
  **修法**：狠心删减。如果 Claude 在没有这条指令的情况下已经做对了，就删掉它，或者把它转成钩子。
- **先信任再验证的缺口。** Claude 产出一个看起来很合理的实现，但没处理边界情况。
  **修法**：始终提供验证手段（测试、脚本、截图）。如果你无法验证，就别交付。
- **无限探索。** 你让 Claude 去「调研」某件事，却没划定范围。Claude 读了上百个文件，把上下文填满。
  **修法**：把调研范围收窄，或者用子智能体，让探索不消耗你的主上下文。

## 培养你的直觉

本指南里的这些模式并非金科玉律。它们是普遍情况下好用的起点，但不一定对每种情形都是最优的。有时你该让上下文堆积，因为你正深陷一个复杂问题，历史很有价值。有时你该跳过规划，让 Claude 自己搞定，因为任务本身是探索性的。有时含糊的提示词恰恰是对的，因为你想先看看 Claude 怎么理解这个问题，再去约束它。留意什么有效。当 Claude 产出很好的结果时，注意你做了什么：提示词结构、你提供的上下文、你当时所处的模式。当 Claude 卡壳时，问问为什么。是上下文太嘈杂？提示词太含糊？还是任务太大，一次过不完？久而久之，你会培养出任何指南都捕捉不到的直觉。你会知道什么时候该具体、什么时候该放开，什么时候该规划、什么时候该探索，什么时候该清空上下文、什么时候该让它积累。

## 相关资源

- 《Claude Code 工作原理》：智能体循环、工具和上下文管理
- 《扩展 Claude Code》：技能、钩子、MCP、子智能体和插件
- 《常见工作流》：调试、测试、PR 等场景的逐步操作指南
- 《CLAUDE.md》：存放项目约定和持久上下文

<!-- NEW-TERM: classifier model | 分类器模型 -->
<!-- NEW-TERM: fixture | 基准文件（fixture） -->
<!-- NEW-TERM: finding | 发现（finding） -->
<!-- NEW-TERM: worktree | worktree（工作树，保留英文） -->
<!-- NEW-TERM: fan-out | 扇出（fan-out） -->
