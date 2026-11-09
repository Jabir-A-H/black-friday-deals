import json
import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"

def verify_all():
    print("=== STARTING FULL TRACKER VERIFICATION GATE ===")

    # 1. Verify DEALS_LEDGER.json
    ledger_path = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_LEDGER.json")
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    assert ledger["metadata"]["version"] == "2.69.0", f"Unexpected version: {ledger['metadata']['version']}"
    assert ledger["metadata"]["last_updated"] == "2026-11-09T11:15:00+06:00"
    assert len(ledger["tracked_items"]) == 55, f"Expected 55 items, got {len(ledger['tracked_items'])}"
    assert ledger["reconciled_history"][0]["timestamp"] == "2026-11-09T11:15:00+06:00"
    for item in ledger["tracked_items"]:
        assert item["last_checked"] == "2026-11-09T11:15:00+06:00", f"Item {item['id']} has wrong last_checked"
        assert item["current_price_bdt_bank"] == round(item["current_price_usd"] * 128)
        assert item["current_price_bdt_landed"] == round(item["current_price_usd"] * 135)
    print("DEALS_LEDGER.json: PASSED (55 items, valid JSON, correct calculations)")

    # 2. Verify ALL_CHECKED_DEALS.md
    acd_path = os.path.join(WORKSPACE, "docs/laptop-tracker/ALL_CHECKED_DEALS.md")
    with open(acd_path, "r", encoding="utf-8") as f:
        acd_content = f.read()

    assert acd_content.count("\ufffd") == 0, "Found replacement character in ALL_CHECKED_DEALS.md"
    assert "Total%20Audited-96%20Listings-blue" in acd_content
    assert "Active%20Tracked-55%20Models-success" in acd_content
    assert "Archived%20%2F%20Filtered-41%20Listings-lightgrey" in acd_content
    assert "(#A1 – #A41)" in acd_content
    assert "### #A41: ASUS Vivobook 15 & Vivobook 15 OLED" in acd_content
    
    active_items = re.findall(r'### (#\d+): \[(.*?)\]', acd_content)
    archived_items = re.findall(r'### (#A\d+): (.*)', acd_content)
    assert len(active_items) == 55, f"Expected 55 active items, got {len(active_items)}"
    assert len(archived_items) == 41, f"Expected 41 archived items, got {len(archived_items)}"
    print(f"ALL_CHECKED_DEALS.md: PASSED ({len(active_items)} active + {len(archived_items)} archived = 96 audited)")

    # 3. Verify README.md and DEALS_SUMMARY.md
    for filename in ["README.md", "docs/laptop-tracker/DEALS_SUMMARY.md"]:
        filepath = os.path.join(WORKSPACE, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        assert content.count("\ufffd") == 0, f"Found replacement character in {filename}"
        assert "badge/Ledger-v2.69.0-informational" in content, f"Missing v2.69.0 badge in {filename}"
        assert "Checked%20Listings-96%20Audited%20Deals-success" in content, f"Missing 96 audited badge in {filename}"
        assert "2026-11-09 11:15:00 (+06:00 Asia/Dhaka)" in content, f"Missing 11:15:00 timestamp in {filename}"
        assert "candidate #A41" in content, f"Missing candidate #A41 callout in {filename}"
        
        # Verify rows
        serials = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|', content)
        assert len(serials) == 55, f"Expected 55 table rows, got {len(serials)} in {filename}"
        champions = re.findall(r'\|\s*(👑|🪶|✍️|🏆|💎|🛠️|🔄|☀️|🦄|🏗️|🎮)\s*\*\*.*?\*\*\s*\|', content)
        assert len(champions) == 11, f"Expected 11 champions, got {len(champions)} in {filename}"
        print(f"{filename}: PASSED (55 table rows, 11 champions, valid badges and links)")

    print("\n>>> ALL QUALITY AND INTEGRITY GATES PASSED 100% CLEANLY! <<<")

if __name__ == "__main__":
    verify_all()
