# Awesome Banker Skills

面向银行人、聊天大模型和 Agent 的 repo-first 能力底座。

它不是银行客服系统。  
它要做的是把银行人的共识技能、可公开知识和可复用方法沉淀成一个可以直接给豆包或 Agent 使用的仓库。

## 项目定位

这个项目重点解决三件事：

- 公开沉淀银行岗位共识技能、优秀人员可复用的方法、产品经营路径和可公开知识
- 支持每个用户在本地继续长出自己的 private skills / knowledge packs / methods / memories / case notes
- 让银行人少踩坑、少重复劳动、少加班，让业务推动更丝滑

当前优先级很明确：

- 先优化“仓库直接给豆包 / Agent 使用”的体验
- 先不做前端依赖
- 为未来行内落地预留结构，但暂不实现具体内网接口

## 资产结构

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

三层核心资产边界：

- `skills`：岗位与流程的执行型能力
- `knowledge-packs`：公开、稳定、可引用的知识事实
- `methods`：跨岗位、跨流程复用的判断与推进框架

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

这个设计保证：

- 公共仓库更新时，private 层不会被覆盖
- Agent 可以同时读取 public 和 private
- 用户可以把 private 中的内容整理为 public contribution candidate
- 自进化先写 private memory / patch proposal，经确认后再更新正文

详细见：

- [架构说明](./docs/architecture/README.md)
- [Overlay 规则](./docs/architecture/overlay.md)
- [Methods 层说明](./docs/architecture/methods.md)

## 豆包主入口

这个仓库重点适配豆包。  
推荐直接复制以下入口 prompt 文件内容，再附上仓库地址给豆包：

- `prompts/entrypoints/doubao/public-consulting.md`
  面向公开咨询用户，优先读取公开 knowledge packs
- `prompts/entrypoints/doubao/bank-staff.md`
  面向银行员工，自动路由 skills + methods + knowledge packs
- `prompts/entrypoints/doubao/frontline-manager.md`
  面向基层管理者，强调拆任务、盯进度、做汇报
- `prompts/entrypoints/doubao/head-office-leadership.md`
  面向总行/分行领导层，强调判断、风险、取舍、拍板项
- `prompts/entrypoints/doubao/auto.md`
  不确定身份或场景时使用

这些入口统一要求模型：

- 先读取 `registry/*.json`
- 回答前先列出准备读取的文件路径
- 显式写出调用了哪些 `skill / method / pack`
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
3. 根据问题路由到最相关的 `skills / methods / knowledge packs`
4. 读取对应正文
5. 输出时显式区分：
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

后续支持这些落地方向，但当前版本只做结构预留：

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
