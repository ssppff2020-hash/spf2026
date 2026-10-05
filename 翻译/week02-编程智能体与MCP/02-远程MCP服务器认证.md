# 远程 MCP 服务器认证

> **原文标题**：Remote MCP Server Authentication
> **原文来源**：https://developers.cloudflare.com/agents/guides/remote-mcp-server/
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week 2
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.3
> **覆盖**：全文完整翻译，未删节

---

本指南将展示如何在 Cloudflare 上使用 Streamable HTTP 传输方式（当前 MCP 规范的标准）部署你自己的远程 MCP 服务器。你有两种选择：

- 不带认证 —— 任何人都可以连接并使用该服务器（无需登录）。
- 带认证与授权 —— 用户需要先登录才能访问工具，你可以根据用户权限控制智能体能调用哪些工具。

> 译注：源文件中的部分破折号与 emoji 在抽取过程中因编码问题损坏，译文按语义还原为破折号，并略去无法辨识的 emoji。

## 选择方案

Agents SDK 提供了多种创建 MCP 服务器的方式。选择适合你使用场景的方案：

| 方案 | 有状态？ | 需要 Durable Objects？ | 最适合 |
|---|---|---|---|
| `createMcpHandler()` | 否 | 否 | 无状态工具，配置最简单 |
| `McpAgent` | 是 | 是 | 有状态工具、按会话保存状态、elicitation（服务端向用户征询补充信息） |
| 原始 `WebStandardStreamableHTTPServerTransport` | 否 | 否 | 完全控制权，不依赖 SDK |

`createMcpHandler()` 是让无状态 MCP 服务器跑起来最快的方式。当你的工具不需要按会话保存状态时，就用它。

`McpAgent` 为每个会话提供一个 Durable Object，内置状态管理、对 elicitation 的支持，并且同时支持 SSE 和 Streamable HTTP 两种传输方式。

如果你希望直接使用 `@modelcontextprotocol/sdk` 而不借助 Agents SDK 的辅助封装，原始传输方式能给你完全的控制权。

## 部署你的第一个 MCP 服务器

你可以先部署一个公开的 MCP 服务器——不带认证，之后再添加用户认证和带作用域的授权。如果你已经确定自己的服务器需要认证，可以直接跳到下一节。

### 通过控制面板

下面的按钮会引导你完成向你的 Cloudflare 账户部署示例 MCP 服务器所需的全部步骤：

部署完成后，该服务器将运行在你的 workers.dev 子域名下（例如 `remote-mcp-server-authless.your-account.workers.dev/mcp`）。你可以立即使用 AI Playground（一个远程 MCP 客户端）、MCP inspector 或其他 MCP 客户端连接到它。

你的 GitHub 或 GitLab 账户上会为这个 MCP 服务器新建一个 git 仓库，并配置为每次你推送变更或向仓库主分支合并拉取请求时自动部署到 Cloudflare。你可以克隆这个仓库、在本地开发，并开始用自己的工具定制这个 MCP 服务器。

### 通过 CLI

你可以使用 Wrangler CLI 在本地机器上创建一个新的 MCP 服务器，并将其部署到 Cloudflare。

打开终端，运行以下命令：

```bash
npm create cloudflare@latest -- remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```bash
yarn create cloudflare remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

```bash
pnpm create cloudflare@latest remote-mcp-server-authless --template=cloudflare/ai/demos/remote-mcp-authless
```

在初始化过程中，按如下选择：

- 对于「Do you want to add an AGENTS.md file to help AI coding tools understand Cloudflare APIs?」，选择 **No**。
- 对于「Do you want to use git for version control?」，选择 **No**。
- 对于「Do you want to deploy your application?」，选择 **No**（我们会在部署前先测试服务器）。

现在你已经搭好了 MCP 服务器，依赖也已安装完成。

进入项目文件夹：

终端窗口

```bash
cd remote-mcp-server-authless
```

在新项目所在目录中，运行以下命令启动开发服务器：

终端窗口

```bash
npm start
```

```
⛅ Starting local server...
[wrangler:info] Ready on http://localhost:8788
```

查看命令输出中的本地端口。在本例中，MCP 服务器运行在 8788 端口，MCP 端点 URL 是 `http://localhost:8788/mcp`。

要在本地测试服务器：

在新终端中运行 MCP inspector。MCP inspector 是一个交互式 MCP 客户端，让你能在 Web 浏览器中连接到自己的 MCP 服务器并调用工具。

终端窗口

```bash
npx @modelcontextprotocol/inspector@latest
```

```
🚀 MCP Inspector is up and running at:
http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3
🌐 Opening browser...
```

