# OWASP Top 10：十大 Web 应用安全风险

> **原文标题**：OWASP Top Ten Web Application Security Risks
> **原文来源**：https://owasp.org/www-project-top-ten/
> **课程**：CS146S The Modern Software Developer（Stanford，2025 秋）· Week 6
> **译文状态**：机器翻译（Claude）+ 术语表校准 + 人工抽检（见 `pipeline/qa_report.md`）
> **术语依据**：[术语表.md](../../术语表.md) v1.3
> **覆盖**：全文完整翻译，未删节

---

当前最新发布的版本是 OWASP Top Ten 2025。

以往版本可在 OWASP Top Ten 2021 和 OWASP Top 10 2017（PDF）获取。更早的版本可在 Github 仓库中找到。

> 译注：原文此处写作「Older versiona are available」，其中 versiona 应为 versions 的拼写错误。按规范照译，不静默改正。

OWASP Top 10 是一份面向开发者和 Web 应用安全的标准化意识文档。它代表了关于 Web 应用最关键安全风险的广泛共识。

它是全球开发者公认的、迈向更安全编码的第一步。

各公司应当采纳这份文档，并着手确保其 Web 应用把这些风险降到最低。使用 OWASP Top 10，也许就是最有效的第一步——把你的组织内部的软件开发文化，转变为产出更安全代码的文化。

## 翻译工作

为了让 OWASP Top 10 - 2025 覆盖更多语言，我们已经开展了大量翻译工作。如果你有兴趣帮忙，请联系你想贡献的那门语言对应的团队成员；如果你没有看到你的语言被列出（这里和 github 上都没有），请发邮件至 [email protected] 告诉我们你想帮忙，我们会为你的语言组建一个志愿者小组。

### Top10:2025 已完成的翻译：

翻译进行中 —— 请稍后再来查看！

## 历史版本：

### Top10:2021 已完成的翻译：

ar - العربية

es - Español

fr - Français

id - Indonesian

it - Italiano

ja - 日本語]

pt_BR - Português (Brasil)

zh_CN - 简体中文

zh_TW - 繁體中文

### Top10:2017 已完成的翻译：

中文：OWASP Top 10-2017 - 中文版（PDF)

项目组长： 王颉 （ [email protected] ）

翻译人员：陈亮、王厚奎、王颉、王文君、王晓飞、吴楠、徐瑞祝、夏天泽、杨璐、张剑钟、赵学文（排名不分先后，按姓氏拼音排列）

审查人员：Rip、包悦忠、李旭勤、杨天识、张家银（排名不分先后，按姓氏拼音排列）

汇编人员：赵学文

法语：OWASP Top 10 2017 法语版（Git/Markdown）

德语：OWASP Top 10 2017 德语版 V1.0（Pdf）（网页）

由 Christian Dresen、Alexios Fakos、Louisa Frick、Torsten Gigler、Tobias Glemser、Dr. Frank Gut、Dr. Ingo Hanke、Dr. Thomas Herzog、Dr. Markus Koegel、Sebastian Klipper、Jens Liebau、Ralf Reinhardt、Martin Riedel、Michael Schaefer 汇编

希伯来语：OWASP Top 10-2017 - Hebrew（PDF）（PPTX）

由 Eyal Estrin（Twitter：@eyalestrin）和 Omer Levi Hevroni（Twitter：@omerlh）翻译。

日语：OWASP Top 10-2017 - 日本語版（PDF）

由 Akitsugu ITO、Albert Hsieh、Chie TAZAWA、Hideko IGARASHI、Hiroshi TOKUMARU、Naoto KATSUMI、Riotaro OKADA、Robert DRACEA、Satoru TAKAHASHI、Sen UENO、Shoichi NAKATA、Takanori NAKANOWATARI、Takanori ANDO、Tomohiro SANAE 翻译并审校。

韩语：OWASP Top 10-2017 - 한글（PDF）（PPTX）

