---
type: index
status: active
area: learning
tags:
  - foc/learning
---

# 学习索引

## 主线顺序

1. 工具链与 NUCLEO 基础：[[materials/START_HERE]]
2. TIM1/ADC/JEOC 时序：[[docs/01_architecture/tim1_adc_jeoc_timing]]
3. Clarke/Park/SVPWM：[[docs/02_algorithm_b/clarke_park_svpwm]]
4. Hall 闭环：[[docs/02_algorithm_b/hall_sequence]]
5. PI 调参：[[docs/02_algorithm_b/pi_tuning]]
6. CORDIC/FMAC：[[docs/02_algorithm_b/cordic_fmac]]
7. SMO/PLL 无感：[[docs/02_algorithm_b/smo_pll_sensorless]]

## 学习卡片

```dataview
TABLE status, stage, source, evidence_level AS evidence
FROM "notes/10_learning"
WHERE type = "learning-note"
SORT file.mtime DESC
```

## 学习待办

```tasks
not done
path includes notes/10_learning
sort by due
```
