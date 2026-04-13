# Distillation Workflow

## 目标

把个人经验中的“可复用工作方式”沉淀为可安装 Skill，并可贡献到仓库。

## 步骤

1. **采集原料**  
   填写 `templates/distill-skill/intake.md`，记录真实工作样本。
2. **提炼结构**  
   抽取：触发场景、判断框架、动作顺序、输出格式、失败场景。
3. **落地 Skill**  
   创建 `SKILL.md + references/ + scripts/*.py`。
4. **关联知识**  
   在 `related_packs` 和 `references/knowledge-routing.md` 中显式声明关联。
5. **注册发现**  
   更新 `registry/skills.json`（必要时更新 `registry/prompts.json`）。
6. **提 PR**  
   说明来源、边界和验证方式。

## 可复用判断标准

- 脱离个人背景后仍可执行
- 输入输出可描述、可校验
- 风险边界清晰
- 能与现有 knowledge packs 协同
