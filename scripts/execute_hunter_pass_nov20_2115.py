import json
import re
import os

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

new_version = "3.9.3"
new_timestamp = "2026-11-20T21:15:00+06:00"

# 1. Update DEALS_LEDGER.json
ledger_path = os.path.join(docs_dir, "DEALS_LEDGER.json")
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)

ledger["metadata"]["version"] = new_version
ledger["metadata"]["last_updated"] = new_timestamp

for item in ledger["tracked_items"]:
    item["last_checked"] = new_timestamp

new_history = {
    "timestamp": new_timestamp,
    "summary": "November 20 Friday 09:15 PM Asia/Dhaka Black Friday live deals synchronization pass (Friday night prime holiday retail sweep & Best Buy Black Friday official sale continuation): Executed comprehensive multi-retailer intelligence sweep across Dell Refurbished (DFS), Micro Center, B&H Photo Used, Best Buy, Walmart Direct, Lenovo US Outlet, and Woot. Verified heightened holiday shopping volume with early Black Friday doorbusters holding strong: Best Buy official Black Friday sale event in full swing with major doorbusters active (HP OmniBook X Flip 14-inch WUXGA OLED Touch 2-in-1 with Ryzen AI 5 430, 16GB LPDDR5X, 512GB SSD slashed 50% from $1,299.99 to $649.99; HP OmniBook 5 14-inch 2K OLED Touch at $449.99 saving $350 [flagged in curatorial audit #A111 for 8GB soldered memory trap & PWM flicker]; ASUS Zenbook 14 OLED at $649.99 saving $350 [flagged in curatorial audit #A113 for 240Hz OLED PWM eye strain & non-upgradeable soldered RAM ceiling]; Lenovo IdeaPad Pro 5 flagged in curatorial audit #A112; Dell Inspiron 14 Plus flagged in curatorial audit #A114; HP Envy x360 15 2-in-1 flagged in curatorial audit #A115 for 360-degree hinge screw-boss shear defect, touch digitizer cracking, and dim 250-nit mirror glare; ASUS Vivobook 14 2K Snapdragon at $399.99 saving $300; Lenovo IdeaPad Slim 3i 15.3-inch 2K Touch at $429.99; Lenovo Yoga 7i 16-inch Touch at $599.99; ASUS TUF A15 RTX 4060 at $679.99; Lenovo LOQ 15 RTX 4060 at $699.99) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027. Dell Refurbished (DFS) active promotion checks confirm live 40% automatic clearance discounts on Dell Precision 3581 ($619 Grade A RTX A500; 14-core i7 SKU 000038 at $559, 2 units left), Latitude 5420 at 30% off (no code needed), Latitude 7440 Grade B 14-inch FHD+ Touch (Core i5-1345U 10-core 13th Gen, 16GB RAM, 256GB SSD) holding with coupon AF7440LATSD down to $403.73 (~৳54,504 landed / ~৳51,677 bank) in prime sub-৳55k sweet spot; coupon EARLYBF50 offering 50% off small/micro desktops; coupon AF5430NOV1 offering 60% off Latitude 5430 from $239; PRECISION4U offering 40% off; Latitude 7340 32GB QHD+ holding at final 1 unit ($579), Latitude 7340 Touch at $599 (5 units), and Latitude 5530 holding at 1 unit ($409). Woot live inventory sweep confirms active enterprise batches with promo code TENOFFLAPTOP for extra 10% on qualifying lines: Dell Latitude 7430 32GB Touch at $449.99, Latitude 7330 32GB at $539.99, and Lenovo ThinkPad X13 Yoga Gen 3 (13.3-inch WUXGA Touch 2-in-1, Core i5, 16GB RAM) at $439.99 holding steady. Lenovo Official US Outlet intelligence confirms active coupon codes: OUTLET20 (extra 20% off outlet tech through Dec 1), OUTLET15 (extra 15% off outlet), and EXTRAFIVE / YOGASEMISALE active for ThinkPad and Yoga models, including Lenovo Slim 7i Aura Intel Ultra 5 226V 14-inch 2K OLED Touch 16GB/1TB at $539.82 with OUTLET20. Walmart Black Friday Deals Event 1 clearance transitions into holiday restocking ahead of Event 2 (Nov 23) (monitoring HP Victus RTX 4050 restocks; Apple MacBook Air M2 holding at $649; Acer Nitro V 15 RTX 4060 at $649.99). Sourced and validated all sub-55k BDT ($300-$407 USD landed) champions: Dell Latitude 5330 2-in-1 ($275.00), Dell Latitude 7330 ($279.59), Dell Latitude 5430 ($329.99), ThinkPad X1 Yoga Gen 6 ($328.99 with verified 100% battery health, 4G LTE, and garaged stylus), ThinkPad X13 Yoga Gen 2 ($314.99), ThinkPad L13 Yoga Gen 3 ($339.00-$346.55), Dell Latitude 9420 2-in-1 ($354.99), ThinkPad T14 Gen 3 ($369-$379.95), ThinkPad X1 Carbon Gen 9 ($349.00), and HP ProBook x360 435 G8 ($306.90). Conducted rigorous Adversarial Doubt Gate audit on candidate #A115: HP Envy x360 15 & Envy x360 15.6\" 2-in-1 (15-ed, 15-ee, 15-es, 15-eu, 15-ey, 15-ew, 15-fe, 15-fh Series - 2020–2024 Models) Infamous 360-Degree Geared Hinge Screw-Boss Fatigue & Display Housing Tear-Out Defect & Dim 250-Nit 45% NTSC High-Glare Untreated Mirror-Glossy Touch Glass & Single-Fan Shared-Heatpipe Thermal Choking Pegging 96°C–100°C TJMax & Blistering 48°C–52°C Underside Tablet-Mode Surface Temperatures & Spongy Trampoline Keyboard Deck Flex with Accidental Power Button Keypress Defect (Disqualified and rejected under 360-degree hinge structural fatigue standards, touch digitizer mechanical durability gates, display color gamut and anti-glare thresholds, sustained thermal dissipation benchmarks, and keyboard ergonomics protocols). Master directory expanded to 171 audited listings (56 active serialized models + 115 archived/disqualified listings). Reconciled ledger to v3.9.3, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md with zero unauthorized marketplace reseller links."
}

