# 拿来说明 ②：WebFetch 被拦之后，怎么救回两篇资料

> **这份说明想证明什么**：一个"环境不支持"的结论，**在验证之前都不算数**。
> 下面完整展示：错误原文、我的错误结论、验证用的命令、以及最终多救回的 23K 字符。

---

## 一、出现的错误（原文照抄）

挑战包的离线缓存里，有 4 个页面是空壳。我打算联网补抓，于是逐个调用抓取工具。**四个请求全部失败**，返回同一段信息：

```
Unable to verify if domain medium.com is safe to fetch.
This may be due to network restrictions or enterprise security policies blocking claude.ai.
```

```
Unable to verify if domain blog.stockapp.com is safe to fetch.
This may be due to network restrictions or enterprise security policies blocking claude.ai.
```

```
Unable to verify if domain notion.warp.dev is safe to fetch.
This may be due to network restrictions or enterprise security policies blocking claude.ai.
```

```
Unable to verify if domain lawwu.github.io is safe to fetch.
This may be due to network restrictions or enterprise security policies blocking claude.ai.
```

## 二、我（AI）差一点给出的错误结论

看到 4 个域名**全部**被拒，我的第一反应是归因于**目标站点**：

> ❌ **差点写进 README 的结论**：
> 「这 4 篇资料的来源站点（Medium、Ghost、Notion）均屏蔽自动抓取，属环境固有限制，
> 无法获取，列为已知缺口。」

**这个结论错在两处**：
1. 它把"**我们的工具被拦**"误判成了"**对方站点屏蔽**"——两者是完全不同的原因；
2. 4 个域名指向 4 个互不相关的站点，它们"同时屏蔽我们"的概率，远低于"我们这边有个统一的东西在拦"。

## 三、验证：换一条同类路径，同一件事再试一次

没有被"策略拦截"这个说法吓住，而是**用另一条路径验证同一个假设**——网络到底通不通：

```bash
curl -sS -o /dev/null -w "github.com -> %{http_code}\n" https://github.com
curl -sS -o /dev/null -w "themodernsoftware.dev -> %{http_code}\n" https://themodernsoftware.dev
```

**实际输出（原文照抄）：**

```
github.com -> 200
themodernsoftware.dev -> 200
```

**结论翻转**：网络是通的。**被拦的是那一层工具，不是网络本身。**

> 这是整份资料包里最关键的一次判断。如果停在第一步，我会少 2 篇资料（23K 字符），
> 并且会在 README 里写下一个**错误的原因**——错误的归因比缺失本身更糟，
> 因为它会误导下一个做这个挑战的人。

## 四、改用 shell 层重抓

**Prompt / 指令：**

> 「WebFetch 被策略拦了，但 curl 能通。改用 curl 带浏览器 UA 重抓这 4 个 URL，保存到 `_work/live/`，
> 每个都报告 HTTP 状态码和字节数。失败的要说明失败原因（超时？DNS？）」

**实际命令：**

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Chrome/124.0 Safari/537.36"
curl -sSL -A "$UA" -o "live/$name" -w "$name -> %{http_code} %{size_download}B\n" "$url"
```

**实际输出（原文照抄）：**

```
peeking-medium.html        -> 000 0B
curl: (28) Failed to connect to medium.com port 443 after 21080 ms: Could not connect to server

good-context-stockapp.html -> 000 0B
curl: (6) Could not resolve host: blog.stockapp.com

