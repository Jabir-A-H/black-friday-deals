import json

with open("D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["tracked_items"]:
    u = item["url"]
    if any(k in u for k in ["searchpage", "search?q", "/b/", "/str/", "plus/"]):
        print(f"{item['id']} --> {u}")
