import json

ledger_path = "D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json"

with open(ledger_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["metadata"]["version"] = "2.39.0"
data["metadata"]["last_updated"] = "2026-11-06T06:45:00+06:00"

items = data["tracked_items"]
for item in items:
    item["last_checked"] = "2026-11-06T06:45:00+06:00"
    if item["id"] == "dell-latitude-7430-2in1-woot":
        item["current_price_usd"] = 379.0
        item["current_price_bdt_bank"] = 48512
        item["current_price_bdt_landed"] = 51165
        item["lowest_seen_price_usd"] = 379.0
        item["notes"] = "PRICE DROP -$70.99 (DOWN TO $379.00): Slashes down from $449.99 to $379.00 USD (~৳51,165 landed / ~৳48,512 bank card rate) on Woot / eBay Refurbished. Packs 12th Gen 10-core Core i7-1265U with 16GB RAM, full 360° convertible touch form factor, dual Thunderbolt 4 (40Gbps eGPU ready), Corning Gorilla Glass 6 DX, active stylus support, and 1-year warranty. Enters the prime sub-৳55,000 BDT sweet spot!"
        item["alert_trigger"] = "PRICE_DROP"
    elif item["id"] == "thinkpad-l13-yoga-gen3":
        item["current_price_usd"] = 339.0
        item["current_price_bdt_bank"] = 43392
        item["current_price_bdt_landed"] = 45765
        item["lowest_seen_price_usd"] = 339.0
        item["notes"] = "PRICE DROP -$20.00 (SUB-৳46k SWEET SPOT): Slashes down to $339.00 USD (~৳45,765 landed / ~৳43,392 bank card rate). Upgrades the classic L13 Yoga with a modern taller 16:10 WUXGA (1920x1200) touch panel, 10-core 12th Gen Intel Core i5-1245U vPro or 8-core AMD Ryzen 7 PRO 5875U silicon, 16GB RAM (meeting the non-negotiable convertible protocol), integrated rechargeable ThinkPad Pen Pro garaged directly in the side frame, Thunderbolt 4 (eGPU ready on Intel), MicroSD card reader, and MIL-STD-810H durability. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty."
        item["alert_trigger"] = "PRICE_DROP"

if not any(i["id"] == "thinkpad-x1-yoga-gen7" for i in items):
    new_item = {
        "id": "thinkpad-x1-yoga-gen7",
        "title": "Lenovo ThinkPad X1 Yoga Gen 7 14.0\" 16:10 WUXGA Touch 2-in-1 - Intel Core i5-1245U vPro / i7-1265U - 16GB LPDDR5 - 256GB/512GB Gen 4 SSD - Garaged Pen Pro",
        "retailer": "eBay Certified Refurbished / Amazon Renewed",
        "sku": "ThinkPad-X1-Yoga-G7-WUXGA",
        "url": "https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000",
        "tier": "Tier 2: Mid Budget ($350-$450)",
        "current_price_usd": 389.0,
        "current_price_bdt_bank": 49792,
        "current_price_bdt_landed": 52515,
        "original_msrp_usd": 1899.0,
        "lowest_seen_price_usd": 389.0,
        "stock_status": "IN_STOCK",
        "ram_status": "SOLDERED",
        "cpu": "Intel Core i5-1245U vPro / i7-1265U (10 Cores / 12 Threads, 2 P-cores + 8 E-cores, up to 4.80 GHz, 12MB Cache)",
        "gpu": "Intel Iris Xe Graphics (96 EUs)",
        "display": "14.0\" 16:10 WUXGA (1920x1200) Low Power IPS 360° Touchscreen (400 nits, 100% sRGB, Anti-reflective / Anti-smudge, Eyesafe Certified)",
        "touchscreen": True,
        "notes": "NEW DOORBUSTER ADDITION / EXECUTIVE 12TH GEN FLAGSHIP: Slashes 79%+ off original $1,899 MSRP down to $389.00 USD (~৳52,515 landed / ~৳49,792 bank card rate), entering directly into our prime sub-৳55,000 BDT sweet spot. The apex 12th Gen Alder Lake ThinkPad X1 Yoga Gen 7 features a CNC machined Deep Black / Storm Grey aluminum chassis, 10-core 12th Gen Intel hybrid processor, 16GB LPDDR5-5200 dual-channel RAM (satisfies 16GB convertible protocol), 256GB/512GB PCIe Gen 4 x4 NVMe SSD, built-in rechargeable ThinkPad Pen Pro garaged in the chassis, dual Thunderbolt 4 / USB4 40Gbps ports (full eGPU ready), 57Wh battery with Rapid Charge, quad Dolby Atmos speakers, quad 360-degree far-field microphones, FHD 1080p + IR webcam with privacy shutter and Computer Vision human presence sensing, and MIL-STD-810H military durability. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty.",
        "last_checked": "2026-11-06T06:45:00+06:00",
        "alert_trigger": "NEW_DOORBUSTER"
    }
    items.append(new_item)

with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated DEALS_LEDGER.json successfully. Total items: {len(data['tracked_items'])}")
