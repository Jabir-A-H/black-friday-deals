param(
    [string]$Message = ""
)

# Auto-sync Black Friday Deals to GitHub
$repoDir = "D:\WebDev\BlackFridayDeals"
Set-Location -Path $repoDir

# Stage updated dashboard, ledger, and docs
git add docs/ README.md scripts/

# Check for staged changes
$diff = git diff --staged --name-only
if ($diff) {
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm")
    if (-not $Message -or $Message.Trim() -eq "") {
        $Message = "chore(tracker): auto-sync live deals [$timestamp]"
    }
    Write-Host "Staged changes in: $diff"
    Write-Host "Commit message: $Message"
    git commit -m "$Message"
    Write-Host "Pushing to GitHub..."
    git push origin main
    Write-Host "Push complete at $timestamp."
} else {
    Write-Host "No changes detected. Repository is up-to-date."
}
