import json

with open('D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, it in enumerate(data['tracked_items']):
    iid = it['id']
    cpu = it.get('cpu', 'N/A')
    ram_status = it.get('ram_status', 'N/A')
    gpu = it.get('gpu', 'N/A')
    display = it.get('display', 'N/A')
    tier = it.get('tier', 'N/A')
    print(f"[{i+1:02d}] {iid} ({tier})\n  CPU: {cpu}\n  GPU: {gpu}\n  RAM: {ram_status}\n  Display: {display}\n")
