---
name: branch-operating-diagnosis-lens
description: Use when you need a judgment framework for interpreting branch or frontline operating results, separating result issues from structure issues, and identifying what to check next.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 经营分析视角
  audience: [bank-practitioner, manager]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
  related_skills:
    - skill.action.branch-operating-diagnosis
    - skill.action.report-decision-brief
    - skill.reference.executive-briefing-decision-support
    - skill.action.interpret-financial-signal
  related_prompts: []
  boundary:
    - "本 skill 提供经营分析判断框架，不替代内部经营分析报表、考核口径和经营例会决策"
    - "没有口径一致的数据时，应优先补数而不是硬下结论"
    - "涉及内部经营考核规则、内部目标分解或敏感客户数据时，当前仓库未覆盖"
---

# 经营分析视角 Skill

## Scope

这是一个 reference skill。
它解决的不是“替你写经营报告”，而是当你拿到一组经营数据、目标和自我判断时，先知道该怎么看、先分什么层、哪些地方要继续追问。

## When To Use

- 需要先判断分支行、网点或团队经营结果是好还是不好
- 需要区分问题更像结果问题、结构问题、过程问题还是外部环境问题
- 需要为后续经营建议、汇报简报或动作排序提供稳定判断框架
- 需要在“数据很多但不知道先看什么”时快速收束视角

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次进入经营分析，至少先明确：

1. **结果判断**：当前结果到底是亮点、持平还是短板
2. **结构判断**：结果背后是客户结构、产品结构、区域结构还是过程动作问题
3. **变化判断**：与目标、上期、去年同期相比，变化到底来自哪里
4. **归因判断**：是内生经营能力问题，还是外部环境和阶段性因素影响
5. **下一步判断**：当前还缺哪些关键补数，哪些结论可以先说，哪些要保留

## Not For

- 直接给出内部经营考核结论
- 替代具体的经营分析 action skill
- 在没有口径一致的数据时硬写“结论先行”的经营报告
- 把公开行业常识冒充为当前机构的真实经营状态

## Quality Gate

- 是否优先回答“结果好不好、结构好不好、变化来自哪里”
- 是否把判断框架和执行脚本分开
- 是否避免落入流水账式报数
- 是否明确写出待补数项和边界

## Boundary With Related Assets

| 资产 | 做什么 | 使用时机 |
|------|--------|----------|
| `skill.reference.branch-operating-diagnosis-lens`（本 skill） | 判断框架：先看什么、先分什么层、先追什么问题 | 刚开始做经营分析 |
| `skill.action.branch-operating-diagnosis` | 执行脚本：采集目标、关键数据、自评并生成结构化结论 | 需要直接开始分析输出 |
| `skill.action.report-decision-brief` | 汇报执行：把经营判断整理成可拍板或可汇报的表达 | 需要向上汇报 |