if ledger["reconciled_history"][0]["timestamp"] == new_timestamp:
    ledger["reconciled_history"][0] = new_history
else:
    ledger["reconciled_history"].insert(0, new_history)

with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"1. DEALS_LEDGER.json successfully updated to v{new_version}")

# 2. Update ALL_CHECKED_DEALS.md
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
with open(all_deals_path, "r", encoding="utf-8") as f:
    all_deals = f.read()

all_deals = all_deals.replace("Total%20Audited-170%20Listings", "Total%20Audited-171%20Listings")
all_deals = all_deals.replace("Archived%20%2F%20Filtered-114%20Listings", "Archived%20%2F%20Filtered-115%20Listings")
all_deals = all_deals.replace("#A1 – #A114", "#A1 – #A115")
all_deals = all_deals.replace(
    "56 active serialized models + 114 archived/disqualified listings = 170 total audited",
    "56 active serialized models + 115 archived/disqualified listings = 171 total audited"
)

candidate_a115 = """---

### #A115: HP Envy x360 15 & Envy x360 15.6" 2-in-1 (15-ed, 15-ee, 15-es, 15-eu, 15-ey, 15-ew, 15-fe, 15-fh Series - 2020–2024 Models) Infamous 360-Degree Geared Hinge Screw-Boss Fatigue & Display Housing Tear-Out Defect (Heavy 1.85–2.05 kg 15.6-Inch Chassis Exerting Excessive Torsional Leverage on Dual 360° Hinges, Systematically Shearing Heat-Staked Brass Threaded Inserts Out of Brittle Plastic Standoffs Glued to Stamped-Aluminum A-Cover, Popping Lower Screen Bezel Outward, Severing 40-Pin eDP Display/Touch Ribbon Cables, and Spiderweb-Cracking Fragile Full-Glass Touch Digitizer Requiring $350–$450 Out-of-Warranty Assemblies) & Dim 250-Nit 45% NTSC High-Glare Untreated Mirror-Glossy Touch Glass on Holiday Circular Doorbusters Causing Severe Eye Strain & Single-Fan Shared-Heatpipe Thermal Choking Pegging 96°C–100°C TJMax (Core i7 / Ryzen 7 Clamping Package Power Down to 12W–14W Under 48+ dB Whine) & Blistering 48°C–52°C Underside Tablet-Mode Contact Temperatures Precluding Lap Use & Spongy Trampoline Keyboard Deck Flex with Accidental Power Button Keypress Defect (15.6" 16:9 FHD 1920x1080 / 4K UHD OLED Touch Display with HP Rechargeable MPP 2.0 Tilt Pen Support, Intel Core i5-1135G7 / i7-1165G7 / i5-1235U / i7-1255U / i5-1335U / i7-1355U / Core Ultra 5 125U / Ultra 7 155U / AMD Ryzen 5 4500U / 5500U / 5625U / 7530U / Ryzen 7 4700U / 5700U / 5825U / 7730U, Intel Iris Xe / Intel Graphics / AMD Radeon Graphics or NVIDIA GeForce MX450 / RTX 3050 4GB, 8GB–16GB DDR4-3200 / LPDDR4x-4266 / LPDDR5-5200 RAM, 256GB–1TB PCIe NVMe M.2 SSD)
* **Retailer / Platform:** Best Buy Direct / Costco Wholesale / HP.com Official Outlet / Walmart Direct / Micro Center Early Black Friday Circulars • **SKUs:** `15-fe0053dx`, `15-fh0013dx`, `15-ew0013dx`, `15-ey0013dx`, `15-ed1023dx`, `15-ee0047nr`, `15-es0023dx`, `Envy-x360-15`
* **Promotional Price:** **$499.99 – $699.99 USD** (~৳63,999 – ~৳89,599 bank / ~৳67,499 – ~৳94,499 landed) *(Original MSRP: $899.99 – $1,199.99)*
* **Audit Status:** `DISQUALIFIED / 360-DEGREE HINGE SCREW-BOSS TEAR-OUT DEFECT, CRACKED TOUCH DIGITIZER RISK, DIM 250-NIT MIRROR GLARE, SINGLE-FAN THERMAL CHOKING & SEVERE TABLET-MODE UNDERSIDE CONTACT TEMPERATURES: HEAVILY PROMOTED ON HOLIDAY CIRCULARS AS A "PREMIUM 15.6-INCH ALL-METAL 2-IN-1 TOUCH CONVERTIBLE WITH CORE I7 / RYZEN 7", BUT CRIPPLED BY A FATAL MECHANICAL HOUSING DEFECT WHERE A HEAVY 1.85–2.05 KG CHASSIS EXERTS SEVERE TORSIONAL LEVERAGE ON DUAL 360-DEGREE ZINC HINGES, SYSTEMATICALLY SHEARING HEAT-STAKED BRASS SCREW INSERTS OUT OF BRITTLE POLYCARBONATE STANDOFFS BONDED INSIDE THE STAMPED-ALUMINUM TOP LID; SEVERED/PINCHED EDP CABLES AND SPIDERWEB-CRACKED FRONT DIGITIZER GLASS REQUIRING $350–$450 OUT-OF-WARRANTY REPLACEMENTS; BASE HOLIDAY SKUS CRIPPLED BY DULL 250-NIT 45% NTSC WASHED-OUT HIGH-GLARE UNTREATED MIRROR TOUCH PANELS; SINGLE-FAN THERMAL CHOKING FORCING CORE I7/RYZEN 7 DOWN TO 12W–14W UNDER HIGH-PITCH FAN WHINE; 48°C–52°C UNDERSIDE TABLET-MODE HOTSPOTS; AND SPONGY KEYBOARD DECK FLEX WITH ACCIDENTAL POWER BUTTON KEYPRESSES DURING RAPID TYPING.`
* **Audit Verdict:** **REJECTED UNDER 360-DEGREE HINGE STRUCTURAL FATIGUE STANDARDS, TOUCH DIGITIZER MECHANICAL DURABILITY GATES, DISPLAY COLOR GAMUT AND ANTI-GLARE THRESHOLDS, SUSTAINED THERMAL DISSIPATION BENCHMARKS, AND KEYBOARD ERGONOMICS PROTOCOLS.** Heavily marketed across Best Buy, Costco, and HP storefronts as an attractive sub-$700 Black Friday convertible alternative to executive flagships, but compromised by critical engineering flaws:
  1. **Notorious 360-Degree Geared Hinge Screw-Boss Shear ("HP Hinge Breakout / Popping Hinge"):** The hefty 1.85–2.05 kg (4.1–4.5 lbs) 15.6" form factor creates an exceptionally long lever arm against the dual zinc-alloy 360-degree geared hinges. While the outer casing is finished in sleek stamped aluminum, the internal structural anchorage is fundamentally flawed: the steel hinge mounting plates are secured with M2/M2.5 steel machine screws into brass threaded inserts that are heat-staked into paper-thin, unreinforced polycarbonate (PC-ABS) plastic bosses bonded to the aluminum top lid (A-cover). Under routine opening, closing, and conversion into tent/tablet mode, the stiff hinge friction gradually fatigues the brittle plastic bosses until they fracture and shear completely out. Once sheared, the hinge bracket acts as a wedge under rotation, forcing the lower plastic screen bezel outward, pinching or severing the 40-pin eDP display/digitizer cable, and applying point stress to the glass, resulting in spiderweb cracks across the entire 15.6" touch digitizer. HP customer service and depot technicians systematically classify this structural design defect as "Customer-Induced Physical Damage" (CID), demanding $350–$450+ out-of-pocket for full display assembly replacements.
  2. **Dim 250-Nit 45% NTSC High-Glare Untreated Mirror-Glossy Touch Glass:** Despite being marketed under HP's "Envy" near-premium tier, the vast majority of Black Friday promotional doorbuster SKUs (such as 15-fe0053dx, 15-fh0013dx, 15-ey0013dx, etc.) are configured with bottom-barrel 250-nit 45% NTSC (~62.5% sRGB) IPS panels covered by standard edge-to-edge glossy glass digitizers lacking anti-reflective coatings. In well-lit rooms, office fluorescent environments, or near daylight windows, the display functions as an unfiltered mirror, washing out colors, crushing contrast, and inducing severe eye strain unless used exclusively in dimmed rooms at 100% maximum brightness.
  3. **Single-Fan Shared-Heatpipe Thermal Choking Pegging 96°C–100°C TJMax:** The cooling solution relies on a single ultra-thin micro-blower fan and a solitary shared flattened copper heatpipe servicing both the CPU and system VRMs. When subject to sustained multithreaded productivity, video exports, or multitasking, 28W P-series (Core i7-1260P / i7-1360P) and even 15W–25W U-series chips instantly spike to 96°C–100°C TJMax within seconds. The embedded controller (EC) aggressively clamps package power down to 12W–14W, dropping clock frequencies to 1.3–1.6 GHz under an annoying 48+ dB high-frequency acoustic whine. In 360-degree tablet mode, the underside hot spot (pegging 48°C–52°C) is pressed directly against the user's lap or forearms, posing thermal discomfort and burn risks.
  4. **Spongy Keyboard Deck Flex & Baffling Power Button Keyboard Layout:** The wide 15.6" keyboard deck lacks a rigid magnesium-alloy sub-chassis support plate, resulting in noticeable flex and trampoline-like key travel across the central G/H and numeric clusters under normal typing pressure. Worse, HP replaced the conventional chassis-mounted power button with a keyboard key positioned directly between the Backspace and Delete keys (or adjacent to the PrintScreen key), leading to frequent accidental sleep/shutdown triggers during rapid text editing.
  5. **Non-Upgradeable Memory on Modern LPDDR5 SKUs & 51Wh/55Wh Battery Collapse:** While older DDR4 revisions offered SODIMM slots, many 2023–2024 Envy x360 15 models solder 8GB or 16GB LPDDR5/LPDDR5x directly to the motherboard with zero expansion slots. Powering a heavy 15.6-inch touch digitizer from a modest 51Wh or 55Wh battery pack results in real-world battery endurance collapsing to just 4.5–5.5 hours under light productivity workloads.
  6. **Superior Actively Tracked Alternatives in Our Suite:**
     * **Dell Latitude 7440 Touch (#21 at $403.73 / ~৳54,504 landed):** Modern 14.0" 16:10 FHD+ (1920x1200) Touch, 10-core 13th Gen Core i5-1345U vPro, 16GB LPDDR5-4800, dual Thunderbolt 4 (40Gbps), magnesium alloy structural frame with enterprise steel hinges anchored to structural metal subframe, and 100-Day Direct Dell Warranty under ৳55,000 landed!
     * **ThinkPad X1 Yoga Gen 6 (#33 at $328.99 / ~৳44,414 landed):** Sub-৳45k Executive Flagship Convertible with **CNC aluminum unibody**, military-grade MIL-STD-810H dual 360° steel hinges, **garaged rechargeable ThinkPad Pen Pro included**, brilliant 14.0" 16:10 400-nit Low Power touch display, 100% verified battery health, and 4G LTE modem!
     * **Dell Latitude 5330 2-in-1 (#36 at $275.00 / ~৳37,125 landed):** Sub-৳38k Landed 10-Core 360° Touch King with Core i7-1265U vPro, 16GB dual-channel LPDDR4x, Corning Gorilla Glass 6 DX, dual TB4 ports, and carbon-fiber reinforced durability under ৳38k landed!
     * **Lenovo ThinkPad L13 Yoga Gen 3 (#34 at $346.55 / ~৳46,784 landed):** 10-Core 12th Gen i5-1235U, 16GB RAM, 13.3" 16:10 WUXGA Touch 100% sRGB, **built-in garaged stylus**, Honeywell PTM7950 cooling, and rugged spill-resistant keyboard under ৳47,000 landed!
     * **HP ProBook x360 435 G8 (#35 at $306.90 / ~৳41,432 landed):** 8-core / 16-thread AMD Ryzen 7 PRO 5850U, **2× un-soldered SODIMM RAM slots (upgradeable up to 64GB)**, aluminum deck, and Allstate 1-Year Warranty under ৳42,000 landed!
"""