MCP Inspector 会在你的 Web 浏览器中打开。你也可以手动打开浏览器并访问 `http://localhost:<PORT>` 来启动它。查看命令输出，找到 MCP Inspector 正在运行的本地端口。在本例中，MCP Inspector 服务在 5173 端口。

在 MCP inspector 中，输入你的 MCP 服务器 URL（`http://localhost:8788/mcp`），然后选择 **Connect**。选择 **List Tools** 即可显示你的 MCP 服务器对外暴露的工具。

现在你可以把 MCP 服务器部署到 Cloudflare 了。在项目目录下运行：

终端窗口

```bash
npx wrangler@latest deploy
```

如果你已经把包含 MCP 服务器的 Worker 关联到一个 git 仓库，那么只要推送变更或向仓库主分支合并拉取请求，就能完成部署。

MCP 服务器将部署到你的 `*.workers.dev` 子域名，地址为 `https://remote-mcp-server-authless.your-account.workers.dev/mcp`。

要测试这个远程 MCP 服务器，请取你已部署的 MCP 服务器 URL（`https://remote-mcp-server-authless.your-account.workers.dev/mcp`），填入运行在 `http://localhost:5173` 的 MCP inspector。

现在你有了一个 MCP 客户端可以连接的远程 MCP 服务器。

## 通过本地代理从 MCP 客户端连接

现在你的远程 MCP 服务器已经在运行，你可以使用 mcp-remote 本地代理，把 Claude Desktop 或其他 MCP 客户端连接到它——即使你的 MCP 客户端本身不支持远程传输或授权。这样你就能用真实的 MCP 客户端测试与远程 MCP 服务器交互是什么样子。

例如，要从 Claude Desktop 连接：

更新你的 Claude Desktop 配置，指向你的 MCP 服务器 URL：

```json
{
  "mcpServers": {
    "math": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://remote-mcp-server-authless.your-account.workers.dev/mcp"
      ]
    }
  }
}
```

重启 Claude Desktop 以加载该 MCP 服务器。完成后，Claude 就能调用你的远程 MCP 服务器了。

要测试，可以让 Claude 使用你的某个工具。例如：

```text
Could you use the math tool to add 23 and 19?
```

Claude 应该会调用该工具，并显示远程 MCP 服务器生成的结果。

要了解如何把远程 MCP 服务器与其他 MCP 客户端配合使用，请参阅 Test a Remote MCP Server。

## 添加认证

你之前部署的公开 MCP 服务器示例允许任何客户端无需登录就连接并调用工具。要为你的 MCP 服务器添加用户认证，你可以接入 Cloudflare Access 或第三方服务作为 OAuth 提供方。你的 MCP 服务器负责处理安全的登录流程，并签发访问令牌，供 MCP 客户端发起带认证的工具调用。用户通过 OAuth 提供方登录，并以带作用域的权限，授予其 AI 智能体与你的 MCP 服务器所暴露工具交互的许可。

### Cloudflare Access OAuth

你可以把 MCP 服务器配置为要求通过 Cloudflare Access 进行用户认证。Cloudflare Access 充当身份聚合器，验证用户邮箱、来自你现有身份提供方（如 GitHub 或 Google）的信号，以及 IP 地址或设备证书等其他属性。当用户连接 MCP 服务器时，会被提示登录已配置的身份提供方，只有通过你的 Access 策略才会被授予访问权限。

分步部署指南请参阅 Secure MCP servers with Access for SaaS。

### 第三方 OAuth

你可以把 MCP 服务器接入任何支持 OAuth 2.0 规范的 OAuth 提供方，包括 GitHub、Google、Slack、Stytch、Auth0、WorkOS 等等。

下面的示例演示如何使用 GitHub 作为 OAuth 提供方。

#### 第 1 步 —— 创建一个新的 MCP 服务器

运行以下命令，创建一个带 GitHub OAuth 的新 MCP 服务器：

```bash
npm create cloudflare@latest -- my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```bash
yarn create cloudflare my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

```bash
pnpm create cloudflare@latest my-mcp-server-github-auth --template=cloudflare/ai/demos/remote-mcp-github-oauth
```

现在 MCP 服务器已经搭好，依赖也装好了。进入该项目文件夹：

终端窗口

```bash
cd my-mcp-server-github-auth
```

你会注意到，在这个示例 MCP 服务器中，如果你打开 `src/index.ts`，最主要的区别是 `defaultHandler` 被设置为 `GitHubHandler`：

TypeScript

```typescript
import GitHubHandler from "./github-handler";

export default new OAuthProvider({
  apiRoute: "/mcp",
  apiHandler: MyMCP.serve("/mcp"),
  defaultHandler: GitHubHandler,
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  clientRegistrationEndpoint: "/register",
});
```

