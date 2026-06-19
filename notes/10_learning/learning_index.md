---
type: index
status: active
area: learning
language: zh-CN
tags:
  - foc/learning
  - foc/learning/index
---

# 中文学习索引

这个索引服务中文优先的 STM32 / FOC 学习卡片。`notes/10_learning/` 可以记录个人理解、问题和复习材料；只有经过项目事实核对、实验记录或正式文档回写的内容，才可以作为项目结论使用。

## 主线顺序

1. 工具链与 NUCLEO 基础：[[materials/START_HERE]]
2. TIM1 / ADC / JEOC 时序：[[docs/01_architecture/tim1_adc_jeoc_timing]]
3. Clarke / Park / SVPWM：[[docs/02_algorithm_b/clarke_park_svpwm]]
4. Hall 闭环概念：[[docs/02_algorithm_b/hall_sequence]]
5. PI 调参：[[docs/02_algorithm_b/pi_tuning]]
6. CORDIC / FMAC：[[docs/02_algorithm_b/cordic_fmac]]
7. SMO / PLL 无感概念：[[docs/02_algorithm_b/smo_pll_sensorless]]

## 中文卡片类型

| 类型 | 适合内容 | 模板 | 必备标签 |
| --- | --- | --- | --- |
| 概念卡 | 一个原理、时序、算法或接口边界 | [[notes/99_templates/chinese_concept_card|chinese_concept_card]] | `foc/learning/zh`, `foc/concept` |
| 术语卡 | 一个缩写、变量名、函数名或英文术语 | [[notes/99_templates/chinese_term_card|chinese_term_card]] | `foc/learning/zh`, `foc/glossary` |
| 复习卡 | 错题、薄弱点、间隔复习问题 | [[notes/99_templates/chinese_review_card|chinese_review_card]] | `foc/learning/zh`, `foc/review` |

## 标签规则

基础标签：

- `foc/learning/zh`：所有中文优先学习卡。
- `foc/concept`：概念卡。
- `foc/glossary`：术语 / 缩写 / 函数名解释。
- `foc/review`：复习卡、错题卡、薄弱点。

主题标签：

- `foc/topic/timing`：TIM、ADC、JEOC、ISR、采样时序。
- `foc/topic/hall`：Hall 状态、方向、速度估计、软件 Hall 学习。
- `foc/topic/mcsdk`：MCSDK / Workbench / 生成工程边界。
- `foc/topic/algorithm`：Clarke、Park、SVPWM、PI、SMO/PLL。
- `foc/topic/safety`：安全边界、禁区、上电前检查概念。
- `foc/topic/gateway`：ESP32-C3、UART、WebSocket、看板。

状态标签：

- `foc/status/draft`：草稿理解，不能作为项目事实。
- `foc/status/reviewed`：已由 Codex 或人工复核为学习材料。
- `foc/status/needs-source`：需要补来源或官方资料。

## 链接策略

每张中文卡片至少包含三类链接：

- 上游来源：链接到 `docs/`、`workflow/`、`learning/` 或可信资料，例如 [[docs/00_project_truth/project_context]]。
- 邻近概念：链接到 1-3 张相关概念或术语卡，例如 [[hall-state-sequence-cn]]。
- 回写目标：如果内容可能影响项目方案、实验结论或答辩材料，写明应回写到 `docs/`、`experiments/`、`interfaces/` 或 `deliverables/`。

命名建议：

- 概念卡：`concept-name-cn.md`，例如 [[tim1-adc-jeoc-window-cn]]。
- 术语卡：`term-name-cn.md`，例如 [[hall-state-sequence-cn]]。
- 复习卡：`review-topic-cn.md`，例如 [[software-hall-review-cn]]。

## 示例卡片

- [[notes/10_learning/chinese/tim1-adc-jeoc-window-cn|TIM1 / ADC / JEOC 采样窗口]]
- [[notes/10_learning/chinese/hall-state-sequence-cn|Hall 状态序列]]
- [[notes/10_learning/chinese/software-hall-review-cn|软件 Hall 复习卡]]

## Dataview 查询

### 最近中文学习卡

```dataview
TABLE status, card_type AS type, topic, mastery, review_due
FROM "notes/10_learning/chinese"
WHERE contains(tags, "foc/learning/zh")
SORT file.mtime DESC
```

### 需要补来源的卡片

```dataview
TABLE topic, source_status, project_writeback
FROM "notes/10_learning/chinese"
WHERE contains(tags, "foc/status/needs-source") OR source_status = "needs-source"
SORT file.mtime DESC
```

### 到期复习

```dataview
TABLE topic, mastery, review_due, weak_point
FROM "notes/10_learning/chinese"
WHERE contains(tags, "foc/review") AND review_due <= date(today)
SORT review_due ASC
```

## 学习待办

```tasks
not done
path includes notes/10_learning
sort by due
```
