import json

with open("D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Version: {data['metadata']['version']}, Last Updated: {data['metadata']['last_updated']}")
tiers = {}
for item in data['tracked_items']:
    tiers.setdefault(item.get('tier', 'Unknown'), []).append(item)

for tier, items in tiers.items():
    print(f"\n=== {tier} ({len(items)} items) ===")
    for item in items:
        touch = "TOUCH/360" if item.get('touchscreen') else "CLAMSHELL"
        print(f"  - [{item['id']}] ${item['current_price_usd']} | {item['stock_status']} | {touch} | {item['title'][:70]}")
