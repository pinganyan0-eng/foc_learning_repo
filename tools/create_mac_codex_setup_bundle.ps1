param(
    [string]$OutputPath
)

$ErrorActionPreference = "Stop"

$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$projectRoot = $projectRoot.Path

if (-not (Test-Path (Join-Path $projectRoot "CURRENT_STATUS.md")) -or
    -not (Test-Path (Join-Path $projectRoot "AGENTS.md"))) {
    throw "Run this script from the foc_learning_repo tools directory, or keep it inside that repository."
}

if (-not $OutputPath) {
    $parent = Split-Path -Parent $projectRoot
    $OutputPath = Join-Path $parent "foc_learning_repo_mac_codex_setup_bundle.zip"
}

$OutputPath = [System.IO.Path]::GetFullPath($OutputPath)
$stageRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("foc_codex_mac_setup_" + [Guid]::NewGuid().ToString("N"))
$repoStage = Join-Path $stageRoot "foc_learning_repo"
$skillsStage = Join-Path $stageRoot "codex\skills"

New-Item -ItemType Directory -Force -Path $repoStage, $skillsStage | Out-Null

Write-Host "Packaging repository copy..."
$robocopyArgs = @(
    $projectRoot,
    $repoStage,
    "/MIR",
    "/NFL",
    "/NDL",
    "/NJH",
    "/NJS",
    "/NP",
    "/XD",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "node_modules",
    "build",
    ".cache",
    "CMakeFiles",
    "/XF",
    "*.pyc",
    "*.pyo",
    "*.o",
    "*.obj",
    "*.elf",
    "*.bin",
    "*.hex",
    "*.map"
)

& robocopy.exe @robocopyArgs | Out-Host
$robocopyExitCode = $LASTEXITCODE
if ($robocopyExitCode -gt 7) {
    throw "robocopy failed with exit code $robocopyExitCode"
}

$skillNames = @(
    "stm32g474-foc-assistant",
    "jupyter-notebook",
    "screenshot"
)

$repoSkillsRoot = Join-Path $projectRoot "codex_skills"
$sourceSkillsRoot = Join-Path $env:USERPROFILE ".codex\skills"
foreach ($skillName in $skillNames) {
    $repoSkill = Join-Path $repoSkillsRoot $skillName
    $installedSkill = Join-Path $sourceSkillsRoot $skillName
    $targetSkill = Join-Path $skillsStage $skillName

    if (Test-Path $repoSkill) {
        Write-Host "Including repo-managed Codex skill: $skillName"
        Copy-Item -Recurse -Force -Path $repoSkill -Destination $targetSkill
    } elseif (Test-Path $installedSkill) {
        Write-Host "Including Codex skill: $skillName"
        Copy-Item -Recurse -Force -Path $installedSkill -Destination $targetSkill
    } else {
        Write-Warning "Codex skill not found and will be skipped: $skillName"
    }
}

$installer = @'
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_SRC="$SCRIPT_DIR/foc_learning_repo"
DEFAULT_DEST="$HOME/Documents/Codex/qiansai"
DEST_ROOT="${1:-$DEFAULT_DEST}"
DEST_REPO="$DEST_ROOT/foc_learning_repo"
SKILLS_SRC="$SCRIPT_DIR/codex/skills"
SKILLS_DEST="$HOME/.codex/skills"

if [[ ! -d "$PROJECT_SRC" ]]; then
  echo "Cannot find foc_learning_repo next to this installer."
  exit 1
fi

mkdir -p "$DEST_ROOT"

if [[ -e "$DEST_REPO" ]]; then
  echo "Destination already exists: $DEST_REPO"
  echo "Move or rename it first, then run this installer again."
  exit 1
fi

echo "Creating the Mac project copy at: $DEST_REPO"
rsync -a \
  --exclude '__pycache__/' \
  --exclude '.pytest_cache/' \
  --exclude '.mypy_cache/' \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude 'node_modules/' \
  "$PROJECT_SRC/" "$DEST_REPO/"

if [[ -d "$SKILLS_SRC" ]]; then
  echo "Installing this project's Codex skills to: $SKILLS_DEST"
  mkdir -p "$SKILLS_DEST"
  for skill in "$SKILLS_SRC"/*; do
    [[ -d "$skill" ]] || continue
    rsync -a "$skill/" "$SKILLS_DEST/$(basename "$skill")/"
  done
fi

if command -v python3 >/dev/null 2>&1; then
  echo "Rebuilding local search index..."
  (cd "$DEST_REPO" && python3 tools/build_vector_store.py)

  echo "Running repository tests..."
  (cd "$DEST_REPO" && python3 -m unittest discover -s tests)
else
  echo "python3 was not found. Install Python 3, then run from the project:"
  echo "  python3 tools/build_vector_store.py"
  echo "  python3 -m unittest discover -s tests"
fi

echo
echo "Done."
echo "Open this folder in Codex on the Mac:"
echo "  $DEST_REPO"
echo "Restart Codex if the installed skills do not appear immediately."
echo
echo "For normal two-computer use, sync project changes through Git after this first setup."
'@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText(
    (Join-Path $stageRoot "INSTALL_ON_MAC.sh"),
    ($installer -replace "`r`n", "`n"),
    $utf8NoBom
)

$readme = @"
# MacBook Codex Setup Bundle

This bundle contains:

- `foc_learning_repo/`: a second copy of the project repository for the MacBook, including Git history and current uncommitted files.
- `codex/skills/`: local Codex skills used by this project when available.
- `INSTALL_ON_MAC.sh`: the Mac installer.

On the Mac:

```bash
cd /path/to/unzipped/bundle
bash INSTALL_ON_MAC.sh
```

The default install location is:

```text
~/Documents/Codex/qiansai/foc_learning_repo
```

To install somewhere else:

```bash
bash INSTALL_ON_MAC.sh ~/Documents/Codex/my_workspace
```

This bundle intentionally does not include Codex account data, API keys, or conversation history.

After this first setup, use the same Git remote from both computers to keep the two project copies synchronized.
"@

[System.IO.File]::WriteAllText(
    (Join-Path $stageRoot "README_SETUP_MAC_CODEX.md"),
    ($readme -replace "`r`n", "`n"),
    $utf8NoBom
)

if (Test-Path $OutputPath) {
    Remove-Item -Force $OutputPath
}

Write-Host "Creating archive: $OutputPath"
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::Open(
    $OutputPath,
    [System.IO.Compression.ZipArchiveMode]::Create
)

try {
    $stageRootPrefix = $stageRoot.TrimEnd("\", "/") + [System.IO.Path]::DirectorySeparatorChar
    Get-ChildItem -LiteralPath $stageRoot -Recurse -Force -File | ForEach-Object {
        $relativePath = $_.FullName.Substring($stageRootPrefix.Length)
        $entryName = $relativePath.Replace("\", "/")
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
            $zip,
            $_.FullName,
            $entryName,
            [System.IO.Compression.CompressionLevel]::Optimal
        ) | Out-Null
    }
} finally {
    $zip.Dispose()
}

Remove-Item -Recurse -Force $stageRoot

Write-Host ""
Write-Host "Mac Codex setup bundle created:"
Write-Host $OutputPath
Write-Host ""
Write-Host "Copy this zip to the Mac, unzip it, then run:"
Write-Host "bash INSTALL_ON_MAC.sh"
