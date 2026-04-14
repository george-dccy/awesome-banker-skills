# Awesome Banker Skills

面向银行人、聊天大模型和 Agent 的 repo-first 能力底座。

它能做银行问答客服，但更重要的是可以把银行人的共识技能、可公开知识和可复用方法沉淀下来，直接给豆包或 Agent 使用。

## 项目背景

银行工作的很多技能是跨岗位、跨流程复用的。
银行人需要不断学习、积累、总结，才能在业务中游刃有余。
但银行人往往没有时间、精力、动力去整理这些知识。
 而且，这些知识往往分散在各个人的大脑中，难以共享和复用。

### 这个项目希望能够

- 沉淀银行岗位共识技能、优秀人员可复用的方法、产品经营路径和可公开知识
- 支持每个用户在本地继续长出自己的 private skills / knowledge packs / methods / memories / case notes
- 不管是银行人还是银行客户，直接给豆包 / Agent 发送一段提示词，就能开始工作
- 为未来银行内部落地预留结构，支持添加行内知识源、连接客户数据，进行更复杂的判断和决策
- 让银行人少踩坑、少重复劳动、少加班，让业务推动更丝滑、业绩节节高，有更多时间陪伴家人、享受生活、提升消费，从而让我们的社会变得更好

当前版本优先级：

- 先优化“仓库直接给豆包 / Agent 使用”的体验
- 先不做前端依赖
- 为未来行内落地预留结构，但暂不实现具体内网接口

## 项目结构

```text
.
├─ skills/
│  ├─ roles/
│  └─ workflows/
├─ knowledge-packs/
│  ├─ banks/
│  └─ common/
├─ methods/
│  ├─ business-operations/
│  ├─ management/
│  ├─ communication-reporting/
│  └─ reusable/
├─ prompts/
│  ├─ entrypoints/
│  ├─ roles/
│  ├─ workflows/
│  ├─ knowledge-packs/
│  └─ methods/
├─ registry/
│  ├─ skills.json
│  ├─ knowledge-packs.json
│  ├─ methods.json
│  └─ prompts.json
├─ docs/
└─ templates/
```

结构解释：

- `skills/roles`：岗位 skill，沉淀角色视角与职责重点
- `skills/workflows`：workflow skills，作为场景化编排资产，负责组织输入、调用 methods 和 knowledge packs
- `knowledge-packs`：公开、稳定、可引用的知识事实
- `methods`：可复用判断与推进框架，不直接替代具体 workflow 的场景编排

### workflow / method 三问法

1. 脱离当前场景是否还能复用
2. 这是在讲框架，还是在讲场景编排
3. 换一个岗位或流程后是否仍自然

推荐路由层级：

`scene -> workflow -> method -> knowledge pack`

## Public / Private Overlay

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

这个设计可保证：

- 公共仓库更新时，private 层不会被覆盖
- Agent 可以同时读取 public 和 private
- 用户可以把 private 中的内容整理为 public contribution candidate
- 自进化先写 private memory / patch proposal，经确认后再更新正文

详细见：

- [架构说明](./docs/architecture/README.md)
- [Overlay 规则](./docs/architecture/overlay.md)
- [Methods 层说明](./docs/architecture/methods.md)

## 豆包主入口

项目适配了豆包/千问等大模型聊天应用。推荐直接复制以下入口 prompt 文件内容，再附上仓库地址给豆包：

- `prompts/entrypoints/doubao/public-consulting.md`
  面向公开咨询用户，优先读取公开 knowledge packs
- `prompts/entrypoints/doubao/bank-staff.md`
  面向银行员工，先识别 scene，再由 workflow 调用 methods 和 knowledge packs
- `prompts/entrypoints/doubao/frontline-manager.md`
  面向基层管理者，优先进入管理或汇报 workflow，再组织方法与知识读取
- `prompts/entrypoints/doubao/head-office-leadership.md`
  面向总行/分行领导层，优先进入决策支持 workflow，再补方法和事实依据
- `prompts/entrypoints/doubao/auto.md`
  不确定身份或场景时使用

这些入口要求模型：

- 先读取 `registry/*.json`
- 回答前先列出准备读取的文件路径
- 先识别 `scene`，再选择 `workflow`
- 显式写出调用了哪些 `workflow skill / method / pack`
- 把“方法/判断依据”和“公开知识依据”分层表达
- 覆盖不足时明确写出“当前仓库未覆盖”

补充说明见 [豆包入口说明](./docs/prompts/doubao.md)。

## Agent 使用方式

如果你是用 Claude Code、Codex、OpenClaw 或其他 Agent，推荐这样使用这个仓库：

1. 先读取：
   - `registry/skills.json`
   - `registry/knowledge-packs.json`
   - `registry/methods.json`
   - `registry/prompts.json`
2. 如果存在 `workspace/private/registry/*.json`，再合并 private overlay
3. 先识别 `scene`，再路由到最相关的 `workflow`
4. 由 `workflow` 决定需要调用哪些 `methods / knowledge packs`
5. 读取对应正文
6. 输出时显式区分：
   - 方法/判断依据
   - 公开知识依据

## 当前重点资产

### Skills

- `role.corp-relationship-manager`
- `workflow.market-corporate-client`
- `workflow.accompany-corporate-client`
- `workflow.report-to-leader`
- `workflow.distill-and-contribute`

### Knowledge Packs

- `pack.banks.ceb.corporate-settlement.basic-settlement`
- `pack.banks.ceb.transaction-banking.yangguang-e-pay`
- `pack.banks.ceb.trade-finance.yangguang-electricity-certificate`
- `pack.common.banker-thinking.top-performer`
- `pack.common.economics.business-basics`
- `pack.common.sales.consultative-b2b`
- `pack.common.psychology.business-communication`

### Methods

- `method.business-operations.problem-opportunity-scan`
- `method.business-operations.client-advance-map`
- `method.communication-reporting.leader-decision-brief`
- `method.management.team-followup-loop`

## 贡献方式

推荐走 `private-first -> public-candidate -> merge to public`：

1. 先用私有层沉淀草稿
2. 用 `distill-and-contribute` 整理资产类型、目标路径和变更摘要
3. 去敏感化、补来源、补边界
4. 再整理成公开贡献候选

相关入口：

- [CONTRIBUTING](./CONTRIBUTING.md)
- [公开蒸馏流程](./docs/contribution/distillation-workflow.md)
- `templates/distill-skill/intake.md`

## 行内落地方向

后续计划支持这些落地方向，当前版本只做结构预留：

- 可引入行内 claw 类应用安装
- 可接行内部署的本地模型
- 可接内部知识源和系统接口
- 可把 public / private overlay 映射成行内个人或部门工作区

## 内容边界

仓库不会收录：

- 真实客户数据
- 内部制度原文
- 内部审批、授信、定价结论
- 额度、费率、时效承诺
- 真实敏感参数、账号、证件、合同、流水

仓库中的所有内容都只用于：

- 前期理解与准备
- 沟通、汇报、推进辅助
- 公开知识和可复用方法沉淀

如果仓库没有依据，应明确写出：`当前仓库未覆盖`

## License

[MIT](./LICENSE)
