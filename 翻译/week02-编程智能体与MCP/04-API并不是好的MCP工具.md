# API 并不是好的 MCP 工具

> **原文标题**：APIs Don't Make Good MCP Tools
> **原文来源**：https://www.reillywood.com/blog/apis-dont-make-good-mcp-tools/
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week 2
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.3
> **覆盖**：全文完整翻译，未删节

---

模型上下文协议（MCP）如今是件大事。它已经成为让 LLM 使用别人写的工具的**事实标准**，而这当然会把 LLM 变成智能体。但为一个新的 MCP 服务器编写工具很难，所以人们常常提议把现有的 API 自动转换成 MCP 工具；通常借助 OpenAPI 元数据（1、2）。

以我的经验看，这条路可行，但效果并不好。原因有几点：

## 智能体应付不了大量的工具

出了名的是，VS Code 对工具数量有 128 个的硬性上限——但许多模型远在这个数字之前，就已经难以准确地调用工具了。而且，每个工具及其描述都会占用宝贵的上下文窗口空间。

大多数 Web API 在设计时根本没有考虑这些约束！当 API 由代码调用时，一个产品领域有无数个 API 也没问题；但如果把每个 API 都映射成一个 MCP 工具，效果可能就不太好了。

从零开始设计的 MCP 工具通常比单个 Web API 灵活得多，一个工具就能完成好几个 API 的工作。

## API 会很快耗尽上下文窗口

想象一个 API 每次返回 100 条记录，而每条记录都很宽（比如 50 个字段）。把这些结果原样发给智能体，会消耗大量 token；即便一个查询只用几个字段就能满足，最终所有字段还是会进入上下文窗口。

API 通常按记录条数分页，但记录的大小可能相差悬殊。一条记录可能包含一个占用 100,000 个 token 的大文本字段，另一条可能只占 10 个 token。把这些 API 结果直接塞进智能体的上下文窗口是一场赌博；有时能行，有时就会炸掉。

数据的格式也可能是个问题。如今大多数 Web API 都返回 JSON，但 JSON 是一种 token 效率非常低的格式。比如这个：

```json
[{"firstName": "Alice", "lastName": "Johnson", "age": 28}, {"firstName": "Bob", "lastName": "Smith", "age": 35}]
```

与同样数据在 CSV 格式下的样子对比：

```csv
firstName,lastName,age
Alice,Johnson,28
Bob,Smith,35
```

CSV 数据简洁得多——每条记录消耗的 token 只有一半。通常 CSV、TSV，或者（针对嵌套数据）YAML 都比 JSON 更合适。

这些问题都不是无法解决的。你可以设想自动添加工具参数，让智能体挑选字段；自动截断或摘要过大的结果；自动把 JSON 结果转换成 CSV（嵌套数据则转成 YAML）。但我见过的大多数服务器这些都没做。

## API 没有充分发挥智能体独有的能力

API 返回的是供程序消费的结构化数据。这通常也是智能体希望从工具调用中得到的东西……但智能体也能处理其他更自由形式的指令。

例如，一个 `ask_question` 工具可以先对某些文档做一次检索增强生成（RAG）查询，然后用纯文本返回信息，供下一次工具调用参考——完全跳过结构化数据。

或者，调用 `search_cities` 工具可以返回一个结构化的城市列表，并建议下一步该调用什么：

```csv
city_name,population,country,region
Tokyo,37194000,Japan,Asia
Delhi,32941000,India,Asia
Shanghai,28517000,China,Asia
Suggestion: To get more specific information (weather, attractions, demographics), try calling get_city_details with the city_name parameter.
```

这种分层和工具链式调用在 MCP 服务器里可能非常有效，而如果你把 API 自动转换成工具，就会彻底错过这一点。

## 如果智能体需要调用 API，它直接调就行了

像 Claude Code 这样的智能体，如今在编写并执行代码方面能力非常强，包括调用 Web API 的脚本。有些人甚至据此认为 MCP 根本没存在的必要！

我不同意这个结论，但我确实认为我们应该滑向冰球将要到达的地方。智能体的沙箱化正在快速改进，如果智能体直接调用 API 既简单又安全，那我们不如就这么做，省掉中间商。

## 结论

智能体与 API 的典型消费者有本质区别。从现有 API 自动生成 MCP 工具是可行的，但这样做不太可能效果好。智能体在拿到专为其独有能力与局限而设计的工具时，表现最好。

<!-- NEW-TERM: tool chaining | 工具链式调用 -->
