# Knowledge Routing

## Pack Mapping

- `pack.banks.ceb.corporate-settlement.basic-settlement`
  - 关键词：结算、账户、收款、付款、回单、对账、权限
- `pack.banks.ceb.transaction-banking.yangguang-e-pay`
  - 关键词：e付通、订单、账单、开票、线上协同、供应链协同
- `pack.banks.ceb.trade-finance.yangguang-electricity-certificate`
  - 关键词：电费证、电费缴纳、电网、国内证、福费廷

## Priority

1. 先匹配最强关键词。
2. 多包命中时按“基础结算 -> 交易协同 -> 贸易融资场景”顺序解释。
3. 无匹配时仅输出方法论，不编造知识细节。