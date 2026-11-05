import os
import json
import subprocess

# 1. Patch generate_all_checked_deals.py
gen_deals_path = 'D:/WebDev/BlackFridayDeals/scripts/generate_all_checked_deals.py'
with open(gen_deals_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Fix unescaped quote in line 302
old_quote = '"display_arch": "14.0" 16:10 WUXGA (1920x1200) IPS Anti-glare display,'
new_quote = '"display_arch": "14.0\\" 16:10 WUXGA (1920x1200) IPS Anti-glare display,'
if old_quote in code:
    code = code.replace(old_quote, new_quote)
    print("Fixed unescaped quote in thinkpad-t14s-gen3-ebay OEM profile.")

# Add #A10, #A11, #A12 if not in code
a10_marker = "### #A10: Lenovo Legion 5"
if a10_marker not in code:
    old_a9_end = """### #A9: HP Envy x360 16" Core Ultra 7 2-in-1 (16.0" 2K Touch, Core Ultra 7 155U, 16GB LPDDR5, 512GB SSD)
* **Retailer / Platform:** eBay Certified Refurbished (Allstate 2-Year Warranty) • **SKU:** `Envy-x360-16-U7`
* **Historical Cart Price:** **$676.97 USD** (~৳86,652 bank / ~৳91,391 landed)
* **Audit Status:** `ARCHIVED (SOLD OUT)`
* **Audit Verdict:** Premium 16-inch 2K 360-degree convertible with Intel Core Ultra 7 Meteor Lake silicon and active stylus support. Official eBay refurbished inventory was exhausted during pre-holiday clearance. Actively tracked alternatives on the dashboard: the **Lenovo Yoga 7i 16" 2-in-1 ($599.99 / ~৳80,999 landed)** delivers identical 16-inch Core Ultra convertible capabilities with Dolby Vision for over $76 less, and the **HP OmniBook X Flip 14" ($649.99 / ~৳87,749 landed)** brings revolutionary Intel Lunar Lake Copilot+ architecture.

---"""

    new_archives = """### #A9: HP Envy x360 16" Core Ultra 7 2-in-1 (16.0" 2K Touch, Core Ultra 7 155U, 16GB LPDDR5, 512GB SSD)
* **Retailer / Platform:** eBay Certified Refurbished (Allstate 2-Year Warranty) • **SKU:** `Envy-x360-16-U7`
* **Historical Cart Price:** **$676.97 USD** (~৳86,652 bank / ~৳91,391 landed)
* **Audit Status:** `ARCHIVED (SOLD OUT)`
* **Audit Verdict:** Premium 16-inch 2K 360-degree convertible with Intel Core Ultra 7 Meteor Lake silicon and active stylus support. Official eBay refurbished inventory was exhausted during pre-holiday clearance. Actively tracked alternatives on the dashboard: the **Lenovo Yoga 7i 16" 2-in-1 ($599.99 / ~৳80,999 landed)** delivers identical 16-inch Core Ultra convertible capabilities with Dolby Vision for over $76 less, and the **HP OmniBook X Flip 14" ($649.99 / ~৳87,749 landed)** brings revolutionary Intel Lunar Lake Copilot+ architecture.

### #A10: Lenovo Legion 5 / Slim 5 16" Gaming Laptop (16.0" WQXGA 165Hz, AMD Ryzen 7 7735HS / 8845HS, 16GB DDR5, NVIDIA GeForce RTX 4060 8GB, 512GB/1TB SSD)
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

### #A12: HP Pavilion x360 14" 2-in-1 (14.0" FHD Touch, Intel Core i5-1335U / i3-1215U, 8GB DDR4 Soldered, 256GB/512GB SSD)
* **Retailer / Platform:** Best Buy / Target / Walmart Early Black Friday Doorbuster • **SKUs:** `14-ek0033dx` / `14-ek1013dx`
* **Promotional Door-buster Price:** **$349.99 – $399.99 USD** (~৳44,799 – ~৳51,199 bank / ~৳47,249 – ~৳53,999 landed)
* **Audit Status:** `DISQUALIFIED / FAILED 16GB MINIMUM PROTOCOL`
* **Audit Verdict:** **REJECTED UNDER CONVERTIBLE QUALITY & LONGEVITY PROTOCOL.** While marketed aggressively as an entry-level Black Friday touch convertible doorbuster under $400:
  1. **8GB Soldered RAM Bottleneck:** Sub-$400 retail configurations ship with 8GB non-upgradeable DDR4 RAM soldered to the motherboard. In 2026, running Windows 11 with typical browser tabs and web apps immediately consumes 85%+ system memory, leading to heavy paging and system stutters.
  2. **Fragile Plastic Hinge Mounts:** Consumer Pavilion x360 chassis use plastic screw mount anchors inside the palmrest casing rather than magnesium or aluminum structural reinforcement. In heavy 360-degree daily rotation, these hinges are prone to cracking or separating from the display housing.
  3. **Dim 250-Nit 45% NTSC Display:** The panel suffers from washed-out colors (~62.5% sRGB) and low brightness unsuitable for well-lit rooms.
  4. **Superior Actively Tracked Alternatives:** In the identical sub-$350 price bracket, the **Dell Latitude 5330 2-in-1 ($349.00 / ~৳47,115 landed)** delivers 10-core i5 vPro performance, **16GB RAM**, dual Thunderbolt 4 (eGPU ready), and military-grade durability. For pen work, the **ThinkBook 14s Yoga ($319.00 / ~৳43,065 landed)** provides un-soldered upgradeable RAM (up to 40GB), dual M.2 NVMe slots, all-aluminum unibody, and an internal garaged rechargeable Smart Pen for less money!

---"""
    if old_a9_end in code:
        code = code.replace(old_a9_end, new_archives)
        print("Appended #A10, #A11, #A12 to generate_all_checked_deals.py.")
    else:
        print("Warning: old_a9_end pattern not found verbatim, checking normalized newlines...")
        # try normalizing CRLF
        code_norm = code.replace('\r\n', '\n')
        old_a9_norm = old_a9_end.replace('\r\n', '\n')
        if old_a9_norm in code_norm:
            code = code_norm.replace(old_a9_norm, new_archives.replace('\r\n', '\n'))
            print("Appended #A10, #A11, #A12 using normalized newlines.")

# Update print message
code = code.replace(
    'ALL_CHECKED_DEALS.md successfully generated with {active_count} active + 9 archived listings',
    'ALL_CHECKED_DEALS.md successfully generated with {active_count} active + 12 archived listings'
)

with open(gen_deals_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_all_checked_deals.py written cleanly.")

# 2. Patch generate_full_dashboard.py
gen_dash_path = 'D:/WebDev/BlackFridayDeals/scripts/generate_full_dashboard.py'
with open(gen_dash_path, 'r', encoding='utf-8') as f:
    dash_code = f.read()

dash_code = dash_code.replace(
    '52 serialized models and 61 audited listings',
    '53 serialized models and 65 audited listings'
)

with open(gen_dash_path, 'w', encoding='utf-8') as f:
    f.write(dash_code)

print("generate_full_dashboard.py written cleanly.")

# 3. Execute generate_all_checked_deals.py
print("Running generate_all_checked_deals.py...")
res1 = subprocess.run(['python', gen_deals_path], capture_output=True, text=True, encoding='utf-8')
print("generate_all_checked_deals.py stdout:", res1.stdout)
if res1.stderr:
    print("generate_all_checked_deals.py stderr:", res1.stderr)

# 4. Execute generate_full_dashboard.py
print("Running generate_full_dashboard.py...")
res2 = subprocess.run(['python', gen_dash_path], capture_output=True, text=True, encoding='utf-8')
print("generate_full_dashboard.py stdout:", res2.stdout)
if res2.stderr:
    print("generate_full_dashboard.py stderr:", res2.stderr)

print("All regenerations finished.")
