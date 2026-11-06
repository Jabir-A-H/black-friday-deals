# 🔗 Laptop Tracker: Live Link & Listing Audit Protocol

This document defines the strict operational standard for auditing, verifying, and maintaining live purchase links across the Black Friday Laptop Tracker.

## 1. Zero-Placeholder & Specificity Rule
- **Direct Item Listings for Specific Items:** When a specific model and price are recommended (especially in the Top Champions table and active tier tables), the primary link MUST point directly to a specific, live, purchasable listing:
  - eBay: `https://www.ebay.com/itm/<item_id>`
  - Best Buy: `https://www.bestbuy.com/site/<product-slug>/<skuId>.p?skuId=<skuId>`
  - Woot: `https://computers.woot.com/offers/<offer-slug>`
  - Dell DFS: `https://www.dellrefurbished.com/item/<item-slug>`
  - Walmart: `https://www.walmart.com/ip/<product-slug>/<id>`
  - Target: `https://www.target.com/p/<product-slug>/-/A-<id>`
- **No Search Page Masquerading:** Never present an eBay search results URL (`/sch/i.html`) as an individual product deal link.
- **Discoverability Links:** Clean search query URLs are permitted ONLY as secondary links clearly labeled for exploratory browsing (e.g., `[Search More Listings →](url)`).

## 2. The Adversarial "Defect Gate" (Doubt Gate)
Every candidate listing MUST be scrutinized against critical hardware defect traps:
- **Battery Defect Trap:** Disqualify any listing with "BATTERY ISSUE", "dead battery", "does not hold charge", or "battery not detected". For Bangladesh buyers, importing replacement lithium batteries carries severe courier restrictions and $75–$100+ costs.
- **Display Flaws:** Disqualify listings with cracked screens, pressure marks, bright spots, dead pixel clusters, or damaged digitizers.
- **Parts / Scrap Trap:** Disqualify any listing categorized under "For parts or not working" (`LH_ItemCondition=7000`) or labeled "AS-IS / UNTESTED".
- **Enterprise Locks:** Disqualify any unit with locked BIOS, Absolute Computrace enabled, or Corporate MDM enrollment.
- **Missing Essentials:** Ensure RAM is at least 16GB, SSD is present, and for convertibles, touch digitizer and stylus compatibility are intact.

## 3. Search Filter Sanitization
- Do NOT use broken or overly narrow filters like `LH_ItemCondition=2000|2500` that wipe out clean Grade A Refurbished inventory and leave only $800+ irrelevant items.
- If providing a discoverability search URL, use:
  `https://www.ebay.com/sch/i.html?_nkw=<Clean+Model+Keywords>+16GB&LH_BIN=1` (with optional `_udhi=<max_price>`).

## 4. Required Report Fields per Model
When auditing a batch of laptops, report:
1. `model_id`: ID from DEALS_LEDGER.json
2. `direct_url`: Exact live direct link
3. `listing_title`: Exact seller listing title
4. `price_usd`: Live Buy It Now price in USD
5. `condition`: eBay Refurbished Grade (Excellent/Very Good/Good) or Grade A
6. `warranty`: Allstate 1-2 Year or Seller Return period
7. `battery_status`: Verified healthy / working
8. `notes`: Key hardware highlights
