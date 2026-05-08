# MacBook Codex 双机配置流程

目标：在 MacBook 上再配置一份和 Windows 近似一致的 Codex 项目环境。Windows 和 MacBook 都继续使用，不是把项目从 Windows 搬走。

推荐模型：

1. 第一次用 setup bundle 给 MacBook 初始化一份项目和 Codex Skills。
2. 之后两台电脑通过同一个 Git 远端同步项目文件。
3. Codex 登录状态、历史会话、API Key、系统软件安装状态各机器独立维护。

当前双机同步远端：

```text
origin -> https://github.com/pinganyan0-eng/foc_learning_repo
```

这个仓库应保持私有。

## 第一次配置 MacBook

在 Windows 端项目根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\create_mac_codex_setup_bundle.ps1
```

脚本会在项目外层生成：

```text
foc_learning_repo_mac_codex_setup_bundle.zip
```

把这个 zip 传到 MacBook，解压后在解压目录运行：

```bash
bash INSTALL_ON_MAC.sh
```

默认会安装到：

```text
~/Documents/Codex/qiansai/foc_learning_repo
```

如果要换位置：

```bash
bash INSTALL_ON_MAC.sh ~/Documents/Codex/my_workspace
```

安装完成后，在 MacBook 的 Codex 中打开安装后的 `foc_learning_repo` 目录。若 Skill 没有立即出现，重启 Codex。

## 会复制什么

- 当前仓库文件。
- `.git/`，包括 Git 历史和当前未提交改动。
- 项目本地检索资料和 `vector_store/`。
- 可用时复制这些 Codex Skills：
  - `stm32g474-foc-assistant`
  - `jupyter-notebook`
  - `screenshot`

## 不会复制什么

- Codex 登录状态。
- API Key。
- Codex 历史会话。
- Windows 专属软件安装状态，例如 STM32CubeMX、MCSDK、VS Code 插件。

这些内容应在 MacBook 上重新登录或重新安装。

## 后续双机同步

第一次配置完成后，不建议反复用 zip 覆盖另一台电脑。正常使用应该走 Git：

```bash
git status
git add .
git commit -m "update project state"
git push
```

到另一台电脑继续前：

```bash
git pull
```

如果这台仓库还没有远端，先建一个私有 GitHub/GitLab 仓库，然后在 Windows 和 MacBook 两边都使用同一个远端。当前项目已经配置为：

```bash
git remote add origin https://github.com/pinganyan0-eng/foc_learning_repo
git push -u origin master
```

之后另一台电脑可以用：

```bash
git clone https://github.com/pinganyan0-eng/foc_learning_repo
```

如果是通过 setup bundle 初始化的 MacBook，本地已经有 `.git/`，只需要补同一个 `origin` 即可。

## 双机使用规则

- 换电脑前先提交并推送。
- 换电脑后先拉取。
- 同一天两台电脑都改了同一批文档时，先 `git status` 看清楚再合并。
- 修改 `materials/`、`docs/`、`references/` 或 `workflow/` 后，重建 `vector_store/`。
- Codex Skills 不是 Git 自动同步的系统配置；首次 setup bundle 会复制一份，后续如果改了 Skill，需要重新打 setup bundle 或手动同步 `~/.codex/skills/` 中对应目录。

## Mac 端验证

安装脚本会自动尝试运行：

```bash
python3 tools/build_vector_store.py
python3 -m unittest discover -s tests
```

如果 Mac 上还没有 `python3`，先安装 Python 3，再在项目目录手动运行上面两条命令。

## 备注

这个 setup bundle 解决的是“让 MacBook 上的 Codex 也能理解并继续这个项目”。真实 STM32/ESP32 工具链是否能在 Mac 上完整构建，取决于 STM32CubeMX、MCSDK、VS Code 插件和对应调试器支持情况，需要另行验证。
