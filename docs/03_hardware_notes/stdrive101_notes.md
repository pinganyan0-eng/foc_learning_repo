# stdrive101_notes

STDRIVE101 设计注意事项。以 Datasheet 和最新审查为准。

当前本地消化入口：

- 官方 PDF digest：`materials/extracted/st_manuals/st_stdrive101_datasheet_digest.md`
- 官方 URL：<https://www.st.com/resource/en/datasheet/stdrive101.pdf>
- 状态：2026-05-13 已通过 ST 官网 PDF reader 核验 DS13472 Rev 2 并整理 digest；raw PDF 二进制下载仍因 ST 链路超时未归档。

P2/P3 前必须检查：

- `nFAULT` 是开漏故障输出，拉低原因包括过流、VDS 保护、热关断和 REG12 UVLO；STM32 侧当前候选为 `PB12/TIM1_BKIN`，但板上拉电压和走线必须用 EDA/netlist 证明。
- `DT/MODE` 决定 ENx/INx 或 INHx/INLx 控制方式；MCSDK/TIM1 输出策略必须和硬件绑法一致。
- VDS monitoring 假设 `VS` 与功率级 `VM` 同压；如果不同压，必须按 datasheet 处理 `SCREF`，否则可能误触发。
- `REG12` 负载和电容、bootstrap 电容、CP/SCREF 网络、STBY 默认状态，都属于上电前 no-power review 项。
