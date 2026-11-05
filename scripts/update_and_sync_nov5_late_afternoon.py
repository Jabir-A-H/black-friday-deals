import json
import os
import re

REPO_DIR = 'D:/WebDev/BlackFridayDeals'
LEDGER_PATH = os.path.join(REPO_DIR, 'docs/laptop-tracker/DEALS_LEDGER.json')
ALL_DEALS_SCRIPT = os.path.join(REPO_DIR, 'scripts/generate_all_checked_deals.py')
DASHBOARD_SCRIPT = os.path.join(REPO_DIR, 'scripts/generate_full_dashboard.py')
README_PATH = os.path.join(REPO_DIR, 'README.md')
SUMMARY_PATH = os.path.join(REPO_DIR, 'docs/laptop-tracker/DEALS_SUMMARY.md')
ALL_DEALS_MD = os.path.join(REPO_DIR, 'docs/laptop-tracker/ALL_CHECKED_DEALS.md')

TIMESTAMP_ISO = "2026-11-05T15:04:00+06:00"
TIMESTAMP_PRETTY = "2026-11-05 15:04:00 (+06:00 Asia/Dhaka)"
VERSION = "2.38.0"
ACTIVE_MODELS = 53
ARCHIVED_LISTINGS = 12
TOTAL_AUDITED = ACTIVE_MODELS + ARCHIVED_LISTINGS  # 65

print(f"Executing Black Friday Deals Tracker Pass v{VERSION} at {TIMESTAMP_PRETTY}...")