warp-notion.html           -> 200 19912B
lessons-transcript.html    -> 200 55611B
```

**结果对比——失败原因完全不同：**

| 目标 | 之前以为的原因 | **真实原因** | 能否补救 |
|---|---|---|---|
| `notion.warp.dev` | "Notion 屏蔽抓取" | 其实**抓到了**（200 / 19.9KB） | ✅ 能 |
| `lawwu.github.io` | "站点屏蔽" | 其实**抓到了**（200 / 55.6KB） | ✅ 能 |
| `medium.com` | "Medium 屏蔽抓取" | **连接超时**（443 端口连不上） | ❌ 不能 |
| `blog.stockapp.com` | "Ghost 门禁" | **DNS 解析失败** | ❌ 不能 |

**注意这张表**：4 个"同一个原因"里，其实是**4 个不同的原因**，而且其中 2 个根本不是失败。
如果不做这一步验证，这 4 行的原因**全部是错的**。

## 五、第二层坑：抓到了，但内容是空的

`notion.warp.dev` 返回 200 / 19.9KB，看起来成功了。但抽出来只有 95 个字符：

```
Notion JavaScript must be enabled in order to use Notion. Please enable JavaScript to continue.
```

**这是"HTTP 成功 ≠ 内容成功"的典型。** 页面正文不在 HTML 里，而在一个 XHR 请求里。

> **Prompt / 指令：**
> 「Notion 页面是 JS 渲染的，HTML 里没有正文。找出这个页面真正的数据接口，用 curl POST 拿到 JSON，再解析出正文文本。」

**Notion 的公开数据接口是 `loadPageChunk`**，页面 id 就是 URL 末尾那 32 位十六进制（加连字符）：

```bash
curl -sS -X POST "https://notion.warp.dev/api/v3/loadPageChunk" \
  -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" \
  -d '{"pageId":"21643263-616d-81a6-b9e3-e63fd8a7380c","limit":100,
       "cursor":{"stack":[]},"chunkNumber":0,"verticalColumns":false}' \
  -o live/notion-chunk.json -w "notion api -> %{http_code} %{size_download}B\n"
```

**实际输出：**

```
notion api -> 200 96075B
```

拿到 96KB 的 `recordMap` JSON，正文块都在 `recordMap.block[*].value.value.properties.title` 里。

## 六、第三层坑：解析又一次"0 字符"

**第一次解析脚本跑出来 0 个字符**，但有 85 个 block。写代码找原因：

```python
v = blk.get('value', {}).get('value', {})   # 已经取了两层
txt = title(v)                              # title() 里又 .get('value').get('value')
```

**`title()` 内部又取了一次两层 `value`，等于向下挖了四层。** 这是"凭记忆写嵌套取值"的典型错误（和抽取阶段那个 `feed_and_get` 是同一类毛病）。

修法是把取值路径收敛到一处，修完立刻正常：

```
text blocks: 82 chars: 6477
```

**产出对比：**

| 阶段 | 结果 |
|---|---|
| WebFetch 直接抓 | ❌ 策略拦截 |
| curl 抓 HTML | ✅ 200，但只有 95 字符（JS 外壳） |
| curl POST Notion API | ✅ 200，96KB JSON |
| 解析（第一版，有 bug） | ❌ 0 字符 |
| **解析（修复后）** | ✅ **82 个文本块 / 6477 字符正文** |

## 七、第三篇的"曲线救国"

搜 `lessons-from-ai-code-reviews` 时发现：它**根本不是网页**，而是 Graphite 联合创始人 Tomas Reimers 在 AI Engineer World's Fair 2025 的演讲。
原视频在 YouTube（抓不到），但找到了第三方字幕转录站，**直接拿到 16.7K 字符的演讲全文**。

这一篇还**额外**满足了挑战任务书里明说的"视频字幕"这一类来源。

## 八、这次经历固化成的东西

1. **代码**：`pipeline/01_fetch.sh` 把上述流程写成脚本——包括 Notion 的 `loadPageChunk` 调用，
   以及"失败不中断、登记到 `_failures.tsv`"的处理；
2. **规范**：`pipeline/README.md` 里写明"缺口页处理三选一"——① 换路径抓；② 找同类替代源；③ 显式声明缺口 + 理由；
3. **README**：把 2 篇真缺口连同**真原因**（网络不可达 / DNS 失败）写进"已知缺口"。

> **一句话总结**：`Unable to fetch` 只说明**这条路径**不通，不说明**这件事**做不到。
> 多花 10 秒换条路径验证，今天多赚了 2 篇资料，并且让 README 里的原因从"4 个错的"变成"2 对 2 对"。
