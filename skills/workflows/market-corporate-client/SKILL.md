---
name: market-corporate-client
description: 对公客户营销流程技能。用于营销前诊断、切入口设计、会谈目标定义和会后推进动作。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户营销
  orchestration_focus: 首访营销场景编排
  related_methods:
    - method.business-operations.problem-opportunity-scan
    - method.business-operations.client-advance-map
  related_packs:
    - pack.banks.ceb.corporate-settlement.basic-settlement
    - pack.banks.ceb.transaction-banking.yangguang-e-pay
    - pack.banks.ceb.trade-finance.yangguang-electricity-certificate
    - pack.common.banker-thinking.top-performer
    - pack.common.economics.business-basics
    - pack.common.sales.consultative-b2b
    - pack.common.psychology.business-communication
  related_prompts:
    - prompt.workflow.market-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户营销 Skill

## Scope

这个 workflow 是“首访营销场景编排器”，聚焦“营销前”和“首次接触”，负责组织输入、调用方法框架和知识包，不再承载通用客户推进方法本体。
强调“先诊断再推荐”，避免一上来堆产品信息。

## 适用场景

- 计划首次拜访客户，想要明确开场与切入口
- 客户意向模糊，需要先把场景与痛点说清楚
- 准备业务会议演示，需要可直接讲解的营销路径

## Required Reads

1. `references/pre-call-diagnosis.md`
2. `references/opening-playbook.md`
3. `references/knowledge-routing.md`
4. `method.business-operations.problem-opportunity-scan`
5. `method.business-operations.client-advance-map`
6. 命中业务包后，读取对应 `README.md`、`modules/*`、`faq.md`

## Orchestration Rule

1. 先用 `problem-opportunity-scan` 判断客户卡点与机会
2. 再用 `client-advance-map` 明确首次会谈目标和最小推进动作
3. 最后按 `knowledge-routing` 命中需要补充的公开知识包

## Input Contract

最低输入：

- 行业
- 当前卡点
- 会谈对象
- 希望达成的最小结果

## Output Contract

输出至少包含：

1. 客户场景初判
2. 推荐切入口（1-3 个）
3. 首次会谈目标
4. 不宜过早触达的话题
5. 会后推进动作
6. 客户常见追问与建议回答（公开口径）

## Quality Gate

- 是否先输出场景判断，再输出产品建议
- 是否先调用相关 method，再落到具体知识包
- 是否引用了相应产品包 FAQ 进行客户问题应答
- 是否包含明确下一步时间点与责任人
- 是否避免审批、额度、费率、时效承诺

## Script Hooks

- `scripts/build-context.py`：根据问题路由知识包并返回建议读取顺序
- `scripts/validate-output.py`：校验结构完整性与承诺风险