这段代码让用户被重定向到 GitHub 完成认证。不过要让它跑起来，你还需要按下面的步骤创建 OAuth 客户端应用。

#### 第 2 步 —— 创建一个 OAuth 应用

你需要创建两个 GitHub OAuth 应用，才能把 GitHub 作为 MCP 服务器的认证提供方——一个用于本地开发，一个用于生产环境。

#### 第 2.1 步 —— 为本地开发创建一个新的 OAuth 应用

前往 `github.com/settings/developers`，按以下设置创建一个新的 OAuth 应用：

- 应用名称（Application name）：**My MCP Server (local)**
- 主页 URL（Homepage URL）：`http://localhost:8788`
- 授权回调 URL（Authorization callback URL）：`http://localhost:8788/callback`

对于你刚创建的 OAuth 应用，把该应用的 client ID 作为 `GITHUB_CLIENT_ID` 添加进去，并生成 client secret，将其作为 `GITHUB_CLIENT_SECRET` 写入项目根目录的 `.env` 文件，本地开发时会用它来设置密钥。

终端窗口

```bash
touch .env
echo 'GITHUB_CLIENT_ID="your-client-id"' >> .env
echo 'GITHUB_CLIENT_SECRET="your-client-secret"' >> .env
cat .env
```

运行以下命令启动开发服务器：

终端窗口

```bash
npm start
```

你的 MCP 服务器现在运行在 `http://localhost:8788/mcp`。

在新终端中运行 MCP inspector。MCP inspector 是一个交互式 MCP 客户端，让你能在 Web 浏览器中连接到自己的 MCP 服务器并调用工具。

终端窗口

```bash
npx @modelcontextprotocol/inspector@latest
```

在你的 Web 浏览器中打开 MCP inspector：

终端窗口

```bash
open http://localhost:5173
```

在 inspector 中，输入你的 MCP 服务器 URL：`http://localhost:8788/mcp`

在右侧的主面板中，点击 **OAuth Settings** 按钮，然后点击 **Quick OAuth Flow**。

你应该会被重定向到 GitHub 的登录或授权页面。在你授权 MCP 客户端（即 inspector）访问你的 GitHub 账户后，会被重定向回 inspector。

在侧边栏点击 **Connect**，你应该就能看到 "List Tools" 按钮，它会列出你的 MCP 服务器暴露的工具。

#### 第 2.2 步 —— 为生产环境创建一个新的 OAuth 应用

你需要重复第 2.1 步，为生产环境创建一个新的 OAuth 应用。

前往 `github.com/settings/developers`，按以下设置创建一个新的 OAuth 应用：

- 应用名称（Application name）：**My MCP Server (production)**
- 主页 URL（Homepage URL）：填写你已部署的 MCP 服务器的 workers.dev URL（例如 `worker-name.account-name.workers.dev`）
- 授权回调 URL（Authorization callback URL）：填写你已部署的 MCP 服务器 workers.dev URL 的 `/callback` 路径（例如 `worker-name.account-name.workers.dev/callback`）

对于你刚创建的 OAuth 应用，使用 Wrangler CLI 添加 client ID 和 client secret：

终端窗口

```bash
npx wrangler secret put GITHUB_CLIENT_ID
```

终端窗口

```bash
npx wrangler secret put GITHUB_CLIENT_SECRET
npx wrangler secret put COOKIE_ENCRYPTION_KEY # add any random string here e.g. openssl rand -hex 32
```

设置一个 KV 命名空间

a. 创建 KV 命名空间：

终端窗口

```bash
npx wrangler kv namespace create "OAUTH_KV"
```

b. 用生成的 KV ID 更新 `wrangler.jsonc` 文件：

```json
{
  "kvNamespaces": [
    {
      "binding": "OAUTH_KV",
      "id": "<YOUR_KV_NAMESPACE_ID>"
    }
  ]
}
```

把 MCP 服务器部署到你的 Cloudflare workers.dev 域名：

终端窗口

```bash
npm run deploy
```

使用 AI Playground、MCP Inspector 或其他 MCP 客户端连接到运行在 `worker-name.account-name.workers.dev/mcp` 的服务器，并用 GitHub 进行认证。

## 下一步

- **MCP 工具** —— 向你的 MCP 服务器添加工具。
- **授权** —— 自定义认证与授权。

<!-- NEW-TERM: elicitation | 服务端向用户征询补充信息（暂保留英文 elicitation） -->
<!-- NEW-TERM: Streamable HTTP transport | Streamable HTTP 传输方式 -->
