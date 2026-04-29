# 第三个链接落地状态

来源链接：`https://chatgpt.com/s/t_69f259fcb988819194d1c21ef795da43`

## 已落地

- 已把仓库从资料堆放型扩展为分层工程结构：`apps/`、`interfaces/`、`docs/`、`experiments/`、`tools/`、`assets/`、`deliverables/`、`references/`。
- 已建立 STM32 与 ESP32 分仓壳：
  - `apps/stm32_g474_foc/`
  - `apps/esp32_c3_gateway/`
- 已为 STM32、ESP32、docs 三个高风险工作区建立专门规则：
  - `apps/stm32_g474_foc/AGENTS.md`
  - `apps/esp32_c3_gateway/AGENTS.md`
  - `docs/AGENTS.md`
- 已把 UART 协议、状态帧、命令帧、错误码抽到 `interfaces/`，作为后续代码、测试、答辩文档的共同契约。
- 已建立联调实验目录模板 `experiments/_template/`，便于后续问题定位时提供统一上下文。
- 已建立答辩交付目录 `deliverables/`，把报告、PPT、演示脚本和提交清单与学习资料分开。
- 已建立 `references/`，用于沉淀官方链接、Datasheet 索引和不可信来源提醒。
- 已把新增结构纳入本地检索构建脚本 `tools/build_vector_store.py`。

## 尚需真实材料

- 真实 STM32CubeMX/MCSDK 工程还没有导入；当前 `apps/stm32_g474_foc/` 是安全占位壳。
- 真实 ESP-IDF 工程还没有导入；当前 `apps/esp32_c3_gateway/` 是安全占位壳。
- `experiments/` 中还没有真实波形、串口日志、供电条件、故障复现记录。
- `deliverables/` 中还没有最终答辩 PPT、演示视频脚本和提交版报告。

## 使用边界

- 这个阶段只配置 Codex 学习助手环境，不安装或改动实际嵌入式开发环境。
- 后续导入真实工程时，先保持 CubeMX/MCSDK 生成目录原貌，再逐步加测试、审查和文档索引。
