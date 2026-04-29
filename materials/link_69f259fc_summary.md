# 链接 t_69f259fc 固化摘要

来源：`https://chatgpt.com/s/t_69f259fcb988819194d1c21ef795da43`

## 核心要求

把仓库从“资料堆放型”升级为“工程可构建 + 学习可追踪 + 答辩可复用”的竞赛工程仓库。

## 落地原则

- 代码、文档、实验数据、答辩材料、AI 指令分层。
- STM32 与 ESP32 分仓管理，分别放在 `apps/stm32_g474_foc/` 与 `apps/esp32_c3_gateway/`。
- V9 事实源和实测数据单独沉淀。
- MCSDK/CubeMX 生成代码不要为了好看乱拆。
- ESP32 源文件多时拆 `components/`，不要全部塞进 `main/`。
- 接口契约单独放入 `interfaces/`。
- `deliverables/` 单独放比赛提交物，不混入 `docs/`。

## 已落实

- 新增 `apps/`、`interfaces/`、分层 `docs/`、`experiments/`、`assets/`、`deliverables/`、`references/`。
- 新增 STM32/ESP32 分层 `AGENTS.md`。
- 新增 `.vscode/` 推荐配置。
- 更新本地检索索引入口。
