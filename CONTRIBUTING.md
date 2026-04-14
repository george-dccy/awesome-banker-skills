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

原因很简单：

- 很多高价值内容一开始还带有个人经验色彩
- 很多素材最初还没有完成去敏感化
- 很多方法需要先在本地磨一轮再决定是否公开

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

## workflow 应优先承载什么

- 某个具体场景的最低输入
- 场景内的编排顺序与调用关系
- 输出契约、边界和风险提示
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
- [公开蒸馏流程](./docs/contribution/distillation-workflow.md)

## 内容红线

- 禁止真实客户数据
- 禁止内部制度原文
- 禁止审批、授信、定价、时效承诺
- 禁止无法公开传播的敏感内容
