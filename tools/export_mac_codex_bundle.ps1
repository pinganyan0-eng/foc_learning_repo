param(
    [string]$OutputPath
)

$ErrorActionPreference = "Stop"

$script = Join-Path $PSScriptRoot "create_mac_codex_setup_bundle.ps1"

Write-Warning "This script name is kept for compatibility. Use create_mac_codex_setup_bundle.ps1 for the two-computer setup workflow."

if ($OutputPath) {
    & $script -OutputPath $OutputPath
} else {
    & $script
}
