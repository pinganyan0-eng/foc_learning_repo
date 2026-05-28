# 软件 Hall 固件入口审查清单 - 2026-05-27

UTF-8 readable compatibility note:
当前仍是入口清单，不是固件实现。PB3 = LIN1，不参与 Hall。PCB2 仍未焊接完成。
DMM 连续性 / 短路表暂缓。暂缓不是通过。时间戳来源、low-frequency debug 和
separate MCSDK firmware-integration review / boundary draft exists but no hook permission
都还只是 no-power 审查边界。不改 TIM1 PWM；不改 JEOC / FOC ISR；不替换 HALL_M1；
不写 MCSDK speed feedback；不可声明 Hall 闭环可运行。
# 杞欢 Hall 鍥轰欢鍏ュ彛瀹℃煡娓呭崟 - 2026-05-27

Decision:
`Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.

鏈枃鏄湭鏉ョ涓€娆″啓 `PA0/PA1/PB4` 杞欢 Hall adapter 鍓嶇殑鍏ュ彛娓呭崟銆傚畠鍙瀹?浠€涔堟椂鍊欏彲浠ュ紑浠ｇ爜銆佷唬鐮佺涓€姝ュ彧鑳藉啓鍒板摢閲屻€佸摢浜涜矾寰勫繀椤诲仠涓嬨€傚畠涓嶆槸鍥轰欢
瀹炵幇锛屼笉鏄?MCSDK 鎺ュ叆锛屼笉鏄瀯寤鸿褰曪紝涔熶笉鏄‖浠堕獙璇併€?
## 褰撳墠杈圭晫

褰撳墠璺嚎淇濇寔涓嶅彉锛?
```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1锛屼笉鍙備笌 Hall
P14/P15 = 3V3/GND
```

PCB2 浠嶆湭鐒婃帴瀹屾垚锛孌MM 杩炵画鎬?/ 鐭矾琛ㄦ殏缂撱€傛殏缂撲笉鏄€氳繃銆?
褰撳墠宸茬粡鏈夛細

- 杞欢 Hall no-power 绠楁硶鍑嗗鏂囨。锛?- 鐘舵€佹満缁冧範鍜岃窡杩?review锛?- 澶勭悊椤哄簭涓枃鍗＄墖锛?- 浼唬鐮佽崏妗堬紱
- host-side Python 鍙傝€冩ā鍨嬶紱
- golden vectors 鍥炴斁娴嬭瘯锛?- MCSDK 鏍囧噯 TIM2 Hall 鍙鎺ュ叆绾跨储鍕樺療銆?
褰撳墠浠嶆病鏈夛細

- PCB2 鐒婃帴瀹屾垚璇佹嵁锛?- DMM 杩炵画鎬?/ 鐭矾琛紱
- `PA0/PA1/PB4` GPIO/EXTI 杈圭晫宸叉湁 no-power 鑽夋锛屼絾涓嶆槸瀹炵幇璁稿彲锛?- 鏃堕棿鎴虫潵婧愬凡鏈?no-power 鑽夋锛屼絾涓嶆槸 timer 閰嶇疆鎴栧疄鐜拌鍙紱
- low-frequency debug-output route 宸叉湁 no-power 鑽夋锛屼絾涓嶆槸 UART 鎴栧浐浠跺疄鐜拌鍙紱
- MCSDK 閫熷害 / 浣嶇疆鍙嶉瀹夊叏鎺ュ叆鍐崇瓥锛?- separate MCSDK firmware-integration review / boundary draft exists but no hook permission锛?- no-power STM32 build-only 璁板綍锛?- 浠讳綍 Hall 闂幆銆丟ate PWM銆佺數鏈烘垨鍔熺巼绾ч獙璇併€?
## 鍔熻兘鍙?
鏈潵杞欢 Hall adapter 绗竴鐗堝彧鑳藉仛杩欎欢浜嬶細

```text
GPIO/EXTI 閲?PA0/PA1/PB4
-> 璁板綍鍘熷涓変綅 Hall 鍜屾椂闂存埑
-> 浣庝紭鍏堢骇鐘舵€佹満杩囨护 000/111銆侀噸澶嶃€佹姈鍔ㄥ€欓€夊拰寮傚父璺冲彉
-> 杈撳嚭浣庨 debug snapshot
```

瀹冧笉鑳界洿鎺ヨ瘉鏄?Hall 闂幆锛屼篃涓嶈兘鐩存帴鎺ョ MCSDK 閫熷害鐜€?
## 鍏ュ彛娓呭崟

| 缂栧彿 | 寮€浠ｇ爜鍓嶅繀椤绘槑纭殑浜嬮」 | 褰撳墠鐘舵€?| 涓嶆弧瓒虫椂鐨勫鐞?|
| --- | --- | --- | --- |
| `FIRM-ENTRY-01` | PCB2 宸茬剨鎺ュ苟鍙仛鏂數妫€鏌?| 鏈弧瓒?| 涓嶅啓鏉跨骇 GPIO/EXTI 鍥轰欢 |
| `FIRM-ENTRY-02` | DMM 琛ㄨ瘉鏄?`IA->PA0`銆乣IB->PA1`銆乣IC->PB4` 鍜岀煭璺鏌ラ€氳繃 | 鏈弧瓒?| 鍙繚鐣?no-power 鏂囨。鍜?host 妯″瀷 |
| `FIRM-ENTRY-03` | `PB3=LIN1` 浣滀负鍥哄畾绾︽潫锛屼笉鍐嶈繘鍏?Hall 浠ｇ爜 | 宸叉槑纭?| 浠绘剰浣跨敤 `PB3` 鍋?Hall 閮藉繀椤诲仠涓?|
| `FIRM-ENTRY-04` | GPIO 杈撳叆妯″紡銆佷笂鎷?涓嬫媺绛栫暐銆丒XTI 瑙﹀彂绛栫暐鍙鏌?| 鑽夋宸叉柊澧烇紝浠嶆湭婊¤冻瀹炵幇鏉′欢 | 涓嶅啓鍒濆鍖栦唬鐮?|
| `FIRM-ENTRY-05` | 鏃堕棿鎴虫潵婧愩€乼ick 鍒嗚鲸鐜囧拰婧㈠嚭澶勭悊鍙鏌?| 鑽夋宸叉柊澧烇紝浠嶆湭婊¤冻瀹炵幇鏉′欢 | 涓嶅啓閫熷害鍊欓€夎绠?|
| `FIRM-ENTRY-06` | ISR 鍙仛 `raw_state + timestamp + pending/event count` | 宸插舰鎴愯鍒?| ISR 鍐呭鏉傚鐞嗗繀椤婚€€鍥炶璁″鏌?|
| `FIRM-ENTRY-07` | 鐘舵€佹満琛屼负蹇呴』鑳藉榻?host 妯″瀷鍜?golden vectors | 宸叉湁 host 璇佹嵁 | 鍥轰欢琛屼负涓嶄竴鑷存椂鍏堟敼璁捐鎴栨祴璇曪紝涓嶇鍔熺巼绾?|
| `FIRM-ENTRY-08` | 浣庨 debug 瀛楁鍜岃緭鍑鸿矾寰勬槑纭?| 鑽夋宸叉柊澧烇紝浠嶆湭婊¤冻瀹炵幇鏉′欢 | 涓嶅湪 ISR 閲屾墦鍗版垨鏍煎紡鍖栬緭鍑?|
| `FIRM-ENTRY-09` | MCSDK 鎺ュ叆鐐圭粡杩囧崟鐙?firmware-integration review | 鑽夋宸叉柊澧烇紝浠嶆湭婊¤冻瀹炵幇鏉′欢 | 涓嶅啓鍏?`HALL_M1`銆侀€熷害鐜垨 FOC ISR |
| `FIRM-ENTRY-10` | no-power build-only 宸ュ叿閾惧彲鐢ㄥ苟璁板綍缁撴灉 | 鏈弧瓒?| 涓嶈兘鎶婁唬鐮佽崏妗堝崌绾т负鍙瀯寤鸿瘉鎹?|

## 绗竴鐗堜唬鐮佸彧鍏佽鐨勫舰鐘?
濡傛灉鏈潵鎵€鏈夊叆鍙ｆ潯浠舵弧瓒筹紝绗竴鐗堜篃鍙兘鏄嫭绔?adapter 杈圭晫锛?
```text
software_hall_adapter.h/.c
-> 涓嶆敼 TIM1 PWM
-> 涓嶆敼 JEOC / FOC ISR
-> 涓嶆浛鎹?HALL_M1
-> 涓嶅啓 MCSDK speed feedback
-> 涓嶈緭鍑?Gate PWM
-> 涓嶅埛瀹炴澘
```

绗竴鐗堝嚱鏁拌亴璐ｅ彧鍏佽瑕嗙洊锛?
- `Hall_ReadRaw3()`锛氳鍙?`PA0/PA1/PB4` 骞舵嫾鎴愪笁浣嶇姸鎬侊紱
- `Hall_CaptureEdge_ISR()`锛氫繚瀛樺師濮嬬姸鎬併€佹椂闂存埑鍜屼簨浠舵爣蹇楋紱
- `Hall_ProcessEvent()`锛氬湪浣庝紭鍏堢骇涓婁笅鏂囨墽琛岀姸鎬佹満鍒ゆ柇锛?- `Hall_GetDebugSnapshot()`锛氫綆棰戣鍙栬皟璇曢噺锛?- `Hall_ResetDebugCounters()`锛氫粎鐢ㄤ簬 no-power 璋冭瘯璁℃暟澶嶄綅銆?
## ISR 纭竟鐣?
ISR 鍐呭厑璁革細

- 璇诲彇鎴栫紦瀛樹笁浣?Hall 鍘熷鐘舵€侊紱
- 璇诲彇鏃堕棿鎴筹紱
- 鍐欎竴涓皬浜嬩欢妲姐€乸ending flag 鎴栬交閲忚鏁帮紱
- 蹇呰鏃舵竻 EXTI pending銆?
ISR 鍐呯姝細

- `printf`锛?- JSON 瑙ｆ瀽鎴栨牸寮忓寲锛?- `HAL_Delay`锛?- 闃诲绛夊緟锛?- 鍔ㄦ€佸垎閰嶏紱
- WebSocket / ESP32 閫氫俊锛?- 澶嶆潅 MCSDK 璋冪敤锛?- 淇敼 TIM1 PWM 鏇存柊璺緞锛?- 淇敼 JEOC / FOC ISR锛?- 鍋氭渶缁堥€熷害闂幆鎴栫數娴佺幆鎺у埗鍐崇瓥銆?
## 鐘舵€佹満楠屾敹瑙勫垯

鍥轰欢瀹炵幇浠ュ悗锛屽繀椤诲厛鍦?no-power 鏉′欢涓嬪榻愯繖浜?host 渚х粨鏋滐細

| 杈撳叆 | 鏈熸湜 |
| --- | --- |
| `000` / `111` | 闈炴硶鐘舵€侊紝涓嶆洿鏂版湁鏁堣搴︼紝涓嶈鍚堟硶杈规部 |
| 绗竴娆″悎娉曠姸鎬?| 鍙缓绔嬭捣鐐癸紝涓嶈杈规部 |
| `100 -> 100` | 閲嶅鐘舵€侊紝涓嶈鍚堟硶杈规部 |
| `100 -> 110` | 姝ｅ悜鍊欓€夌浉閭讳竴姝ワ紝璁″悎娉曡竟娌?|
| `100 -> 101` | 鍙嶅悜鍊欓€夌浉閭讳竴姝ワ紝璁″悎娉曡竟娌?|
| `100 -> 011` | 鍚堟硶浣嗛潪鐩搁偦锛岃寮傚父璺冲彉锛屼笉璁″悎娉曡竟娌?|
| 鏃堕棿闂撮殧杩囩煭 | 鍙 bounce candidate锛屼笉澹版槑楂橀€熸棆杞?|

鐪熷疄姝ｅ弽鏂瑰悜鍚嶇О蹇呴』绛夌數鏈哄拰鐩稿簭瀹炴祴鍚庢牎鍑嗐€傚綋鍓嶅彧鑳藉彨
`direction_candidate`銆?
## MCSDK 纭仠姝?
閬囧埌浠ヤ笅浠绘剰闇€姹傦紝蹇呴』鏂板紑 firmware-integration review锛屼笉鍏佽鍦ㄦ湰娓呭崟鍐?缁х画锛?
- 闇€瑕佷慨鏀?`hall_speed_pos_fdbk.c/.h`锛?- 闇€瑕佹浛鎹㈡垨澶嶇敤 `HALL_M1`锛?- 闇€瑕佷慨鏀?`SpeednTorqCtrlM1` 鎴栭€熷害 PID 杈撳叆锛?- 闇€瑕佹妸杞欢 Hall 閫熷害鍊欓€夌洿鎺ュ啓鍏?MCSDK 闂幆锛?- 闇€瑕佷慨鏀?TIM1 PWM銆丣EOC銆丄DC injected 鎴?FOC 楂橀璺緞锛?- 闇€瑕佷互 build-only 鎴愬姛鏇夸唬 Hall銆丟ate PWM銆佺數鏈烘垨鍔熺巼绾у畨鍏ㄨ瘉鎹€?
## 褰撳墠鍙仛涓庝笉鍙仛

褰撳墠绠楁硶渚у彲鍋氾細

- 缁х画闃呰涓枃澶勭悊椤哄簭鍗★紱
- 澶嶈堪涓€鍙ヨ瘽澶勭悊椤哄簭锛?- 瀹℃煡 host model / golden vectors锛?- 缁存姢 no-power 鏂囨。鍜屾祴璇曞悎鍚屻€?
褰撳墠绠楁硶渚т笉鍙仛锛?
- 鍐?STM32 鍥轰欢 adapter锛?- 鏀?CubeMX / Workbench / MCSDK 鐢熸垚浠ｇ爜锛?- 杩愯 Motor Profiler / Motor Pilot锛?- 鍒峰啓瀹炴澘锛?- 鎺?24V銆佸姛鐜囨澘鎴栫數鏈猴紱
- 杈撳嚭 Gate PWM锛?- 澹版槑 Hall 闂幆鍙繍琛屻€?
## 涓嬩竴鐢ㄦ埛妫€鏌ョ偣

浣犵幇鍦ㄤ笉闇€瑕佸仛纭欢鍔ㄤ綔銆侾CB2 娌＄剨瀹屽墠锛屼篃涓嶉渶瑕佸～ DMM 琛ㄣ€?
涓嬩竴姝ュ彧闇€瑕佽兘鎸夎嚜宸辩殑璇濊鍑鸿繖鍙ワ細

```text
鍏堣 PA0/PA1/PB4锛屽厛鎷?000/111锛岀涓€娆″悎娉曞€煎彧褰撹捣鐐癸紝閲嶅鍊间笉绠楄竟娌匡紝
澶揩鍏堟€€鐤戞姈鍔紝鐒跺悗鍒ゆ柇姝?鍙嶅悜鐩搁偦涓€姝ワ紝涓嶇浉閭荤殑鍚堟硶璺冲彉璁板紓甯搞€?```

濡傛灉杩欏彞璇濊兘璇存竻妤氾紝鍚庣画纭欢鐒婂ソ骞惰繑鍥?DMM 琛ㄥ悗锛屾墠杩涘叆
`GPIO/EXTI`銆乼imestamp-source銆乨ebug-output route 鍜?MCSDK 鎺ュ叆杈圭晫澶嶅锛?浠嶇劧涓嶆槸鐩存帴涓婄數鎴栭棴鐜€?
## 绂佹缁撹

鏈枃涓嶈兘鐢ㄤ簬澹版槑锛?
- No software Hall adapter implementation is claimed.
- 涓嶅彲澹版槑 software Hall adapter 宸插疄鐜帮紱
- 涓嶅彲澹版槑 MCSDK Hall 宸叉帴鍏ワ紱
- 涓嶅彲澹版槑 Hall 闂幆鍙繍琛岋紱
- 涓嶅彲澹版槑 no-power build 宸查€氳繃锛?- 涓嶅彲澹版槑 DMM 宸查€氳繃锛?- 涓嶅彲澹版槑 Gate PWM 瀹夊叏锛?- 涓嶅彲澹版槑鐢垫満鍙帴锛?- 涓嶅彲澹版槑鍔熺巼绾у彲涓婄數锛?- 涓嶅彲澹版槑 Motor Profiler / Motor Pilot 鍙繍琛岋紱
- 涓嶅彲澹版槑 sensorless / SMO 宸查獙璇併€?
