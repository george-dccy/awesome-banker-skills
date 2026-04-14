# Invocation Rules

推荐主路由：

`role overlay -> workflow -> method -> knowledge pack`

role skill 只负责提供岗位视角，不替代 workflow 的场景编排。

## 先决定是否调用 workflow

- 首访、开场、找切入口、初步判断客户价值 -> `workflow.market-corporate-client`
- 会后跟进、跨团队协同、问题闭环、持续关系推进 -> `workflow.accompany-corporate-client`
- 对内汇报、同步风险、提请拍板、梳理上提事项 -> `workflow.report-to-leader`

## 再决定是否补 method

- 识别真实卡点、机会点、优先级 -> `method.business-operations.problem-opportunity-scan`
- 设计下一步最小推进动作、协同链和时间点 -> `method.business-operations.client-advance-map`

## 最后再补 knowledge pack

- 结算、账户、收付、回单、对账、权限 -> `pack.banks.ceb.corporate-settlement.basic-settlement`
- e付通、订单、账单、开票、线上协同 -> `pack.banks.ceb.transaction-banking.yangguang-e-pay`
- 电费证、电费、电网、国内证、福费廷 -> `pack.banks.ceb.trade-finance.yangguang-electricity-certificate`

## 一条硬规则

如果问题主要是“这个岗位通常先看什么、先判断什么、先怎么和不同对象沟通”，优先用 role skill。  
如果问题主要是“这个场景要收什么输入、按什么顺序推进、输出什么”，优先进入 workflow。
