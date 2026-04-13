---
name: corp-relationship-manager
description: 面向对公客户经理场景的方法论技能。用于客户洞察、机会判断、推进策略、沟通口径与跨流程协同，不输出审批或授信结论。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: role
  display_name_zh: 对公客户经理
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
  related_prompts:
    - prompt.role.corp-relationship-manager
  references_dir: references
  scripts_dir: scripts
---

# 对公客户经理 Skill

## Scope

这是岗位方法论 skill，不是产品知识库，不是审批系统，不替代正式业务受理。

## Required Reads

执行前按顺序读取：

1. `references/role-methodology.md`
2. `references/knowledge-routing.md`
3. `references/output-contract.md`
4. 按路由结果读取对应 knowledge pack 的 `README.md` 与 `modules/`

## Knowledge Routing

根据问题关键词从 `references/knowledge-routing.md` 选包：

- 结算、账户、收付、回单、对账 -> `pack.banks.ceb.corporate-settlement.basic-settlement`
- e付通、订单、账单、开票、协同 -> `pack.banks.ceb.transaction-banking.yangguang-e-pay`
- 电费证、电费、电网、福费廷、国内证 -> `pack.banks.ceb.trade-finance.yangguang-electricity-certificate`

如果命中多个包，先输出跨包判断，再分包给建议。

## Input Contract

最低输入字段：

- 客户类型与行业
- 当前经营或交易场景
- 当前卡点
- 目标推进动作

输入不足时先追问关键缺口，不直接给方案结论。

## Output Contract

输出必须包含以下段落：

1. `场景判断`
2. `机会假设`
3. `建议切入口`
4. `下一步推进动作`
5. `风险与边界`

## Quality Gate

输出前自检：

- 是否把公开知识和岗位判断分层表达
- 是否出现审批/授信/定价承诺
- 是否要求或复述了敏感数据
- 是否给出了明确下一步动作

## Script Hooks

- `scripts/build-context.py`：根据问题自动给出推荐知识包与参考材料
- `scripts/validate-output.py`：校验输出结构是否完整
