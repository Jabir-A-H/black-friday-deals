import json
import re
import os
import sys

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

errors = []

# 1. Verify DEALS_LEDGER.json
ledger_path = os.path.join(docs_dir, "DEALS_LEDGER.json")
try:
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    if ledger["metadata"]["version"] != "3.5.1":
        errors.append(f"Ledger version is {ledger['metadata']['version']}, expected 3.5.1")
    if ledger["metadata"]["last_updated"] != "2026-11-16T01:30:00+06:00":
        errors.append(f"Ledger last_updated is {ledger['metadata']['last_updated']}, expected 2026-11-16T01:30:00+06:00")
    if len(ledger["tracked_items"]) != 55:
        errors.append(f"Tracked items count is {len(ledger['tracked_items'])}, expected 55")
    for item in ledger["tracked_items"]:
        if item.get("last_checked") != "2026-11-16T01:30:00+06:00":
            errors.append(f"Item {item['id']} last_checked is {item.get('last_checked')}")
except Exception as e:
    errors.append(f"Failed parsing DEALS_LEDGER.json: {e}")

# 2. Check for eBay links across all files
files_to_check = [
    ledger_path,
    os.path.join(repo_dir, "README.md"),
    os.path.join(docs_dir, "DEALS_SUMMARY.md"),
    os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
]
ebay_re = re.compile(r"ebay\.com", re.IGNORECASE)
for fpath in files_to_check:
    with open(fpath, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            if ebay_re.search(line):
                errors.append(f"FORBIDDEN eBay URL found in {fpath}:{idx}: {line.strip()[:80]}")

# 3. Check ALL_CHECKED_DEALS.md consistency
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
with open(all_deals_path, "r", encoding="utf-8") as f:
    all_deals_content = f.read()

if "Total%20Audited-139%20Listings" not in all_deals_content:
    errors.append("ALL_CHECKED_DEALS badge missing Total%20Audited-139%20Listings")
if "Archived%20%2F%20Filtered-84%20Listings" not in all_deals_content:
    errors.append("ALL_CHECKED_DEALS badge missing Archived%20%2F%20Filtered-84%20Listings")
if "#A1 – #A84" not in all_deals_content:
    errors.append("ALL_CHECKED_DEALS missing #A1 – #A84 in navigation")
if "### #A84: HP Omen 16" not in all_deals_content:
    errors.append("ALL_CHECKED_DEALS missing ### #A84: HP Omen 16")
if "55 active serialized models + 84 archived/disqualified listings = 139 total audited" not in all_deals_content:
    errors.append("ALL_CHECKED_DEALS footer count mismatch")

# 4. Check README.md and DEALS_SUMMARY.md consistency
for dash_path in [os.path.join(repo_dir, "README.md"), os.path.join(docs_dir, "DEALS_SUMMARY.md")]:
    with open(dash_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "Ledger-v3.5.1" not in content:
        errors.append(f"{dash_path} missing Ledger-v3.5.1 badge")
    if "Checked%20Listings-139%20Audited%20Deals" not in content:
        errors.append(f"{dash_path} missing 139 Audited Deals badge")
    if "2026-11-16 01:30:00 (+06:00 Asia/Dhaka)" not in content:
        errors.append(f"{dash_path} missing updated timestamp")
    if "Disqualified candidate #A84" not in content:
        errors.append(f"{dash_path} missing #A84 in Adversarial Defect Gate")
    if "138" in content:
        # Check if 138 still appears as a total audited count
        if re.search(r"\b138\b", content):
            lines = [l.strip() for l in content.split("\n") if "138" in l]
            errors.append(f"{dash_path} still contains '138': {lines}")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)
else:
    print("ALL VERIFICATION GATES PASSED CLEANLY! (100% compliant, 0 eBay links, 139 total audited deals)")
