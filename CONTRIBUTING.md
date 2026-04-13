# CONTRIBUTING

## 我可以贡献什么

1. 新增岗位 skill（`skills/roles/*`）
2. 新增流程 skill（`skills/workflows/*`）
3. 新增知识包（`knowledge-packs/*`）
4. 改进 prompts、registry、文档

## 用户自蒸馏贡献流程

1. 先完成蒸馏采集  
   使用 [templates/distill-skill/intake.md](./templates/distill-skill/intake.md)
2. 生成 skill 草稿  
   使用 [templates/distill-skill/SKILL.template.md](./templates/distill-skill/SKILL.template.md)
3. 补齐 `references/` 与 `scripts/*.py`
4. 在 `registry/skills.json` 注册 skill
5. 如果涉及公开事实，新增或关联对应 knowledge pack
6. 更新 README 相关目录说明并提交 PR

## PR 最低检查项

- `SKILL.md` 的 `name` 与目录名一致
- skill 目录包含 `references/` 与 `scripts/`
- `scripts/` 使用 Python 文件（`.py`）
- `related_packs` 与 `references/knowledge-routing.md` 一致
- `registry/*.json` 已同步更新
- 不包含真实敏感信息与内部材料

## 内容红线

- 禁止真实客户数据
- 禁止内部制度原文
- 禁止审批、授信、定价承诺
- 禁止无法公开传播的敏感内容
