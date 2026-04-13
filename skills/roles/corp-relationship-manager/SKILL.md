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
    - pack.common.banker-thinking.top-performer
    - pack.common.economics.business-basics
    - pack.common.sales.consultative-b2b
    - pack.common.psychology.business-communication
  related_prompts:
    - prompt.role.corp-relationship-manager
  references_dir: references
  scripts_dir: scripts
---

# 对公客户经理 Skill

## Scope

这是岗位方法论 skill，不是产品知识库，不是审批系统，不替代正式业务受理。  
目标是帮助客户经理把“模糊问题”转成“可执行动作”。

## 适用场景

- 客户首次接触前，不确定从哪个业务问题切入
- 客户提出“先了解一下产品”，但真实需求尚不清晰
- 业务会谈后需要形成下一步推进动作
- 需要把公开知识与岗位判断分层表达，避免空泛输出

## 工作循环（建议）

1. 场景定性：先判断客户处于“经营动作、交易动作、融资动作”哪一层
2. 卡点定位：识别资金、结算、协同、决策链上的主要阻塞点
3. 假设生成：给出 1-2 个可验证的机会假设，不直接下结论
4. 动作设计：输出下一次沟通可执行动作和验证口径
5. 复盘迭代：记录反馈并更新下一轮问题清单

## Required Reads

执行前按顺序读取：

1. `references/role-methodology.md`
2. `references/knowledge-routing.md`
3. `references/output-contract.md`
4. 按路由结果读取对应 knowledge pack 的 `README.md` 与 `modules/`
5. 需要演示时读取 `faq.md`，优先回答常见客户问题

## Knowledge Routing

根据问题关键词从 `references/knowledge-routing.md` 选包：

- 结算、账户、收付、回单、对账 -> `pack.banks.ceb.corporate-settlement.basic-settlement`
- e付通、订单、账单、开票、协同 -> `pack.banks.ceb.transaction-banking.yangguang-e-pay`
- 电费证、电费、电网、福费廷、国内证 -> `pack.banks.ceb.trade-finance.yangguang-electricity-certificate`
- 思维框架、复盘、优先级、执行节奏 -> `pack.common.banker-thinking.top-performer`
- 利率、通胀、周期、现金流 -> `pack.common.economics.business-basics`
- 销售、异议、需求洞察、推进 -> `pack.common.sales.consultative-b2b`
- 心理、信任、认知偏差、沟通摩擦 -> `pack.common.psychology.business-communication`

如果命中多个包，先输出跨包判断，再分包给建议。

## Input Contract

最低输入字段：

- 客户类型与行业
- 当前经营或交易场景
- 当前卡点
- 目标推进动作

输入不足时先追问关键缺口，不直接给方案结论。
推荐补充字段：

- 主要交易对手或上下游关系
- 当前流程是否线上化、是否多角色协同
- 本次沟通对象（老板/财务/业务负责人）
- 希望达成的最小结果（例如：明确下一次会谈主题）

## Output Contract

输出必须包含以下段落：

1. `场景判断`
2. `机会假设`
3. `建议切入口`
4. `下一步推进动作`
5. `风险与边界`
6. `客户可能会问的3个问题`
7. `建议应答话术（公开口径）`

## Quality Gate

输出前自检：

- 是否把公开知识和岗位判断分层表达
- 是否出现审批/授信/定价承诺
- 是否要求或复述了敏感数据
- 是否给出了明确下一步动作
- 是否引用了知识包 `faq.md` 的常见问题口径

## Script Hooks

- `scripts/build-context.py`：根据问题自动给出推荐知识包与参考材料
- `scripts/validate-output.py`：校验输出结构是否完整
