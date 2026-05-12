# 2026-05-12 UART DMA buffer boundary

## Topic

NUCLEO UART DMA + IDLE receive boundary: why counters such as `count` and DMA `Size` cannot replace command buffers.

## Summary

ChatGPT continued the P1 NUCLEO UART lesson under the dual-teacher workflow. The lesson focused on the boundary between counters and buffers:

- `count` / `Size` only describe how many bytes were received.
- `rx_buf[]` stores the actual bytes in the current DMA batch.
- `rx_line[]` stores a command line across batches until a newline is received.
- `AppFeedRxByte(ch)` feeds one byte at a time into the line assembler.
- `AppHandleCommand(rx_line)` should only run after a complete newline-terminated command is formed.

A visual flowchart was generated in the ChatGPT session for the learning explanation, but the image file itself is not yet stored in the repository. If this artifact should become a durable project artifact, Codex should regenerate or save it under an appropriate repository path.

## Learner evidence

The user correctly answered:

1. A raw `count = 5` cannot identify `STOP`; it only gives byte length, not byte contents.
2. `rx_buf = ['P', 'I']`, `Size = 2` is not enough to execute `PING`, because the command is incomplete.
3. Two DMA batches, `['S', 'T', 'O']` followed by `['P', '\n']`, should assemble and execute `STOP` after the newline is processed.

## Evidence level

- L2 for concept understanding in guided examples.
- Not L4/L5: no real callback code reading, build, flash, or COM-port validation was performed in this ChatGPT turn.

## Weak points observed

No new weak point should be added from this turn. Existing WP-029 remains open because the user has repaired the `Size` count-vs-content idea in guided examples, but still needs transfer to the real HAL callback implementation.

## Next review

Do not repeat simple single-batch yes/no questions. Next review should ask the user to draw or verbally reconstruct the full DMA + IDLE path:

`UART bytes -> DMA rx_buf[] -> IDLE callback -> Size -> for i < Size -> AppFeedRxByte(rx_buf[i]) -> rx_line[] -> newline -> AppHandleCommand() -> restart DMA + IDLE`.

Then Codex can open the real callback code and map each code block to this flow.

## Not validated

No source code was changed, no build was run, no firmware was flashed, and no serial log was captured in this turn.
