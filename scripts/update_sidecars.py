import json

def update_laptop_deal_tracker():
    path = 'C:/Users/ONE/.gemini/config/sidecars/laptop-deal-tracker/sidecar.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_prompt = (
        "You are the Black Friday Laptop Deal Tracker. Your mission is to execute an intelligent deal-tracking and publishing pass defined in 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/TRACKER_SPEC.md'. "
        "Strategic Focus: 1) Conduct thorough research for sub-50k to 55k BDT items ($300-$407 USD landed). "
        "2) Keep a dedicated eye out for Touchscreen and 360-degree convertibles with 16GB RAM. "
        "3) Maintain active radar for massive outlier discounts (Tier 4 Gravity Stretchers up to $699+) slashed 40%+ off MSRP. "
        "Steps: 1) Read 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json' to review currently tracked models, baseline specs, and price thresholds. "
        "2) Check live US Black Friday deals across Best Buy, Target, Walmart, Amazon, Woot, and Dell Refurbished using native web search (0 API credits). "
        "3) Reconcile prices, stock statuses, and new doorbusters in 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json' and save to disk. "
        "4) Always intelligently compose, reconcile, and overwrite the primary GitHub dashboard in 'D:/WebDev/BlackFridayDeals/README.md' and 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_SUMMARY.md' with updated comparison tables, live stock badges, and executive callouts. "
        "5) Always reconcile and update the comprehensive directory in 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md' with every verified or evaluated listing for readers wanting full deal telemetry. "
        "6) User authorization granted: You are explicitly instructed and authorized to stage, commit, and push changes to GitHub by executing: powershell -ExecutionPolicy Bypass -File D:/WebDev/BlackFridayDeals/scripts/sync-deals.ps1 -Message 'feat(tracker): auto-sync live deals, dashboard, and checked inventory'. "
        "7) Output a concise report highlighting any new price drops, doorbusters, or stock changes."
    )
    data['args'][4] = new_prompt

    grants = set(data['agent_permissions']['access_grants'])
    grants.add("read_file(D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md)")
    grants.add("write_file(D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md)")
    data['agent_permissions']['access_grants'] = sorted(list(grants))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Updated laptop-deal-tracker/sidecar.json")

def update_firecrawl_deep_hunter():
    path = 'C:/Users/ONE/.gemini/config/sidecars/firecrawl-deep-deal-hunter/sidecar.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_prompt = (
        "You are the Firecrawl Daily Deep Deal Hunter. Your mission is to conduct a daily deep-web intelligence sweep across primary retailers, certified refurbished outlets, deal forums, and reseller marketplaces following 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/TRACKER_SPEC.md'. "
        "Strategic Focus: 1) Prioritize thorough research for sub-50k to 55k BDT items ($300-$407 USD landed). "
        "2) Continuously track 16GB Touchscreen and 360-degree convertibles. "
        "3) Track massive high-gravity outlier discounts (Tier 4 Gravity Stretchers up to $699+) slashed 40%+ off MSRP. "
        "Credit Conservation Rule: Limit Firecrawl calls to 15-20 credits per run. "
        "Steps: 1) Read 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json' to review current tracked items. "
        "2) Use 'firecrawl_search' to query deep deal threads on Slickdeals, Woot, eBay Refurbished, and Dell Outlet. "
        "3) Use 'firecrawl_scrape' on top 2-4 candidate URLs to extract verified prices, coupon codes, and specs. "
        "4) Reconcile changes into 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json' and save. "
        "5) Always intelligently compose, reconcile, and overwrite the primary GitHub dashboard in 'D:/WebDev/BlackFridayDeals/README.md' and 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_SUMMARY.md'. "
        "6) Always reconcile and update the comprehensive directory in 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md' with every inspected and audited listing. "
        "7) User authorization granted: You are explicitly instructed and authorized to stage, commit, and push changes to GitHub by executing: powershell -ExecutionPolicy Bypass -File D:/WebDev/BlackFridayDeals/scripts/sync-deals.ps1 -Message 'feat(deep-hunter): daily deal sweep, dashboard, and checked inventory'. "
        "8) Produce a concise intelligence report."
    )
    data['args'][4] = new_prompt

    grants = set(data['agent_permissions']['access_grants'])
    grants.add("read_file(D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md)")
    grants.add("write_file(D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md)")
    data['agent_permissions']['access_grants'] = sorted(list(grants))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Updated firecrawl-deep-deal-hunter/sidecar.json")

if __name__ == '__main__':
    update_laptop_deal_tracker()
    update_firecrawl_deep_hunter()
