import json
import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"

def verify_all():
    print("=== STARTING FULL TRACKER VERIFICATION GATE (v3.2.1) ===")

    # 1. Verify DEALS_LEDGER.json
    ledger_path = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_LEDGER.json")
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert ledger["metadata"]["version"] == "3.2.1", f"Unexpected version: {ledger['metadata']['version']}"
    assert ledger["metadata"]["last_updated"] == "2026-11-14T17:15:00+06:00"
    assert len(ledger["tracked_items"]) == 55, f"Expected 55 items, got {len(ledger['tracked_items'])}"
    assert ledger["reconciled_history"][0]["timestamp"] == "2026-11-14T17:15:00+06:00"
    for item in ledger["tracked_items"]:
        assert item["last_checked"] == "2026-11-14T17:15:00+06:00", f"Item {item['id']} has wrong last_checked"
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
    assert "Total%20Audited-128%20Listings-blue" in acd_content, "Missing Total%20Audited-128%20Listings-blue"
    assert "Active%20Tracked-55%20Models-success" in acd_content, "Missing Active%20Tracked-55%20Models-success"
    assert "Archived%20%2F%20Filtered-73%20Listings-lightgrey" in acd_content, "Missing Archived%20%2F%20Filtered-73%20Listings-lightgrey"
    assert "(#A1 – #A73)" in acd_content, "Missing (#A1 – #A73) in navigation index"
    assert "### #A73: Dell Inspiron 14 & 15 2-in-1" in acd_content, "Missing ### #A73 entry"
    assert "ebay.com" not in acd_content.lower(), "Found forbidden ebay.com in ALL_CHECKED_DEALS.md"
    
    active_items = re.findall(r'### (#\d+): \[(.*?)\]', acd_content)
    archived_items = re.findall(r'### (#A\d+): (.*)', acd_content)
    assert len(active_items) == 55, f"Expected 55 active items, got {len(active_items)}"
    assert len(archived_items) == 73, f"Expected 73 archived items, got {len(archived_items)}"
    print(f"ALL_CHECKED_DEALS.md: PASSED ({len(active_items)} active + {len(archived_items)} archived = 128 audited, zero ebay links)")

    # 3. Verify README.md and DEALS_SUMMARY.md
    for filename in ["README.md", "docs/laptop-tracker/DEALS_SUMMARY.md"]:
        filepath = os.path.join(WORKSPACE, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        assert content.count("\ufffd") == 0, f"Found replacement character in {filename}"
        assert "badge/Ledger-v3.2.1-informational" in content, f"Missing v3.2.1 badge in {filename}"
        assert "Checked%20Listings-128%20Audited%20Deals-success" in content, f"Missing 128 audited badge in {filename}"
        assert "2026-11-14 17:15:00 (+06:00 Asia/Dhaka)" in content, f"Missing 17:15:00 timestamp in {filename}"
        assert "candidate #A73" in content, f"Missing candidate #A73 callout in {filename}"
        assert "ebay.com" not in content.lower(), f"Found forbidden ebay.com in {filename}"
        print(f"{filename}: PASSED (v3.2.1, 128 audited badge, fresh timestamp, candidate #A73 callout, zero ebay links)")

    print("\n>>> ALL 4 CORE FILES FULLY VERIFIED & COMPLIANT WITH INVARIANTS! <<<")

if __name__ == "__main__":
    verify_all()
