# 🔗 Laptop Tracker: Live Link & Listing Audit Protocol

This document defines the strict operational standard for auditing, verifying, and maintaining live purchase links across the Black Friday Laptop Tracker.

## 1. Zero-Placeholder & Specificity Rule
- **Direct Item Listings for Specific Items:** When a specific model and price are recommended (especially in the Top Champions table and active tier tables), the primary link MUST point directly to a specific, live, purchasable listing on 1st-party manufacturer direct outlets or authorized tier-1 major direct retailers:
  - Dell Refurbished (DFS Direct): `https://www.dellrefurbished.com/item/<slug>`
  - Lenovo US Outlet: `https://www.lenovo.com/us/en/p/laptops/<slug>/<part-number>`
  - Acer Recertified Direct: `https://acerrecertified.com/laptops/<slug>`
  - HP Business Outlet: `https://www.hp.com/us-en/shop/cv/hp-outlet`
  - Micro Center: `https://www.microcenter.com/product/<id>/<slug>`
  - B&H Photo Video Used: `https://www.bhphotovideo.com/c/product/<id>-REG/<slug>.html`
  - Best Buy Direct: `https://www.bestbuy.com/site/<product-slug>/<skuId>.p?skuId=<skuId>`
  - Woot! Direct: `https://computers.woot.com/offers/<offer-slug>`
  - Walmart Direct: `https://www.walmart.com/ip/<product-slug>/<id>`
- **Absolute 3rd-Party Marketplace & eBay Ban:** Under NO circumstances allow `ebay.com` URLs (no item listings, no /sch/ search queries, no /b/ categories, no store links) anywhere in active tracking.
- **No Search Page Masquerading:** Never present an unverified search results page as an individual product deal link.
- **Discoverability Links:** Clean store search query URLs are permitted ONLY as secondary links clearly labeled for exploratory browsing on authorized platforms (e.g., Dell DFS search, Lenovo Outlet search, Micro Center search).

## 2. The Adversarial "Defect Gate" (Doubt Gate)
Every candidate listing MUST be scrutinized against critical hardware defect traps:
- **Battery Defect Trap:** Disqualify any listing with "BATTERY ISSUE", "dead battery", "does not hold charge", or "battery not detected". For Bangladesh buyers, importing replacement lithium batteries carries severe courier restrictions and $75–$100+ costs.
- **Display Flaws:** Disqualify listings with cracked screens, pressure marks, bright spots, dead pixel clusters, or damaged digitizers.
- **Parts / Scrap Trap:** Disqualify any listing categorized under "For parts or not working" (`LH_ItemCondition=7000`) or labeled "AS-IS / UNTESTED".
- **Enterprise Locks:** Disqualify any unit with locked BIOS, Absolute Computrace enabled, or Corporate MDM enrollment.
- **Missing Essentials:** Ensure RAM is at least 16GB, SSD is present, and for convertibles, touch digitizer and stylus compatibility are intact.

## 3. Search Filter Sanitization
- Exclusively use official outlet search filters or tier-1 retailer refurbished/open-box filters.
- If providing a discoverability search URL, use official outlets:
  - Dell Refurbished: `https://www.dellrefurbished.com/laptops?filter_memory_capacity=16gb`
  - Lenovo Outlet: `https://www.lenovo.com/us/en/outletus/laptops/`
  - Micro Center: `https://www.microcenter.com/category/4294967288/refurbished-laptops`

## 4. Required Report Fields per Model
When auditing a batch of laptops, report:
1. `model_id`: ID from DEALS_LEDGER.json
2. `direct_url`: Exact live direct link
3. `listing_title`: Exact retailer listing title
4. `price_usd`: Live price in USD
5. `condition`: Official Manufacturer Refurbished (Grade A / Excellent / Certified)
6. `warranty`: Manufacturer 90-day to 2-Year or Authorized Retailer warranty
7. `battery_status`: Verified healthy / working
8. `notes`: Key hardware highlights
