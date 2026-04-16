---
name: problem-opportunity-framework
description: Use when you need a reusable banking or finance analysis frame to identify the most urgent problem, the most plausible opportunity hypothesis, and the next validation move.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 问题-机会框架
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 问题-机会框架 Skill

## Scope

这是一个 reference skill。
它帮助你先识别真实问题，再形成最值得验证的机会假设，而不是一上来就跳到解决方案。

## When To Use

- 还不确定问题是否成立
- 需要判断哪条机会线索更值得跟
- 需要从“聊得很多”收束为“下一步先验证什么”

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次至少给出三样东西：

1. 当前最痛的 1 个问题
2. 最值得验证的 1 个机会假设
3. 下一次沟通该验证的 1 个动作

## Not For

- 直接代替 action skill 产出完整方案
- 直接下产品结论
- 替代最新事实核验
