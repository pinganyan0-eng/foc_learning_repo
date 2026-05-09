param(
    [string]$SkillName = "stm32g474-foc-assistant"
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$source = Join-Path $repoRoot "codex_skills\$SkillName"
$targetRoot = Join-Path $env:USERPROFILE ".codex\skills"
$target = Join-Path $targetRoot $SkillName

if (-not (Test-Path (Join-Path $source "SKILL.md"))) {
    throw "Project skill source not found: $source"
}

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null

if (Test-Path $target) {
    Remove-Item -Recurse -Force $target
}

Copy-Item -Recurse -Force -Path $source -Destination $target
Write-Host "Installed $SkillName to $target"
Write-Host "Restart Codex if the updated skill does not appear immediately."
