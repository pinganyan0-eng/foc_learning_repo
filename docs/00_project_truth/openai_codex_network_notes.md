# OpenAI Codex 联网与安全笔记

更新时间：2026-04-30

## 官方核查结论

- OpenAI Help Center 说明 Codex 是用于写代码、审查和交付代码的 coding agent，可以在本地工具中配合使用，也可以把任务委托到云端。
- OpenAI Platform 的 Codex agent internet access 文档说明：Codex Cloud 任务中，setup scripts 阶段有完整互联网访问；交给 agent 后，默认互联网访问关闭，因为存在 prompt injection、代码或密钥外泄、恶意依赖、许可证风险等安全问题；需要时可以开启并配置域名和 HTTP 方法白名单。

## 对本项目的意义

- 本仓库允许 Codex 在需要外部动态事实时联网核查，但要优先官方来源。
- 涉及外部网页、依赖 README、issue、论坛帖时，要警惕 prompt injection。
- 对硬件危险参数，联网核查只能提供证据，不能直接作为“可以上电”的许可。

## 本地环境现状

- 当前 Codex Desktop 会话中，普通 Web 搜索可用。
- 本机 `codex --help` 可运行，但 `codex exec` 在当前桌面会话里被系统权限拦截，错误为 `Access is denied`。
- 因此真实 Codex CLI Suggest 仍需在能正常运行 `codex exec` 的终端中复跑；本仓库当前使用只读等价稿记录结构讲解。

## 官方来源

- OpenAI Help Center: `https://help.openai.com/en/articles/11369540`
- OpenAI Platform: `https://platform.openai.com/docs/codex/agent-network`
