# 2026-05-30 Hall 软件状态机 ChatGPT 复习回传

- Summary: 用户把 ChatGPT 教学后的 5 道 Hall 软件状态机题目贴回 Codex。答案正确覆盖 `110 -> 010` 正向相邻、`010 -> 110` 反向相邻、`111` 非法、7 极对电机 `60 / 7 = 8.57 deg` 机械角度换算，以及 `PB3=LIN1` 不能复用为 Hall。
- Evidence level: Hall 状态机跳变分类和 PB3 路线约束达到 L4 no-power 概念证据；电角度/机械角度换算为 L2-L3 公式练习证据。
- Confidence: medium-high。关键修正点已经明确：反向相邻跳转不是异常。
- Weak point update: “反向相邻跳转不是异常；只有 `000/111` 或跨状态跳变才异常”已修正。完整 software Hall adapter 处理顺序仍需下一次复述。
- Safety boundary: 不上电、不接电机、不输出 Gate PWM、不运行 Motor Profiler / Motor Pilot、不声明 Hall 闭环或 MCSDK Hall 接入可用。
- Source: `learning/review_items/2026-05-30_hall_state_machine_chatgpt_followup.md`
