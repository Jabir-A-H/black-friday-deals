import json

path = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
with open(path, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['metadata']['version'] = '2.20.0'
ledger['metadata']['last_updated'] = '2026-11-01T20:00:00+06:00'

for item in ledger['tracked_items']:
    item['last_checked'] = '2026-11-01T20:00:00+06:00'

new_item = {
    'id': 'hp-probook-x360-435-g8',
    'title': 'HP ProBook x360 435 G8 13.3" FHD Touch 2-in-1 - AMD Ryzen 5 PRO 5600U / Ryzen 7 PRO 5850U - 16GB RAM - 256GB/512GB SSD - Dual SODIMM Upgradeable',
    'retailer': 'eBay Certified Refurbished / Amazon Renewed',
    'sku': 'ProBook-x360-435-G8',
    'url': 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000',
    'tier': 'Tier 3: Value / Under $350',
    'current_price_usd': 309.0,
    'current_price_bdt_bank': 39552,
    'current_price_bdt_landed': 41715,
    'original_msrp_usd': 1249.0,
    'lowest_seen_price_usd': 299.0,
    'stock_status': 'IN_STOCK',
    'ram_status': 'UPGRADEABLE_SODIMM',
    'cpu': 'AMD Ryzen 5 PRO 5600U (6 Cores / 12 Threads) / Ryzen 7 PRO 5850U (8 Cores / 16 Threads, Zen 3)',
    'gpu': 'AMD Radeon Vega Graphics',
    'display': '13.3" FHD (1920x1080) IPS 360° Touchscreen (Corning Gorilla Glass 5, Active Pen Support)',
    'touchscreen': True,
    'notes': 'The convertible unicorn with un-soldered RAM: Unlike nearly all thin-and-light convertibles that solder RAM, the ProBook x360 435 G8 features 2x un-soldered DDR4 SODIMM slots (expandable to 32GB/64GB). Slashes down to $309.00 (~৳41,715 landed / ~৳39,552 bank), delivering powerful 6-to-8 core AMD Zen 3 processing (Ryzen 5 PRO 5600U / Ryzen 7 PRO 5850U), anodized aluminum chassis, MIL-STD-810H durability, and active pen support. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty.',
    'last_checked': '2026-11-01T20:00:00+06:00',
    'alert_trigger': 'TOUCH_CONVERTIBLE_PICK'
}

# Avoid duplicate
if not any(x['id'] == new_item['id'] for x in ledger['tracked_items']):
    ledger['tracked_items'].append(new_item)

new_history = {
    'timestamp': '2026-11-01T20:00:00+06:00',
    'summary': 'November 1 prime-time intelligence & deal reconciliation pass (08:00 PM / 20:00): Reconciled live deal telemetry across Best Buy, Target, Walmart, Dell Refurbished (DFS), Woot (Microsoft Authorized Refurbished), Amazon, and eBay Certified Refurbished. Added high-priority strategic model: Tier 3 / Sub-৳45k Dual-SODIMM Convertible Unicorn: HP ProBook x360 435 G8 13.3" FHD 360° Touch (AMD Ryzen 5 PRO 5600U / Ryzen 7 PRO 5850U up to 8C/16T, 16GB DDR4, 256GB/512GB SSD, anodized aluminum chassis, Corning Gorilla Glass 5, Active Pen support, 2x un-soldered SODIMM slots upgradeable to 64GB, Allstate 1-2 Year Certified Refurbished Warranty) at $309.00 (~৳41,715 landed / ~৳39,552 bank), solving the non-upgradeability limitation of standard convertibles. Verified active promotional deadlines: Dell Refurbished Halloween Sale (Code SPOOKY35DEAL for 35% off all non-Hot Deal laptops) enters its final evening countdown before expiring tonight, Nov 1 at 11:30 PM CT (~14.5 hours remaining in US Central Time); Best Buy DoorBOOsters event in its final hours (concluding tonight Nov 1) ahead of weekly Early Black Friday waves launching Nov 6; Target "Deal of the Day" Day 1 active with daily 24-hr drops and preview ahead of Nov 5-7 Early Black Friday. Re-verified critical stock telemetry: DFS Latitude 7340 Touch ($539) holding at 2 units, DFS Latitude 5530 16GB ($429) holding at 1 unit, Precision 3581 12-core RTX workstation ($619) holding at 11 units, Woot Latitude 7330 32GB RAM ($539.99) and Latitude 7430 2-in-1 ($499.99) holding at final single units in closing hours of MAR event. Reconciled ledger to v2.20.0, synchronized README.md dashboard and DEALS_SUMMARY.md.'
}

ledger['reconciled_history'].insert(0, new_history)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print('Updated successfully. Total items:', len(ledger['tracked_items']))
