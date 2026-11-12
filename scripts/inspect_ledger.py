import json

with open('D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total items: {len(data['tracked_items'])}")
for i, item in enumerate(data['tracked_items'], 1):
    print(f"{i:02d}. [{item['id']}] {item['retailer']} | ${item['current_price_usd']} | {item['stock_status']}")
