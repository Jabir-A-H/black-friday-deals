import json
import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"

def verify_all():
    print("=== STARTING FULL TRACKER VERIFICATION GATE (v2.90.0) ===")

    # 1. Verify DEALS_LEDGER.json
    ledger_path = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_LEDGER.json")
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert ledger["metadata"]["version"] == "2.90.0", f"Unexpected version: {ledger['metadata']['version']}"
    assert ledger["metadata"]["last_updated"] == "2026-11-13T17:15:00+06:00"
    assert len(ledger["tracked_items"]) == 55, f"Expected 55 items, got {len(ledger['tracked_items'])}"
    assert ledger["reconciled_history"][0]["timestamp"] == "2026-11-13T17:15:00+06:00"
    for item in ledger["tracked_items"]:
        assert item["last_checked"] == "2026-11-13T17:15:00+06:00", f"Item {item['id']} has wrong last_checked"
        assert item["current_price_bdt_bank"] == round(item["current_price_usd"] * 128)
        assert item["current_price_bdt_landed"] == round(item["current_price_usd"] * 135)
        # Ensure zero ebay URLs
        assert "ebay.com" not in item.get("url", "").lower(), f"Forbidden ebay URL in item {item['id']}"
        assert "ebay.com" not in item.get("search_url", "").lower(), f"Forbidden ebay search_url in item {item['id']}"
    print("DEALS_LEDGER.json: PASSED (55 items, valid JSON, correct calculations, updated history, zero ebay links)")

    # 2. Verify ALL_CHECKED_DEALS.md
    acd_path = os.path.join(WORKSPACE, "docs/laptop-tracker/ALL_CHECKED_DEALS.md")
    with open(acd_path, "r", encoding="utf-8") as f:
        acd_content = f.read()

    assert acd_content.count("\ufffd") == 0, "Found replacement character in ALL_CHECKED_DEALS.md"
    assert "Total%20Audited-115%20Listings-blue" in acd_content, "Missing Total%20Audited-115%20Listings-blue"
    assert "Active%20Tracked-55%20Models-success" in acd_content, "Missing Active%20Tracked-55%20Models-success"
    assert "Archived%20%2F%20Filtered-60%20Listings-lightgrey" in acd_content, "Missing Archived%20%2F%20Filtered-60%20Listings-lightgrey"
    assert "(#A1 – #A60)" in acd_content, "Missing (#A1 – #A60) in navigation index"
    assert "### #A60: Lenovo ThinkPad E-Series" in acd_content, "Missing ### #A60 entry"
    assert "ebay.com" not in acd_content.lower(), "Found forbidden ebay.com in ALL_CHECKED_DEALS.md"
    
    active_items = re.findall(r'### (#\d+): \[(.*?)\]', acd_content)
    archived_items = re.findall(r'### (#A\d+): (.*)', acd_content)
    assert len(active_items) == 55, f"Expected 55 active items, got {len(active_items)}"
    assert len(archived_items) == 60, f"Expected 60 archived items, got {len(archived_items)}"
    print(f"ALL_CHECKED_DEALS.md: PASSED ({len(active_items)} active + {len(archived_items)} archived = 115 audited, zero ebay links)")

    # 3. Verify README.md and DEALS_SUMMARY.md
    for filename in ["README.md", "docs/laptop-tracker/DEALS_SUMMARY.md"]:
        filepath = os.path.join(WORKSPACE, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        assert content.count("\ufffd") == 0, f"Found replacement character in {filename}"
        assert "badge/Ledger-v2.90.0-informational" in content, f"Missing v2.90.0 badge in {filename}"
        assert "Checked%20Listings-115%20Audited%20Deals-success" in content, f"Missing 115 audited badge in {filename}"
        assert "2026-11-13 17:15:00 (+06:00 Asia/Dhaka)" in content, f"Missing 17:15:00 timestamp in {filename}"
        assert "candidate #A60" in content, f"Missing candidate #A60 callout in {filename}"
        assert "ebay.com" not in content.lower(), f"Found forbidden ebay.com in {filename}"
        print(f"{filename}: PASSED (v2.90.0, 115 audited badge, fresh timestamp, candidate #A60 callout, zero ebay links)")

    print("\n>>> ALL 4 CORE FILES FULLY VERIFIED & COMPLIANT WITH INVARIANTS! <<<")

if __name__ == "__main__":
    verify_all()
