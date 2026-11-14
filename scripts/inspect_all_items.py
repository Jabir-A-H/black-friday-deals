import json

with open('D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total tracked items: {len(d['tracked_items'])}")
for i, it in enumerate(d['tracked_items']):
    print(f"{i+1:02d}. [{it['tier']}] {it['id']} | ${it['current_price_usd']:.2f} | {it['stock_status']} | Touch: {it['touchscreen']} | {it['retailer']}")