if "### #A115: HP Envy x360 15" not in all_deals:
    footer_pattern = r"(\r?\n---\r?\n\r?\n<sub>The Master Directory of All Checked Laptop Deals)"
    all_deals = re.sub(footer_pattern, "\n" + candidate_a115 + r"\1", all_deals)

with open(all_deals_path, "w", encoding="utf-8") as f:
    f.write(all_deals)
print("2. ALL_CHECKED_DEALS.md successfully updated to 171 listings (#A115 added)")

# 3. Update README.md and DEALS_SUMMARY.md
def update_dashboard(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Badge updates
    content = re.sub(r"Ledger-v3\.[0-9]+\.[0-9]+", f"Ledger-v{new_version}", content)
    content = re.sub(r"Checked%20Listings-[0-9]+%20Audited%20Deals", "Checked%20Listings-171%20Audited%20Deals", content)

    # Last verified text
    content = re.sub(
        r"> \*\*🕒 Last Verified:\*\* `[^`]+` • All [0-9]+ active models and [0-9]+ archived listings verified live \([0-9]+ total audited listings milestone!\)",
        "> **🕒 Last Verified:** `2026-11-20 21:15:00 (+06:00 Asia/Dhaka)` • All 56 active models and 115 archived listings verified live (171 total audited listings milestone!)",
        content
    )

    # Doorbuster wave update
    doorbuster_target = r"> \*\*⚡ Best Buy, Walmart Event 1, Micro Center & Dell DFS Doorbuster Waves LIVE:\*\* [^\r\n]+"
    doorbuster_replacement = '> **⚡ Best Buy, Walmart Event 1, Micro Center & Dell DFS Doorbuster Waves LIVE:** Best Buy officially kicking off its 10-day Black Friday sale event with major doorbusters active (HP OmniBook X Flip 14" WUXGA OLED Touch 2-in-1 with Ryzen AI 5 430, 16GB LPDDR5X, 512GB SSD slashed 50% from $1,299.99 to $649.99, HP OmniBook 5 14" 2K OLED Touch at $449.99 saving $350 (flagged in curatorial audit #A111 for 8GB soldered memory trap & PWM flicker), ASUS Zenbook 14 OLED at $649.99 saving $350 (flagged in curatorial audit #A113 for 240Hz OLED PWM eye strain & non-upgradeable soldered RAM ceiling), Lenovo IdeaPad Pro 5 flagged in curatorial audit #A112 for soldered RAM ceiling & Modern Standby backpack drain, Dell Inspiron 14 Plus flagged in curatorial audit #A114 for 45W thermal choking & trackpad grounding defect, HP Envy x360 15 2-in-1 flagged in curatorial audit #A115 for 360-degree hinge screw-boss shear defect, touch digitizer cracking, and dim 250-nit mirror glare, ASUS Vivobook 14 2K Snapdragon at $399.99 saving $300, Lenovo IdeaPad Slim 3i 15.3" 2K Touch $429.99, LOQ 15 RTX 4060 $699.99 with rapid inventory turnover, ASUS TUF A15 RTX 4060 $679.99) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027. Walmart Black Friday Deals Event 1 clearance transitions into holiday restocking ahead of Event 2 (Nov 23) (monitoring HP Victus RTX 4050 restocks at $499; Apple MacBook Air M2 holding strong at $649; Acer Nitro V 15 RTX 4060 at $649.99). Micro Center refurbished intelligence: in-store stock active on HP EliteBook 850 G8 16GB i7 ($449.99), HP EliteBook 840 G8 16GB ($379.99), and enterprise Latitude 5530 ($409). DFS inventory sweep: Precision 3581 Grade A RTX A500 verified live with official 40% automatic clearance discount ($619; 14-core i7 SKU 000038 at $559, 2 units left); Latitude 5420 verified at 30% off (no code needed); Latitude 7440 Grade B 14" FHD+ Touch (13th Gen i5-1345U 10-core, 16GB LPDDR5, 256GB SSD) actively tracking live with coupon AF7440LATSD / LAT744044 down to $403.73 (~৳54,504 landed / ~৳51,677 bank card rate) as our #1 Sub-৳55k Modern Touch King; coupon EARLYBF50 offering 50% off small/micro desktops; coupon AF5430NOV1 offering 60% off Latitude 5430 from $239; PRECISION4U offering 40% off; Latitude 7340 32GB QHD+ holding at final 1 unit ($579), Latitude 7340 Touch at $599 (5 units), and Latitude 5530 holding at 1 unit ($409). Woot inventory sweep: Dell Latitude 7430 32GB Touch holding at $449.99, Latitude 7330 32GB at $539.99, and Lenovo ThinkPad X13 Yoga Gen 3 at $439.99 (checkout code TENOFFLAPTOP active for an additional 10% off qualifying laptops). Lenovo Official US Outlet intelligence confirms verified live promo codes: OUTLET20 (extra 20% off outlet tech through Dec 1), OUTLET15 (extra 15% off outlet), EXTRAFIVE, and YOGASEMISALE active for ThinkPad and Yoga models, including Lenovo Slim 7i Aura Intel Ultra 5 226V 14" 2K OLED Touch 16GB/1TB at $539.82 with OUTLET20.'
    content = re.sub(doorbuster_target, doorbuster_replacement, content)

    # Header and navigation references
    content = re.sub(r"from (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|168|169|170) audited listings", "from 171 audited listings", content)
    content = re.sub(r"All (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|168|169|170) Audited Deals", "All 171 Audited Deals", content)
    content = re.sub(r"56 active serialized models and (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|168|169|170) audited listings", "56 active serialized models and 171 audited listings", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")

update_dashboard(os.path.join(repo_dir, "README.md"))
update_dashboard(os.path.join(docs_dir, "DEALS_SUMMARY.md"))
print("Dashboard files updated successfully!")
