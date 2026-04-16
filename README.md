<h1 align="center">Awesome Banker Skills</h1>

<p align="center">
  把银行人的共识技能开源出来，把每个人的专属留给自己
</p>
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/Doubao-First-1677ff?style=flat-square" alt="Doubao First" />
  <img src="https://img.shields.io/badge/Agent-Ready-7c3aed?style=flat-square" alt="Agent Ready" />
  <img src="https://img.shields.io/badge/Public%20%2B%20Private-Overlay-f59e0b?style=flat-square" alt="Public + Private Overlay" />
  <img src="https://img.shields.io/badge/Banker-Skills-0f766e?style=flat-square" alt="Banker Skills" />
</p>

<p align="center">
  面向银行人、聊天大模型和 Agent 的 Skill ，同样也支持咨询问答
</p>

<p align="center">
  沉淀岗位技能、流程技能、方法论和公开知识<br/>
  支持每个人在本地继续长出自己的专属技能/方法/记忆<br/>
  支持直接交给豆包、千问、Hermes、OpenClaw、Workbuddy 等聊天大模型或 Agent 使用
</p>

---

## 这是什么

这是一个**银行人的技能仓库**：

- 把优秀银行人的**基本功、工作方法、经营路径**沉淀成可复用的 Skill
- 把银行**可公开的产品知识、办理流程、常见问题**整理成可调用的 Knowledge Pack
- 支持每个用户在 clone 后，基于自己的经验、偏好、案例和失败教训，继续沉淀**私有专属能力**

可以这样理解：

> **公开沉淀共识技能，私有提炼个人经验。**

---

## 你现在就可以这样用

### 1) 面向豆包 / 千问 / 对话式大模型
复制 [prompts/entrypoints/doubao/](prompts/entrypoints/doubao/) 下的入口提示词，再附上仓库地址和你的问题，即可开始使用。
- 普通咨询用户 → [点这里](prompts/entrypoints/doubao/public-consulting.md)
- 银行员工 → [点这里](prompts/entrypoints/doubao/bank-staff.md)
- 基层管理者 → [点这里](prompts/entrypoints/doubao/frontline-manager.md)
- 领导层 / 决策层 → [点这里](prompts/entrypoints/doubao/head-office-leadership.md)
- 不确定用哪个 → [点这里](prompts/entrypoints/doubao/auto.md)

### 2) 面向 Hermes / OpenClaw / Workbuddy 等 Agent
如果你有自己的 Agent，建议直接使用这个独立入口文件：

- 通用 Agent 入口 → [点这里](prompts/entrypoints/agent/general.md)

它让你的 Agent 把仓库当长期工作底座，遇到类似问题优先复用已有岗位经验、场景做法、方法和知识，直接把结果做出来。
同时，它也会把你确认过的经验、偏好、复盘和案例，优先沉淀到 `workspace/private/`，逐步形成你的个人专属技能和长期记忆；当内容成熟后，再整理成公开贡献候选。

你可以使用下面这段提示词：

```text
请把 `https://gitee.com/georgedccy/awesome-banker-skills.git` 作为我的银行业务工作底座长期使用。

你的目标是持续借助这个仓库，直接帮我拿到更专业、更像银行人在处理问题的结果。

