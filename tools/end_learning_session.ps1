param(
    [string]$Topic = "",
    [string]$Summary = "",
    [string]$Weak = "",
    [string]$Next = "",
    [string]$Evidence = "L1",
    [string]$Confidence = "medium",
    [string]$Due = "next learning turn",
    [switch]$SkipVectorStore,
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

Write-Host "FOC learning session end"
Write-Host "Repository: $repoRoot"

if ($Topic.Trim() -and $Summary.Trim()) {
    $args = @("tools/record_learning_session.py", "--topic", $Topic, "--summary", $Summary, "--evidence", $Evidence, "--confidence", $Confidence)
    if ($Weak.Trim()) {
        $args += @("--weak", $Weak)
    }
    if ($Next.Trim()) {
        $args += @("--next", $Next, "--due", $Due)
    }
    Run-InRepo (@("python") + $args)
} else {
    Write-Host "No learning note recorded. To record one, pass -Topic and -Summary."
}

Run-InRepo @("python", "tools/normalize_learning_loop.py")

if (-not $SkipVectorStore) {
    Run-InRepo @("python", "tools/build_vector_store.py")
}

if (-not $SkipTests) {
    Run-InRepo @("python", "-m", "unittest", "discover", "-s", "tests")
}

Write-Host ""
Write-Host "Open review items:"
Get-Content -Encoding UTF8 (Join-Path $repoRoot "learning\review_queue.md") |
    Select-String -Pattern "\| open \|" |
    Select-Object -First 8

Write-Host ""
git -C $repoRoot status --short --branch
