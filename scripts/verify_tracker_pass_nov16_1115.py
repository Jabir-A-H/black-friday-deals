import json
import re
import os
import sys

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

print("=== RUNNING FULL VERIFICATION GATE FOR PASS NOV 16 11:15 AM ===")

# 1. Verify DEALS_LEDGER.json
ledger_path = os.path.join(docs_dir, "DEALS_LEDGER.json")
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)

assert ledger["metadata"]["version"] == "3.6.2", f"Expected v3.6.2, got {ledger['metadata']['version']}"
assert ledger["metadata"]["last_updated"] == "2026-11-16T11:15:00+06:00", f"Unexpected timestamp {ledger['metadata']['last_updated']}"
assert len(ledger["tracked_items"]) == 55, f"Expected 55 tracked items, got {len(ledger['tracked_items'])}"

for i, item in enumerate(ledger["tracked_items"]):
    assert item["last_checked"] == "2026-11-16T11:15:00+06:00", f"Item {item['id']} has stale timestamp {item['last_checked']}"

print("✓ DEALS_LEDGER.json passed all structural, version, and timestamp checks (55 items verified).")

# 2. Strict eBay Invariant across all files
ebay_regex = re.compile(r"ebay\.com", re.IGNORECASE)
files_to_check = [
    os.path.join(repo_dir, "README.md"),
    os.path.join(docs_dir, "DEALS_SUMMARY.md"),
    os.path.join(docs_dir, "DEALS_LEDGER.json"),
    os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
]

for file_path in files_to_check:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    matches = ebay_regex.findall(content)
    assert len(matches) == 0, f"CRITICAL ERROR: Found {len(matches)} eBay occurrences in {file_path}!"
    print(f"✓ {os.path.basename(file_path)}: ZERO ebay.com occurrences verified.")

# 3. Check ALL_CHECKED_DEALS.md milestones
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
with open(all_deals_path, "r", encoding="utf-8") as f:
    all_deals_text = f.read()

assert "Total%20Audited-143%20Listings" in all_deals_text, "Badge Total Audited 143 not found in ALL_CHECKED_DEALS.md"
assert "Archived%20%2F%20Filtered-88%20Listings" in all_deals_text, "Badge Filtered 88 not found in ALL_CHECKED_DEALS.md"
assert "#A1 – #A88" in all_deals_text, "#A1 – #A88 range not found in ALL_CHECKED_DEALS.md"
assert "### #A88: ASUS ROG Flow X13" in all_deals_text, "Candidate #A88 header not found in ALL_CHECKED_DEALS.md"
print("✓ ALL_CHECKED_DEALS.md: 143 listings milestone verified with candidate #A88.")

# 4. Check README.md and DEALS_SUMMARY.md
for doc_name, file_path in [("README.md", os.path.join(repo_dir, "README.md")), ("DEALS_SUMMARY.md", os.path.join(docs_dir, "DEALS_SUMMARY.md"))]:
    with open(file_path, "r", encoding="utf-8") as f:
        doc_text = f.read()
    assert "Ledger-v3.6.2" in doc_text, f"Ledger-v3.6.2 badge missing from {doc_name}"
    assert "Checked%20Listings-143%20Audited%20Deals" in doc_text, f"143 Audited Deals badge missing from {doc_name}"
    assert "2026-11-16 11:15:00 (+06:00 Asia/Dhaka)" in doc_text, f"Timestamp missing from {doc_name}"
    assert "Disqualified candidate #A88" in doc_text, f"Candidate #A88 callout missing from {doc_name}"
    assert "All 143 Audited Deals" in doc_text, f"All 143 Audited Deals link missing from {doc_name}"
    print(f"✓ {doc_name}: All badges, timestamps, and #A88 callouts verified.")

print("\n🎯 ALL PRE-FLIGHT VERIFICATION GATES PASSED CLEANLY (EXIT CODE 0)!")
