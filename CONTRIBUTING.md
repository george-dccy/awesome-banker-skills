# CONTRIBUTING

## 你可以贡献什么

- 新增或改进岗位 skill：`skills/roles/*`
- 新增或改进流程 skill：`skills/workflows/*`
- 新增或改进 knowledge pack：`knowledge-packs/*`
- 新增或改进 method：`methods/*`
- 改进 prompts、registry、docs、模板与路由说明

## 推荐贡献路径

当前推荐走：

`private-first -> public-candidate -> merge to public`

原因是：

- 很多高价值内容一开始还带有个人经验色彩
- 很多素材最初还没有完成去敏感化
- 很多方法需要先在本地磨一轮再决定是否公开

## 仓库协作入口

- Gitee 主仓库：`https://gitee.com/georgedccy/awesome-banker-skills.git`
- GitHub 镜像仓库：`https://github.com/george-dccy/awesome-banker-skills.git`

贡献协作默认约定：

- 优先向 Gitee 提交 PR
- GitHub 主要用于展示、同步和备份
- 如无特殊说明，以 Gitee 上的 PR 讨论、review 和合并结果为准

## 建议流程

1. 先采集或整理原料
   - 文档
   - 公开链接
   - 公开网页
   - 说明材料
   - 用户经验与案例
2. 使用 `distill-and-contribute` 判断资产类型与推荐落点
3. 默认先生成到 `workspace/private/*`
4. 做增量补全，而不是每次全量重写
5. 确认可以公开后，再整理为 public candidate
6. 同步更新对应 `registry/*.json`

## 如何使用 distill-and-contribute 做贡献

推荐把 `workflow.distill-and-contribute` 作为默认贡献入口。

它可以帮助你：

- 判断内容属于 role skill、workflow skill、knowledge pack 还是 method
- 推荐应该放到 public 还是 `workspace/private/*`
- 基于仓库已有内容做增量更新
- 自动整理 README、sources、faq、modules、registry 变更建议和 PR 摘要

推荐使用顺序：

1. 准备原料
   - 公开文档
   - 公开链接
   - 公开网页
   - 个人经验与案例
   - 失败复盘
2. 先让 Agent 调用 `workflow.distill-and-contribute` 判断资产类型与推荐落点
3. 默认先生成到 `workspace/private/*`
4. 让 Agent 按现有结构做增量补全，不要每次全量重写
5. 你自己检查去敏感化、来源、边界和结构完整性
6. 再让 Agent 生成 public candidate、变更摘要和 PR 草稿
7. 优先向 Gitee 提交 PR

常用指令示例：

- “请使用 `workflow.distill-and-contribute`，把这份公开资料整理成 knowledge pack 草稿，先写到 private。”
- “请使用 `workflow.distill-and-contribute`，补全这个 method 的 examples、anti-patterns 和 related-assets。”
- “请使用 `workflow.distill-and-contribute`，把 `workspace/private` 里的草稿整理成可公开贡献候选，并给出 Gitee PR 摘要。”

## 最低检查项

- 资产类型归类正确，没有混层
- `skills`、`knowledge-packs`、`methods` 的边界清楚
- registry path 与真实目录一致
- 不包含真实敏感信息与内部材料
- 公开知识类资产补齐来源
- 公开贡献前明确边界，不输出审批、授信、定价、时效承诺

## workflow / method 三问法

1. 脱离当前场景还是否可复用
2. 这是在讲框架，还是在讲场景编排
3. 换一个岗位或流程后是否仍自然

## role skill 应优先承载什么

- 岗位使命与边界
- 默认视角与优先级规则
- 关键对象沟通差异
- 常见误区与反模式
- 何时调用 workflow / method / knowledge pack

## role skill 不应承载什么

- 场景最低输入
- 场景编排顺序
- 固定输出结构
- 详细知识路由
- 可跨岗位复用的方法框架

## workflow 应优先承载什么

- 某个具体场景的最低输入
- 场景内的编排顺序与调用关系
- 输出约定、边界和风险提示
- 该场景下需要调用哪些 methods 与 knowledge packs

## method 应优先承载什么

- 跨岗位、跨流程仍可复用的判断框架
- 跨场景复用的推进方法、复盘方法、汇报方法
- 适用边界、反模式和复用提醒

## 各类资产最低结构

### Skill

- `SKILL.md`
- `references/`
- `scripts/*.py`

### Knowledge Pack

- `README.md`
- `faq.md`
- `sources.md`
- `modules/*`
- `pack.json`（如适用）

### Method

- `README.md`
- `method.json`
- `frameworks.md`
- `examples.md`

## 推荐参考

- [架构说明](./docs/architecture/README.md)
- [Methods 层说明](./docs/architecture/methods.md)
- [公开提炼流程](./docs/contribution/distillation-workflow.md)

## 内容红线

- 禁止真实客户数据
- 禁止内部制度原文
- 禁止审批、授信、定价、时效承诺
- 禁止无法公开传播的敏感内容
