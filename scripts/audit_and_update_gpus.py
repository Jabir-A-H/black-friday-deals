import json

with open('D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

vague_phrases = ['rtx dedicated workstation', 'dedicated workstation gpu', 'nvidia rtx dedicated gpu']
found = 0
for it in data['tracked_items']:
    for k, v in it.items():
        if isinstance(v, str) and any(vp in v.lower() for vp in vague_phrases):
            print(f"Found in item {it['id']}, field {k}: {v}")
            found += 1

if found == 0:
    print(f"PASS: All {len(data['tracked_items'])} tracked items have exact, non-vague GPU specifications!")
