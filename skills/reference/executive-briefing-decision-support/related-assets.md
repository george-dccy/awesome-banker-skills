# 相关资产

## Related Skills

### skill.reference.decision-brief-framework

**路径**：`skills/reference/decision-brief-framework/SKILL.md`

**关系**：本 skill 判断"用什么结构"，decision-brief-framework 输出"五段式表达骨架"。

**使用顺序**：先判断汇报类型和结构（executive-briefing-decision-support），再选表达骨架（decision-brief-framework）。

**边界**：
- executive-briefing-decision-support：判断框架（汇报前用）
- decision-brief-framework：结构模板（写汇报时用）

---

### skill.action.report-decision-brief

**路径**：`skills/action/report-decision-brief/SKILL.md`

**关系**：本 skill 做判断，report-decision-brief 执行——采集事实、调用框架、输出汇报文稿。

**使用顺序**：先判断汇报结构（executive-briefing-decision-support），再决定是否需要调用 report-decision-brief 输出文稿。

**边界**：
- executive-briefing-decision-support：判断框架（汇报前用）
- report-decision-brief：执行脚本（写汇报时用）

---

## Related Knowledge

### knowledge.common.banker-thinking.top-performer

理解银行top performer的思维方式，有助于预判领导在汇报中的关注点和判断逻辑。

### knowledge.common.psychology.business-communication

商业沟通心理学知识，有助于理解汇报中的认知偏差和说服机制。

---

## Source Frameworks（公开方法论）

1. **Pyramid Principle** — Barbara Minto（麦肯锡），《金字塔原理》
   - 结论先行的理论基础

2. **BCG Decision Framework** — 波士顿咨询决策框架
   - 决策点识别的参考框架

3. **电梯演讲（Elevator Pitch）** — 麦肯锡等咨询机构广泛使用
   - 30秒汇报的结构基准

4. **SCQA Framework** — 麦肯锡《金字塔原理》章节
   - 背景先行汇报的结构框架

5. **麦肯锡七步法** — 《麦肯锡方法》
   - 反对意见预演步骤的参考

---

## Skill Registry Entry (Task Patterns)

本 skill 的 task_patterns 与现有 skill 的区分：

| Skill | Task Patterns | 差异 |
|-------|--------------|------|
| skill.reference.executive-briefing-decision-support（本 skill） | 汇报前判断、决策点识别、汇报结构选择、风险预判 | 汇报前判断框架 |
| skill.reference.decision-brief-framework | 向领导汇报、拍板简报、口头汇报、书面简报 | 表达结构模板 |
| skill.action.report-decision-brief | 向领导汇报、拍板、书面简报、口头汇报 | 执行脚本 |
| skill.reference.team-followup-framework | 团队跟进、检查点、复盘、责任人、闭环 | 团队管理闭环 |