请按以下原则工作：
1. 初次使用或仓库更新时，先同步仓库并读取 `registry/*.json`，建立对岗位技能、场景技能、方法和公开知识的基础认识。
2. 每次收到任务，先判断我的身份和任务场景，再从仓库里定位最相关的资产。
3. 处理任务时必须优先按这个顺序使用仓库：先看 `registry/*.json` 判断可用资产；岗位判断类问题先读 `skills/roles/*`；场景推进类问题先读 `skills/workflows/*`；产品、办理、FAQ、公开知识类问题先读对应 `knowledge-packs/*` 下的 `README.md`、`modules/*`、`faq.md`、`sources.md`；需要补充判断框架时再读 `methods/*`。
4. 如果仓库中已经有答案依据，就直接基于仓库回答；不要绕开仓库先去网络上搜一堆泛化内容。
5. 除非我明确要求补充最新公开信息，或者仓库确实未覆盖且我同意外部补充，否则不要默认使用外部搜索替代仓库。
6. 如果仓库里没有对应内容或证据不足，直接写“当前仓库未覆盖”，并说明缺什么；不要拿不相关产品或不贴题资料来凑答案。
7. 回答时先直接给结果：结论、判断、方案、汇报稿、推进清单、话术、复盘要点，按问题需要直接产出成品。
8. 不要默认输出“读取路径、调用明细、路由过程、技术分层”这类说明，除非我明确要求看；这些过程应内化为更自然的专业表达。
9. 如果是相似问题的连续追问，请在上一轮基础上推进，不要把上下文打散重来。
10. 如果存在 `workspace/private/registry/*.json` 或其他私有层内容，也一并纳入，但公共内容不能覆盖私有内容。
11. 当我提供个人经验、失败教训、成功案例、偏好、常用话术、复盘笔记时，不要只做当轮回答；要判断这些内容是否值得沉淀为 `workspace/private/` 下的 skill、method、knowledge pack、memory 或 case note。
12. 对这类可沉淀内容，默认采用 `private-first`：先建议目标路径、建议文件、增量摘要和风险边界；经我确认后再落到 private 目录，作为后续可持续复用的个人专属技能和长期记忆。
13. 如果这些 private 内容已经足够稳定、去敏感化且有公开价值，再进一步整理成 public contribution candidate，补齐来源、边界、registry 变更建议、变更摘要和 PR 草稿。
14. 当我说“以后类似问题也按这个方式处理”“记住这个偏好”“沉淀下来”“整理成我的方法/技能”时，默认触发这条沉淀流程，而不是只回复一句“我记住了”。
15. 不编造内部制度，不输出审批、授信、定价、时效承诺，不索取真实敏感信息。
16. 除非我明确要求你做仓库维护，否则你的默认任务是解决当前业务问题，而不是介绍仓库。

