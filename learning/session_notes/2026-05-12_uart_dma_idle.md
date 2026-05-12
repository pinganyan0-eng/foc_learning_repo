# 2026-05-12 NUCLEO UART DMA + IDLE learning closeout

- Topic: UART receive path from polling command assembly into DMA + IDLE batching.
- Summary: User confirmed the previous AppPollCommand line-assembly material was already covered, then passed a short check on newline detection, string termination, command dispatch, and overflow handling. The lesson moved into DMA + IDLE: user correctly identified DMA as the byte mover into `rx_buf`, IDLE as the batch-complete signal, and the need to restart DMA + IDLE reception after handling each batch.
- Evidence level: L2
- Confidence: medium
- Weak point observed: User initially answered that `Size = 6` should process 5 bytes, showing a count-versus-final-index mix-up. After correction, user answered that `Size = 3` processes indices `0, 1, 2`, showing immediate repair at concept-check level.
- Next review: Before showing real HAL callback code, ask the user to restate: `Size` is count, the loop condition is `i < Size`, and the final processed index is `Size - 1`.
- Not validated: No firmware edit, build, flash, or VOFA+/serial log validation was performed in this ChatGPT turn.
