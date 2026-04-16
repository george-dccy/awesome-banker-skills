# Distillation Workflow

## 目标

把公开材料、仓库已有资产和用户经验，持续蒸馏成可复用的：

- reference skill
- action skill
- knowledge

默认先沉淀到 private，再由用户决定是否整理为 public contribution。

## 推荐流程

1. 采集原料
   - 文档
   - 公开链接
   - 公开网页
   - 说明材料
   - 用户补充经验
2. 判断资产类型
   - 专业视角、判断框架、表达结构 -> `skills/reference`
   - 场景最低输入、动作顺序、输出结构、检查点 -> `skills/action`
   - 公开知识、产品资料、FAQ、来源 -> `knowledge`
3. 先生成 private draft
   - 写入 `workspace/private/*`
   - 记录 patch proposal 或 memory
   - 明确这次更像一次性笔记，还是值得长期复用的个人资产
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

## Agent 默认动作

如果 Agent 接收到的是“经验、偏好、复盘、失败教训、典型案例、常用表达、长期提醒”，默认不要只做当轮回答，建议按下面顺序处理：

1. 先解决当前问题
2. 再判断哪些内容值得长期保留
3. 给出建议归类
   - 专业视角或判断习惯 -> `workspace/private/skills/reference`
   - 可重复执行的任务打法 -> `workspace/private/skills/action`
   - 公开知识专题 -> `workspace/private/knowledge`
   - 个人偏好、提醒、教训 -> `workspace/private/memories`
   - 具体案例材料 -> `workspace/private/case-notes`
4. 输出最小沉淀建议
   - 建议目标路径
   - 建议新增或修改的文件
   - 建议保留的关键信息
   - 风险和公开边界
5. 经用户确认后，再写入 private
6. 如适合公开，再整理成 public candidate

## 标准化产物

根据资产类型，至少补齐以下内容：

- `SKILL.md` / `README.md` / `pack.json` / `skill.json`
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
