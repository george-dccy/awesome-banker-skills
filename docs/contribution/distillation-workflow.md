# Distillation Workflow

## 目标

把公开材料、仓库已有资产和用户经验，持续蒸馏成可复用的：

- role skill
- workflow skill
- knowledge pack
- method

默认先沉淀到 private，再由用户决定是否整理为 public contribution。

## 推荐流程

1. 采集原料
   - 文档
   - 公开链接
   - 公开网页
   - 说明材料
   - 用户补充经验
2. 判断资产类型
   - 岗位方法 -> `skills/roles`
   - 流程动作 -> `skills/workflows`
   - 公开知识 -> `knowledge-packs/banks` 或 `knowledge-packs/common`
   - 通用框架 -> `methods`
3. 先生成 private draft
   - 写入 `workspace/private/*`
   - 记录 patch proposal 或 memory
4. 做增量更新
   - 优先补缺口
   - 避免每次整包重写
5. 用户确认
   - 确认是否继续保留 private
   - 或整理为 public candidate
6. 生成标准化输出
   - 目录结构
   - 正文文件
   - registry 更新
   - 变更摘要
   - PR 草稿

## 标准化产物

根据资产类型，至少补齐以下内容：

- `README.md`
- `SKILL.md` / `pack.json` / `method.json`
- `frameworks.md` / `faq.md` / `sources.md`
- `modules/*`
- `registry/*.json`
- 贡献说明或变更摘要

## 判断标准

- 脱离个人背景后仍可执行
- 输入输出可描述、可校验
- 边界清楚
- 能与现有仓库结构协同
- 公开版不包含敏感内容
