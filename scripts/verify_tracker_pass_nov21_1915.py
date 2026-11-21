import json
import re
import os
import sys

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

expected_version = "3.10.1"
expected_timestamp = "2026-11-21T19:15:00+06:00"
expected_total_audited = 180
expected_active_models = 56
expected_archived_models = 124

errors = []

# 1. Verify DEALS_LEDGER.json
ledger_path = os.path.join(docs_dir, "DEALS_LEDGER.json")
try:
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    
    if ledger["metadata"]["version"] != expected_version:
        errors.append(f"Ledger version mismatch: expected {expected_version}, got {ledger['metadata']['version']}")
    if ledger["metadata"]["last_updated"] != expected_timestamp:
        errors.append(f"Ledger timestamp mismatch: expected {expected_timestamp}, got {ledger['metadata']['last_updated']}")
    if len(ledger["tracked_items"]) != expected_active_models:
        errors.append(f"Tracked items count mismatch: expected {expected_active_models}, got {len(ledger['tracked_items'])}")
    
    for item in ledger["tracked_items"]:
        if item.get("last_checked") != expected_timestamp:
            errors.append(f"Item {item.get('id')} last_checked mismatch: {item.get('last_checked')}")
        for url_field in ["url", "search_url"]:
            val = item.get(url_field, "")
            if "ebay.com" in val.lower():
                errors.append(f"FORBIDDEN EBAY LINK in item {item.get('id')} {url_field}: {val}")

    print("DEALS_LEDGER.json checks passed.")
except Exception as e:
    errors.append(f"Error checking DEALS_LEDGER.json: {e}")

# 2. Verify ALL_CHECKED_DEALS.md
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
try:
    with open(all_deals_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if f"Total%20Audited-{expected_total_audited}%20Listings" not in content:
        errors.append(f"ALL_CHECKED_DEALS.md missing Total Audited-{expected_total_audited} Listings badge")
    if f"Archived%20%2F%20Filtered-{expected_archived_models}%20Listings" not in content:
        errors.append(f"ALL_CHECKED_DEALS.md missing Archived-{expected_archived_models} Listings badge")
    if "#A124: Lenovo IdeaPad Gaming 3" not in content:
        errors.append("ALL_CHECKED_DEALS.md missing candidate #A124")
    if "ebay.com" in content.lower():
        errors.append("FORBIDDEN EBAY LINK in ALL_CHECKED_DEALS.md")
    
    print("ALL_CHECKED_DEALS.md checks passed.")
except Exception as e:
    errors.append(f"Error checking ALL_CHECKED_DEALS.md: {e}")

# 3. Verify README.md and DEALS_SUMMARY.md
for doc_name in ["README.md", "docs/laptop-tracker/DEALS_SUMMARY.md"]:
    file_path = os.path.join(repo_dir, doc_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            c = f.read()
        
        if f"Ledger-v{expected_version}" not in c:
            errors.append(f"{doc_name} missing Ledger-v{expected_version} badge")
        if f"Checked%20Listings-{expected_total_audited}%20Audited%20Deals" not in c:
            errors.append(f"{doc_name} missing Checked Listings-{expected_total_audited} badge")
        if "#A124" not in c:
            errors.append(f"{doc_name} missing #A124 mention")
        if "ebay.com" in c.lower():
            errors.append(f"FORBIDDEN EBAY LINK in {doc_name}")
        
        print(f"{doc_name} checks passed.")
    except Exception as e:
        errors.append(f"Error checking {doc_name}: {e}")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print(f"ALL AUDIT VERIFICATIONS PASSED CLEANLY (v{expected_version}, {expected_total_audited} audited listings, ZERO eBay URLs)!")
    sys.exit(0)
