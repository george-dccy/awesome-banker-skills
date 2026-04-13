---
name: <slug-name>
description: <一句话描述这个 skill 的职责和边界>
license: MIT
metadata:
  banker_kind: <role|workflow>
  display_name_zh: <中文展示名>
  related_packs:
    - <pack-id-1>
  related_prompts:
    - <prompt-id-1>
  references_dir: references
  scripts_dir: scripts
---

# <中文标题>

## Scope

写清楚这个 skill 负责什么，不负责什么。

## Required Reads

1. `references/<file-1>.md`
2. `references/knowledge-routing.md`
3. `references/output-contract.md`

## Knowledge Routing

用关键词 -> pack id 的方式写清楚路由规则。

## Input Contract

写清楚最低输入字段。

## Output Contract

写清楚必须出现的输出段落。

## Quality Gate

写清楚发布前自检项。

## Script Hooks

- `scripts/build-context.py`
- `scripts/validate-output.py`