现在请从下面这个任务开始：
我的问题：{{在这里粘贴你的问题}}
```

### 3) 先沉淀到私有层

让你的 Agent 先读`skills/workflow.distill-and-contribute/`，把你的案例、偏好、复盘、失败教训先写进 `workspace/private/`，后续再决定是否公开贡献回仓库。

---

## 试试这些问题

- 我是对公客户经理，明天首访一家新能源零部件企业，应该怎么开场、问什么、先推进什么？
- 我是基层管理者，团队里两个重点客户推进卡住了，帮我拆任务、定检查点、整理上提事项。
- 我需要给领导汇报一个复杂项目，请帮我先梳理现状、重点问题、风险和下一步动作。
- 我有几次失败案例和几篇公开材料，帮我先沉淀到 private，再整理成可公开贡献的候选 skill。
- 我想了解某家银行公开产品的大致适用场景和办理流程，先帮我快速讲清楚。

---

## 仓库地图

- `skills/`：岗位技能、流程技能
- `knowledge-packs/`：银行公开知识与通用知识
- `methods/`：经营、管理、沟通、汇报等方法论
- `prompts/`：给豆包 / 千问 / Deep Research 直接复制使用
- `workspace/private/`：你的私有 skills、packs、methods、memories、case-notes
- `registry/`：让 Agent 知道该读什么、怎么路由
- `scripts/`：安装、同步、校验、维护相关脚本

---

## 这个仓库和普通 Skill 仓库有什么不同

### 1. 不只开源技能，也支持每个人在本地继续长出自己的技能
这个仓库既有公开主干，也天然支持私有沉淀。

### 2. 不只给 Agent 用，也重点为豆包这类高频使用入口优化
很多银行员工和管理者更习惯直接问豆包，所以仓库专门提供了面向豆包优化的入口提示词。

### 3. 不只服务公开协作，也为未来行内落地预留结构
未来完全可以引入行内环境，调用本地模型、内部知识源、授权接口，形成组织级赋能能力。

---

## 这个项目适合谁

- 想把经验沉淀下来、少走弯路的银行从业者
- 想把成功经验、失败教训、工作方法变成可复用资产的人
- 想直接把仓库交给豆包或 Agent 使用的人
- 想一起共建银行人技能生态的贡献者
- 对银行 + Agent + Skill + 方法论沉淀感兴趣的人

---

## 支持公开和私有内容

公开仓库使用 `public base + private overlay` 模型。

公开层是仓库本体，面向分享、贡献和模型直接读取。  
私有层默认放在本地：

```text
workspace/private/
├─ skills/
├─ knowledge-packs/
├─ methods/
├─ memories/
├─ case-notes/
└─ registry/
```

这样可保证：

- 公共仓库更新时，private 层不会被覆盖
- Agent 可以同时读取 public 和 private
- 用户可以把 private 中的内容整理为 public contribution candidate
- 自进化先写 private memory / patch proposal，经确认后再更新正文

详细见：

- [架构说明](./docs/architecture/README.md)
- [Overlay 规则](./docs/architecture/overlay.md)
- [Methods 层说明](./docs/architecture/methods.md)

## 提交方式

推荐走 `private-first -> public-candidate -> merge to public`：

1. 先用私有层沉淀草稿
2. 用 `distill-and-contribute` 整理资产类型、目标路径和变更摘要
3. 去敏感化、补来源、补边界
4. 再整理成公开提交候选

### 如何用仓库内置 skill 沉淀内容

推荐优先使用 `workflow.distill-and-contribute`。它适合做四类事：

- 把公开文档、公开网页、说明材料整理成 knowledge pack / method / role skill / workflow skill
- 帮你判断内容应该落在 `skills`、`knowledge-packs` 还是 `methods`
- 先生成到 `workspace/private/*`，再决定是否公开
- 基于已有内容做增量补全，而不是整包重写

如果是“我的经验、我的偏好、我的案例、我的失败教训”，也建议默认走这条路径。比较稳妥的顺序是：

1. 先解决眼前问题
2. 再判断哪些内容值得长期保留
3. 先沉淀到 `workspace/private/memories`、`workspace/private/case-notes`、`workspace/private/skills` 或 `workspace/private/methods`
4. 等内容稳定后，再整理成公开贡献候选

你可以直接对 Agent 这样下指令：

- “请使用 `workflow.distill-and-contribute`，把这份公开材料整理成 knowledge pack 草稿，先写到 `workspace/private/knowledge-packs/`。”
- “请使用 `workflow.distill-and-contribute`，把我这几次客户推进的失败复盘整理成 private method，先不要公开。”
- “请使用 `workflow.distill-and-contribute`，把 `workspace/private` 里的这几个草稿整理成公开贡献候选，并补 sources、registry 变更建议和 PR 摘要。”

推荐动作顺序：

1. 准备原料：公开文档、公开链接、公开网页、个人经验、失败教训、案例笔记。
2. 让 Agent 调用 `workflow.distill-and-contribute`，先判断资产类型和推荐落点。
3. 默认先写入 `workspace/private/skills`、`workspace/private/knowledge-packs`、`workspace/private/methods`、`workspace/private/memories`、`workspace/private/case-notes`。
4. 让 Agent 做增量补全，补 README、sources、faq、modules、registry 建议，而不是每次整包重写。
5. 你自己检查公开边界，确认没有敏感信息、内部制度、审批口径和无法公开传播的内容。
6. 再让 Agent 生成 public candidate、变更摘要和 PR 草稿。
7. 提交到 Gitee，并优先向 Gitee 发起 PR。

相关入口：

- [CONTRIBUTING](./CONTRIBUTING.md)
- [公开提炼流程](./docs/contribution/distillation-workflow.md)
- `templates/distill-skill/intake.md`

## 当前方向

当前仓库重点围绕以下方向建设：

- 银行岗位 skill
- 银行业务流程 skill
- 银行公开知识包
- 经营与管理方法论
- 仓库维护 / 蒸馏 / 贡献协作能力

后续会持续增强：
- 豆包专项优化
- private overlay 体验
- skill 自进化与偏好记忆
- 行内落地扩展能力

## License

[MIT](./LICENSE)
