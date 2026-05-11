# Tools

- `build_vector_store.py`：构建本地检索索引。
- `ask_local.py`：基于本地资料问答。
- `record_learning_session.py`：追加学习记录，并在出现薄弱点时自动分配稳定 `WP-001` 编号。
- `normalize_learning_loop.py`：整理 `learning/weak_points.md` 与 `learning/review_queue.md`，修复临时 `WP-new` 引用。
- `start_learning_session.ps1` / `start_learning_session.sh`：开工入口，更新项目 Skill、整理学习队列、显示当前状态与复习项。
- `end_learning_session.ps1` / `end_learning_session.sh`：收工入口，记录学习摘要、整理学习队列、重建检索索引并跑测试。
- `sync_project.ps1` / `sync_project.sh`：Windows/Mac 双机同步入口；`push` 前会整理学习队列、重建检索索引并跑测试。
- `run_rehearsal.py`：Suggest -> Auto Edit -> 验证 -> 回滚演练。
- `log_parser/`：后续放串口日志解析工具。
- `plot_current_speed/`：后续放电流/速度画图工具。
- `uart_frame_tester/`：后续放 UART 帧测试工具。
