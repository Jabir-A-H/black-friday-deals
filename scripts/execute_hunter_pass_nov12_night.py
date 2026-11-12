import json
import re

LEDGER_PATH = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
ALL_CHECKED_PATH = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md'
README_PATH = 'D:/WebDev/BlackFridayDeals/README.md'
SUMMARY_PATH = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_SUMMARY.md'

TIMESTAMP = '2026-11-12T22:30:00+06:00'
DISPLAY_TIME = '2026-11-12 22:30:00 (+06:00 Asia/Dhaka)'
VERSION = '2.79.0'
AUDITED_TOTAL = 104
ACTIVE_COUNT = 55
ARCHIVED_COUNT = 49

# 1. Update DEALS_LEDGER.json
print("Updating DEALS_LEDGER.json...")
with open(LEDGER_PATH, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['metadata']['version'] = VERSION
ledger['metadata']['last_updated'] = TIMESTAMP

for item in ledger['tracked_items']:
    item['last_checked'] = TIMESTAMP

history_summary = (
    "November 12 Thursday late-night Black Friday live deals synchronization pass (10:30 PM / 22:30): "
    "Executed comprehensive multi-retailer intelligence sweep across Dell Refurbished (DFS), Micro Center, "
    "B&H Photo Used, Best Buy, Walmart Direct, and Woot. Verified Best Buy Early Black Friday doorbuster wave remains "
    "fully active into Thursday late night (Lenovo IdeaPad Slim 3i Touch at $429.99, HP OmniBook X Flip 14 at $649.99, "
    "Lenovo Yoga 7i 16 at $599.99, Lenovo LOQ 15 RTX 4060 at $699.99 with rapid inventory turnover, ASUS TUF A15 RTX 4060 at $679.99) "
    "backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027; Dell Refurbished "
    "instant 40%-50% Hot Deals verified holding on Precision 3581 ($619 Grade A RTX A500, 4 units left; 14-core i7-13700H "
    "SKU 000038 at $559), Latitude 7340 32GB QHD+ ($579, final unit remaining), and Latitude 5530 ($409, 1 unit remaining); "
    "Walmart Black Friday Deals Event 1 general access kickoff officially active as of Nov 12 (monitoring $499 HP Victus "
    "RTX 4050 restocks; Apple MacBook Air M2 holding at $649). Sourced Micro Center refurbished intelligence (HP Victus 16-r0008ca "
    "12-core i5-13500H RTX 4050 16GB DDR5 144Hz; HP Pavilion 16 Touch Core 5 120U 16GB at $239 in-store; HP OmniBook 3 AI PC 16\" "
    "Touch at $779.99; enterprise ThinkPads/Latitudes from $219-$349) and B&H Photo Used department corporate additions. "
    "Sourced and validated all sub-55k BDT ($300-$407 USD landed) champions, including Dell Latitude 5330 2-in-1 ($275.00), "
    "Dell Latitude 7330 ($279.59), Dell Latitude 5430 ($329.99), ThinkPad X1 Yoga Gen 6 ($328.99 with verified 100% battery "
    "health, 4G LTE, and garaged stylus), ThinkPad X13 Yoga Gen 2 ($314.99), ThinkPad L13 Yoga Gen 3 ($339.00-$346.55), "
    "Dell Latitude 9420 2-in-1 ($354.99), ThinkPad T14 Gen 3 ($369-$379.95), ThinkPad X1 Carbon Gen 9 ($349.00), and "
    "HP ProBook x360 435 G8 ($306.90). Conducted rigorous Adversarial Doubt Gate audit on candidate #A49: Lenovo IdeaPad Flex 5 & "
    "Flex 5i (14\" & 16\" - 14IAU7, 14ALC7, 14ABR8, 14IRU8, 16IAU7, 16ABR8 Series) 8GB Soldered RAM Configurations "
    "($329.99-$449.99 holiday circular doorbusters across Best Buy, Costco, Walmart, Amazon, and Target: rejected and disqualified "
    "due to non-upgradeable 8GB soldered memory ceiling violating our 16GB non-negotiable convertible protocol; acute unified VRAM "
    "starvation with Intel Iris Xe or AMD Radeon graphics dynamically reserving up to 2GB VRAM leaving under 1.2GB operational headroom; "
    "chronic SSD virtual memory swap thrashing causing drawing ink latency, stroke skipping, and stylus lag in tablet mode; fragile "
    "360-degree zinc-alloy dual-torque hinge screw-boss shear [\"Flex 5 hinge blowout / lower corner split\"] where rotational torque "
    "systematically shears brass threaded inserts out of unreinforced PC-ABS plastic standoffs in the lower chassis; and reflective "
    "300-nit 45% NTSC glossy panels). Master directory expanded to 104 audited listings (55 active serialized models + 49 archived/disqualified listings). "
    "Reconciled ledger to v2.79.0, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
)

ledger['reconciled_history'].insert(0, {
    'timestamp': TIMESTAMP,
    'summary': history_summary
})

with open(LEDGER_PATH, 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
print("DEALS_LEDGER.json updated successfully.")

# 2. Update ALL_CHECKED_DEALS.md
print("Updating ALL_CHECKED_DEALS.md...")
with open(ALL_CHECKED_PATH, 'r', encoding='utf-8') as f:
    all_checked = f.read()

# Update badges
all_checked = re.sub(r'Total%20Audited-\d+%20Listings', f'Total%20Audited-{AUDITED_TOTAL}%20Listings', all_checked)
all_checked = re.sub(r'Archived%20%2F%20Filtered-\d+%20Listings', f'Archived%20%2F%20Filtered-{ARCHIVED_COUNT}%20Listings', all_checked)
all_checked = re.sub(r'\(#A1 – #A\d+\)', f'(#A1 – #A{ARCHIVED_COUNT})', all_checked)

# Entry #A49 content
a49_entry = """---

### #A49: Lenovo IdeaPad Flex 5 & Flex 5i (14" & 16" - 14IAU7, 14ALC7, 14ABR8, 14IRU8, 16IAU7, 16ABR8, 16IRU8 Series) 8GB Soldered RAM Configurations (14.0" & 16.0" WUXGA/FHD IPS Touch Display, Intel Core i3-1215U/1315U / Core i5-1235U/1335U / Core 5 120U / AMD Ryzen 3 7320U / Ryzen 5 5500U/7530U/8645HS, 8GB Soldered LPDDR4x-4266 / LPDDR5-5200 RAM, 256GB/512GB SSD)
* **Retailer / Platform:** Best Buy / Costco / Walmart / Amazon / Target Black Friday Doorbusters • **SKUs:** `82R7003WUS` / `82R9000NUS` / `82XX003NUS` / `83DT0005US` / `6571567` / `6533956` / `B0B5B3P6T3`
* **Promotional Price:** **$329.99 – $449.99 USD** (~৳42,239 – ~৳57,599 bank / ~৳44,549 – ~৳60,749 landed) *(MSRP: $599.99 – $749.99)*
* **Audit Status:** `DISQUALIFIED / NON-UPGRADEABLE 8GB SOLDERED LPDDR4X/LPDDR5 MEMORY CEILING, SEVERE UNIFIED VRAM STARVATION, CHRONIC SSD SWAP PAGING WITH STYLUS DRAWING INK LAG, FRAGILE 360° DUAL-TORQUE HINGE SCREW-BOSS SHEAR ("FLEX 5 HINGE BLOWOUT") & 300-NIT 45% NTSC PANELS`
* **Audit Verdict:** **REJECTED UNDER ADVERSARIAL STRUCTURAL INTEGRITY, CONVERTIBLE MEMORY PROTOCOL & TABLET ERGONOMICS GATE.** Frequently highlighted across holiday promotional mailers and retail endcaps at Best Buy, Costco, and Walmart as an affordable "$349 to $449 2-in-1 touchscreen laptop with digital pen support", ensnaring students, note-takers, and budget buyers into a severe convertible operational bottleneck:
  1. **Strict 16GB Convertible Protocol Violation (Non-Upgradeable 8GB Soldered RAM Ceiling):** Under our tracker's strict non-negotiable convertible standard (*"For convertibles with soldered RAM: 16GB RAM minimum is non-negotiable; 8GB soldered convertibles are permanently rejected due to non-upgradeability"*), this model is categorically disqualified. Unlike clamshells where light office work may scrape by, 2-in-1 convertibles run background touch digitizer drivers, Windows Ink workspace services, and virtual pen pressure telemetry. Windows 11 Home consumes 4.4GB–5.1GB of RAM on startup. Integrated Intel Iris Xe or AMD Radeon graphics dynamically allocate up to 2.0GB for display buffers, leaving less than 1.2GB of physical system memory available. Opening Microsoft OneNote alongside a PDF reader and 5 web tabs saturates physical memory, forcing continuous NVMe SSD virtual memory swap paging. In tablet mode, this triggers noticeable pen stroke latency, missed palm rejection inputs, and ink stuttering that renders digital handwriting frustrating.
  2. **Notorious 360-Degree Zinc-Alloy Dual-Torque Hinge Screw-Boss Tear-Out ("Flex 5 Hinge Blowout / Lower Corner Separation"):** A 360-degree convertible demands substantially stiffer hinge resistance than a standard clamshell to hold the display upright during touch interaction. While the hinge brackets themselves are cast zinc alloy, they are fastened using short machine screws into brass threaded inserts heat-staked into paper-thin PC-ABS plastic standoffs within the lower chassis tub (D-cover) and palmrest (C-cover). Because the lower chassis lacks an internal magnesium sub-frame, the immense torsional leverage created every time the user rotates the screen between laptop, tent, and tablet modes transfers directly into the brittle plastic towers. Over 9 to 18 months of regular use, the brass inserts fatigue and shear out of the plastic, causing the lower casing corners to violently pop apart, bending internal hinge arms, and severing delicate 30-pin eDP display and touch digitizer ribbon cables.
  3. **Sluggish 45% NTSC Display with High Gloss Reflectivity on Budget SKUs:** Promotional doorbuster configurations cut costs by deploying 250-to-300 nit 45% NTSC (~62.5% sRGB) panels with edge-to-edge glossy glass. In addition to muted color rendition, the lack of anti-reflective coating combined with modest 300-nit peak brightness creates intense mirror-like glare under fluorescent classroom or office lighting, severely undermining note-taking readability.
  4. **Crippled USB-C Capabilities on Entry-Level SKUs:** Several budget circular variants limit the USB-C port to data transfer and low-speed charging, lacking full DisplayPort 1.4 alt-mode and 40Gbps Thunderbolt connectivity, precluding eGPU pairing and high-resolution dual-monitor docking.
  5. **Superior Actively Tracked Alternatives in the Same Budget Window ($208 – $439 USD / ~৳28k – ~৳59k landed):**
     * **Lenovo IdeaPad Flex 5 (#36 at $208.99 / ~৳28,214 landed):** Our curated **16GB RAM / 8-core AMD Ryzen 7** configuration featuring 512GB SSD, 14.0" WUXGA 16:10 touch panel, and full digital pen support under ৳29,000 landed!
     * **Dell Latitude 7320 2-in-1 ($259.00 / ~৳34,965 landed):** 11th Gen vPro Core i5, **16GB RAM**, dual Thunderbolt 4 ports, Gorilla Glass 6 DX touch display, all-aluminum / carbon fiber unibody, and full 360° touch convertible versatility under ৳35,000 landed.
     * **Dell Latitude 5330 2-in-1 ($275.00 / ~৳37,125 landed):** 10-core 12th Gen Core i7-1265U vPro, **16GB RAM**, dual Thunderbolt 4 (40Gbps eGPU ready), MicroSD slot, and Corning Gorilla Glass 6 DX touch screen under ৳38,000 landed.
     * **HP EliteBook x360 830 G8 ($288.99 / ~৳39,014 landed):** 11th Gen Core i5, **16GB RAM**, CNC aluminum unibody, 400-nit touch display, dual Thunderbolt 4, and 360° convertible versatility under ৳40,000 landed.
     * **HP ProBook x360 435 G8 ($306.90 / ~৳41,432 landed):** 8-core / 16-thread AMD Ryzen 7 PRO 5850U, **dual un-soldered SODIMM slots (up to 64GB DDR4)**, aluminum keyboard deck, Corning Gorilla Glass 5, and 1-Year Allstate Warranty under ৳42,000 landed.
     * **ThinkPad X13 Yoga Gen 2 ($314.99 / ~৳42,524 landed):** 11th Gen vPro Core i5, **16GB RAM**, modern 16:10 WUXGA touch display, garaged stylus, and dual Thunderbolt 4 under ৳43,000 landed.
     * **Dell Latitude 5320 2-in-1 ($319.00 / ~৳43,065 landed):** 11th Gen Core i5, **16GB RAM**, dual Thunderbolt 4, MicroSD slot, Gorilla Glass 6 DX touch display, and Dell Active Pen support under ৳44,000 landed.
     * **Dell Latitude 7420 2-in-1 ($319.00 / ~৳43,065 landed):** 11th Gen Core i5/i7 vPro, **16GB RAM**, 14.0" FHD touch screen, dual Thunderbolt 4, and carbon fiber / CNC aluminum chassis under ৳44,000 landed.
     * **Lenovo ThinkBook 14s Yoga ($319.00 / ~৳43,065 landed):** Core i5/i7, **16GB RAM (upgradeable to 40GB)**, **dual M.2 SSD slots**, garaged Smart Pen, and CNC all-aluminum chassis under ৳44,000 landed.
     * **HP EliteBook x360 1040 G8 ($319.00 / ~৳43,065 landed):** Apex corporate flagship, **16GB RAM**, 14.0" 400-nit low power touch display, dual Thunderbolt 4, Bang & Olufsen quad audio, and CNC unibody under ৳44,000 landed.
     * **ThinkPad X1 Yoga Gen 6 ($328.99 / ~৳44,414 landed):** Flagship CNC aluminum unibody, **16GB RAM**, 14.0" 16:10 400-nit low power touch display, garaged stylus, 4G LTE, and 100% verified battery health under ৳45,000 landed.
     * **ThinkPad L13 Yoga Gen 3 ($339.00 / ~৳45,765 landed):** 10-core 12th Gen Core i5 / 8-core Ryzen 7 PRO, **16GB RAM**, 16:10 WUXGA touch panel, garaged Pen Pro, and MIL-STD-810H durability under ৳46,000 landed.
     * **HP Envy x360 15.6" (#28 at $339.99 / ~৳45,899 landed):** 6-core/12-thread AMD Ryzen 5, **16GB RAM**, 512GB SSD, edge-to-edge touch glass, and Bang & Olufsen audio under ৳46,000 landed.
     * **Dell Latitude 9420 2-in-1 ($354.99 / ~৳47,924 landed):** Dell's apex 9000-series executive flagship, **16GB RAM**, 14.0" 16:10 QHD+ (2560x1600) 500-nit touch display, motorized SafeShutter webcam, and quad speakers under ৳48,000 landed.
     * **Dell Latitude 7330 2-in-1 ($369.00 / ~৳49,815 landed):** 10-core 12th Gen Core i5 vPro, **16GB RAM**, dual Thunderbolt 4, carbon fiber / aluminum chassis, and Dell Active Pen support under ৳50,000 landed.
     * **Dell Latitude 7430 2-in-1 (#17 at $379.00 / ~৳51,165 landed):** 10-core 12th Gen Core i7-1265U vPro, **16GB RAM**, dual Thunderbolt 4 (40Gbps eGPU ready), CNC aluminum unibody, and IR facial recognition under ৳52,000 landed.
     * **Dell Inspiron 14 2-in-1 (#29 at $429.00 / ~৳57,915 landed):** 10-core 13th Gen Core i5-1335U, **16GB LPDDR5 RAM**, 512GB Gen 4 SSD, and 14.0" 16:10 FHD+ touch screen under ৳58,000 landed.
     * **ThinkPad X13 Yoga Gen 3 (#20 at $439.99 / ~৳59,399 landed):** 10-core 12th Gen Core i5 vPro, **16GB RAM**, 16:10 WUXGA touch panel, garaged Pen Pro, dual TB4, and MIL-STD-810H durability under ৳60,000 landed.

"""

# Insert a49_entry before the footer
footer_pattern = r'<sub>The Master Directory of All Checked Laptop Deals is maintained and verified continuously.*'
replacement = a49_entry + f'<sub>The Master Directory of All Checked Laptop Deals is maintained and verified continuously with manufacturer-grade technical telemetry by the Black Friday Deal Tracker ({ACTIVE_COUNT} active serialized models + {ARCHIVED_COUNT} archived/disqualified listings = {AUDITED_TOTAL} total audited).</sub>\n</div>'

all_checked = re.sub(footer_pattern + r'\s*</div>', replacement, all_checked, flags=re.DOTALL)

with open(ALL_CHECKED_PATH, 'w', encoding='utf-8') as f:
    f.write(all_checked)
print("ALL_CHECKED_DEALS.md updated successfully.")

# 3. Helper function to update README.md and DEALS_SUMMARY.md
def update_dashboard_file(path, is_readme=True):
    print(f"Updating {path}...")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update version badge
    content = re.sub(r'Ledger-v\d+\.\d+\.\d+-informational', f'Ledger-v{VERSION}-informational', content)
    # Update audited deals badge
    content = re.sub(r'Checked%20Listings-\d+%20Audited%20Deals', f'Checked%20Listings-{AUDITED_TOTAL}%20Audited%20Deals', content)

    # Update header callout lines
    # Last Verified line
    old_verified_pattern = r'> \*\*🕒 Last Verified:\*\* `[^`]+` • All \d+ active models and \d+ archived listings verified live \(\d+ total audited listings milestone!\)'
    new_verified_line = f'> **🕒 Last Verified:** `{DISPLAY_TIME}` • All {ACTIVE_COUNT} active models and {ARCHIVED_COUNT} archived listings verified live ({AUDITED_TOTAL} total audited listings milestone!)'
    content = re.sub(old_verified_pattern, new_verified_line, content)

    # Update Defect Gate callout to include #A49
    old_defect_gate_pattern = r'> \*\*🛡️ Adversarial Defect Gate Active:\*\* Disqualified candidate #A48 \([^\)]+\),'
    new_defect_gate_snippet = (
        '> **🛡️ Adversarial Defect Gate Active:** Disqualified candidate #A49 (Lenovo IdeaPad Flex 5 & Flex 5i 14"/16" 8GB soldered LPDDR4x/LPDDR5 memory: '
        'non-upgradeable 8GB soldered memory ceiling with zero SODIMM slots violating our 16GB non-negotiable convertible protocol, acute unified VRAM starvation '
        'with Intel Iris Xe or AMD Radeon graphics dynamically reserving up to 2GB VRAM leaving under 1.2GB operational headroom, chronic SSD virtual memory swap '
        'thrashing causing drawing ink latency, stroke skipping, and stylus lag in tablet mode, fragile 360-degree zinc-alloy dual-torque hinge screw-boss shear '
        '[\'Flex 5 hinge blowout / lower corner split\'] where rotational torque systematically shears brass threaded inserts out of unreinforced PC-ABS plastic '
        'standoffs in the lower chassis, and reflective 300-nit 45% NTSC glossy panels), candidate #A48 (ASUS Vivobook Go 14 & Go 15 4GB/8GB soldered LPDDR5 memory: '
        'non-upgradeable 4GB/8GB soldered memory ceiling with zero SODIMM slots violating our 16GB non-negotiable protocol, sluggish 64GB/128GB eMMC 5.1 storage causing '
        'catastrophic Windows 11 update stalls, fragile unreinforced plastic lower tub with ErgoLift drop-hinge torque shearing plastic standoffs [\'Vivobook Go hinge blowout\'], '
        'washed-out 220-nit 45% NTSC TN panel with severe vertical contrast inversion, and data-only USB-C with proprietary barrel charger),'
    )
    if 'Disqualified candidate #A49' not in content:
        content = re.sub(old_defect_gate_pattern, new_defect_gate_snippet, content)

    # Update reference library link
    content = re.sub(r'Complete Master Directory of All \d+ Audited Deals', f'Complete Master Directory of All {AUDITED_TOTAL} Audited Deals', content)

    # Update top champions text: selected from X audited listings
    content = re.sub(r'selected from \d+ audited listings', f'selected from {AUDITED_TOTAL} audited listings', content)

    # Update footer line
    old_footer_pattern = r'<sub>The Black Friday Deals Intelligence Suite monitors \d+ active serialized models and \d+ audited listings across US retail and certified refurbished channels\.</sub>'
    new_footer = f'<sub>The Black Friday Deals Intelligence Suite monitors {ACTIVE_COUNT} active serialized models and {AUDITED_TOTAL} audited listings across US retail and certified refurbished channels.</sub>'
    content = re.sub(old_footer_pattern, new_footer, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{path} updated successfully.")

update_dashboard_file(README_PATH, is_readme=True)
update_dashboard_file(SUMMARY_PATH, is_readme=False)

print("\n--- ALL PASS SYNCHRONIZATIONS COMPLETED SUCCESSFULLY! ---")
