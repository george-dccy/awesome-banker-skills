# CONTRIBUTING

## 你可以贡献什么

这个仓库是一个面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力，甚至可以不断成长为金融人面对客户时的分身。

- 新增或改进 `skills/reference/*`
- 新增或改进 `skills/action/*`
- 新增或改进 `knowledge/*`
- 改进 prompts、registry、docs、模板与路由说明

## 推荐贡献路径

当前推荐走：

`private-first -> public-candidate -> merge to public`

原因是：

- 很多高价值内容一开始还带有个人经验色彩
- 很多素材最初还没有完成去敏感化
- 很多结构需要先在本地磨一轮再决定是否公开

## 仓库协作入口

- Gitee 主仓库：`https://gitee.com/georgedccy/financial-capability-kit.git`
- GitHub 镜像仓库：`https://github.com/george-dccy/financial-capability-kit.git`

贡献协作默认约定：

- 优先向 Gitee 提交 PR
- GitHub 主要用于展示、同步和备份
- 如无特殊说明，以 Gitee 上的 PR 讨论、review 和合并结果为准

## 建议流程

1. 先采集或整理原料
2. 使用 `skill.action.distill-and-curate` 判断资产类型与推荐落点
3. 默认先生成到 `workspace/private/*`
4. 做增量补全，而不是每次全量重写
5. 确认可以公开后，再整理为 public candidate
6. 同步更新对应 `registry/*.json`

## 如何使用 distill-and-curate 做贡献

推荐把 `skill.action.distill-and-curate` 作为默认贡献入口。

它可以帮助你：

- 判断内容属于 reference skill、action skill 还是 knowledge
- 推荐应该放到 public 还是 `workspace/private/*`
- 基于仓库已有内容做增量更新
- 自动整理 README、sources、faq、modules、registry 变更建议和 PR 摘要

常用指令示例：

- “请使用 `skill.action.distill-and-curate`，把这份公开资料整理成 knowledge 草稿，先写到 private。”
- “请使用 `skill.action.distill-and-curate`，补全这个 reference skill 的 frameworks 和 examples。”
- “请使用 `skill.action.distill-and-curate`，把 `workspace/private` 里的草稿整理成可公开贡献候选，并给出 Gitee PR 摘要。”

## 最低检查项

- 资产类型归类正确，没有混层
- `skills/reference`、`skills/action`、`knowledge` 的边界清楚
- registry path 与真实目录一致
- 不包含真实敏感信息与内部材料
- 公开知识类资产补齐来源
- 公开贡献前明确边界，不输出审批、授信、定价、时效承诺

## 各类资产最低结构

### Reference Skill

- `SKILL.md`
- `skill.json`（如适用）
- `references/*`
- `scripts/*.py`

### Action Skill

- `SKILL.md`
- `references/*`
- `scripts/*.py`

### Knowledge

- `README.md`
- `faq.md`
- `sources.md`
- `modules/*`
- `pack.json`（如适用）

## 推荐参考

- [架构说明](./docs/architecture/README.md)
- [Skill 分类说明](./docs/architecture/skill-taxonomy.md)
- [公开提炼流程](./docs/contribution/distillation-workflow.md)

## 内容红线

- 禁止真实客户数据
- 禁止内部制度原文
- 禁止审批、授信、定价、时效承诺
- 禁止无法公开传播的敏感内容
