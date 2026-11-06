import json
import re

with open("D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json", "r", encoding="utf-8") as f:
    data = json.load(f)
ledger_ids = [item['id'] for item in data['tracked_items']]
print(f"Total in ledger: {len(ledger_ids)}")

content = open("D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md", encoding="utf-8").read()
active_sections = re.findall(r'### (#\d+): \[(.*?)\]\((.*?)\)', content)
print(f"Total numbered listings in ALL_CHECKED_DEALS: {len(active_sections)}")

for num, title, url in active_sections:
    # find Tracking ID in table
    pattern = rf'### {num}:.*?\*\*Tracking ID & SKU\*\*\s*\|\s*`([^`]+)`'
    m = re.search(pattern, content, re.DOTALL)
    tid = m.group(1) if m else "UNKNOWN"
    in_ledger = tid in ledger_ids
    if not in_ledger:
        print(f"NOT in ledger: {num} | {tid} | {title[:50]}")
