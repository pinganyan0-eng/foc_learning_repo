# 2026-05-11 UART line buffer closeout

- Topic: NUCLEO UART polling command line assembly.
- Summary: User correctly explained that AppHandleCommand does not run until a newline arrives, that rx_line[rx_len] = '\0' terminates the C string, that PING is the final command string after receiving P I N G newline, that CRLF only dispatches once because rx_len is reset after '\r', that HAL_UART_Receive(..., 0U) returns immediately when no byte is available, and that APP_CMD_LINE_MAX reserves one slot for the terminating null byte.
- Evidence level: L2
- Confidence: medium
- Weak point observed: Initial answer for partial input P I described only P; corrected to rx_line[0]='P', rx_line[1]='I', rx_len=2, not yet a completed C string. This is recorded as WP-029 in learning/weak_points.md.
- Next review: Given partial input A B without newline, identify rx_line contents, rx_len, whether it is a valid C string, then repeat after newline adds the null terminator.
- Source: ChatGPT teaching closeout on 2026-05-11.

Note: This append-only note mirrors the session closeout requested by the user. If desired, merge this entry into learning/session_notes.md in a follow-up cleanup PR.
