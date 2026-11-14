import json
import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"
LEDGER_PATH = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_LEDGER.json")
ALL_CHECKED_PATH = os.path.join(WORKSPACE, "docs/laptop-tracker/ALL_CHECKED_DEALS.md")
README_PATH = os.path.join(WORKSPACE, "README.md")
SUMMARY_PATH = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_SUMMARY.md")

def verify():
    print("=== VERIFYING TRACKER PASS (v3.2.7) ===")

    # 1. Verify DEALS_LEDGER.json
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert ledger["metadata"]["version"] == "3.2.7", f"Wrong ledger version: {ledger['metadata']['version']}"
    assert ledger["metadata"]["last_updated"] == "2026-11-15T05:15:00+06:00", "Wrong ledger timestamp"
    assert len(ledger["tracked_items"]) == 55, f"Expected 55 tracked items, got {len(ledger['tracked_items'])}"

    for item in ledger["tracked_items"]:
        assert item["last_checked"] == "2026-11-15T05:15:00+06:00", f"Item {item['id']} has wrong timestamp"
        assert item["current_price_bdt_bank"] == round(item["current_price_usd"] * 128)
        assert item["current_price_bdt_landed"] == round(item["current_price_usd"] * 135)
        assert "ebay.com" not in item.get("url", "").lower(), f"eBay link in url of {item['id']}"
        assert "ebay.com" not in item.get("search_url", "").lower(), f"eBay link in search_url of {item['id']}"

    # 2. Verify ALL_CHECKED_DEALS.md
    with open(ALL_CHECKED_PATH, "r", encoding="utf-8") as f:
        all_checked = f.read()

    assert "ebay.com" not in all_checked.lower(), "eBay link found in ALL_CHECKED_DEALS.md"
    assert "Total%20Audited-133%20Listings" in all_checked, "Total audited badge not updated in ALL_CHECKED_DEALS.md"
    assert "Archived%20%2F%20Filtered-78%20Listings" in all_checked, "Archived badge not updated in ALL_CHECKED_DEALS.md"
    assert "(#A1 – #A78)" in all_checked, "(#A1 - #A78) not found in ALL_CHECKED_DEALS.md"
    assert "### #A78: Dell Inspiron 16 Plus" in all_checked, "#A78 header not found in ALL_CHECKED_DEALS.md"

    # 3. Verify README.md & DEALS_SUMMARY.md
    for path in [README_PATH, SUMMARY_PATH]:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        assert "ebay.com" not in content.lower(), f"eBay link found in {path}"
        assert "Ledger-v3.2.7-informational" in content, f"Version badge not updated in {path}"
        assert "Checked%20Listings-133%20Audited%20Deals" in content, f"Checked listings badge not updated in {path}"
        assert "2026-11-15 05:15:00 (+06:00 Asia/Dhaka)" in content, f"Timestamp not updated in {path}"
        assert "Disqualified candidate #A78" in content, f"#A78 not mentioned in defect gate of {path}"
        assert "133 total audited listings" in content, f"133 total audited listings milestone not found in {path}"
        assert "selected from 133 audited listings" in content, f"Top champions count not updated in {path}"

    print("ALL VERIFICATIONS PASSED WITH ZERO VIOLATIONS!")

if __name__ == "__main__":
    verify()