번역 프로젝트 관리 및 감수 : 박형근(Hyungkeun Park) / 감수(ㄱㄴㄷ순) : 강용석(YongSeok Kang), 박창렴(Park Changryum), 조민재(Johnny Cho) / 편집 및 감수 : 신상원(Shin Sangwon) / 번역(ㄱㄴㄷ순) : 김영하(Youngha Kim), 박상영(Sangyoung Park), 이민욱(MinWook Lee), 정초아(JUNG CHOAH), 조광렬(CHO KWANG YULL), 최한동(Handong Choi)

葡萄牙语：OWASP Top 10 2017 - Portuguese（PDF）（ODP）

由 Anabela Nogueira、Carlos Serrão、Guillaume Lopes、João Pinto、João Samouco、Kembolle A. Oliveira、Paulo A. Silva、Ricardo Mourato、Rui Silva、Sérgio Domingues、Tiago Reis、Vítor Magano 翻译。

俄语：OWASP Top 10-2017 - на русском языке（PDF）

由 JZDLin（ @JZDLin ）、Oleksii Skachkov（ @hamster4n ）、Ivan Kochurkin（ @KvanTTT ）和 Taras Ivashchenko 翻译并审校

西班牙语：OWASP Top 10-2017 - Español（PDF）

Gerardo Canedo （ [email protected] - [Twitter: @GerardoMCanedo]）

Cristian Borghello （ [email protected] - [Twitter: @seguinfo]）

### Top10:2017 候选发布版翻译团队：

阿塞拜疆语：Rashad Aliyev ( [email protected] )

中文 RC2：Rip、包悦忠、李旭勤、王颉、王厚奎、吴楠、徐瑞祝、夏天泽、张家银、张剑钟、赵学文(排名不分先后，按姓氏拼音排列) OWASP Top10 2017 RC2 - Chinese PDF

法语：Ludovic Petit: [email protected] , Sébastien Gioria: [email protected] 。

其他待列出。

### Top10:2013 已完成的翻译：

阿拉伯语：OWASP Top 10 2013 - Arabic PDF

翻译：Mohannad Shahat: [email protected] , Fahad: @SecurityArk, Abdulellah Alsaheel: [email protected] , Khalifa Alshamsi: [email protected] 和 Sabri(KING SABRI): [email protected] , Mohammed Aldossary: [email protected]

中文 2013：中文版2013 OWASP Top 10 2013 - Chinese (PDF) 。

项目组长： Rip、王颉， 参与人员： 陈亮、 顾庆林、 胡晓斌、 李建蒙、 王文君、 杨天识、 张在峰

捷克语 2013：OWASP Top 10 2013 - Czech (PDF) OWASP Top 10 2013 - Czech (PPTX)

CSIRT.CZ - CZ.NIC, z.s.p.o. (.cz domain registry): Petr Zavodsky: [email protected] , Vaclav Klimes, Zuzana Duracinska, Michal Prokop, Edvard Rejthar, Pavel Basta

法语 2013：OWASP Top 10 2013 - French PDF

Ludovic Petit: [email protected] , Sébastien Gioria: [email protected] , Erwan Abgrall: [email protected] , Benjamin Avet: [email protected] , Jocelyn Aubert: [email protected] , Damien Azambour: [email protected] , Aline Barthelemy: [email protected] , Moulay Abdsamad Belghiti: [email protected] , Gregory Blanc: [email protected] , Clément Capel: [email protected] , Etienne Capgras: [email protected] , Julien Cayssol: [email protected] , Antonio Fontes: [email protected] , Ely de Travieso: [email protected] , Nicolas Grégoire: [email protected] , Valérie Lasserre: [email protected] , Antoine Laureau: [email protected] , Guillaume Lopes: [email protected] , Gilles Morain: [email protected] , Christophe Pekar: [email protected] , Olivier Perret: [email protected] , Michel Prunet: [email protected] , Olivier Revollat: [email protected] , Aymeric Tabourin: [email protected]

德语 2013：OWASP Top 10 2013 - German PDF

[email protected] 即 Frank Dölitzscher、Torsten Gigler、Tobias Glemser、Dr. Ingo Hanke、Thomas Herzog、Kai Jendrian 、Ralf Reinhardt 、Michael Schäfer

