# 2026-05-12 NUCLEO UART DMA + IDLE callback/flag closeout

- Topic: UART DMA + IDLE callback structure, callback safety boundaries, and `volatile` flag handoff to the main loop.
- Summary: Continued from the UART DMA + IDLE learning branch after the user corrected ChatGPT for reading only `master`. The user correctly restated that `Size = 8` means indices `0..7`, that the callback loop condition should be `i < Size`, and that DMA + IDLE reception must be restarted or the next command may not be received. The user also correctly classified callback skeleton lines: target-UART check, byte loop, `AppFeedRxChar(rx_buf[i])`, and receive restart. The user correctly explained that the callback should not directly change `app_mode`, and that slow debug printing should be moved to the main loop through a flag.
- Evidence level: L2
- Confidence: medium
- Correct answers observed:
  - `Size = 8` -> process `rx_buf[0]` through `rx_buf[7]`.
  - Use `i < Size`, not `i <= Size`.
  - Restart DMA + IDLE reception after each handled batch.
  - `HAL_UARTEx_RxEventCallback` should feed bytes to `AppFeedRxChar(...)`, not directly parse `PING`/`STOP` or modify `app_mode`.
  - Large `printf` debug output belongs in the main loop through a flag, not directly in the callback.
  - `volatile` tells the compiler the flag may change outside ordinary main-loop flow, such as from callback/interrupt context.
  - A one-bit flag only records that an event happened at least once; it cannot count three back-to-back events. Use a counter when exact event count matters.
- Weak point observed: User initially classified the callback `for` loop over `rx_buf[0..Size-1]` as not suitable for the callback, mixing up "callback should stay light" with "callback should not even iterate and dispatch received bytes." User repaired this immediately after correction by explaining that the loop is suitable because it only搬运/分发字节.
- Next review: Ask the user to classify callback actions as suitable or unsuitable: byte loop + `AppFeedRxChar`, receive restart, direct `app_mode` assignment, `HAL_Delay`, large `printf`, flag set, and counter increment. Then decide whether to hand back to Codex for real `main.c` inspection, build, flash, COM5 validation, and learning-file synchronization.
- Not validated: No firmware edit, build, flash, or COM5/VOFA+ serial validation was performed in this ChatGPT turn.
