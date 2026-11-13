param(
    [string]$Message = ""
)

# Auto-sync Black Friday Deals to GitHub
$repoDir = "D:\WebDev\BlackFridayDeals"
Set-Location -Path $repoDir

# Stage updated dashboard, ledger, and docs
git add docs/ README.md scripts/ .gitignore

# Check for staged changes
$diff = git diff --staged --name-only
if ($diff) {
    # Strict validation gate: ZERO eBay links of any kind permitted in active repository
    $ebayRegex = 'https?://[^\s\)\"\>]*ebay\.com'
    $ebayFileHits = Select-String -Path "docs/laptop-tracker/DEALS_LEDGER.json", "README.md", "docs/laptop-tracker/DEALS_SUMMARY.md", "docs/laptop-tracker/ALL_CHECKED_DEALS.md" -Pattern $ebayRegex
    $ebayAddedHits = git diff --staged | Select-String -Pattern "^\+[^+].*$ebayRegex"
    if ($ebayFileHits -or $ebayAddedHits) {
        Write-Error "CRITICAL INVARIANT VIOLATION: Staged changes or active files contain forbidden eBay links ('ebay.com'). Commit aborted. Only 1st-party manufacturer outlets and authorized tier-1 major direct retailers are permitted."
        exit 1
    }
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm")
    if (-not $Message -or $Message.Trim() -eq "") {
        $Message = "feat(tracker): auto-sync live deals, dashboard, and checked inventory"
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
