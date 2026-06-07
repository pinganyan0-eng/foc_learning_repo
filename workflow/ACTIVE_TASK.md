# 当前任务

## Task ID

- ID：TASK-2026-06-07-L4-power-board-mcu-prejoin-pwm-gate-prep
- 主题：自研功率板 MCU 接入前审查与空载 PWM/Gate 波形检查准备
- Status：done
- User Approval：2026-06-07
- Risk Level：L4
- Definition of Done：`workflow/definition_of_done.md#硬件审查任务`
- Evidence ID：EV-2026-06-07-HW-GATE-PREP-001
- Review Required：yes

## 背景

自研 STDRIVE101 功率板已完成 24V/0.2A 级别限流静态上电。HSPY-30-05 处于 CV，输入电流 0.04A；5V=5V，3V3=3.34V，REG12=12V，nFAULT=3.3V；无异味、异响和快速发热。证据已登记为 `EV-2026-06-05-HW-STATIC-PWR-001`。

当前尚未接电机、尚未输出 PWM、尚未测 Gate 波形。静态上电通过不能等同于动态功率级通过。

## 当前阶段

- 阶段 5：自研板首次上电 / 空载 PWM 与 Gate 波形检查准备。
- 当前不是电机运行、Hall 闭环或 SMO 无感阶段。
- 本任务只完成 MCU 接入前审查和空载 PWM/Gate 检查准备，不执行动态功率测试。

## 任务目标

1. 审查 MCU 接入前必须满足的硬件、供电、地线、信号、保护和测量条件。
2. 建立空载 PWM/Gate 波形检查准备表、示波器接地安全表、照片/波形命名规则和异常回退表。
3. 核对 STDRIVE101 官方资料和可靠的示波器接地/差分测量资料。
4. 明确当前已确认项、未确认项、禁止动作和下一阶段进入条件。

## 允许做

- 读取项目状态、阶段闸门、风险矩阵、原理图截图/BOM 线索、无电 DMM 和首次静态上电记录。
- 核验 STDRIVE101 官方 Datasheet/Application Note 和仪器厂商的示波器接地/差分测量资料。
- 新增 MCU 接入前审查、空载 PWM/Gate 准备、示波器安全、照片/波形目录和实验记录模板。
- 更新 `CURRENT_STATUS.md`、`docs/file_map.md`、`workflow/evidence_register.md` 和本任务结果区。
- 运行文档、索引和仓库状态检查命令。

## 禁止做

- 不接电机、不带载、不提高母线电压、不放开限流。
- 不远程指挥用户上电、反复上电或输出 PWM。
- 不修改 PWM、Gate、FOC、TIM1/TIM8、MCSDK 实时代码。
- 不修改保护阈值、死区、过流或 VDS 参数。
- 不把普通示波器地夹接到 OUTU/OUTV/OUTW、BOOT 或其他开关节点。
- 不采用断开示波器保护地的浮地测量方式。
- 不声称动态功率级、电流采样、电机运行、Hall 闭环或 SMO 已通过。

## 输入文件

- `CURRENT_STATUS.md`
- `workflow/teaching_contract.md`
- `workflow/phase_gate_checklist.md`
- `workflow/risk_gate_matrix.md`
- `docs/03_hardware_notes/power_board_evidence_package.md`
- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.md`
- `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`
- `hardware/bom/2026-05-09_user_provided_power_stage_parts.md`
- `experiments/2026-06-01_power_board_no_power_dmm/logs/2026-06-01_hall_control_connector_dmm_check.md`
- `experiments/2026-06-01_power_board_first_limited_power_precheck/`
- STDRIVE101 官方资料和仪器厂商测量安全资料

## 输出文件

- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/README.md`
- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/2026-06-07_mcu_prejoin_review_checklist.md`
- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/2026-06-07_pwm_gate_waveform_prep_sheet.md`
- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/2026-06-07_scope_grounding_safety_table.md`
- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/photos/README.md`
- `experiments/2026-06-07_power_board_mcu_prejoin_pwm_gate_prep/waveforms/README.md`
- `workflow/evidence_register.md`
- `docs/file_map.md`
- 必要时更新 `CURRENT_STATUS.md`

## 验收证据

- MCU 接入前审查清单、示波器接地安全表和空载 PWM/Gate 准备表已完成。
- 照片和波形截图命名规范已完成。
- 官方资料来源、当前缺失证据、异常回退和禁止动作已明确。
- 未修改固件实时控制代码，未执行或指挥危险硬件动作。
- `workflow/evidence_register.md` 登记本任务证据。

## Blocked Handling

如果缺少原始 EDA、明确的控制接口引脚映射、示波器/探头型号或固件版本，只将对应项标记为未确认，不推断、不放行动态测试。若无法形成最低限度风险清单，则把任务状态改为 `blocked`。

## Codex 结果区

- 执行状态：done，等待 ChatGPT 或用户复盘为 `reviewed`。
- 已完成：
  - 核对原理图截图、用户 BOM 线索、无电 DMM、静态上电记录和 baseline 固件状态。
  - 核验 STDRIVE101 DS13472 Rev 2、ST 官方产品/评估板资料和 Tektronix 浮地测量安全资料。
  - 建立 MCU 接入前清单、PWM/Gate 准备表、示波器接地安全表、照片和波形证据规范。
  - 更新 `CURRENT_STATUS.md`、`docs/file_map.md`、`references/datasheet_index.md` 和 `workflow/evidence_register.md`。
- 关键结论：本任务的准备文档已完成，但动态 PWM/Gate 检查未放行。仍缺 DT/MODE 实物或 EDA 证据、六路 MCU 映射、可回滚 PWM 固件、示波器/探头型号和断电接线照片。
- 证据：`EV-2026-06-07-HW-GATE-PREP-001`。
- 验证：
  - `python3 tools/build_vector_store.py`：成功，生成 7548 chunks。
  - `python3 -m unittest discover -s tests`：成功，14 tests OK。
- 硬件动作：未执行；未指导输出 PWM、上电或接电机。
- 固件动作：未修改 PWM、Gate、FOC、TIM1/TIM8 或 MCSDK 代码。
- Review Required：yes。

## 建议 commit message

```text
docs: prepare power-board PWM and gate review
```
