---
name: online-credit-admission-strategy-patterns
description: Use when you need a judgment framework for suggesting admission-strategy structure in online credit automated approval proposals without pretending to set internal credit policy.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 线上授信准入策略建议
  audience: [bank-practitioner, manager]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
  related_skills:
    - skill.reference.online-credit-solution-lens
    - skill.action.online-credit-approval-solution-drafting
    - skill.action.product-matching-boundary
    - skill.reference.enterprise-cash-flow-judgment
  related_prompts: []
  boundary:
    - "本 skill 只提供准入策略建议框架，不替代内部准入政策、评分卡、审批规则和阈值设定"
    - "需要真实客户、平台或核心企业材料时，应明确写待补资料或待人工确认"
    - "涉及授信额度、定价、期限和审批结论的最终口径时，当前仓库未覆盖"
---

# 线上授信准入策略建议 Skill

## Scope

这是一个 reference skill。
它聚焦“准入策略怎么想、怎么表达、怎么留边界”，用于线上授信自动化审批业务方案中的准入策略章节。

## When To Use

- 需要为线上授信自动化审批业务方案设计准入策略章节
- 已有业务模式和场景信息，但不确定从哪些维度判断准入
- 需要区分“可给建议的框架”和“必须内部拍板的政策”
- 需要为 action skill 提供稳定的准入策略判断框架

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次给准入策略建议时，至少要分清楚：

1. **业务模式**：这是什么样的对公或产业场景融资
2. **准入对象**：谁是核心企业、平台、经销商、供应商或借款主体
3. **还款来源**：靠真实交易、经营现金流、应收账款、回款归集还是其他来源
4. **数据可核验性**：哪些关键数据真实、连续、可交叉验证
5. **风控与管理闭环**：反欺诈、反洗钱、资金用途、放款审核、贷后管理是否有抓手

## Not For

- 直接设定准入阈值、评分分数线或命中规则
- 替代内部风控模型、授信政策或审批意见
- 在没有场景、数据和还款来源信息时硬写“准入标准”

## Quality Gate

- 是否按业务模式、场景、主体、还款来源、数据、风控、风险缓释几个维度组织
- 是否把“建议框架”和“内部政策”分开
- 是否适合直接嵌入“授信方案”章节
- 是否明确写了待补资料和待人工确认项

## Boundary With Related Assets

| 资产 | 做什么 | 使用时机 |
|------|--------|----------|
| `skill.reference.online-credit-admission-strategy-patterns`（本 skill） | 准入策略建议框架 | 已经进入准入策略章节 |
| `skill.reference.online-credit-solution-lens` | 整体方案判断框架 | 刚开始搭方案骨架 |
| `skill.action.online-credit-approval-solution-drafting` | 问答补数和章节草拟 | 需要直接起草 |
