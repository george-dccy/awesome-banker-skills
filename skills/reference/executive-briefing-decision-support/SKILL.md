---
name: executive-briefing-decision-support
description: Use when you need a judgment framework to decide how to structure an executive briefing, identify decision points, and anticipate risks before presenting to leadership.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: communicate
  display_name_zh: 向上汇报与决策支持判断框架
  audience: [finance-learner, bank-practitioner, manager]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
  related_skills:
    - skill.reference.decision-brief-framework
    - skill.action.report-decision-brief
  related_knowledge:
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.reference.executive-briefing-decision-support
  boundary:
    - "本 skill 提供汇报前的判断框架，不是写报告的模板或脚本"
    - "写报告结构用 skill.reference.decision-brief-framework"
    - "写报告内容用 skill.action.report-decision-brief"
    - "三者边界：判断框架 vs. 结构模板 vs. 执行脚本"
---

# 向上汇报与决策支持判断框架 Skill

## Scope

这是一个 reference skill。
它不输出具体汇报内容，而是提供汇报前的判断框架：用什么结构、识别哪些是真正的决策点、预判哪些风险需要提前准备。

## When To Use

- 准备向领导汇报前，犹豫用哪种汇报结构
- 需要识别汇报中的决策点有哪些
- 需要预判领导可能的质疑和风险点
- 需要判断这件事需要领导"知道"还是"拍板"
- 不确定汇报应该结论先行还是背景先行

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次汇报前至少明确：

1. **汇报类型判断**：同步型 vs. 请求型 vs. 说服型
2. **结构选择**：结论先行还是背景先行（见 frameworks.md）
3. **决策点列表**：这次汇报需要领导做几个决定
4. **风险预判**：领导可能质疑什么，需要提前准备什么
5. **资源需求**：需要领导给什么（时间、人、钱、权）

## Not For

- 提供具体汇报话术或文字内容
- 替代 `skill.reference.decision-brief-framework` 的结构输出
- 替代 `skill.action.report-decision-brief` 的执行脚本
- 在没有基础事实时硬做判断

## Quality Gate

- 是否仍有判断框架而非内容模板
- 是否有银行/金融场景针对性
- 是否与 decision-brief-framework 和 report-decision-brief 边界清楚
- 是否有管理咨询公开方法论来源支撑

## Boundary With Related Assets

| 资产 | 做什么 | 使用时机 |
|------|--------|----------|
| `skill.reference.executive-briefing-decision-support`（本 skill） | 判断框架：用什么结构、识别决策点、预判风险 | 汇报前不知道怎么结构化 |
| `skill.reference.decision-brief-framework` | 结构模板：五段式表达骨架 | 知道要汇报，需要怎么组织 |
| `skill.action.report-decision-brief` | 执行脚本：替你采集事实写汇报 | 需要直接输出汇报文稿 |
