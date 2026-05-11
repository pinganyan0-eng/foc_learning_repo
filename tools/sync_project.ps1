param(
    [ValidateSet("check", "pull", "push")]
    [string]$Mode = "check",

    [string]$Message = "",

    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$repoRoot = $repoRoot.Path

function Run-Git {
    param([string[]]$GitArgs)
    & git -C $repoRoot @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($GitArgs -join ' ') failed"
    }
}

function Run-Tests {
    if ($SkipTests) {
        Write-Host "Skipping tests."
        return
    }

    Write-Host "Running repository tests..."
    Push-Location $repoRoot
    try {
        python -m unittest discover -s tests
        if ($LASTEXITCODE -ne 0) {
            throw "Tests failed"
        }
    } finally {
        Pop-Location
    }
}

function Install-ProjectSkill {
    $installer = Join-Path $repoRoot "tools\install_project_skill.ps1"
    if (Test-Path $installer) {
        Write-Host "Installing repo-managed project skill..."
        & powershell -ExecutionPolicy Bypass -File $installer
        if ($LASTEXITCODE -ne 0) {
            throw "Project skill install failed"
        }
    }
}

function Run-ProjectMaintenance {
    Write-Host "Normalizing learning loop..."
    Push-Location $repoRoot
    try {
        python tools/normalize_learning_loop.py
        if ($LASTEXITCODE -ne 0) {
            throw "Learning loop normalization failed"
        }

        Write-Host "Rebuilding local retrieval index..."
        python tools/build_vector_store.py
        if ($LASTEXITCODE -ne 0) {
            throw "Vector store rebuild failed"
        }
    } finally {
        Pop-Location
    }
}

Write-Host "Repository: $repoRoot"
Run-Git @("status", "--short", "--branch")

if ($Mode -eq "check") {
    Write-Host ""
    Write-Host "Remote:"
    Run-Git @("remote", "-v")
    Run-Tests
    exit 0
}

if ($Mode -eq "pull") {
    $dirty = git -C $repoRoot status --porcelain
    if ($dirty) {
        Write-Error "Working tree has local changes. Commit or stash them before pulling."
    }

    Run-Git @("pull", "--ff-only")
    Install-ProjectSkill
    Run-Tests
    exit 0
}

if ($Mode -eq "push") {
    if (-not $Message.Trim()) {
        Write-Error "Push mode requires -Message `"your commit message`"."
    }

    Run-ProjectMaintenance
    Run-Tests

    Run-Git @("add", "-A")

    $dirtyAfterAdd = git -C $repoRoot diff --cached --name-only
    if (-not $dirtyAfterAdd) {
        Write-Host "No staged changes to commit."
        Run-Git @("pull", "--ff-only")
        exit 0
    }

    Run-Git @("commit", "-m", $Message)
    Run-Git @("pull", "--rebase", "--autostash")
    Run-Git @("push")
    Run-Git @("status", "--short", "--branch")
}