希伯来语 2013：OWASP Top 10 2013 - Hebrew PDF

翻译：Or Katz、Eyal Estrin、Oran Yitzhak、Dan Peled、Shay Sivan。

意大利语 2013：OWASP Top 10 2013 - Italian PDF

翻译：Michele Saporito: [email protected] , Paolo Perego: [email protected] , Matteo Meucci: [email protected] , Sara Gallo: [email protected] , Alessandro Guido: [email protected] , Mirko Guido Spezie: [email protected] , Giuseppe Di Cesare: [email protected] , Paco Schiaffella: [email protected] , Gianluca Grasso: [email protected] , Alessio D’Ospina: [email protected] , Loredana Mancini: [email protected] , Alessio Petracca: [email protected] , Giuseppe Trotta: [email protected] , Simone Onofri: [email protected] , Francesco Cossu: [email protected] , Marco Lancini: [email protected] , Stefano Zanero: [email protected] , Giovanni Schmid: [email protected] , Igor Falcomata’: [email protected]

日语 2013：OWASP Top 10 2013 - Japanese PDF

翻译：Chia-Lung Hsieh: ryusuke.tw(at)gmail.com，审校：Hiroshi Tokumaru、Takanori Nakanowatari

韩语 2013：OWASP Top 10 2013 - Korean PDF (이름가나다순)

김병효: [email protected] , 김지원: [email protected] , 김효근: [email protected] , 박정훈: [email protected] , 성영모: [email protected] , 성윤기: [email protected] , 송보영: [email protected] , 송창기: [email protected] , 유정호: [email protected] , 장상민: [email protected] , 전영재: [email protected] , 정가람: [email protected] , 정홍순: [email protected] , 조민재: [email protected] ,허성무: [email protected]

巴西葡萄牙语 2013：OWASP Top 10 2013 - Brazilian Portuguese PDF

翻译：Carlos Serrão、Marcio Machry、Ícaro Evangelista de Torres、Carlo Marcelo Revoredo da Silva、Luiz Vieira、Suely Ramalho de Mello、Jorge Olímpia、Daniel Quintão、Mauro Risonho de Paula Assumpção、Marcelo Lopes、Caio Dias、Rodrigo Gularte

西班牙语 2013：OWASP Top 10 2013 - Spanish PDF

Gerardo Canedo: [email protected] , Jorge Correa: [email protected] , Fabien Spychiger: [email protected] , Alberto Hill: [email protected] , Johnatan Stanley: [email protected] , Maximiliano Alonzo: [email protected] , Mateo Martinez: [email protected] , David Montero: [email protected] , Rodrigo Martinez: [email protected] , Guillermo Skrilec: [email protected] , Felipe Zipitria: [email protected] , Fabien Spychiger: [email protected] , Rafael Gil: [email protected] , Christian Lopez: [email protected] , jonathan fernandez [email protected] , Paola Rodriguez: [email protected] , Hector Aguirre: [email protected] , Roger Carhuatocto: [email protected] , Juan Carlos Calderon: [email protected] , Marc Rivero López: [email protected] , Carlos Allendes: [email protected] , [email protected] : [email protected] , Manuel Ramírez: [email protected] , Marco Miranda: [email protected] , Mauricio D. Papaleo Mayada: [email protected] , Felipe Sanchez: [email protected] , Juan Manuel Bahamonde: [email protected] , Adrià Massanet: [email protected] , Jorge Correa: [email protected] , Ramiro Pulgar: [email protected] , German Alonso Suárez Guerrero: [email protected] , Jose A. Guasch: [email protected] , Edgar Salazar: [email protected]

乌克兰语 2013：OWASP Top 10 2013 - Ukrainian PDF

Kateryna Ovechenko、Yuriy Fedko、Gleb Paharenko、Yevgeniya Maskayeva、Sergiy Shabashkevich、Bohdan Serednytsky

### 2010 年已完成的翻译：

