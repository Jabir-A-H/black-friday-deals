const fs = require('fs');
const path = require('path');

const ledgerPath = path.join('D:', 'WebDev', 'BlackFridayDeals', 'docs', 'laptop-tracker', 'DEALS_LEDGER.json');
const rawData = fs.readFileSync(ledgerPath, 'utf8');
const ledger = JSON.parse(rawData);

ledger.metadata.version = "2.39.0";
ledger.metadata.last_updated = "2026-11-06T00:50:00+06:00";

const newItem = {
  id: "dell-latitude-9420-2in1",
  title: "Dell Latitude 9420 14.0\" QHD+ Touch 2-in-1 - Intel Core i7-1185G7 vPro - 16GB RAM - 512GB SSD - SafeShutter - Quad Speakers",
  retailer: "eBay Certified Refurbished / Amazon Renewed / Dell Financial Services",
  sku: "Latitude-9420-2in1-QHD",
  url: "https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000",
  tier: "Tier 2: Mid Budget ($350-$450)",
  current_price_usd: 369.0,
  current_price_bdt_bank: 47232,
  current_price_bdt_landed: 49815,
  original_msrp_usd: 1699.0,
  lowest_seen_price_usd: 359.0,
  stock_status: "IN_STOCK",
  ram_status: "SOLDERED",
  cpu: "Intel Core i7-1185G7 vPro (4 Cores / 8 Threads, up to 4.8 GHz Turbo, 11th Gen)",
  gpu: "Intel Iris Xe Graphics (96EU, Dual Thunderbolt 4 40Gbps eGPU ready)",
  display: "14.0\" 16:10 QHD+ (2560x1600) IPS 360° Touchscreen (500 nits, 100% sRGB, ComfortView Plus, Gorilla Glass 6 DX, Active Pen Support)",
  touchscreen: true,
  notes: "Dell's Apex 9000-Series Executive Flagship Convertible: Slashes 78%+ off original $1,699+ MSRP down to $369.00 (~৳49,815 landed / ~৳47,232 bank card rate), breaking the sub-৳50,000 landed barrier. The 9420 is Dell's highest-tier commercial machine (positioned above the 7000 and 5000 series, directly rivaling the ThinkPad X1 Yoga and HP EliteBook 1040). Features an ultra-premium CNC-machined aluminum unibody chassis with diamond-cut edges, 14.0-inch 16:10 QHD+ (2560x1600) 500-nit touch display, 16GB dual-channel RAM (satisfying the non-negotiable 16GB convertible protocol), 512GB PCIe NVMe SSD, dual Thunderbolt 4 / USB-C ports (40Gbps full eGPU support), MicroSD 4.0 slot, motorized SafeShutter webcam that automatically opens and closes, quad-speaker array with dual top-firing tweeters and bottom woofers, quad noise-canceling beamforming microphones, and Dell Active Pen support. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty.",
  last_checked: "2026-11-06T00:50:00+06:00",
  alert_trigger: "TOUCH_CONVERTIBLE_PICK"
};

// Check if already exists
const existingIndex = ledger.tracked_items.findIndex(item => item.id === newItem.id);
if (existingIndex === -1) {
  ledger.tracked_items.push(newItem);
} else {
  ledger.tracked_items[existingIndex] = newItem;
}

const newHistoryEntry = {
  timestamp: "2026-11-06T00:50:00+06:00",
  summary: "November 6 Friday early morning Black Friday doorbuster launch & 9000-series flagship convertible pass (12:50 AM / 00:50): Executed comprehensive multi-retailer intelligence sweep across Best Buy, Target, Walmart, Woot, Amazon, Dell Refurbished (DFS), BlairTech, and eBay Certified Refurbished. Confirmed Best Buy Early Black Friday full weekly doorbuster rollout is OFFICIALLY LIVE TODAY (Friday, Nov 6) backed by Best Buy's Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027 (active doorbusters holding: HP OmniBook X Flip 14 Lunar Lake Copilot+ PC at $649.99, Lenovo Yoga 7i 16 at $599.99, Lenovo LOQ 15 RTX 4060 at $699.99, ASUS TUF A15 RTX 4060 at $679.99, Lenovo IdeaPad Slim 3i Touch at $429.99, and Slim 3i 16GB at $499.99); Target 3-Day Early Black Friday Sale is LIVE IN DAY 2 (Thursday, Nov 5 through Saturday, Nov 7) featuring rolling Target Circle tech markdowns; Dell Refurbished instant 40%–50% Hot Deals holding on Precision 3581 12-core RTX A500 workstation ($619, 10 units left) and Latitude 7340 32GB QHD+ ($579, 25 units left); Walmart Event 1 confirmed for Nov 12–15 (monitoring HP Victus RTX 4050 restocks at $499); Woot MAR inventory holding steady on Latitude 7330 32GB ($539.99), Latitude 7430 32GB Touch ($449.99), and Latitude 7430 2-in-1 ($449.99). Added 1 major strategic Tier 2 / Sub-৳50k BDT 16:10 QHD+ 9000-series executive flagship convertible: Dell Latitude 9420 2-in-1 Touch (Intel Core i7-1185G7 vPro, 16GB LPDDR4x-4266, 512GB PCIe NVMe SSD, 14.0\" 16:10 QHD+ 2560x1600 500-nit Gorilla Glass 6 DX 360° Touch, motorized SafeShutter webcam, quad-speaker array with dual top-firing tweeters & bottom woofers, quad-mic array, dual Thunderbolt 4 eGPU ready, MicroSD 4.0 reader, CNC diamond-cut aluminum unibody, Allstate 1-2 Year Warranty) slashed 78%+ off $1,699 MSRP down to $369.00 USD (~৳49,815 landed / ~৳47,232 bank card rate) on eBay Refurbished, shattering the sub-৳50,000 landed barrier for Dell's top-tier 9000-series executive convertible. Audited candidate #A13: Microsoft Surface Laptop Go (Go 2 / Go 3) 12.4\" evaluated and disqualified/rejected due to sub-1080p display (1536x1024), 4GB-8GB soldered RAM violating the 16GB non-negotiable protocol, lack of keyboard backlighting on base configs, lack of Thunderbolt/eGPU, and glued zero-repairability chassis, establishing the Latitude 7320 2-in-1 ($259), ThinkBook 14s Yoga ($319), and Latitude 9420 2-in-1 ($369) as vastly superior choices. Master directory expanded to 67 audited listings (54 active serialized models + 13 archived/disqualified listings). Reconciled ledger to v2.39.0, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
};

ledger.reconciled_history.unshift(newHistoryEntry);

fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2) + '\n', 'utf8');
console.log(`Updated ledger successfully! Version: ${ledger.metadata.version}, Items: ${ledger.tracked_items.length}, History entries: ${ledger.reconciled_history.length}`);
