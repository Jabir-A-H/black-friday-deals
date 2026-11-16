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
    
    if ledger["metadata"]["version"] != "3.6.6":
        errors.append(f"Ledger version mismatch: expected 3.6.6, got {ledger['metadata']['version']}")
    
    if ledger["metadata"]["last_updated"] != "2026-11-16T19:15:00+06:00":
        errors.append(f"Ledger last_updated mismatch: got {ledger['metadata']['last_updated']}")
        
    if len(ledger["tracked_items"]) != 55:
        errors.append(f"Expected 55 tracked items, got {len(ledger['tracked_items'])}")
        
    for item in ledger["tracked_items"]:
        if item["last_checked"] != "2026-11-16T19:15:00+06:00":
            errors.append(f"Item {item['id']} last_checked mismatch: {item['last_checked']}")
            break

    if ledger["reconciled_history"][0]["timestamp"] != "2026-11-16T19:15:00+06:00":
        errors.append(f"Reconciled history top entry timestamp mismatch: {ledger['reconciled_history'][0]['timestamp']}")

    print("✔ DEALS_LEDGER.json checks passed.")
except Exception as e:
    errors.append(f"Failed to verify DEALS_LEDGER.json: {e}")

# 2. Verify ALL_CHECKED_DEALS.md
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
try:
    with open(all_deals_path, "r", encoding="utf-8") as f:
        all_deals = f.read()

    if "Total%20Audited-147%20Listings" not in all_deals:
        errors.append("ALL_CHECKED_DEALS.md missing Total%20Audited-147%20Listings badge")

    if "Archived%20%2F%20Filtered-92%20Listings" not in all_deals:
        errors.append("ALL_CHECKED_DEALS.md missing Archived%20%2F%20Filtered-92%20Listings badge")

    if "#A92: Dell G15 & G16 Gaming Laptops" not in all_deals:
        errors.append("ALL_CHECKED_DEALS.md missing candidate #A92")

    if "55 active serialized models + 92 archived/disqualified listings = 147 total audited" not in all_deals:
        errors.append("ALL_CHECKED_DEALS.md footer count mismatch")

    print("✔ ALL_CHECKED_DEALS.md checks passed.")
except Exception as e:
    errors.append(f"Failed to verify ALL_CHECKED_DEALS.md: {e}")

# 3. Verify README.md and DEALS_SUMMARY.md
for fname in ["README.md", os.path.join("docs", "laptop-tracker", "DEALS_SUMMARY.md")]:
    fpath = os.path.join(repo_dir, fname)
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "Ledger-v3.6.6" not in content:
            errors.append(f"{fname} missing Ledger-v3.6.6 badge")

        if "Checked%20Listings-147%20Audited%20Deals" not in content:
            errors.append(f"{fname} missing Checked%20Listings-147%20Audited%20Deals badge")

        if "2026-11-16 19:15:00 (+06:00 Asia/Dhaka)" not in content:
            errors.append(f"{fname} missing 19:15:00 timestamp")

        if "Disqualified candidate #A92" not in content:
            errors.append(f"{fname} missing candidate #A92 callout")

        if "from 147 audited listings" not in content:
            errors.append(f"{fname} missing 'from 147 audited listings' text")

        print(f"✔ {fname} checks passed.")
    except Exception as e:
        errors.append(f"Failed to verify {fname}: {e}")

# 4. Invariant: ZERO ebay.com links in active repository markdown and json files
target_files = [
    os.path.join(docs_dir, "DEALS_LEDGER.json"),
    os.path.join(repo_dir, "README.md"),
    os.path.join(docs_dir, "DEALS_SUMMARY.md"),
    os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
]

ebay_pattern = re.compile(r'https?://[^\s\)\"\>]*ebay\.com', re.IGNORECASE)
for tf in target_files:
    with open(tf, "r", encoding="utf-8") as f:
        c = f.read()
    matches = ebay_pattern.findall(c)
    if matches:
        errors.append(f"CRITICAL INVARIANT VIOLATION in {tf}: found eBay URLs: {matches}")

if not errors:
    print("🌟 ALL VERIFICATION GATES PASSED! Zero errors, zero eBay links, 100% consistent.")
    sys.exit(0)
else:
    print("❌ VERIFICATION FAILURES:")
    for err in errors:
        print("  -", err)
    sys.exit(1)
