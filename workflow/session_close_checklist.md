# 收工检查清单

每次学习、工程修改、实验记录或自动化巡检结束前，用本清单确认交接证据完整。它不替代 `workflow/phase_gate_checklist.md`；任何硬件、功率、电机、PWM、Gate、nFAULT、电流采样、Hall/SMO 相关动作仍必须先过阶段闸门。

## 学习收工

- [ ] 是否更新 `CURRENT_STATUS.md`。
- [ ] 是否更新 `learning/weak_points.md` 或 `learning/review_queue.md`。
- [ ] 是否把临时想法回写到 `docs/`、`experiments/` 或 `interfaces/`。
- [ ] 是否运行 `python tools/normalize_learning_loop.py`。

## 工程收工

- [ ] 是否更新 `CURRENT_STATUS.md`。
- [ ] 是否把影响接口、状态机、命令协议或工程约束的内容回写到 `docs/` 或 `interfaces/`。
- [ ] 是否运行 `python tools/build_vector_store.py`。
- [ ] 是否运行 `python -m unittest discover -s tests`。
- [ ] 是否确认没有越过 `workflow/phase_gate_checklist.md`。

## 实验收工

- [ ] 是否更新 `experiments/` 中的实验记录。
- [ ] 是否记录日期、目的、环境、步骤、结果、异常和下一步。
- [ ] 是否保存关键串口日志、截图、波形或仪器读数。
- [ ] 是否把实测事实与假设区分开。

## 硬件相关收工

- [ ] 是否确认没有越过 `workflow/phase_gate_checklist.md`。
- [ ] 是否明确记录未接 24V、未接功率板或未接电机，或记录已通过的闸门证据。
- [ ] 是否记录 nFAULT、Gate、VS/REG12/VREG、电流采样、Hall/SMO 相关证据路径。
- [ ] 是否保留限流、回退和不上电验证方案。

## 提交前检查

- [ ] 是否运行 `python tools/normalize_learning_loop.py`。
- [ ] 是否运行 `python tools/build_vector_store.py`。
- [ ] 是否运行 `python -m unittest discover -s tests`。
- [ ] 是否查看 `git status`。
- [ ] 是否确认没有误提交 build、临时日志、敏感信息。
- [ ] 是否确认没有越过 `workflow/phase_gate_checklist.md`。
- [ ] 是否确认没有自动 commit 或 push。
