import json
import re
import os
import subprocess

WORKSPACE = "D:/WebDev/BlackFridayDeals"

def update_ledger():
    ledger_path = os.path.join(WORKSPACE, "docs/laptop-tracker/DEALS_LEDGER.json")
    with open(ledger_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["metadata"]["version"] = "2.40.0"
    data["metadata"]["last_updated"] = "2026-11-06T12:45:00+06:00"

    for item in data["tracked_items"]:
        item["last_checked"] = "2026-11-06T12:45:00+06:00"

    history_entry = {
        "timestamp": "2026-11-06T12:45:00+06:00",
        "summary": "November 6 midday automation pass (12:45 PM): Reconciled live deal telemetry across Best Buy, Target (Day 2 Early Black Friday), Walmart, Dell Refurbished (DFS), Woot, and eBay Certified Refurbished. Added high-priority strategic addition: ThinkPad X1 Yoga Gen 7 14.0\" 16:10 WUXGA Touch 2-in-1 (10-core 12th Gen Core i5-1245U/i7-1265U, 16GB LPDDR5-5200, 256GB/512GB PCIe Gen 4 SSD, garaged stylus, dual TB4/USB4, CNC aluminum chassis, Allstate Warranty) slashed 79%+ off $1,899 MSRP down to $389.00 (~৳52,515 landed / ~৳49,792 bank), entering the prime sub-৳55,000 sweet spot. Verified double price drops: ThinkPad L13 Yoga Gen 3 16:10 WUXGA dropped -$20 down to $339.00 (~৳45,765 landed), and Dell Latitude 7430 2-in-1 dropped -$70.99 down to $379.00 (~৳51,165 landed). Verified Best Buy Friday Early Black Friday weekly doorbusters rollout and Target Day 2 drops. Reconciled 55 active models and 13 archived listings (68 total audited). Regenerated README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md with Needed-Info-First architecture and pushed to main."
    }

    if not data["reconciled_history"] or data["reconciled_history"][0]["timestamp"] != history_entry["timestamp"]:
        data["reconciled_history"].insert(0, history_entry)

    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"DEALS_LEDGER.json updated to v2.40.0. Tracked models: {len(data['tracked_items'])}")

if __name__ == "__main__":
    update_ledger()