韩语 2010：OWASP Top 10 2010 - Korean PDF

Hyungkeun Park, ( [email protected] )

西班牙语 2010：OWASP Top 10 2010 - Spanish PDF

Daniel Cabezas Molina、Edgar Sanchez、Juan Carlos Calderon、Jose Antonio Guasch、Paulo Coronado、Rodrigo Marcos、Vicente Aguilera

法语 2010：OWASP Top 10 2010 - French PDF

[email protected] , [email protected] , [email protected] , [email protected] , [email protected] , [email protected] , [email protected]

德语 2010：OWASP Top 10 2010 - German PDF

[email protected] 即 Frank Dölitzscher、Tobias Glemser、Dr. Ingo Hanke、Kai Jendrian 、Ralf Reinhardt 、Michael Schäfer

印尼语 2010：OWASP Top 10 2010 - Indonesian PDF

Tedi Heriyanto（协调人）、Lathifah Arief、Tri A Sundara、Zaki Akhmad

意大利语 2010：OWASP Top 10 2010 - Italian PDF

Simone Onofri、Paolo Perego、Massimo Biagiotti、Edoardo Viscosi、Salvatore Fiorillo、Roberto Battistoni、Loredana Mancini、Michele Nesta、Paco Schiaffella、Lucilla Mancini、Gerardo Di Giacomo、Valentino Squilloni

日语 2010：OWASP Top 10 2010 - Japanese PDF

[email protected] , Dr. Masayuki Hisada, Yoshimasa Kawamoto, Ryusuke Sakamoto, Keisuke Seki, Shin Umemoto, Takashi Arima

中文 2010：OWASP Top 10 2010 - Chinese PDF

感谢以下为中文版本做出贡献的翻译人员和审核人员: Rip Torn, 钟卫林, 高雯, 王颉, 于振东

越南语 2010：OWASP Top 10 2010 - Vietnamese PDF

翻译由 Cecil Su 牵头 - 翻译团队：Dang Hoang Vu、Nguyen Ba Tien、Nguyen Tang Hung、Luong Dieu Phuong、Huynh Thien Tam

希伯来语 2010：OWASP Top 10 Hebrew Project – OWASP Top 10 2010 - Hebrew PDF 。

由 Or Katz 牵头，贡献者名单见翻译页面。

## 2021 项目赞助方

OWASP Top 10:2021 由 Secure Code Warrior 赞助。

## 2017 项目赞助方

OWASP Top 10 - 2017 项目由 Autodesk 赞助，并得到 OWASP NoVA Chapter 支持。

## 2003-2013 项目赞助方

感谢 Aspect Security 赞助了更早的版本。

## OWASP Top 10 2025 数据分析计划

### 目标

收集迄今为止关于已识别应用漏洞的最全面的数据集，以便对 Top 10 以及未来的其他研究进行分析。这些数据应当来自多种来源：安全厂商和安全咨询公司、漏洞赏金（bug bounty）项目，以及公司/组织的贡献。数据会被归一化，以便在「人工辅助的工具」（Human assisted Tooling）与「工具辅助的人工」（Tooling assisted Humans）之间做同等水平的比较。

### 分析基础设施

计划利用 OWASP Azure 云基础设施来收集、分析和存储所贡献的数据。

### 贡献

我们计划同时支持实名贡献和化名贡献。我们更希望贡献是实名的；这对提交数据的验证/质量/可信度有极大帮助。如果提交者希望自己的数据以匿名方式存储，甚至干脆匿名提交数据，那么这些数据就必须被归类为「未验证」（unverified），而不是「已验证」（verified）。

#### 已验证数据贡献

情形 1：提交者身份已知，并同意被列为一个贡献方。

情形 2：提交者身份已知，但不希望被公开点名。

情形 3：提交者身份已知，但不希望它被记录在数据集中。

#### 未验证数据贡献

情形 4：提交者匿名。（我们应该支持吗？）

当未验证数据属于被分析的数据集的一部分时，数据分析会做出仔细的区分。

### 贡献流程

