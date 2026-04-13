# Awesome Banker Skills

让银行人的优秀经验可安装、可传承、可复用。  
Installable skills and structured knowledge packs for bankers and banking clients.

`awesome-banker-skills` 是一个面向银行岗位与流程的 Skill 集合，支持两类核心资产：

- `skills`：岗位方法论与流程打法
- `knowledge-packs`：机构公开知识

## 核心定位

- 银行人的工作技能库
- 银行岗位与流程 Skill 平台
- 让优秀经验可安装、可传承、可复用

## 当前架构

```text
.
├─ skills/
│  ├─ roles/
│  │  └─ <skill>/SKILL.md + references/ + scripts/
│  └─ workflows/
│     └─ <skill>/SKILL.md + references/ + scripts/
├─ knowledge-packs/
│  └─ banks/ceb/
│     ├─ corporate-settlement/basic-settlement/
│     ├─ transaction-banking/yangguang-e-pay/
│     └─ trade-finance/yangguang-electricity-certificate/
├─ prompts/
├─ registry/
└─ workspace/
```

## 典型使用方式

### 1. 直接给模型使用（轻量）

先用一个“总入口 prompt”：

- `prompts/entrypoints/doubao-auto-router.md`

这段 prompt 会让模型自动读取 `registry/*.json`，自动选择 skill 和 knowledge pack 再回答。

如果你只想做某一个专项任务，再使用 `prompts/roles/*` 或 `prompts/workflows/*`。

### 2. 给 Agent 安装使用（重量）

读取 `registry/skills.json` 加载 `SKILL.md`，并在执行时调用：

- `references/*`（方法论、路由、输出约定）
- `scripts/build-context.py`（知识包路由）
- `scripts/validate-output.py`（结构校验）

## 支持用户自蒸馏并贡献

项目把“个人经验蒸馏 -> 仓库规范化 -> PR 贡献”设计为标准路径：

1. 用模板采集你的真实工作样本与判断逻辑  
   `templates/distill-skill/intake.md`
2. 按模板生成一个 skill 包  
   `templates/distill-skill/SKILL.template.md`
3. 补齐 `references/` 与 `scripts/`
4. 在 `registry/` 注册并提交 PR

详细见 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [docs/distillation/WORKFLOW.md](./docs/distillation/WORKFLOW.md)。

## 边界与合规

- 不会放真实客户数据
- 不会放内部制度原文
- 不会放内部审批、授信、定价结论
- 不会承诺额度、费率、时效与办理结果

## LICENSE

[MIT](./LICENSE)
