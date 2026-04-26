---
name: enterprise-cash-flow-judgment
description: Use when you need a banker's professional lens to read enterprise cash flow signals — assessing cash generation quality, funding balance, and credit-relevant warning signs from financial statements.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 企业现金流判断
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 企业现金流判断 Skill

## Scope

这是一个 reference skill。
它帮助你从银行信审视角，对企业三张报表的现金流信息做出专业判断框架，而不是套用财务教材的现金流公式。

## When To Use

- 需要从财报中判断企业真实现金生成能力
- 需要判断客户现金流是否健康、是否可持续
- 需要在客户拜访前评估一个企业的现金质量
- 需要判断融资需求是否与现金流状态匹配
- 需要区分"账面利润"和"真实现金"的差距

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Banker vs. Accountant Perspective

银行视角与财务视角的核心差异：

| 维度 | 财务视角 | 银行视角 |
|------|----------|----------|
| 关注焦点 | 净利润质量 | 偿还能力 |
| 时间 horizon | 全周期 | 12–24个月 |
| 关键指标 | 净现值、EPS | 经营现金流/债务比、自由现金流 |
| 折旧处理 | 非现金项目 | 还债能力的一部分 |
| 假设前提 | 持续经营假设 | 违约风险下的清偿顺序 |

银行不关心会计利润有多高，只关心：到期的贷款能不能用现金还。

## Required Inputs

- 近三年资产负债表（简化版即可）
- 近三年现金流量表（经营/投资/融资三段）
- 近三年利润表（参考，不作为主判断依据）

## Quality Gate

- 是否区分了"真实现金"与"账面利润"
- 是否指出了现金流信号与融资需求的匹配关系
- 是否标注了还缺什么关键信息
- 是否避免了授信、定价、审批承诺