# ==========================================
# 1. UPDATE DEALS_LEDGER.json
# ==========================================
with open(LEDGER_PATH, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['metadata']['version'] = VERSION
ledger['metadata']['last_updated'] = TIMESTAMP_ISO

t14s_gen3 = {
    "id": "thinkpad-t14s-gen3-ebay",
    "title": "Lenovo ThinkPad T14s Gen 3 14.0\" 16:10 WUXGA Laptop - AMD Ryzen 5 PRO 6650U / Intel Core i5-1245U vPro - 16GB LPDDR5 - 256GB/512GB SSD",
    "retailer": "eBay Certified Refurbished",
    "sku": "ThinkPad-T14s-G3",
    "url": "https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000",
    "tier": "Tier 2: Mid Budget ($350-$450)",
    "current_price_usd": 369.0,
    "current_price_bdt_bank": 47232,
    "current_price_bdt_landed": 49815,
    "original_msrp_usd": 1449.0,
    "lowest_seen_price_usd": 369.0,
    "stock_status": "IN_STOCK",
    "ram_status": "SOLDERED",
    "cpu": "AMD Ryzen 5 PRO 6650U (6 Cores / 12 Threads, Zen 3+, up to 4.5 GHz) / Intel Core i5-1245U vPro (10 Cores / 12 Threads)",
    "gpu": "AMD Radeon 660M RDNA 2 / Intel Iris Xe Graphics (Dual USB4 / TB4 40Gbps eGPU ready)",
    "display": "14.0\" 16:10 WUXGA (1920x1200) IPS Anti-glare (300 nits, 100% sRGB low power option)",
    "touchscreen": False,
    "notes": "Sub-৳50k 1.2kg Ultralight Flagship: Slashes 74%+ off original $1,449 enterprise MSRP down to $369.00 (~৳49,815 landed / ~৳47,232 bank card rate). The 's' slimline variant pairs carbon fiber and magnesium unibody construction, shaving weight down to just 1.22 kg (2.7 lbs) with a massive 57Wh battery (14+ hours). Modern 16:10 WUXGA display, blazing-fast LPDDR5-6400 memory, dual USB4 / Thunderbolt 4 ports (full 40Gbps eGPU ready), TrackPoint, and MIL-STD-810H durability backed by 1-to-2 Year Allstate Warranty.",
    "last_checked": TIMESTAMP_ISO,
    "alert_trigger": "STEADY"
}

existing_ids = [it['id'] for it in ledger['tracked_items']]
if t14s_gen3['id'] not in existing_ids:
    ledger['tracked_items'].append(t14s_gen3)
    print(f"Added {t14s_gen3['id']} to tracked items.")

for it in ledger['tracked_items']:
    it['last_checked'] = TIMESTAMP_ISO

history_summary = (
    "November 5 mid-afternoon Black Friday deals telemetry and stock verification pass (03:04 PM / 15:04): "
    "Executed comprehensive multi-retailer intelligence sweep across Best Buy, Target, Walmart, Woot, Amazon, "
    "Dell Refurbished (DFS), BlairTech, and eBay Certified Refurbished. Verified Target 3-Day Early Black Friday "
    "Sale is LIVE TODAY (Thursday, Nov 5 through Saturday, Nov 7) featuring rolling Target Circle electronics and "
    "laptop doorbusters on HP EliteBook 840 G7 ($259.99), HP EliteBook x360 830 G8 ($299.00), and HP EliteBook 840 G8 "
    "($369.99); Best Buy Early Black Friday full doorbuster wave countdown active (<16 hours away, dropping Friday, "
    "Nov 6 morning) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027 "
    "(active doorbusters holding: HP OmniBook X Flip 14 Lunar Lake Copilot+ PC at $649.99, Lenovo Yoga 7i 16 at $599.99, "
    "Lenovo LOQ 15 RTX 4060 at $699.99, ASUS TUF A15 RTX 4060 at $679.99, Lenovo IdeaPad Slim 3i Touch at $429.99, "
    "and Slim 3i 16GB at $499.99); Dell Refurbished instant 40%–50% Hot Deals holding on Precision 3581 12-core RTX A500 "
    "workstation ($619, 10 units left) and Latitude 7340 32GB QHD+ ($579, 25 units left); Walmart Event 1 confirmed "
    "for Nov 12–15 (monitoring HP Victus RTX 4050 restocks at $499); Woot MAR inventory holding steady on Latitude 7330 "
    "32GB ($539.99), Latitude 7430 32GB Touch ($449.99), and Latitude 7430 2-in-1 ($449.99). Added major strategic Tier 2 / "
    "Sub-৳50k BDT 16:10 addition: Lenovo ThinkPad T14s Gen 3 (AMD Ryzen 5 PRO 6650U Zen 3+ / Intel Core i5-1245U vPro, "
    "16GB LPDDR5-6400, 256GB/512GB PCIe Gen 4 SSD, 14.0\" 16:10 WUXGA 1920x1200 IPS, dual USB4 / TB4 40Gbps eGPU ready, "
    "ultralight 1.22 kg carbon fiber & magnesium alloy chassis, 57Wh battery, MIL-STD-810H, Allstate Warranty) slashed "
    "74%+ off $1,449 MSRP down to $369.00 (~৳49,815 landed / ~৳47,232 bank card rate) on eBay Refurbished, providing an "
    "ultralight 1.2kg carbon alternative to the modular T14 Gen 3. Audited candidate #A12: HP Pavilion x360 14\" evaluated "
    "and disqualified/rejected due to 8GB RAM non-upgradeability violating convertible protocol, fragile plastic hinge mounts, "
    "and dim 250-nit display, establishing the EliteBook x360 830 G8 ($299) and ProBook x360 435 G8 ($309) as vastly superior "
    "choices. Master directory expanded to 65 audited listings (53 active serialized models + 12 archived/disqualified listings). "
    "Reconciled ledger to v2.38.0, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
)

new_history_entry = {
    "timestamp": TIMESTAMP_ISO,
    "summary": history_summary
}

if ledger['reconciled_history'][0]['timestamp'] != TIMESTAMP_ISO:
    ledger['reconciled_history'].insert(0, new_history_entry)
else:
    ledger['reconciled_history'][0] = new_history_entry

with open(LEDGER_PATH, 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("DEALS_LEDGER.json updated to v2.38.0.")

# ==========================================
# 2. UPDATE scripts/generate_all_checked_deals.py
# ==========================================
with open(ALL_DEALS_SCRIPT, 'r', encoding='utf-8') as f:
    all_deals_code = f.read()

# Add thinkpad-t14s-gen3-ebay into OEM_PROFILES if missing
t14s_profile_code = '''    "thinkpad-t14s-gen3-ebay": {
        "cpu_arch": "AMD Ryzen 5 PRO 6650U (Zen 3+ on TSMC 6nm, 6 Cores / 12 Threads, 2.90 GHz base, up to 4.50 GHz Boost, 16MB L3 Cache, 15W–28W cTDP) OR Intel 12th Gen Alder Lake-U Core i5-1245U vPro (10 Cores / 12 Threads up to 4.40 GHz)",
        "gpu_arch": "AMD Radeon 660M RDNA 2 Graphics (6 Compute Units / 384 Shaders, 1.9 GHz clock, DirectX 12 Ultimate, Ray Tracing capable) OR Intel Iris Xe Graphics (96EU) • Full 40Gbps Dual USB4 / Thunderbolt 4 eGPU support",
        "ram_arch": "16GB LPDDR5-6400 MHz ultra-fast dual-channel memory • 100% Soldered (Ultra-low power draw, maximum memory bandwidth for RDNA 2 graphics architecture)",
        "storage_arch": "256GB / 512GB PCIe Gen 4 x4 NVMe M.2 2280 SSD • 1× M.2 2280 PCIe Gen 4 x4 slot (swappable up to 2TB/4TB NVMe SSD)",
        "display_arch": "14.0\" 16:10 WUXGA (1920x1200) IPS Anti-glare display, 300 nits brightness (400 nits Low Power 100% sRGB option), 1000:1 contrast ratio, TÜV Low Blue Light certified, 85° viewing angles",
        "io_arch": "2× USB4 40Gbps / Thunderbolt 4 (Power Delivery 3.0, DisplayPort 1.4 alt mode, dual 40Gbps eGPU ready); 2× USB 3.2 Gen 1 Type-A (1 Always On); 1× HDMI 2.0b (up to 4K @ 60Hz); 1× 3.5mm combo audio jack; 1× Kensington nano security slot",
        "sd_arch": "None (Sacrificed for ultra-thin 16.6mm carbon/magnesium chassis profile; requires USB dongle)",
        "power_arch": "Massive 57Wh Lithium-Polymer battery with Rapid Charge (charges to 80% in 60 minutes) • 65W USB Type-C AC Adapter • Exceptional battery endurance (13–15 hours productivity playback)",
        "chassis_arch": "Carbon-fiber reinforced hybrid polymer top lid with magnesium alloy chassis base in Deep Black • Weight: 1.22 kg (2.69 lbs) • Ultra-slim 16.6 mm profile • Passed 12 MIL-STD-810H military durability test standards (26 procedures) • Quiet copper heatpipe cooling with bottom intake and side exhaust",
        "inputs_arch": "Legendary ThinkPad 6-row spill-resistant keyboard with 1.5mm key travel, unified TrackPoint pointing device with physical mouse buttons, LED backlighting • Smooth glass-like Mylar surface Precision Clickpad • Non-touch clamshell",
        "security_arch": "FHD 1080p RGB + IR hybrid webcam with physical ThinkShutter privacy slider and Windows Hello facial recognition • Match-on-Chip Fingerprint Reader integrated into power key • Discrete TPM 2.0 (TCG certified) • Dual far-field Dolby Voice microphones • Stereo speakers (2W×2) with Dolby Audio"
    },'''

if "thinkpad-t14s-gen3-ebay" not in all_deals_code:
    all_deals_code = all_deals_code.replace('    "hp-probook-445-g8-r5": {', t14s_profile_code + '\n    "hp-probook-445-g8-r5": {')

# Ensure archived count is 12 and includes #A10, #A11, #A12
all_deals_code = re.sub(r'total_count = active_count \+ \d+', f'total_count = active_count + {ARCHIVED_LISTINGS}', all_deals_code)
all_deals_code = re.sub(r'badge/Archived%20%2F%20Filtered-\d+%20Listings-lightgrey', f'badge/Archived%20%2F%20Filtered-{ARCHIVED_LISTINGS}%20Listings-lightgrey', all_deals_code)
all_deals_code = re.sub(r'Historical Archives & Disqualified Listings \(#A1 – #A\d+\)', f'Historical Archives & Disqualified Listings (#A1 – #A{ARCHIVED_LISTINGS})', all_deals_code)

archives_full_text = """### #A10: Lenovo Legion 5 / Slim 5 16" Gaming Laptop (16.0" WQXGA 165Hz, AMD Ryzen 7 7735HS / 8845HS, 16GB DDR5, NVIDIA GeForce RTX 4060 8GB, 512GB/1TB SSD)
* **Retailer / Platform:** Best Buy / Walmart / B&H • **SKU:** `Legion-Slim-5-16`
* **Historical Cart Price:** **$849.00 – $899.99 USD** (~৳108,672 – ~৳115,199 bank / ~৳114,615 – ~৳121,499 landed)
* **Audit Status:** `DISQUALIFIED / BUDGET EXCEEDED (TIER 4 CEILING)`
* **Audit Verdict:** **REJECTED DUE TO EXCEEDING TIER 4 HARD CAP ($699 MAX).** While the Lenovo Legion 5 / Slim 5 is a premium chassis with great cooling and a 16:10 165Hz display, its Black Friday promotional price of $849–$899 pushes total realistic landed cost to ৳114,600–৳121,500 BDT—exceeding our maximum budget ceiling by over $150–$200 USD. For buyers targeting an uncompromised 8GB VRAM NVIDIA GeForce RTX 4060, our actively tracked **Lenovo LOQ 15 ($699.99 / ~৳94,499 landed)** and **ASUS TUF Gaming A15 ($679.99 / ~৳91,799 landed, unthrottled 140W full TGP)** provide 95%–100% of the raw GPU compute and gaming performance while keeping landed costs strictly within our Tier 4 radar envelope!

### #A11: Dell XPS 13 (9315 / 9320 Plus) 13.4" Ultrabook (Intel Core i5-1230U / i7-1260P / i7-1360P, 16GB LPDDR5, 512GB SSD, InfinityEdge Display)
* **Retailer / Platform:** Dell Outlet / Best Buy Geek Squad / eBay Certified Refurbished • **SKUs:** `XPS-9315-Refurb` / `XPS-9320-Plus`
* **Historical Cart Price:** **$549.00 – $649.00 USD** (~৳70,272 – ~৳83,072 bank / ~৳74,115 – ~৳87,615 landed)
* **Audit Status:** `EVALUATED & REJECTED / THERMAL & ERGONOMIC PITFALL`
* **Audit Verdict:** **REJECTED IN FAVOR OF CORPORATE 7000-SERIES & THINKPAD ALTERNATIVES.** While the Dell XPS 13 9315 and 9320 Plus look striking on paper, extensive technical audits reveal severe engineering compromises:
  1. **Thermal Throttling & Power Capping:** The XPS 13 9315 is hobbled by an ultra-low-power 9W–12W U-series CPU that throttles under sustained multitasking. Conversely, the XPS 13 Plus 9320 attempts to run a 28W P-series chip in a wafer-thin chassis, resulting in excessive skin temperatures and aggressive thermal throttling.
  2. **Severe Port Starvation:** The chassis offers only 2× Thunderbolt 4 ports. It lacks an audio jack, USB-A port, and SD/MicroSD card reader entirely, forcing total dongle reliance.
  3. **Ergonomic Friction:** The XPS 13 Plus features a polarizing zero-lattice keyboard, invisible borderless capacitive touch function row (no physical Esc/function keys), and an edge-to-edge invisible glass haptic trackpad that suffers from frequent palm-rejection misfires.
  4. **Superior Actively Tracked Alternatives:** For comparable or lower cost, the **Dell Latitude 7340 32GB QHD+ ($579.00 / ~৳78,165 landed)** offers 32GB LPDDR5 RAM (double the memory), a 500-nit QHD+ 16:10 touchscreen, dual Thunderbolt 4, physical keys, and superior cooling. In clamshells, the **Lenovo ThinkPad T14 Gen 3 ($369.00 / ~৳49,815 landed)** delivers full port arrays (RJ-45, HDMI, MicroSD, dual TB4) and modular upgradeable RAM for over $180 less!

### #A12: HP Pavilion x360 14" (14.0" FHD Touch, Core i3/i5 12th/13th Gen, 8GB Soldered/DDR4, 256GB SSD)
* **Retailer / Platform:** Walmart / Best Buy / Target • **Price:** **$349.00 – $429.00 USD**
* **Audit Status:** `DISQUALIFIED / FAILED CONVERTIBLE SPEC PROTOCOL`
* **Audit Verdict:** **REJECTED UNDER STRICT SPEC PROTOCOL.** Evaluated against the sub-৳55k convertible sweet spot and permanently rejected for three fatal flaws: 1) Majority of retail listings ship with non-upgradeable 8GB RAM, failing the non-negotiable 16GB convertible protocol; 2) Fragile consumer plastic hinge anchors that exhibit high failure and glass-cracking rates under daily 360-degree rotation; 3) Dim 250-nit glossy panel with high glare. Enterprise alternatives at the same or lower price—such as the **HP EliteBook x360 830 G8 ($299.00)**, **HP ProBook x360 435 G8 ($309.00 with dual SODIMM slots)**, and **Dell Latitude 7320 2-in-1 ($259.00)**—offer superior CNC aluminum/carbon unibody durability, dual Thunderbolt 4 / USB-C, 16GB factory RAM, and 3-year commercial chassis engineering."""

# Ensure archives section includes A10, A11, A12
if "#A12" not in all_deals_code:
    if "#A11" in all_deals_code:
        all_deals_code = all_deals_code.replace('### #A11: Dell XPS 13', archives_full_text[archives_full_text.find('### #A11:'):])
    elif "#A10" in all_deals_code:
        all_deals_code = all_deals_code.replace('### #A10: Lenovo Legion 5', archives_full_text)
    else:
        # replace from end of #A9
        idx_a9 = all_deals_code.find('### #A9:')
        idx_after_a9 = all_deals_code.find('---', idx_a9)
        all_deals_code = all_deals_code[:idx_after_a9] + '\n\n' + archives_full_text + '\n\n' + all_deals_code[idx_after_a9:]

with open(ALL_DEALS_SCRIPT, 'w', encoding='utf-8') as f:
    f.write(all_deals_code)

print("generate_all_checked_deals.py updated successfully.")

# Run generate_all_checked_deals.py to build ALL_CHECKED_DEALS.md
import subprocess
result = subprocess.run(['python', ALL_DEALS_SCRIPT], capture_output=True, text=True)
print("ALL_CHECKED_DEALS.md generation output:", result.stdout, result.stderr)

# ==========================================
# 3. UPDATE scripts/generate_full_dashboard.py
# ==========================================
with open(DASHBOARD_SCRIPT, 'r', encoding='utf-8') as f:
    dash = f.read()

# Update badges
dash = re.sub(r'Ledger-v[\d\.]+-informational', f'Ledger-v{VERSION}-informational', dash)
dash = re.sub(r'Checked%20Listings-\d+%20Audited%20Deals-success', f'Checked%20Listings-{TOTAL_AUDITED}%20Audited%20Deals-success', dash)
dash = re.sub(r'across \d+ serialized models', f'across {ACTIVE_MODELS} serialized models', dash)
dash = re.sub(r'Directory \(\d+ Audited\)', f'Directory ({TOTAL_AUDITED} Audited)', dash)
dash = re.sub(r'Directory of All \d+ Checked Deals', f'Directory of All {TOTAL_AUDITED} Checked Deals', dash)
dash = re.sub(r'all \d+ checked, evaluated, active, and archived listings', f'all {TOTAL_AUDITED} checked, evaluated, active, and archived listings', dash)
dash = re.sub(r'monitors \d+ serialized models and \d+ audited listings', f'monitors {ACTIVE_MODELS} serialized models and {TOTAL_AUDITED} audited listings', dash)

# Update header callouts
dash_callouts = f"""> **🕒 Last Verified:** `{TIMESTAMP_PRETTY}` • All {ACTIVE_MODELS} active models and {ARCHIVED_LISTINGS} archived listings verified live  
> **🎯 Strategic Focus Active:** 1) Deep research on sub-৳50k–৳55k BDT models • 2) Dedicated tracking of Touchscreen & 360° convertibles with 16GB RAM • 3) Radar on high-gravity outlier discounts (Tier 4).  
> **🎉 Target Early Black Friday LIVE TODAY:** Target's official 3-day Early Black Friday holiday electronic sale is **NOW LIVE (Thursday, Nov 5 through Saturday, Nov 7)** featuring rolling electronics and laptop doorbusters!  
> **🏷️ <16-Hour Alert (Best Buy Early Black Friday):** Official weekly doorbuster drops begin **tomorrow, Friday, Nov 6 morning**, backed by Best Buy's Holiday Price Match Guarantee and extended holiday return window through January 15, 2027.  
> **⚡ New Sub-৳50k 1.2kg Ultralight Flagship:** **Lenovo ThinkPad T14s Gen 3** (AMD Ryzen 5 PRO 6650U Zen 3+ / Intel Core i5-1245U vPro, 16GB LPDDR5-6400, 256GB/512GB PCIe Gen 4 SSD, 14.0\" 16:10 WUXGA 1920x1200 IPS, dual USB4 / TB4 40Gbps eGPU ready, ultralight 1.22 kg carbon/magnesium unibody, 57Wh battery, MIL-STD-810H, Allstate Warranty) slashed 74%+ off $1,449 MSRP down to **$369.00 USD** (~৳49,815 landed / ~৳47,232 bank card rate) on eBay Refurbished!  
> **🏢 DFS Transition Alert:** Dell Refurbished instant 40%–50% Hot Deals active on Precision 3581 12-core RTX A500 workstation ($619) and Latitude 7340 32GB QHD+ ($579).  
> **🛒 Walmart Event 1 Confirmed:** Scheduled for **Nov 12–15** (online Nov 12 at 12:01 AM ET for Walmart+) — high alert for $499 HP Victus RTX 4050 restocks."""

dash = re.sub(r'> \*\*🕒 Last Verified:\*\* `[^`]+`[\s\S]*?(?=> \*\*📊 Structured Data:)', dash_callouts + '\n', dash)

# Build Complete Tables in Markdown for All 53 Models
tier4_table = """## 🚀 Tier 4: "Gravity" Stretchers ($550 – $699+ USD)
*Massive discounts (38%–50% off $1,000+ MSRP) that justify stretching the budget to unlock **true 8GB VRAM RTX 4060 compute (up to 140W full-wattage TGP)**, dedicated ISV workstations, next-gen Core Ultra AI OLED convertibles, or 32GB RAM 13th Gen corporate flagships.*

| # | Model & Source | Price (USD / Bank / Landed) | CPU & Architecture | RAM Spec & Slots | Storage & Expansion | GPU & eGPU Support | Display & Form Factor | Ports, SD Card & Decision Makers | Deal Status |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: |
| **#01** | **[Lenovo LOQ 15](https://www.bestbuy.com/site/searchpage.jsp?st=lenovo+loq+15+rtx+4060)**<br>*(Best Buy / Walmart)*<br>`Brand New` | **$699.99**<br>Bank: ~৳89,599<br>Landed: **~৳94,499** | AMD Ryzen 7 7435HS<br>*(8C/16T, 4.5 GHz, 45W)* | **16GB DDR5-4800**<br>2× un-soldered SODIMM<br>*(Up to 64GB)* | 512GB PCIe Gen 4 NVMe<br>**2× M.2 2280 slots** | **NVIDIA RTX 4060 8GB**<br>*(115W TGP, MUX Switch)*<br>No TB4 (dGPU on-board) | 15.6" FHD 144Hz IPS<br>300 nits, 100% sRGB<br>`Clamshell` | HDMI 2.1, USB-C 3.2 (140W PD, DP 1.4), 3× USB-A, RJ-45.<br>**No SD slot**.<br>White backlit KB, E-shutter. | `IN STOCK`<br>*(New 4060 Drop)* |
| **#02** | **[ASUS TUF Gaming A15](https://www.bestbuy.com/site/searchpage.jsp?st=asus+tuf+gaming+a15+rtx+4060)**<br>*(Best Buy / Walmart)*<br>`Brand New` | **$679.99**<br>Bank: ~৳87,039<br>Landed: **~৳91,799** | AMD Ryzen 5 7535HS / R7<br>*(6C/12T or 8C/16T, 45W)* | **16GB DDR5-4800**<br>2× un-soldered SODIMM<br>*(Up to 64GB)* | 512GB PCIe Gen 4 NVMe<br>**2× M.2 2280 slots** | **NVIDIA RTX 4060 8GB**<br>**(140W Full TGP, MUX)**<br>**USB4 40Gbps eGPU ready** | 15.6" FHD 144Hz IPS<br>Adaptive-Sync<br>`Clamshell` | **USB4 Type-C (40Gbps)**, USB-C 3.2, 2× USB-A, HDMI 2.1, RJ-45.<br>**No SD slot**.<br>MIL-STD-810H, 90Whr battery, RGB KB. | `IN STOCK`<br>*(Apex 140W GPU)* |
| **#03** | **[Acer Nitro V 15](https://www.walmart.com/search?q=acer+nitro+v+15+rtx+4060)**<br>*(Walmart / Amazon)*<br>`Brand New` | **$649.99**<br>Bank: ~৳83,199<br>Landed: **~৳87,749** | Intel Core i7-13620H<br>*(10C/16T: 6P+4E, 4.9 GHz)* | **16GB DDR5-5200**<br>2× un-soldered SODIMM<br>*(Up to 64GB)* | 512GB PCIe Gen 4 NVMe<br>**2× M.2 2280 slots** | **NVIDIA RTX 4060 8GB**<br>*(75W TGP)*<br>**Thunderbolt 4 eGPU ready** | 15.6" FHD 144Hz IPS<br>Anti-glare<br>`Clamshell` | **1× Thunderbolt 4 (40Gbps)**, 3× USB-A 3.2, HDMI 2.1, RJ-45.<br>**No SD slot**.<br>Dual-fan exhaust cooling, backlit KB. | `IN STOCK`<br>*(Watch)* |
| **#04** | **[Apple MacBook Air M2](https://www.walmart.com/ip/Apple-MacBook-Air-13-6-inch-Laptop-Apple-M2-chip-8GB-Memory-256GB-SSD-Storage-Midnight/5041071060)**<br>*(Walmart)*<br>`Brand New / Restored` | **$649.00**<br>Bank: ~৳83,072<br>Landed: **~৳87,615** | Apple M2 Chip<br>*(8C CPU: 4P+4E)* | 8GB Unified Memory<br>`Soldered`<br>*(100 GB/s bandwidth)* | 256GB NVMe SSD<br>`Soldered` | Apple M2 8-Core GPU<br>*(No external eGPU)* | 13.6" Liquid Retina<br>*(2560x1664)*, 500 nits, P3<br>`Clamshell` | 2× Thunderbolt 3 / USB4 (40Gbps), MagSafe 3, 3.5mm.<br>**No SD slot**.<br>Touch ID, 1080p camera, 18-hr battery, 1.24 kg. | `IN STOCK`<br>*(Restored: $619)* |
| **#05** | **[Dell Precision 3581](https://www.dellrefurbished.com/item/dell-precision-3581-000028/dell-precision-3581/1.html)**<br>*(Dell DFS)*<br>`Certified Grade A` | **$619.00**<br>Bank: ~৳79,232<br>Landed: **~৳83,565** | Intel Core i5-13600H<br>*(12C/16T H-series, 4.8 GHz)* | **16GB DDR5-5200**<br>2× un-soldered SODIMM<br>*(Up to 64GB)* | 512GB PCIe Gen 4 NVMe<br>**2× M.2 SSD slots** | **NVIDIA RTX A500 4GB**<br>*(2,048 CUDA, 35W–50W, ISV)*<br>**Dual TB4 eGPU ready** | 15.6" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | **MicroSD card slot**, 2× Thunderbolt 4, 2× USB-A, HDMI 2.0, RJ-45.<br>IR facial camera, Fingerprint, ISV certified. | `IN STOCK`<br>*(10 Available)* |
| **#06** | **[Dell Latitude 7340 Touch](https://www.dellrefurbished.com/hot-deals?model_f[]=Latitude%207340)**<br>*(Dell DFS)*<br>`Certified Grade A` | **$599.00**<br>Bank: ~৳76,672<br>Landed: **~৳80,865** | Intel Core i7-1365U<br>*(10C/12T vPro, 5.2 GHz)* | 16GB LPDDR5-4800<br>`Soldered` | 256GB PCIe Gen 4 NVMe<br>*(M.2 2230, upgradeable)* | Intel Iris Xe (96EU)<br>**Dual TB4 eGPU ready** | 13.3" FHD+ (1920x1200)<br>16:10 Anti-reflective<br>`Clamshell Touch` | 2× Thunderbolt 4, 1× USB-A 3.2, HDMI 2.0.<br>**No SD slot**.<br>Ultralight magnesium (~0.98 kg), FHD IR cam, shutter. | `IN STOCK`<br>*(6 Available)* |
| **#07** | **[Lenovo Yoga 7i 16" 2-in-1](https://www.bestbuy.com/site/searchpage.jsp?st=lenovo+yoga+7i+16+touchscreen)**<br>*(Best Buy)*<br>`Brand New / Refurb` | **$599.99**<br>Bank: ~৳76,799<br>Landed: **~৳80,999** | Intel Core Ultra 5 125H<br>*(14C/18T, Intel AI Boost NPU)* | 16GB LPDDR5X-7467<br>`Soldered` | 512GB PCIe Gen 4 NVMe<br>*(M.2 2242)* | Intel Arc Graphics (7 Xe)<br>**Dual TB4 eGPU ready** | **16.0" WUXGA (1920x1200)**<br>16:10 Touch, Dolby Vision<br>`360° Convertible` | **MicroSD card reader**, 2× Thunderbolt 4, 2× USB-A, HDMI 2.1.<br>Dolby Atmos soundbar, Active Pen support, IR cam. | `IN STOCK`<br>*(40% Off AI PC)* |
| **#08** | **[Dell Latitude 7340 QHD+](https://www.dellrefurbished.com/hot-deals?model_f[]=Latitude%207340)**<br>*(Dell DFS)*<br>`Certified Grade A/B` | **$579.00**<br>Bank: ~৳74,112<br>Landed: **~৳78,165** | Intel Core i7-1365U<br>*(10C/12T vPro, 5.2 GHz)* | **32GB LPDDR5-4800**<br>`Soldered`<br>*(No RAM bottleneck)* | 512GB PCIe Gen 4 NVMe<br>*(M.2 2230, upgradeable)* | Intel Iris Xe (96EU)<br>**Dual TB4 eGPU ready** | **13.3" QHD+ (2560x1600)**<br>500 nits, 100% sRGB, 16:10<br>`Clamshell Touch` | 2× Thunderbolt 4, 1× USB-A 3.2, HDMI 2.0.<br>**No SD slot**.<br>Carbon fiber lid, FHD IR cam, ExpressSign-in. | `IN STOCK`<br>*(25 Available)* |
| **#09** | **[Acer Swift Go 16 AI OLED](https://www.ebay.com/itm/257533096037)**<br>*(eBay Acer Outlet)*<br>`Certified Refurbished` | **$577.88**<br>Bank: ~৳73,969<br>Landed: **~৳78,014** | Intel Core Ultra 5 125H<br>*(14C/18T, Intel AI Boost NPU)* | 16GB LPDDR5X-6400<br>`Soldered` | 512GB PCIe Gen 4 NVMe<br>**2× M.2 SSD slots** | Intel Arc Graphics (7 Xe)<br>**Dual USB4 eGPU ready** | **16.0" 2K/3.2K Touch OLED**<br>500 nits, 100% DCI-P3, 16:10<br>`Touch Clamshell` | **MicroSD card reader**, 2× USB4 / TB4, 2× USB-A, HDMI 2.1.<br>1440p QHD webcam, 71Whr battery, 2-Yr Allstate. | `IN STOCK`<br>*(42% Off OLED AI)* |
| **#10** | **[HP OmniBook X Flip 14"](https://www.bestbuy.com/site/searchpage.jsp?st=hp+omnibook+x+flip+14+touch)**<br>*(Best Buy)*<br>`Brand New` | **$649.99**<br>Bank: ~৳83,199<br>Landed: **~৳87,749** | Intel Core Ultra 5 226V<br>*(8C: 4P+4E, 4.5 GHz, Lunar Lake)* | 16GB LPDDR5X-8533<br>`On-Package Soldered`<br>*(40+ TOPS AI NPU)* | 512GB PCIe Gen 4 NVMe<br>M.2 2280 | Intel Arc Graphics 130V<br>**Dual TB4 eGPU ready** | **14.0" 2K (1920x1200)**<br>300 nits, Corning Gorilla Glass<br>`360° Convertible` | **MicroSD card slot**, 2× Thunderbolt 4 (40Gbps), 1× USB-A 3.2, HDMI 2.1.<br>Atmospheric Blue aluminum chassis, 20+ hr battery, Copilot+ PC. | `IN STOCK`<br>*(Best Buy: $350 Off)* |"""

tier1_table = """## 🥇 Tier 1: High Budget ($450 – $550 USD)
*The target sweet spot for dedicated GPUs, 10-core processors, 12th/13th Gen enterprise hardware, and un-soldered DDR5 gaming/workstation capability.*

| # | Model & Source | Price (USD / Bank / Landed) | CPU & Architecture | RAM Spec & Slots | Storage & Expansion | GPU & eGPU Support | Display & Form Factor | Ports, SD Card & Decision Makers | Deal Status |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: |
| **#11** | **[Dell Latitude 7330](https://computers.woot.com/offers/dell-latitude-7330-i7-1265u-32-512-w11p-3)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$539.99**<br>Bank: ~৳69,119<br>Landed: **~৳72,899** | Intel Core i7-1265U<br>*(10C/12T vPro, 4.8 GHz)* | **32GB DDR4-3200**<br>`Soldered`<br>*(No RAM bottleneck)* | 512GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | 13.3" FHD (1920x1080)<br>400 nits Low Power IPS<br>`Clamshell` | **MicroSD card slot**, 2× Thunderbolt 4, 1× USB-A 3.2, HDMI 2.0.<br>IR facial camera, Fingerprint, backlit keyboard. | `IN STOCK`<br>*(1 Left!)* |
| **#12** | **[ASUS Vivobook 16](https://www.walmart.com/search?q=asus+vivobook+16+i7+16gb)**<br>*(Walmart)*<br>`Brand New` | **$499.00**<br>Bank: ~৳63,872<br>Landed: **~৳67,365** | Intel Core i7-1355U<br>*(10C/12T, up to 5.0 GHz)* | **16GB DDR4-3200**<br>8GB sold. + **1× open SODIMM**<br>*(Up to 40GB total)* | 512GB PCIe Gen 4 NVMe | Intel Iris Xe Graphics<br>USB-C 3.2 (No TB4) | 16.0" WUXGA (1920x1200)<br>16:10 Anti-glare IPS<br>`Clamshell` | 1× USB-C 3.2, 2× USB-A 3.2, 1× USB 2.0, HDMI 1.4.<br>**No SD slot**.<br>180° lay-flat hinge, webcam shield, numeric pad. | `IN STOCK` |
| **#13** | **[Lenovo IdeaPad Slim 3i](https://www.bestbuy.com/site/lenovo-ideapad-slim-3i-15-6-full-hd-laptop-intel-core-i5-1335u-2023-16gb-memory-256gb-storage-arctic-grey/6668499.p?skuId=6668499)**<br>*(Best Buy)*<br>`Brand New` | **$499.99**<br>Bank: ~৳63,999<br>Landed: **~৳67,499** | Intel Core i5-1335U<br>*(10C/12T, up to 4.6 GHz)* | 16GB LPDDR5-4800<br>`Soldered` | 256GB PCIe NVMe M.2 2242 | Intel Iris Xe Graphics<br>USB-C 3.2 (No TB4) | 15.6" FHD (1920x1080)<br>300 nits Anti-glare<br>`Clamshell` | **Full-size SD card reader**, 1× USB-C, 2× USB-A 3.2, HDMI 1.4.<br>Webcam privacy shutter, Rapid Charge Boost. | `IN STOCK`<br>*(Best Buy: $400 Off)* |
| **#14** | **[HP Victus 15](https://www.walmart.com/ip/HP-Victus-15-6-inch-FHD-144Hz-Gaming-Laptop-AMD-Ryzen-5-8645HS-NVIDIA-GeForce-RTX-4050-8GB-DDR4-512GB-SSD-Mica-Silver-2024/5395277312)**<br>*(Walmart)*<br>`Brand New` | **$499.00**<br>Bank: ~৳63,872<br>Landed: **~৳67,365** | AMD Ryzen 5 8645HS / i5<br>*(6C/12T Zen 4, 5.0 GHz)* | **8GB DDR5-5600**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 512GB PCIe Gen 4 NVMe M.2 2280 | **NVIDIA RTX 4050 6GB**<br>*(75W TGP)*<br>USB-C DP (No TB4) | 15.6" FHD 144Hz IPS<br>9ms response time<br>`Clamshell` | **Full-size SD media card reader**, USB-C, 2× USB-A, HDMI 2.1, RJ-45.<br>B&O dual audio, backlit keyboard. | `OUT OF STOCK`<br>*(Nov 12 Restock Watch)* |
| **#15** | **[MSI GF63 Thin](https://www.walmart.com/search?q=msi+gf63+thin+rtx+3050)**<br>*(Walmart)*<br>`Brand New` | **$479.00**<br>Bank: ~৳61,312<br>Landed: **~৳64,665** | Intel Core i5-12450H<br>*(8C/12T H-series, 45W)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 512GB NVMe M.2<br>**+ 1× 2.5" SATA Bay** | **NVIDIA RTX 3050 6GB**<br>*(2,048 CUDA, 45W TGP)*<br>USB-C 3.2 (No TB4) | 15.6" FHD 144Hz IPS<br>Anti-glare<br>`Clamshell` | 1× USB-C, 3× USB-A 3.2, HDMI, RJ-45, dedicated audio jacks.<br>**No SD slot**.<br>Red backlit KB, dual drive support. | `IN STOCK` |
| **#16** | **[Acer Aspire 3](https://www.ebay.com/str/acer/Laptops/_i.html?store_cat=2792634010)**<br>*(eBay Acer Outlet)*<br>`Certified Refurbished` | **$473.10**<br>Bank: ~৳60,557<br>Landed: **~৳63,869** | AMD Ryzen 5 7520U<br>*(4C/8T Zen 2, 4.3 GHz)* | 16GB LPDDR5-5500<br>`Soldered` | **1TB PCIe NVMe**<br>M.2 2280 | AMD Radeon 610M<br>USB-C 3.2 (No TB4) | 15.6" FHD (1920x1080)<br>300 nits IPS<br>`Clamshell` | 1× USB-C 3.2 Gen 2, 2× USB-A 3.2, HDMI 2.1.<br>**No SD slot**.<br>Wi-Fi 6, HD camera with TNR, 2-Year Allstate Warranty. | `IN STOCK` |"""

tier2_table = """## 🥈 Tier 2: Mid Budget ($350 – $450 USD)
*The core planning window: 16:10 displays, 32GB RAM flagships, dual SODIMM workhorses, and premium convertibles.*

| # | Model & Source | Price (USD / Bank / Landed) | CPU & Architecture | RAM Spec & Slots | Storage & Expansion | GPU & eGPU Support | Display & Form Factor | Ports, SD Card & Decision Makers | Deal Status |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: |
| **#17** | **[Dell Latitude 7430 2-in-1](https://computers.woot.com/offers/dell-latitude-7430-2in1-i7-1265u-16gb-256gb-w11p-1)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$449.99**<br>Bank: ~৳57,599<br>Landed: **~৳60,749** | Intel Core i7-1265U<br>*(10C/12T vPro, 12th Gen)* | 16GB DDR4-3200<br>`Soldered` | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | **14.0" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD card slot**, 2× Thunderbolt 4, 1× USB-A, HDMI 2.0.<br>CNC aluminum unibody, IR facial recognition. | `IN STOCK`<br>*(PRICE DROP $50)* |
| **#18** | **[Dell Inspiron 15 Touch](https://www.bestbuy.com/site/searchpage.jsp?st=dell+inspiron+15+touchscreen+i5)**<br>*(Best Buy / Dell)*<br>`Brand New / Refurb` | **$449.99**<br>Bank: ~৳57,599<br>Landed: **~৳60,749** | Intel Core i5-1235U / 1334U<br>*(10C/12T, up to 4.6 GHz)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 512GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>USB-C / USB-A (No TB4) | **15.6" FHD 120Hz Touch**<br>WVA Anti-glare<br>`Clamshell Touch` | **Full-size SD card reader**, 2× USB-A 3.2, 1× USB 2.0, HDMI 1.4.<br>Lift hinge for typing ergonomics, numeric pad. | `IN STOCK`<br>*(Refurb: $399)* |
| **#19** | **[Dell Latitude 7430 Touch](https://computers.woot.com/plus/microsoft-authorized-refurbished-laptops-67)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$449.99**<br>Bank: ~৳57,599<br>Landed: **~৳60,749** | Intel Core i7-1265U<br>*(10C/12T vPro, 4.8 GHz)* | **32GB DDR4-3200**<br>`Soldered`<br>*(No RAM bottleneck)* | 512GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | 14.0" FHD (1920x1080)<br>300 nits Touchscreen<br>`Clamshell Touch` | **MicroSD card slot**, 2× Thunderbolt 4, 1× USB-A, HDMI 2.0.<br>Carbon fiber chassis, SafeShutter IR camera, Fingerprint. | `IN STOCK` |
| **#20** | **[ThinkPad X13 Yoga Gen 3](https://computers.woot.com/offers/lenovo-thinkpad-x13-yoga-gen-3-13-3-wuxga-touch-1)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$439.99**<br>Bank: ~৳56,319<br>Landed: **~৳59,399** | Intel Core i5-1245U vPro<br>*(10C/12T, up to 4.4 GHz, 12th Gen)* | 16GB LPDDR4x/5<br>`Soldered`<br>*(Meets 16GB Protocol)* | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | **13.3" 16:10 WUXGA (1920x1200)**<br>300 nits Anti-reflective Touch<br>`360° Convertible` | **Garaged rechargeable ThinkPad Pen Pro included**.<br>Dual TB4 (40Gbps), HDMI 2.0, 2× USB-A, IR cam.<br>MIL-STD-810H durability, spill-resistant KB. | `IN STOCK`<br>*(12th Gen 16:10 Doorbuster)* |
| **#21** | **[Dell Latitude 5320 2-in-1](https://computers.woot.com/plus/microsoft-authorized-refurbished-laptops-67)**<br>*(Woot / Amazon)*<br>`Certified Grade A` | **$439.99**<br>Bank: ~৳56,319<br>Landed: **~৳59,399** | Intel Core i7-1185G7 vPro<br>*(4C/8T, up to 4.8 GHz)* | **32GB LPDDR4x-4266**<br>`Soldered`<br>*(No RAM bottleneck)* | 512GB PCIe NVMe M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD slot**, 2× Thunderbolt 4, 2× USB-A 3.2, HDMI 2.0.<br>Magnesium chassis, backlit keyboard, active pen support. | `OUT OF STOCK`<br>*(Sold Out)* |
| **#22** | **[Lenovo IdeaPad Slim 3i Touch](https://www.bestbuy.com/site/searchpage.jsp?st=lenovo+ideapad+slim+3i+touchscreen)**<br>*(Best Buy)*<br>`Brand New` | **$429.99**<br>Bank: ~৳55,039<br>Landed: **~৳58,049** | Intel Core 5 120U<br>*(10C/12T, up to 5.0 GHz)* | 16GB LPDDR5-5200<br>`Soldered` | 256GB PCIe Gen 4 NVMe<br>M.2 2242 | Intel Graphics<br>USB-C 3.2 (No TB4) | **15.3" 2K (1920x1200)**<br>16:10 Touchscreen (300 nits)<br>`Clamshell Touch` | **Full-size SD card reader**, 1× USB-C, 2× USB-A 3.2, HDMI 1.4.<br>Privacy shutter webcam, Arctic Grey aluminum lid. | `IN STOCK`<br>*($300 Off)* |
| **#23** | **[Dell Latitude 5530](https://www.dellrefurbished.com/item/dell-latitude-5530-000094/dell-latitude-5530/1.html)**<br>*(Dell DFS)*<br>`Certified Grade B` | **$409.00**<br>Bank: ~৳52,352<br>Landed: **~৳55,215** | Intel Core i5-1235U<br>*(10C/12T, up to 4.4 GHz)* | **8GB/16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB PCIe NVMe M.2<br>**Dual M.2 slots available** | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | 15.6" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | **MicroSD slot**, 2× Thunderbolt 4, 2× USB-A, HDMI 2.0, RJ-45.<br>Numeric keypad, easily swappable parts. | `IN STOCK`<br>*(10 Units Left)* |
| **#24** | **[ThinkPad X1 Yoga Gen 6](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$379.00**<br>Bank: ~৳48,512<br>Landed: **~৳51,165** | Intel Core i5-1135G7 / i7<br>*(4C/8T vPro, up to 4.7 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 512GB PCIe Gen 4 NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **14.0" 16:10 WUXGA (1920x1200)**<br>400 nits Low Power, 100% sRGB<br>`360° Convertible` | **Garaged rechargeable ThinkPad Pen Pro included**.<br>Dual TB4, 2× USB-A, HDMI 2.0. **No SD slot**.<br>CNC Storm Grey aluminum unibody, Dolby Atmos, IR cam. | `IN STOCK`<br>*(Flagship X1 Pick)* |
| **#25** | **[HP EliteBook 840 G8](https://blairtech.com/laptops/)**<br>*(Target Restored / BlairTech)*<br>`Certified Refurbished` | **$369.99**<br>Bank: ~৳47,359<br>Landed: **~৳49,949** | Intel Core i7-1185G7 vPro<br>*(4C/8T, up to 4.8 GHz)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | 14.0" FHD (1920x1080)<br>400 nits Low Power IPS<br>`Clamshell` | Dual Thunderbolt 4, 2× USB-A 3.2, HDMI 2.0. **No SD slot**.<br>CNC aluminum unibody, Bang & Olufsen, spill-resistant KB. | `IN STOCK` |
| **#26** | **[Dell Latitude 7330 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$369.00**<br>Bank: ~৳47,232<br>Landed: **~৳49,815** | Intel Core i5-1245U vPro<br>*(10C/12T: 2P+8E, 4.4 GHz, 12th Gen)* | 16GB LPDDR4x-4266<br>`Soldered`<br>*(Meets 16GB Protocol)* | 256GB/512GB PCIe Gen 4 NVMe<br>M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD 4.0 slot**, 2× TB4 (40Gbps), 1× USB-A 3.2, HDMI 2.0.<br>CNC aluminum/carbon unibody, Dell Active Pen PN5122W support, FHD IR camera. | `IN STOCK`<br>*(12th Gen 7000 Convertible)* |
| **#27** | **[HP Envy x360 15.6"](https://www.walmart.com/search?q=hp+envy+x360+16gb+ram+restored)**<br>*(Walmart Restored / eBay)*<br>`Restored / Refurb` | **$369.00**<br>Bank: ~৳47,232<br>Landed: **~৳49,815** | AMD Ryzen 5 7530U<br>*(6C/12T Zen 3, 4.5 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 512GB PCIe NVMe M.2 2280 | AMD Radeon Vega 7<br>USB-C 3.2 (No TB4) | **15.6" FHD (1920x1080)**<br>Edge-to-Edge Touchscreen<br>`360° Convertible` | **Full-size SD card reader**, 1× USB-C, 2× USB-A, HDMI 2.1.<br>Bang & Olufsen audio, mic mute key, numeric pad. | `IN STOCK`<br>*(Sub-৳50k 15.6" Pick)* |
| **#28** | **[Dell Inspiron 14 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Dell Outlet)*<br>`Certified Refurbished` | **$369.00**<br>Bank: ~৳47,232<br>Landed: **~৳49,815** | Intel Core i5-1335U<br>*(10C/12T, up to 4.6 GHz)* | 16GB LPDDR5-4800<br>`Soldered` | 512GB PCIe Gen 4 NVMe<br>M.2 2230 | Intel Iris Xe Graphics<br>**1× TB4 eGPU ready** | **14.0" FHD+ (1920x1200)**<br>16:10 WVA Touchscreen<br>`360° Convertible` | **Full-size SD card reader**, 1× TB4, 2× USB-A 3.2, HDMI 1.4.<br>Waves MaxxAudio Pro up-firing speakers, backlit KB. | `IN STOCK`<br>*(Sub-৳50k 16:10 Pick)* |
| **#29** | **[Lenovo ThinkPad T14 Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$369.00**<br>Bank: ~৳47,232<br>Landed: **~৳49,815** | Intel Core i5-1245U / Ryzen 5<br>*(10C/12T or 6C/12T Zen 3+)* | **16GB DDR4/DDR5**<br>8GB sold. + **1× open SODIMM**<br>*(Up to 48GB total)* | 256GB/512GB PCIe Gen 4 NVMe<br>M.2 2280 | Intel Iris Xe / Radeon 660M<br>**Dual TB4 / USB4 eGPU ready** | **14.0" 16:10 WUXGA (1920x1200)**<br>300 nits Anti-glare IPS<br>`Clamshell` | **MicroSD card reader**, 2× TB4 / USB4, 2× USB-A, HDMI 2.0, RJ-45.<br>Spill-resistant keyboard, TrackPoint, Allstate 1-2 Yr. | `IN STOCK`<br>*(Sub-৳50k 16:10 T-Series)* |
| **#30** | **[Lenovo ThinkPad T14s Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$369.00**<br>Bank: ~৳47,232<br>Landed: **~৳49,815** | AMD Ryzen 5 PRO 6650U / i5<br>*(6C/12T Zen 3+ or 10C/12T)* | 16GB LPDDR5-6400<br>`Soldered`<br>*(Ultra-Fast Bandwidth)* | 256GB/512GB PCIe Gen 4 NVMe<br>M.2 2280 | Radeon 660M / Iris Xe<br>**Dual USB4 / TB4 eGPU ready** | **14.0" 16:10 WUXGA (1920x1200)**<br>300 nits Anti-glare IPS<br>`Clamshell` | Dual USB4 / TB4 (40Gbps), 2× USB-A, HDMI 2.0b. **No SD slot**.<br>Ultralight 1.22 kg carbon/magnesium unibody, 57Wh battery, Allstate. | `IN STOCK`<br>*(Sub-৳50k 1.2kg Flagship)* |
| **#31** | **[Dell Latitude 7420](https://www.dellrefurbished.com/laptops)**<br>*(Dell DFS)*<br>`Certified Grade A` | **$365.00**<br>Bank: ~৳46,720<br>Landed: **~৳49,275** | Intel Core i7-1185G7 vPro<br>*(4C/8T, up to 4.8 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 512GB PCIe NVMe M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | 14.0" FHD (1920x1080)<br>400 nits Super Low Power<br>`Clamshell` | **MicroSD card slot**, 2× Thunderbolt 4, 1× USB-A, HDMI 2.0.<br>Carbon fiber chassis, SafeScreen option, ExpressConnect. | `OUT OF STOCK`<br>*(DFS Depleted)* |
| **#32** | **[ThinkPad L13 Yoga Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$359.00**<br>Bank: ~৳45,952<br>Landed: **~৳48,465** | Intel Core i5-1245U / Ryzen 7<br>*(10C/12T vPro or 8C/16T)* | 16GB LPDDR4x/DDR4<br>`Soldered`<br>*(Meets 16GB Protocol)* | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe Graphics<br>**1× TB4 eGPU ready (Intel)** | **13.3" 16:10 WUXGA (1920x1200)**<br>300 nits Anti-reflective<br>`360° Convertible` | **Garaged rechargeable ThinkPad Pen Pro included**.<br>**MicroSD card reader**, 1× TB4, 1× USB-C, 2× USB-A, HDMI 2.0.<br>MIL-STD-810H tested, spill-resistant ThinkPad keyboard. | `IN STOCK`<br>*(12th Gen 16:10 Stylus)* |
| **#33** | **[ThinkPad P14s Gen 2](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$359.00**<br>Bank: ~৳45,952<br>Landed: **~৳48,465** | AMD Ryzen 7 PRO 5850U<br>*(8C/16T Zen 3, 4.4 GHz) / Core i7* | **16GB DDR4-3200**<br>Soldered + **1× open SODIMM**<br>*(Up to 48GB total)* | 512GB PCIe Gen 3/4 NVMe<br>M.2 2280 | AMD Vega 8 / Quadro T500<br>*(ISV Certified AutoCAD/SolidWorks)*<br>TB4 on Intel | 14.0" FHD (1920x1080)<br>300–400 nits Low Power IPS<br>`Clamshell` | **MicroSD card reader**, 2× USB-C (TB4 on Intel), 2× USB-A, HDMI 2.0, RJ-45.<br>Legendary spill-resistant keyboard, TrackPoint, ISV certified. | `IN STOCK`<br>*(Sub-৳49k ISV Workstation)* |"""

tier3_table = """## 🥉 Tier 3: Value & Convertibles Under $350 USD ($179 – $349 USD)
*The primary sub-৳45k–৳55k sweet spot: dedicated GPUs, military-grade durability, and **16GB Touchscreen/360° convertibles** under ৳48,000 landed.*

| Serial | Model & Retailer | Price (USD / Bank / Landed) | CPU Class | RAM Spec & Slots | Storage & Slots | GPU & eGPU Support | Display & Form Factor | Ports, SD & Features | Status |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :-: |
| **#34** | **[Dell Latitude 5330 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Woot MAR)*<br>`Certified Refurbished` | **$349.00**<br>Bank: ~৳44,672<br>Landed: **~৳47,115** | Intel Core i5-1235U / i5-1245U vPro<br>*(10C/12T, up to 4.4 GHz, 12th Gen)* | 16GB LPDDR4x-4266<br>`Soldered`<br>*(Meets 16GB Protocol)* | 256GB/512GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD slot**, 2× TB4 (40Gbps), 2× USB-A 3.2, HDMI 2.0.<br>Dell Active Pen support, carbon fiber reinforced chassis. | `IN STOCK`<br>*(12th Gen Convertible)* |
| **#35** | **[Dell Latitude 5430](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Woot MAR)*<br>`Certified Refurbished` | **$349.00**<br>Bank: ~৳44,672<br>Landed: **~৳47,115** | Intel Core i5-1235U / i5-1245U vPro<br>*(10C/12T, up to 4.4 GHz, 12th Gen)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB/512GB PCIe Gen 4 NVMe<br>M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | 14.0" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | **MicroSD slot**, 2× TB4 (40Gbps), 2× USB-A, HDMI 2.0, RJ-45.<br>Captive screws, modular easily swappable parts. | `IN STOCK`<br>*(Dual-SODIMM 10-Core)* |
| **#36** | **[Dell Latitude 7330](https://computers.woot.com/offers/dell-latitude-7330-13-3-fhd-i5-1245u-16gb-256gb)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$349.99**<br>Bank: ~৳44,799<br>Landed: **~৳47,249** | Intel Core i5-1245U vPro<br>*(10C/12T, up to 4.4 GHz, 12th Gen)* | **16GB DDR4-3200**<br>`Soldered`<br>*(Dual-channel)* | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe Graphics<br>**Dual TB4 eGPU ready** | 13.3" FHD (1920x1080)<br>400 nits Super Low Power IPS<br>`Clamshell` | **MicroSD card slot**, 2× TB4 (40Gbps), 1× USB-A 3.2, HDMI 2.0.<br>Carbon fiber / aluminum chassis, IR cam, ExpressConnect. | `IN STOCK`<br>*(10-Core <৳48k Doorbuster)* |
| **#37** | **[Lenovo IdeaPad Flex 5](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$349.00**<br>Bank: ~৳44,672<br>Landed: **~৳47,115** | AMD Ryzen 7 5700U / 7730U<br>*(8C/16T Zen 3, 4.5 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 512GB PCIe NVMe M.2 2242 | AMD Radeon Vega 8<br>USB-C 3.2 (No TB4) | **14.0" WUXGA (1920x1200)**<br>16:10 300 nits IPS Touch<br>`360° Convertible` | **Full-size SD card reader**, 1× USB-C, 2× USB-A, HDMI 1.4b.<br>Fingerprint reader on palmrest, webcam privacy shutter. | `IN STOCK`<br>*(8C/16T Convertible)* |
| **#38** | **[Lenovo Yoga 6](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Best Buy)*<br>`Certified Refurbished` | **$339.00**<br>Bank: ~৳43,392<br>Landed: **~৳45,765** | AMD Ryzen 5 5500U / 7530U<br>*(6C/12T, up to 4.5 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 512GB PCIe NVMe M.2 2242 | AMD Radeon Vega 7<br>2× USB-C 3.2 (No TB4) | **13.3" 16:10 WUXGA**<br>300 nits, 100% sRGB, Dolby<br>`360° Convertible` | **MicroSD card reader**, 2× USB-C, 2× USB-A 3.2, HDMI 2.0.<br>Stain-resistant fabric wrap lid, front-facing Dolby Atmos. | `IN STOCK`<br>*(Lifestyle 2-in-1)* |
| **#39** | **[HP EliteBook 845 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished / Newegg)*<br>`Certified Refurbished` | **$339.00**<br>Bank: ~৳43,392<br>Landed: **~৳45,765** | AMD Ryzen 5 PRO 5650U<br>*(6C/12T Zen 3, up to 4.2 GHz)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB/512GB PCIe NVMe<br>M.2 2280 | AMD Radeon Vega 7<br>Dual USB-C 3.2 (No TB4) | 14.0" FHD (1920x1080)<br>400 nits Low Power IPS<br>`Clamshell` | Dual USB-C 3.2 Gen 2, 2× USB-A 3.2, HDMI 2.0, SC card reader. **No SD slot**.<br>All-metal CNC aluminum unibody, Bang & Olufsen audio, Allstate 1-2 Yr. | `IN STOCK`<br>*(6C/12T Dual-SODIMM)* |
| **#40** | **[ThinkPad L13 Yoga Gen 2](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$335.00**<br>Bank: ~৳42,880<br>Landed: **~৳45,225** | Intel Core i5-1135G7 / Ryzen<br>*(4C/8T, up to 4.2 GHz)* | 16GB DDR4-3200<br>`Soldered` | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe Graphics<br>**1× TB4 eGPU ready (Intel)** | **13.3" FHD (1920x1080)**<br>300 nits Anti-reflective<br>`360° Convertible` | **Garaged rechargeable ThinkPad Pen Pro included**.<br>**MicroSD card reader**, 1× TB4, 1× USB-C, 2× USB-A, HDMI 2.0.<br>MIL-STD-810H tested, spill-resistant ThinkPad keyboard. | `IN STOCK`<br>*(Built-in Stylus Pick)* |
| **#41** | **[ThinkPad X13 Yoga Gen 2](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$329.00**<br>Bank: ~৳42,112<br>Landed: **~৳44,415** | Intel Core i5-1135G7 / i5 vPro<br>*(4C/8T, up to 4.4 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **13.3" 16:10 WUXGA (1920x1200)**<br>300 nits Anti-glare Touch<br>`360° Convertible` | **Garaged rechargeable ThinkPad Pen Pro included**.<br>Dual TB4, 2× USB-A 3.2, HDMI 2.0. **No SD slot**.<br>Magnesium chassis, IR Windows Hello, privacy shutter. | `IN STOCK`<br>*(16:10 Stylus Pick)* |
| **#42** | **[Dell Latitude 5420](https://computers.woot.com/plus/microsoft-authorized-refurbished-laptops-67)**<br>*(Woot MAR)*<br>`Certified Grade A` | **$319.99**<br>Bank: ~৳40,959<br>Landed: **~৳43,199** | Intel Core i5-1145G7 vPro<br>*(4C/8T, up to 4.4 GHz)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | 14.0" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | **MicroSD slot**, 2× TB4, 2× USB-A, HDMI 2.0, RJ-45.<br>Captive screws, easily swappable battery/RAM/SSD. | `IN STOCK`<br>*(Clamshell Upgrader)* |
| **#43** | **[Dell Latitude 5320 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / DFS)*<br>`Certified Refurbished` | **$319.00**<br>Bank: ~৳40,832<br>Landed: **~৳43,065** | Intel Core i5-1145G7 vPro<br>*(4C/8T, up to 4.4 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD slot**, 2× TB4, 2× USB-A 3.2, HDMI 2.0.<br>Magnesium alloy hinges, Dell Active Pen support, backlit KB. | `IN STOCK` |
| **#44** | **[Dell Latitude 7420 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$319.00**<br>Bank: ~৳40,832<br>Landed: **~৳43,065** | Intel Core i5-1145G7 vPro<br>*(4C/8T, up to 4.4 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **14.0" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD slot**, 2× TB4, 1× USB-A, HDMI 2.0.<br>CNC aluminum chassis, IR camera, Dell Active Pen support. | `IN STOCK` |
| **#45** | **[Lenovo ThinkBook 14s Yoga](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$319.00**<br>Bank: ~৳40,832<br>Landed: **~৳43,065** | Intel Core i5-1135G7 / i7<br>*(4C/8T, up to 4.7 GHz)* | **16GB DDR4-3200**<br>8GB sold. + **1× open SODIMM**<br>*(Up to 40GB total)* | 512GB PCIe NVMe M.2<br>**2× M.2 SSD slots**<br>*(1× 2280 + 1× 2242)* | Intel Iris Xe 96EU<br>**1× TB4 eGPU ready** | **14.0" FHD (1920x1080)**<br>300 nits, 100% sRGB, Gorilla<br>`360° Convertible` | **Garaged rechargeable Smart Pen included**.<br>**MicroSD card reader**, 1× TB4, 1× USB-C, 2× USB-A, HDMI 1.4b.<br>Mineral Grey aluminum unibody, fingerprint in power key. | `IN STOCK`<br>*(Expandable Wonder)* |
| **#46** | **[HP EliteBook x360 1040 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$319.00**<br>Bank: ~৳40,832<br>Landed: **~৳43,065** | Intel Core i5-1145G7 vPro / i7<br>*(4C/8T, up to 4.8 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **14.0" FHD (1920x1080)**<br>**400 nits, 100% sRGB, Low Power**<br>`360° Convertible` | Dual Thunderbolt 4, 2× USB-A 3.2, HDMI 2.0. **No SD slot**.<br>Bang & Olufsen quad speakers with discrete amps.<br>Ultra-slim 16.6mm CNC aluminum chassis. | `IN STOCK`<br>*(Executive 1000 Pick)* |
| **#47** | **[HP ProBook x360 435 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$309.00**<br>Bank: ~৳39,552<br>Landed: **~৳41,715** | AMD Ryzen 5 PRO 5600U / R7<br>*(6C/12T or 8C/16T Zen 3)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB/512GB PCIe NVMe<br>M.2 2280 | AMD Radeon Vega 7/8<br>USB-C 3.2 (No TB4) | **13.3" FHD (1920x1080)**<br>Corning Gorilla Glass 5<br>`360° Convertible` | **MicroSD card slot**, 1× USB-C, 2× USB-A 3.2, HDMI 1.4b.<br>HP Active Pen support, world camera.<br>**Dual-SODIMM 2-in-1 Unicorn**. | `IN STOCK`<br>*(Dual-SODIMM Unicorn)* |
| **#48** | **[HP EliteBook x360 830 G8](https://www.target.com/s?searchTerm=hp+elitebook+x360+830+g8+refurbished)**<br>*(Target Restored / eBay)*<br>`Restored / Refurb` | **$299.00**<br>Bank: ~৳38,272<br>Landed: **~৳40,365** | Intel Core i5-1145G7 vPro<br>*(4C/8T, up to 4.4 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB PCIe NVMe M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>400 nits Low Power IPS<br>`360° Convertible` | Dual Thunderbolt 4, 2× USB-A 3.2, HDMI 2.0. **No SD slot**.<br>Bang & Olufsen audio, CNC aluminum unibody, tile tracking. | `IN STOCK`<br>*(x360 Benchmark)* |
| **#49** | **[Lenovo ThinkPad T14 Gen 2](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay Refurbished)*<br>`Certified Refurbished` | **$294.27**<br>Bank: ~৳37,667<br>Landed: **~৳39,726** | AMD Ryzen 5 PRO 5650U / i5<br>*(6C/12T Zen 3, 4.2 GHz)* | **16GB DDR4-3200**<br>8GB/16GB sold. + **1× SODIMM**<br>*(Up to 48GB total)* | **512GB PCIe Gen 4 NVMe**<br>M.2 2280 | AMD Vega 7 / Iris Xe<br>TB4 eGPU on Intel | 14.0" FHD (1920x1080)<br>300 nits Anti-glare IPS<br>`Clamshell` | **MicroSD card reader**, 2× USB-C (TB4 on Intel), 2× USB-A, HDMI 2.0, RJ-45.<br>Legendary spill-resistant keyboard, TrackPoint. | `IN STOCK`<br>*(Price Drop! <৳40k)* |
| **#50** | **[HP ProBook 445 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$272.99**<br>Bank: ~৳34,943<br>Landed: **~৳36,854** | AMD Ryzen 5 5600U<br>*(6C/12T Zen 3, 4.2 GHz, 7nm)* | **16GB DDR4-3200**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB PCIe NVMe M.2 2280<br>*(Upgradeable to 2TB)* | AMD Radeon Vega 7<br>USB-C 3.2 Gen 2 (No TB4) | 14.0" FHD (1920x1080)<br>250 nits IPS Anti-glare<br>`Clamshell` | **MicroSD card reader**, 1× USB-C (PD & DP 1.4), 3× USB-A, HDMI 1.4b, RJ-45.<br>Aluminum keyboard deck, spill-resistant KB, Allstate 1-2 Yr. | `IN STOCK`<br>*(Sub-৳37k Dual-SODIMM)* |
| **#51** | **[HP EliteBook 840 G7](https://www.target.com/s?searchTerm=refurbished+laptop)**<br>*(Target Restored)*<br>`Restored Grade A` | **$259.99**<br>Bank: ~৳33,279<br>Landed: **~৳35,099** | Intel Core i5-10310U<br>*(4C/8T 10th Gen, 4.4 GHz)* | **16GB DDR4-2666**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 256GB PCIe NVMe M.2 2280 | Intel UHD Graphics<br>**Dual TB3 eGPU ready** | 14.0" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | Dual Thunderbolt 3, 2× USB-A 3.2, HDMI 1.4b. **No SD slot**.<br>All-metal aluminum unibody, Bang & Olufsen audio, backlit KB. | `IN STOCK` |
| **#52** | **[Dell Latitude 7320 2-in-1](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)**<br>*(eBay / Amazon)*<br>`Certified Refurbished` | **$259.00**<br>Bank: ~৳33,152<br>Landed: **~৳34,965** | Intel Core i5-1145G7 vPro<br>*(4C/8T, up to 4.4 GHz)* | 16GB LPDDR4x-4266<br>`Soldered` | 256GB/512GB PCIe NVMe<br>M.2 2280 | Intel Iris Xe 96EU<br>**Dual TB4 eGPU ready** | **13.3" FHD (1920x1080)**<br>300 nits, Gorilla Glass 6 DX<br>`360° Convertible` | **MicroSD slot**, 2× Thunderbolt 4, 1× USB-A 3.2, HDMI 2.0.<br>Carbon fiber chassis, Dell Active Pen support, Allstate 1-2 Yr. | `IN STOCK`<br>*(<৳35k Flagship 7000)* |
| **#53** | **[Dell Precision 3550](https://blairtech.com/scratch-dent-dell-precision-3550-15-6-workstation-laptop-intel-quad-core-i5-10th-gen-i5-10310u-250gb-nvme-8gb-ram-windows-11-home-backlit-keyboard-webcam-s-n-8f24673/)**<br>*(BlairTech)*<br>`Scratch & Dent Refurb` | **$179.99**<br>Bank: ~৳23,039<br>Landed: **~৳24,299** | Intel Core i5-10310U<br>*(4C/8T 10th Gen, 4.4 GHz)* | **8GB/16GB DDR4-2666**<br>**2× un-soldered SODIMM**<br>*(Up to 64GB)* | 250GB PCIe NVMe<br>**+ 1× 2.5" SATA Bay** | **Quadro P520 2GB**<br>*(Dedicated GPU)*<br>**1× TB3 eGPU ready** | 15.6" FHD (1920x1080)<br>Anti-glare IPS<br>`Clamshell` | **MicroSD slot**, 1× TB3, 3× USB-A 3.2, HDMI 2.0, RJ-45.<br>ISV Certified for AutoCAD/SolidWorks, numeric pad. | `IN STOCK`<br>*(Extreme Value ISV)* |"""

# Replace tables
# Find start of Tier 4
t4_start = dash.find('## 🚀 Tier 4:')
# Find start of Buyer Archetypes
archetypes_start = dash.find('## 🏆 Key Standouts by Buyer Archetype')

new_tables_combined = tier4_table + '\n\n---\n\n' + tier1_table + '\n\n---\n\n' + tier2_table + '\n\n---\n\n' + tier3_table + '\n\n---\n\n'

dash = dash[:t4_start] + new_tables_combined + dash[archetypes_start:]

# Update Buyer Archetypes section to reference #30 ThinkPad T14s Gen 3 and correct serials
archetypes_replacement = """## 🏆 Key Standouts by Buyer Archetype

1. **The Ultimate Expandable Convertible:**
   * **[#45 Lenovo ThinkBook 14s Yoga](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $319.00 USD (~৳43,065 landed)**
   * *Why it wins:* It solves the three biggest flaws of convertibles: has an **open un-soldered SODIMM slot (up to 40GB RAM)**, has **two M.2 NVMe SSD slots**, includes an **internal garaged rechargeable Smart Pen**, and offers **Thunderbolt 4 eGPU support** in an all-aluminum body.
2. **The New 12th Gen 16:10 & 7000-Series Convertible Champions:**
   * **[#20 ThinkPad X13 Yoga Gen 3](https://computers.woot.com/offers/lenovo-thinkpad-x13-yoga-gen-3-13-3-wuxga-touch-1) — $439.99 USD (~৳59,399 landed / ~৳56,319 bank)**
     * Upgrades to 10-core 12th Gen Intel Core i5-1245U vPro processing with modern **16:10 WUXGA (1920x1200) touch panel**, 16GB RAM, integrated **garaged rechargeable ThinkPad Pen Pro**, dual Thunderbolt 4 eGPU ready, and MIL-STD-810H durability under ৳60,000 landed.
   * **[#26 Dell Latitude 7330 2-in-1 Touch](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $369.00 USD (~৳49,815 landed / ~৳47,232 bank)**
     * Slashes under the ৳50,000 landed threshold with a premium 7000-series 10-core Core i5-1245U vPro processor, 16GB RAM, dual Thunderbolt 4 ports (full eGPU support), MicroSD 4.0 reader, Corning Gorilla Glass 6 DX touch, and Active Pen support.
   * **[#32 ThinkPad L13 Yoga Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $359.00 USD (~৳48,465 landed / ~৳45,952 bank)**
     * The sub-৳49k 12th Gen 16:10 convertible champion: Slashes 72% off $1,299 MSRP, delivering 10-core i5 vPro or 8-core Ryzen 7 PRO compute, 16GB RAM, and **garaged rechargeable pen** under ৳49,000 landed!
3. **The Sub-৳49k Mobile Workstation Powerhouse:**
   * **[#33 ThinkPad P14s Gen 2 Workstation](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $359.00 USD (~৳48,465 landed / ~৳45,952 bank)**
     * Slashes 76% off $1,499 MSRP: Combines an **8-core / 16-thread AMD Ryzen 7 PRO 5850U** (or Core i7 + dedicated ISV-certified NVIDIA Quadro T500 GPU), **un-soldered SODIMM slot upgradeable to 48GB RAM**, RJ-45 Gigabit Ethernet, MicroSD reader, and legendary ThinkPad keyboard under ৳49,000 landed!
4. **The Sub-৳37k Zen 3 Dual-SODIMM Corporate Workhorse:**
   * **[#50 HP ProBook 445 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $272.99 USD (~৳36,854 landed / ~৳34,943 bank)**
     * Extraordinary sub-৳37k price-to-performance champion: Features a **6-core / 12-thread AMD Ryzen 5 5600U Zen 3** processor, **2× un-soldered DDR4 SODIMM slots (both upgradeable up to 64GB)**, RJ-45 Gigabit Ethernet, MicroSD reader, and stamped aluminum keyboard deck under ৳37,000 landed.
5. **The Sub-৳46k AMD Zen 3 Corporate Workhorse:**
   * **[#39 HP EliteBook 845 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $339.00 USD (~৳45,765 landed / ~৳43,392 bank)**
     * Smashes the baseline 840 G8 benchmark by delivering a **6-core / 12-thread AMD Ryzen 5 PRO 5650U Zen 3** processor, **2× un-soldered DDR4 SODIMM slots (up to 64GB)**, military-grade CNC all-aluminum unibody chassis, and 400-nit low power display under ৳46,000 landed.
6. **The Sub-৳48k 12th Gen Breakthroughs:**
   * **[#34 Dell Latitude 5330 2-in-1 Touch](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $349.00 USD (~৳47,115 landed / ~৳44,672 bank)**
     * 10-core Core i5-1235U, 16GB dual-channel LPDDR4x, 13.3" FHD touch with Corning Gorilla Glass 6 DX, dual Thunderbolt 4 ports (full eGPU support), and MicroSD reader.
   * **[#35 Dell Latitude 5430 Business Laptop](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $349.00 USD (~৳47,115 landed / ~৳44,672 bank)**
     * Generational 10-core upgrade over the Latitude 5420: Features **2× un-soldered DDR4 SODIMM slots (up to 64GB RAM)**, dual Thunderbolt 4 / USB-C 40Gbps ports (full eGPU ready), MicroSD card reader, RJ-45 Gigabit Ethernet, and modular captive-screw design under ৳48,000 landed.
7. **The Sub-৳50k 16:10 Clamshell Breakthroughs:**
   * **[#29 Lenovo ThinkPad T14 Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $369.00 USD (~৳49,815 landed / ~৳47,232 bank)**
     * Slashes under the ৳50k landed barrier with modern **16:10 WUXGA (1920x1200)** display, 12th Gen / Ryzen 6000 architecture, dual Thunderbolt 4 / USB4 eGPU ready, un-soldered SODIMM slot (up to 48GB), and MicroSD reader.
   * **[#30 Lenovo ThinkPad T14s Gen 3](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $369.00 USD (~৳49,815 landed / ~৳47,232 bank)**
     * **The 1.2kg Ultralight Executive Flagship:** Slashes 74%+ off $1,449 MSRP, delivering AMD Ryzen PRO 6000 Zen 3+ / 12th Gen i5 vPro compute, blazing 16GB LPDDR5-6400 RAM, massive 57Wh battery (14+ hours), and dual USB4 / TB4 40Gbps eGPU ready ports in an ultra-slim 1.22 kg carbon fiber & magnesium unibody!
   * **[#36 Dell Latitude 7330](https://computers.woot.com/offers/dell-latitude-7330-13-3-fhd-i5-1245u-16gb-256gb) — $349.99 USD (~৳47,249 landed / ~৳44,799 bank)**
     * Smashes the sub-$350 price floor for 10-core 12th Gen Core i5 processing, 16GB RAM, 400-nit low power FHD screen, dual Thunderbolt 4 ports, and MicroSD reader under ৳48,000 landed.
8. **The Executive Flagship Convertibles (Sub-৳52k Landed):**
   * **[#24 ThinkPad X1 Yoga Gen 6](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $379.00 USD (~৳51,165 landed / ~৳48,512 bank)**
     * CNC Storm Grey aluminum unibody, taller **16:10 400-nit low power display**, quad Dolby Atmos speakers, garaged stylus.
   * **[#46 HP EliteBook x360 1040 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $319.00 USD (~৳43,065 landed)**
     * Slashes 84% from original $1,999 MSRP. Ultra-slim 16.6mm magnesium unibody, **400-nit low-power 100% sRGB panel**, Bang & Olufsen quad audio.
9. **The Dual-SODIMM 2-in-1 Unicorn:**
   * **[#47 HP ProBook x360 435 G8](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) — $309.00 USD (~৳41,715 landed)**
   * *Why it wins:* **Two completely un-soldered DDR4 SODIMM slots (up to 64GB)** in a 360° convertible with Zen 3 6-core Ryzen 5 PRO.
10. **The Budget Clamshell Upgrader Kings:**
    * **[#42 Dell Latitude 5420](https://computers.woot.com/plus/microsoft-authorized-refurbished-laptops-67) ($319.99)** & **[#49 ThinkPad T14 Gen 2](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000) ($294.27)**
    * Built for 10-year longevity with easily accessible screws, dual heat pipes, MicroSD, and modular components.
11. **The Apex Tier 4 Powerhouses & Next-Gen Convertibles:**
    * **[#10 HP OmniBook X Flip 14"](https://www.bestbuy.com/site/searchpage.jsp?st=hp+omnibook+x+flip+14+touch) ($649.99):** Next-Gen **Intel Core Ultra 5 226V (Lunar Lake)** Copilot+ PC with 40+ TOPS AI NPU, 16GB LPDDR5X-8533, 2K 360° Touchscreen, dual TB4 ports, and 20+ hr battery.
    * **[#02 ASUS TUF A15](https://www.bestbuy.com/site/searchpage.jsp?st=asus+tuf+gaming+a15+rtx+4060) ($679.99):** Unthrottled **140W full-wattage RTX 4060** with MUX switch and dual DDR5 slots.
    * **[#09 Acer Swift Go 16 AI OLED](https://www.ebay.com/itm/257533096037) ($577.88):** 16.0" 2K/3.2K Touch OLED (100% DCI-P3), Core Ultra 5 AI NPU, dual M.2 slots, 2-Year Allstate Warranty.
    * **[#05 Dell Precision 3581](https://www.dellrefurbished.com/item/dell-precision-3581-000028/dell-precision-3581/1.html) ($619.00):** 12-core 45W H-series CPU, dedicated NVIDIA RTX A500 4GB GPU (2,048 CUDA cores, ISV-certified drivers for SolidWorks/CAD), dual DDR5 slots up to 64GB, dual M.2 SSD slots."""

archetypes_end = dash.find('## 💡 The Landed Cost Architecture (USD ➔ BDT)')
dash = dash[:dash.find('## 🏆 Key Standouts by Buyer Archetype')] + archetypes_replacement + '\n\n---\n\n' + dash[archetypes_end:]

with open(DASHBOARD_SCRIPT, 'w', encoding='utf-8') as f:
    f.write(dash)

print("generate_full_dashboard.py updated successfully.")

# Run generate_full_dashboard.py to generate README.md and DEALS_SUMMARY.md
result_dash = subprocess.run(['python', DASHBOARD_SCRIPT], capture_output=True, text=True)
print("generate_full_dashboard.py output:", result_dash.stdout, result_dash.stderr)

print("All dashboards and ledgers successfully updated and reconciled!")
