import json

ledger_path = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
with open(ledger_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['metadata']['version'] = '2.25.0'
data['metadata']['last_updated'] = '2026-11-03T23:45:00+06:00'

for item in data['tracked_items']:
    item['last_checked'] = '2026-11-03T23:45:00+06:00'

history_entry = {
    'timestamp': '2026-11-03T23:45:00+06:00',
    'summary': (
        "November 3 night intelligence & pre-doorbuster synchronization pass (11:45 PM / 23:45): "
        "Reconciled live deal telemetry across Best Buy, Target, Walmart, Dell Refurbished (DFS), "
        "Woot (Microsoft Authorized Refurbished), Amazon, and eBay Certified Refurbished. "
        "Verified official transition into the 48-hour countdown for Target Early Black Friday (Nov 5–7) "
        "and 72-hour countdown for Best Buy Early Black Friday full rollout (Nov 6), backed by Best Buy's "
        "Holiday Price Match Guarantee and extended returns through January 15, 2027. "
        "Walmart confirmed Black Friday Deals Event 1 for November 12–15 (Walmart+ early access Nov 12 at 12:01 AM ET) — "
        "keeping high watch on HP Victus RTX 4050 restocks at $499. "
        "Dell Refurbished Halloween coupon SPOOKY35DEAL officially expired, with DFS transitioning to 40%–50% "
        "instant Hot Deals (Latitude 7340 32GB QHD+ at $579, Precision 3581 12-core RTX workstation at $619). "
        "Re-verified Tier 4 Gravity Outlier: Acer Swift Go 16 AI 16.0\" Touch OLED (Core Ultra 5 AI Boost, 16GB LPDDR5X, "
        "512GB SSD, 100% DCI-P3 500-nit OLED, 71 Whr battery, 2-Year Allstate Warranty) at $577.88 "
        "(~৳78,014 landed / ~৳73,969 bank) at eBay Acer Outlet with coupon NICEFIND10. "
        "Re-verified complete sub-৳55k Touch & 360° Convertible portfolio across 14 models: "
        "Dell Latitude 7320 2-in-1 ($259.00 / ~৳34,965 landed), HP EliteBook x360 830 G8 ($299.00 / ~৳40,365 landed), "
        "HP ProBook x360 435 G8 ($309.00 / ~৳41,715 landed), Lenovo ThinkBook 14s Yoga ($319.00 / ~৳43,065 landed), "
        "HP EliteBook x360 1040 G8 ($319.00 / ~৳43,065 landed), Dell Latitude 5320 2-in-1 ($319.00 / ~৳43,065 landed), "
        "Dell Latitude 7420 2-in-1 ($319.00 / ~৳43,065 landed), ThinkPad X13 Yoga Gen 2 ($329.00 / ~৳44,415 landed), "
        "ThinkPad L13 Yoga Gen 2 ($335.00 / ~৳45,225 landed), Lenovo Yoga 6 13.3\" ($339.00 / ~৳45,765 landed), "
        "Lenovo IdeaPad Flex 5 14\" ($349.00 / ~৳47,115 landed), Dell Inspiron 14 2-in-1 ($369.00 / ~৳49,815 landed), "
        "HP Envy x360 15.6\" ($369.00 / ~৳49,815 landed), and ThinkPad X1 Yoga Gen 6 ($379.00 / ~৳51,165 landed). "
        "Reconciled ledger to v2.25.0, synchronized README.md dashboard and DEALS_SUMMARY.md."
    )
}

if data['reconciled_history'][0]['timestamp'] != history_entry['timestamp']:
    data['reconciled_history'].insert(0, history_entry)

with open(ledger_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print('DEALS_LEDGER.json successfully updated to v2.25.0')
