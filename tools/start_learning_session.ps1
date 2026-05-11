param(
    [switch]$SkipPull,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$repoRoot = $repoRoot.Path

function Run-InRepo {
    param([string[]]$Command)
    Push-Location $repoRoot
    try {
        $exe = $Command[0]
        $cmdArgs = @()
        if ($Command.Length -gt 1) {
            $cmdArgs = $Command[1..($Command.Length - 1)]
        }
        & $exe @cmdArgs
        if ($LASTEXITCODE -ne 0) {
            throw "$($Command -join ' ') failed"
        }
    } finally {
        Pop-Location
    }
}

function Try-Pull {
    if ($SkipPull) {
        Write-Host "Skipping pull."
        return
    }

    $dirty = git -C $repoRoot status --porcelain
    if ($dirty) {
        Write-Host "Working tree has local changes; skipping pull to avoid mixing edits."
        return
    }

    git -C $repoRoot pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw "git pull --ff-only failed"
    }
}

Write-Host "FOC learning session start"
Write-Host "Repository: $repoRoot"
Write-Host ""

Try-Pull

$installer = Join-Path $repoRoot "tools\install_project_skill.ps1"
if (Test-Path $installer) {
    Write-Host "Installing repo-managed project skill..."
    & powershell -ExecutionPolicy Bypass -File $installer
    if ($LASTEXITCODE -ne 0) {
        throw "Project skill install failed"
    }
}

Run-InRepo @("python", "tools/normalize_learning_loop.py")

if (-not $SkipTests) {
    Run-InRepo @("python", "-m", "unittest", "discover", "-s", "tests")
}

Write-Host ""
Write-Host "Current status excerpt:"
Get-Content -Encoding UTF8 (Join-Path $repoRoot "CURRENT_STATUS.md") |
    Select-Object -First 75

Write-Host ""
Write-Host "Next review items:"
Get-Content -Encoding UTF8 (Join-Path $repoRoot "learning\review_queue.md") |
    Select-String -Pattern "^\| next learning turn \|" |
    Select-Object -First 5

Write-Host ""
Write-Host "Safety reminder: no 24V, power board, motor, PWM gate checks, or STDRIVE101 protection changes without the phase-gate evidence."
git -C $repoRoot status --short --branch
