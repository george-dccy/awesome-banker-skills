---
name: market-corporate-client
description: 对公客户营销流程技能。用于营销前诊断、切入口设计、会谈目标定义和会后推进动作。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户营销
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

这个 workflow 聚焦“营销前”和“首次接触”，目标是形成可执行的切入口与下一步动作。  
强调“先诊断再推荐”，避免一上来堆产品信息。

## 适用场景

- 计划首次拜访客户，想要明确开场与切入口
- 客户意向模糊，需要先把场景与痛点说清楚
- 准备业务会议演示，需要可直接讲解的营销路径

## Required Reads

1. `references/pre-call-diagnosis.md`
2. `references/opening-playbook.md`
3. `references/knowledge-routing.md`
4. 命中业务包后，读取对应 `README.md`、`modules/*`、`faq.md`

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
- 是否引用了相应产品包 FAQ 进行客户问题应答
- 是否包含明确下一步时间点与责任人
- 是否避免审批、额度、费率、时效承诺

## Script Hooks

- `scripts/build-context.py`：根据问题路由知识包并返回建议读取顺序
- `scripts/validate-output.py`：校验结构完整性与承诺风险
