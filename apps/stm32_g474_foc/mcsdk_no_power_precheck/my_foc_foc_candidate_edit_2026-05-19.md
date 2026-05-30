# 2026-05-19 MY_FOC Manual FOC Edit And Rollback

## Decision

`Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`.

Stable phrase: no generated-project trust.

## What Happened

Codex backed up the Workbench source project:

`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`

Backup:

`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`

Codex then tried a minimal source-file edit:

```json
"algorithm": "sixStep"
```

to:

```json
"algorithm": "FOC"
```

The user opened Workbench and reported a Chinese GUI error:

`一般错误 / 无法加载文件: C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`

This proves the one-field manual edit is not a valid Workbench FOC conversion
path.

## Rollback

Codex restored the external Workbench source file from the backup.

Current external file after rollback:

- Path: `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`
- Current top-level setting: `"algorithm": "sixStep"`
- SHA256: `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`

The backup has the same SHA256:

`062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`

## Archived Evidence

Archived repo copies:

- Original / restored source:
  `packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.original_2026-05-19.stwb6`
- Failed manual FOC candidate:
  `packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.codex_foc_candidate_2026-05-19.stwb6`

| File | SHA256 |
| --- | --- |
| Original / backup / restored external source | `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD` |
| Failed manual FOC candidate | `81C34DA89DF40980A64964ECB55C05707FDECDC6720274DA97E6F292B4A26F63` |

## Engineering Result

- Do not hand-edit only the top-level `.stwb6` `algorithm` field to convert
  six-step to FOC.
- The current external `MY_FOC.stwb6` is restored to the original six-step
  project so Workbench can try to open it again.
- The failed FOC candidate is useful only as negative evidence.
- A valid FOC path must be created through Workbench GUI or a full reviewable
  FOC `.stwb6` source, not by this one-field edit.
- The generated `MY_FOC.ioc`, `MY_FOC.wbdef`, `Src/`, and `Inc/` outputs are
  still old generated six-step outputs.
- The original `MY_FOC` source still has the demo motor clue `R57BLB50L2`.
- The original details section still has `Number.NaN` fields for motor and
  startup parameters.
- Packet A still not accepted.

## 直接给你的操作

我已经把坏掉的 `MY_FOC.stwb6` 恢复回备份了。你现在重新打开 `MY_FOC`，应该回到原来的六步工程。

下一步不要再让我手改这个字段。要改成 FOC，必须在 Workbench 里面用正常创建/转换流程做，或者新建一个 FOC 工程。

如果你重新打开还是报错，把新的报错图发我；如果能打开，就先停在工程首页，不要点 Generate。

## Safety Boundary

- No Generate.
- No build.
- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
