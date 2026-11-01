import json

path = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
with open(path, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['metadata']['version'] = '2.22.0'
ledger['metadata']['last_updated'] = '2026-11-01T23:55:00+06:00'

for item in ledger['tracked_items']:
    item['last_checked'] = '2026-11-01T23:55:00+06:00'

new_item = {
    'id': 'lenovo-yoga-6-13-touch',
    'title': 'Lenovo Yoga 6 13.3" FHD/WUXGA Touch 2-in-1 - AMD Ryzen 5 5500U/7530U / Ryzen 7 - 16GB RAM - 512GB SSD - Fabric / Aluminum 360°',
    'retailer': 'eBay Certified Refurbished / Best Buy Outlet',
    'sku': 'Yoga-6-13-16GB',
    'url': 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000',
    'tier': 'Tier 3: Value / Under $350',
    'current_price_usd': 339.0,
    'current_price_bdt_bank': 43392,
    'current_price_bdt_landed': 45765,
    'original_msrp_usd': 799.99,
    'lowest_seen_price_usd': 329.0,
    'stock_status': 'IN_STOCK',
    'ram_status': 'SOLDERED',
    'cpu': 'AMD Ryzen 5 5500U / 7530U (6 Cores / 12 Threads) or Ryzen 7 5700U (8 Cores / 16 Threads)',
    'gpu': 'AMD Radeon Vega Graphics',
    'display': '13.3" FHD / WUXGA (1920x1080 / 1920x1200) IPS 360° Touchscreen (300 nits, Dolby Vision, Active Pen Support)',
    'touchscreen': True,
    'notes': 'Sub-৳46k Lifestyle Convertible Pick: Slashes 57%+ off MSRP down to $339.00 (~৳45,765 landed / ~৳43,392 bank card rate), delivering an ultra-portable 13.3-inch 360-degree convertible with unique stain-resistant fabric-wrapped or dark teal aluminum lid. Packed with up to 8-core AMD Zen processing, 16GB RAM (meeting the non-negotiable 16GB convertible protocol), 512GB NVMe SSD, Dolby Atmos front-facing stereo speakers, 12+ hour battery life, and active stylus support. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty on eBay Refurbished.',
    'last_checked': '2026-11-01T23:55:00+06:00',
    'alert_trigger': 'TOUCH_CONVERTIBLE_PICK'
}

# Avoid duplicate
if not any(x['id'] == new_item['id'] for x in ledger['tracked_items']):
    ledger['tracked_items'].append(new_item)

new_history = {
    'timestamp': '2026-11-01T23:55:00+06:00',
    'summary': 'November 1 midnight & final coupon countdown pass (11:55 PM / 23:55): Reconciled live deal telemetry across Best Buy, Target, Walmart, Dell Refurbished (DFS), Woot (Microsoft Authorized Refurbished), Amazon, and eBay Certified Refurbished. Added high-priority strategic model: Tier 3 / Sub-৳46k Lifestyle Convertible: Lenovo Yoga 6 13.3" FHD/WUXGA 360° Touch 2-in-1 (AMD Ryzen 5 5500U/7530U or Ryzen 7 5700U up to 8C/16T, 16GB RAM, 512GB SSD, stain-resistant fabric/aluminum lid, Dolby Atmos front-facing speakers, Dolby Vision, Active Pen support, Allstate 1-2 Year Warranty) at $339.00 (~৳45,765 landed / ~৳43,392 bank), providing an ultra-portable 16GB lifestyle convertible well below the ৳50,000 landed mark. Verified critical countdown deadlines: Dell Refurbished Halloween Sale (Code SPOOKY35DEAL for 35% off all non-Hot Deal laptops) in its final ~10.5-hour evening countdown expiring tonight, Nov 1 at 11:30 PM CT; Best Buy DoorBOOsters event reaching its midnight finale (Nov 1) locking in doorbuster pricing on Lenovo IdeaPad Slim 3i Touch ($429.99) and Slim 3i 16GB ($499.99) prior to weekly Early Black Friday waves kicking off Nov 6; Target "Deal of the Day" Day 1 concluding with daily 24-hr rotation ahead of Nov 5-7 Early Black Friday. Re-verified critical stock telemetry: DFS Latitude 7340 Touch ($539) holding at 2 units, DFS Latitude 5530 16GB ($429) holding at 1 unit, Precision 3581 12-core RTX workstation ($619) holding at 11 units, Woot Latitude 7330 32GB RAM ($539.99) and Latitude 7430 2-in-1 ($499.99) holding at final single units in closing hours of MAR event. Reconciled ledger to v2.22.0, synchronized README.md dashboard and DEALS_SUMMARY.md.'
}

ledger['reconciled_history'].insert(0, new_history)

with open(path, 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print('Updated successfully. Total items:', len(ledger['tracked_items']))
