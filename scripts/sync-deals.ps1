# Auto-sync Black Friday Deals to GitHub
$repoDir = "D:\WebDev\BlackFridayDeals"
Set-Location -Path $repoDir

# Stage updated files
git add docs/ README.md

# Check if there are staged changes
$diff = git diff --staged --name-only
if ($diff) {
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    Write-Host "Staged changes detected in: $diff"
    Write-Host "Committing changes..."
    git commit -m "chore(tracker): auto-sync live deals [$timestamp]"
    Write-Host "Pushing to GitHub..."
    git push origin main
    Write-Host "Push complete at $timestamp."
} else {
    Write-Host "No changes detected. Repository is up-to-date."
}
