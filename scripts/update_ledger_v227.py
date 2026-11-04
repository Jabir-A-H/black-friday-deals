import json

ledger_path = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
with open(ledger_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['metadata']['version'] = '2.27.0'
data['metadata']['last_updated'] = '2026-11-04T23:05:00+06:00'

for it in data['tracked_items']:
    it['last_checked'] = '2026-11-04T23:05:00+06:00'

new_history = {
    'timestamp': '2026-11-04T23:05:00+06:00',
    'summary': (
        "November 4 late night dashboard redefinition & master inventory directory release (11:05 PM / 23:05): "
        "Redefined the primary GitHub dashboard (README.md and DEALS_SUMMARY.md) with modern executive styling, "
        "direct jump navigation pills, and an official callout linking to the newly generated master directory "
        "(ALL_CHECKED_DEALS.md). Published 'docs/laptop-tracker/ALL_CHECKED_DEALS.md' featuring 48 complete listings "
        "(41 active serialized models + 7 archived/disqualified listings) providing exhaustive telemetry, full hardware specs, "
        "eGPU analysis, storage bus configurations, SD card formats, garaged stylus mechanics, and curatorial audit verdicts. "
        "Hardened both persistent sidecar automation configs (laptop-deal-tracker every 2h and firecrawl-deep-deal-hunter daily) "
        "with explicit mandates to continuously reconcile and overwrite README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md "
        "on every execution. Bumped ledger to v2.27.0."
    )
}

if data['reconciled_history'][0]['timestamp'] != new_history['timestamp']:
    data['reconciled_history'].insert(0, new_history)

with open(ledger_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("DEALS_LEDGER.json successfully updated to v2.27.0")