数据可以通过以下几种方式贡献：

把包含数据集的 CSV/Excel 文件通过电子邮件发送到 [email protected]

把 CSV/Excel 文件上传到 https://bit.ly/OWASPTop10Data

模板示例可以在 GitHub 上找到：https://github.com/OWASP/Top10/tree/master/2025/Data

### 贡献时间范围

对于 2021 至 2024 年的数据，我们计划在新一版 Top 10 中接受贡献，截止到 2025 年 7 月 31 日。

### 数据结构

以下数据元素分为必填和可选。

提供的信息越多，我们的分析就越准确。

最基本地，我们需要时间段、数据集中被测应用的总数，以及 CWE 列表和包含该 CWE 的应用数量统计。

如果可能的话，请提供额外的元数据，因为这会极大地帮助我们更深入地了解当前的测试与漏洞状况。

#### 元数据

贡献者名称（组织或匿名）

贡献者联系邮箱

时间段（2024、2023、2022、2021）

被测应用的数量

测试类型（TaH、HaT、Tools）

主要语言（代码）

地理区域（全球、北美、欧盟、亚洲、其他）

主要行业（多个、金融、工业、软件、？？）

数据中是否包含重测或同一应用出现多次（T/F）

#### CWE 数据

CWE 列表，以及被发现包含该 CWE 的应用数量

如果可能的话，请提供数据中的核心 CWE，而不是 CWE 类别。

这有助于分析，本次分析中所做的任何归一化/聚合操作都会被详细记录。

##### 注意：

如果贡献者有两类数据集，一类来自 HaT 来源，一类来自 TaH 来源，那么建议把它们作为两个独立的数据集提交。

HaT = 人工辅助的工具（Human assisted Tools，体量/频率更高，主要来自工具）

TaH = 工具辅助的人工（Tool assisted Human，体量/频率更低，主要来自人工测试）

### 问卷调查

与 Top Ten 2021 类似，我们计划开展一次问卷调查，找出社区认为重要、但可能尚未体现在数据中的最多两个 Top Ten 类别。我们计划在 2025 年初开展这次调查，并像上次一样使用 Google 表单。问卷中的 CWE 将来自当前的热门发现、数据中排在 Top Ten 之外的 CWE，以及其他可能的来源。

### 流程

在高层面上，我们计划做一定程度的数据归一化；不过，我们会保留一份贡献的原始数据，供未来分析使用。我们会分析数据集的 CWE 分布，并可能对部分 CWE 重新分类，把它们合并进更大的类别中。我们会仔细记录所采取的所有归一化操作，让人清楚地知道做过什么。

我们计划沿用 2021 年延续下来的模型来计算可能性，用发生率（incidence rate）而不是频率（frequency）来衡量某个应用包含至少一个 CWE 实例的可能性。这意味着我们关注的不是某个应用中的频率率（发现的数量），而是出现过该 CWE 一个或多个实例的应用数量。我们可以根据数据集中被测应用的总数，与每个 CWE 在多少个应用中被发现，来计算发生率。

此外，我们将为排名前 20-30 的 CWE 制定基础 CWSS 分数，并把潜在影响纳入 Top 10 的权重计算。

另外，我们还想探索能从贡献的数据集中挖掘出的额外洞见，看看还能学到什么对安全社区和开发社区有用的东西。

<!-- NEW-TERM: bug bounty | 漏洞赏金 | 出现于「目标」小节 -->
<!-- NEW-TERM: normalization | 归一化 | 出现于「目标」「流程」小节 -->
<!-- NEW-TERM: CWE | CWE | 出现于「数据结构」小节，保留英文缩写 -->
<!-- NEW-TERM: CWSS | CWSS | 出现于「流程」小节，保留英文缩写 -->
<!-- NEW-TERM: HaT | HaT | 出现于「注意」小节，保留英文缩写 -->
<!-- NEW-TERM: TaH | TaH | 出现于「注意」小节，保留英文缩写 -->
<!-- NEW-TERM: incidence rate | 发生率 | 出现于「流程」小节 -->
