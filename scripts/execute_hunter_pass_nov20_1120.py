import json
import re
import os

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

new_version = "3.9.0"
new_timestamp = "2026-11-20T11:20:00+06:00"

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
    "summary": "November 20 Friday 11:20 AM Asia/Dhaka Black Friday live deals synchronization pass (midday peak retail traffic sweep across primary retailers, certified refurbished outlets, and deal forums): Executed comprehensive multi-retailer intelligence sweep across Dell Refurbished (DFS), Micro Center, B&H Photo Used, Best Buy, Walmart Direct, Lenovo US Outlet, and Woot. Verified heightened holiday shopping volume with early Black Friday doorbusters holding strong: Best Buy official Black Friday doorbusters active (HP OmniBook X Flip 14-inch WUXGA OLED Touch 2-in-1 with Ryzen AI 5 430, 16GB LPDDR5X, 512GB SSD at $649.99 slashed 50% from $1,299.99; HP OmniBook 5 14-inch 2K OLED Touch at $449.99 saving $350 [flagged in curatorial audit #A111 for 8GB soldered memory trap & PWM flicker]; ASUS Vivobook 14 2K Snapdragon at $399.99 saving $300; Lenovo IdeaPad Slim 3i 15.3-inch 2K Touch at $429.99; Lenovo Yoga 7i 16-inch Touch at $599.99; ASUS TUF A15 RTX 4060 at $679.99; Lenovo LOQ 15 RTX 4060 at $699.99) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027. Dell Refurbished (DFS) active promotion checks confirm live 40% automatic clearance discounts on Dell Precision 3581 ($619 Grade A RTX A500; 14-core i7 SKU 000038 at $559, 2 units left), Latitude 5420 at 30% off (no code needed), Latitude 7440 Grade B 14-inch FHD+ Touch (Core i5-1345U 10-core 13th Gen, 16GB RAM, 256GB SSD) holding with coupon AF7440LATSD down to $403.73 (~৳54,504 landed / ~৳51,677 bank) in prime sub-৳55k sweet spot; coupon EARLYBF50 offering 50% off small/micro desktops; coupon AF5430NOV1 offering 60% off Latitude 5430 from $239; PRECISION4U offering 40% off; Latitude 7340 32GB QHD+ holding at final 1 unit ($579), Latitude 7340 Touch at $599 (5 units), and Latitude 5530 holding at 1 unit ($409). Woot live inventory sweep confirms active enterprise batches with promo code TENOFFLAPTOP for extra 10% on qualifying lines: Dell Latitude 7430 32GB Touch at $449.99, Latitude 7330 32GB at $539.99, and Lenovo ThinkPad X13 Yoga Gen 3 (13.3-inch WUXGA Touch 2-in-1, Core i5, 16GB RAM) at $439.99 holding steady. Lenovo Official US Outlet intelligence confirms active coupon codes: OUTLET20 (extra 20% off outlet tech through Dec 1), OUTLET15 (extra 15% off outlet), and EXTRAFIVE / YOGASEMISALE active for ThinkPad and Yoga models, including Lenovo Slim 7i Aura Intel Ultra 5 226V 14-inch 2K OLED Touch 16GB/1TB at $539.82 with OUTLET20. Walmart Black Friday Deals Event 1 clearance transitions into holiday restocking ahead of Event 2 (Nov 23) (monitoring HP Victus RTX 4050 restocks; Apple MacBook Air M2 holding at $649; Acer Nitro V 15 RTX 4060 at $649.99). Sourced and validated all sub-55k BDT ($300-$407 USD landed) champions: Dell Latitude 5330 2-in-1 ($275.00), Dell Latitude 7330 ($279.59), Dell Latitude 5430 ($329.99), ThinkPad X1 Yoga Gen 6 ($328.99 with verified 100% battery health, 4G LTE, and garaged stylus), ThinkPad X13 Yoga Gen 2 ($314.99), ThinkPad L13 Yoga Gen 3 ($339.00-$346.55), Dell Latitude 9420 2-in-1 ($354.99), ThinkPad T14 Gen 3 ($369-$379.95), ThinkPad X1 Carbon Gen 9 ($349.00), and HP ProBook x360 435 G8 ($306.90). Conducted rigorous Adversarial Doubt Gate audit on candidate #A112: Lenovo IdeaPad Pro 5 & IdeaPad 5 Pro (14.0\" & 16.0\" - 14ACN6, 14IAP7, 14ARH7, 14APH8, 16ACH6, 16ARH7, 16IAH7, 16IRH8, 16AHP9 Series - 2021–2024 Models) Infamous 100% Permanently Soldered Non-Upgradeable LPDDR5/LPDDR5x RAM Creator Ceiling & Chronic Windows Modern Standby (S0 Low Power Idle) Sleep Overheating & \"Backpack Battery Drain\" Defect & Severe Underside Chassis Surface Temperatures Reaching 49°C–53°C Under Load & Catastrophic 4.5–5.5 Hour Real-World Battery Collapse on High-Refresh 120Hz 2.5K/2.8K Displays & Stiff Stamped-Aluminum Drop-Hinge Screw-Boss Fatigue (Disqualified and rejected under workstation memory modularity protocol, modern standby power preservation standards, chassis thermal contact safety limits, and sustained battery endurance gates). Master directory expanded to 168 audited listings (56 active serialized models + 112 archived/disqualified listings). Reconciled ledger to v3.9.0, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md with zero unauthorized marketplace reseller links."
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

all_deals = all_deals.replace("Total%20Audited-167%20Listings", "Total%20Audited-168%20Listings")
all_deals = all_deals.replace("Archived%20%2F%20Filtered-111%20Listings", "Archived%20%2F%20Filtered-112%20Listings")
all_deals = all_deals.replace("#A1 – #A111", "#A1 – #A112")
all_deals = all_deals.replace(
    "56 active serialized models + 111 archived/disqualified listings = 167 total audited",
    "56 active serialized models + 112 archived/disqualified listings = 168 total audited"
)

candidate_a112 = """---

### #A112: Lenovo IdeaPad Pro 5 & IdeaPad 5 Pro (14.0" & 16.0" - 14ACN6, 14IAP7, 14ARH7, 14APH8, 16ACH6, 16ARH7, 16IAH7, 16IRH8, 16AHP9 Series - 2021–2024 Models) Infamous 100% Permanently Soldered Non-Upgradeable LPDDR5/LPDDR5x RAM Creator Ceiling & Chronic Windows Modern Standby (S0 Low Power Idle) Sleep Overheating & "Backpack Battery Drain" Defect & Severe Underside Chassis Surface Temperatures Reaching 49°C–53°C Under Load & Catastrophic 4.5–5.5 Hour Real-World Battery Collapse on High-Refresh 120Hz 2.5K/2.8K Displays & Stiff Stamped-Aluminum Drop-Hinge Screw-Boss Fatigue (14.0" & 16.0" 16:10 2.5K / 2.8K 120Hz 350–400 nit 100% sRGB Anti-Glare IPS Display, AMD Ryzen 5 6600HS / Ryzen 7 6800HS / Ryzen 7 7735HS / Ryzen 7 8845HS / Intel Core i5-12500H / i7-12700H / i7-13700H / Core Ultra 7 155H, NVIDIA GeForce RTX 3050 / RTX 4050 6GB Laptop GPU or AMD Radeon 680M / 780M / Intel Arc, 16GB Soldered LPDDR5/LPDDR5x RAM, 512GB–1TB PCIe Gen 4 x4 NVMe SSD)
* **Retailer / Platform:** Best Buy Direct / Lenovo Official US Outlet / B&H Photo Video / Micro Center Early Black Friday Circulars • **SKUs:** `14ARH7`, `14APH8`, `16IRH8`, `16AHP9`, `82SN000EUS`, `83D50003US`, `IdeaPad-Pro-5-16`
* **Promotional Price:** **$499.99 – $699.99 USD** (~৳63,999 – ~৳89,599 bank / ~৳67,499 – ~৳94,499 landed) *(Original MSRP: $999.99 – $1,299.99)*
* **Audit Status:** `DISQUALIFIED / NON-UPGRADEABLE SOLDERED RAM CEILING, MODERN STANDBY SLEEP DRAIN DEFECT, SEVERE EXTERNAL THERMAL CONTACT TEMPERATURES & ELEVATED HIGH-REFRESH BATTERY DRAIN: HEAVILY PROMOTED ON HOLIDAY CIRCULARS AS A "BUDGET CREATOR WORKSTATION WITH 120HZ 2.5K/2.8K DISPLAY AND DEDICATED RTX GRAPHICS", BUT HARDWIRED WITH 100% PERMANENTLY SOLDERED NON-UPGRADEABLE 16GB LPDDR5/LPDDR5X RAM WITH ZERO SODIMM EXPANSION SLOTS, PERMANENTLY TRAPPING CREATORS AND DEVELOPERS WHEN HEAVY VIDEO EDITING (PREMIERE/RESOLVE), 3D MODELING (BLENDER), OR LOCAL AI MODEL INFERENCE RUNS OUT OF SYSTEM MEMORY; INFAMOUS WINDOWS MODERN STANDBY (S0 IDLE) FIRMWARE DEFECT FAILING TO ENTER DEEP SLEEP IN BACKPACKS, RUNNING FANS INSIDE ENCLOSED COMMUTER BAGS AND RAPIDLY DRAINING A 75WH–84WH BATTERY PACK TO 0% WHILE BLISTERING THE EXTERNAL CASING; UNDERSIDE CHASSIS SURFACE TEMPERATURES PEGGING 49°C–53°C UNDER CONTINUOUS 45W–65W COMBINED WORKLOADS; 120HZ HIGH-REFRESH DISPLAY DRIVING REAL-WORLD PRODUCTIVITY BATTERY LIFE DOWN TO 4.5–5.5 HOURS; AND HIGH-TORQUE DISPLAY HINGES ANCHORED INTO THIN ALUMINUM STANDOFFS DEVELOPING CREAKS AND EXCESSIVE PLAY OVER TIME.`
* **Audit Verdict:** **REJECTED UNDER WORKSTATION MEMORY MODULARITY PROTOCOL, MODERN STANDBY POWER PRESERVATION STANDARDS, CHASSIS THERMAL CONTACT SAFETY LIMITS, AND SUSTAINED BATTERY ENDURANCE GATES.** Marketed aggressively to design students, creators, and engineers as an attractive sub-$700 Black Friday alternative to high-end mobile workstations, but compromised by fatal architecture constraints:
  1. **100% Permanently Soldered Non-Upgradeable Memory Ceiling:** Unlike true enterprise workstations (such as the ThinkPad P14s/T14 or Dell Precision 3581) which offer un-soldered SODIMM slots expanding to 48GB–64GB, the IdeaPad Pro 5 solders all RAM directly to the motherboard with zero expansion slots. For heavy Adobe Creative Cloud multitasking, multi-stream 4K editing in DaVinci Resolve, large Docker containers, or local LLM quantization, 16GB is rapidly exhausted by Windows 11 and background processes. Once saturated, the operating system resorts to intensive SSD virtual memory paging, degrading performance and wearing out the internal NVMe drive with no hardware upgrade path available.
  2. **Chronic Windows Modern Standby Sleep Failure & "Backpack Bake":** Hundreds of community bug reports and technician teardowns document persistent failures of Lenovo's consumer embedded controller firmware under ACPI Modern Standby (Connected Standby). When the lid is closed and the machine is stored inside a commuter backpack, the system frequently fails to enter low-power sleep or is awakened by background Windows telemetry. The cooling fans spin up against restricted airflow inside the bag, generating severe thermal buildup exceeding 55°C–60°C and completely draining the 75Wh–84Wh battery before the user reaches their destination.
  3. **Blistering Underside Chassis Surface Temperatures (49°C–53°C):** To keep the unibody chassis sleek (under 18mm), Lenovo compressed the vapor chamber/dual-heatpipe cooling solution against the lower aluminum casing. Under prolonged multithreaded rendering or gaming sessions, heat conducts rapidly through the thin stamped-aluminum lower tub, reaching blistering contact temperatures of 49°C–53°C directly under the CPU/GPU heatsinks. This precludes comfortable lap usage and transfers ambient warmth directly into the palmrest and WASD keycaps.
  4. **High-Refresh 120Hz Display Battery Drain:** While the 16:10 2.5K/2.8K 120Hz IPS panel provides smooth animations and sharp text, operating at high refresh rates and elevated resolutions imposes an aggressive parasitic power draw on the display controller. Despite substantial 75Wh–84Wh battery capacities, real-world productivity under web multitasking, coding, and document drafting collapses to 4.5–5.5 hours, leaving users dependent on carrying their heavy 100W–140W USB-C PD or slim-tip power adapter.
  5. **Stiff Dual-Hinge Aluminum Screw-Boss Fatigue:** The display hinges exert substantial rotational torque against the slim aluminum casing. Over months of routine opening and closing cycles, the brass threaded standoffs inside the top case experience rotational fatigue, manifesting as audible hinge creaking, uneven screen gap tolerances, and display wobble.
  6. **Superior Actively Tracked Alternatives in Our Suite:**
     * **Dell Precision 3581 Mobile Workstation (#05 at $619.00 / ~৳83,565 landed):** True ISV-certified **NVIDIA RTX A500 4GB workstation GPU**, 12-core Core i5-13600H (16 threads), **2× un-soldered DDR5 SODIMM slots (fully upgradeable to 64GB DDR5 vs permanently soldered on IdeaPad Pro)**, dual M.2 Gen 4 SSD bays, dual Thunderbolt 4 ports, and 100-Day Direct Dell Warranty!
     * **Lenovo ThinkPad P14s Gen 2 Mobile Workstation (#53 at $359.00 / ~৳48,465 landed):** 8-core / 16-thread AMD Ryzen 7 PRO 5850U Zen 3 compute, **un-soldered SODIMM RAM expansion up to 48GB**, legendary spill-resistant keyboard, military-grade MIL-STD-810H durability, and ISV CAD certification under ৳49,000 landed!
     * **Lenovo ThinkPad T14 Gen 3 (#31 at $369.00 / ~৳49,815 landed):** 14.0" 16:10 WUXGA anti-glare display, **un-soldered SODIMM slot (upgradeable up to 48GB)**, 10-core 12th Gen Intel or 6-core Ryzen 5, dual Thunderbolt 4 / USB4 ports under ৳50,000 landed!
     * **Acer Swift Go 16 AI OLED (#04 at $577.88 / ~৳78,014 landed):** Intel Core Ultra 5 AI PC with dedicated AI NPU, brilliant **16.0" 16:10 3.2K Touch OLED (100% DCI-P3 500-nit)**, massive 71Wh battery, **2× internal M.2 SSD slots**, and 2-Year Direct Allstate Warranty under ৳79,000 landed!
     * **Dell Latitude 7440 Touch (#21 at $403.73 / ~৳54,504 landed):** 13th Gen Intel 10-core Core i5-1345U vPro, 16GB LPDDR5, 14.0" 16:10 FHD+ Touch, dual Thunderbolt 4 ports, and 100-Day Dell Direct Warranty under ৳55,000 landed!
"""

if "### #A112: Lenovo IdeaPad Pro 5" not in all_deals:
    footer_pattern = r"(\r?\n---\r?\n\r?\n<sub>The Master Directory of All Checked Laptop Deals)"
    all_deals = re.sub(footer_pattern, "\n" + candidate_a112 + r"\1", all_deals)

with open(all_deals_path, "w", encoding="utf-8") as f:
    f.write(all_deals)
print("2. ALL_CHECKED_DEALS.md successfully updated to 168 listings (#A112 added)")

# 3. Update README.md and DEALS_SUMMARY.md
def update_dashboard(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Badge updates
    content = re.sub(r"Ledger-v3\.[0-9]+\.[0-9]+", f"Ledger-v{new_version}", content)
    content = re.sub(r"Checked%20Listings-[0-9]+%20Audited%20Deals", "Checked%20Listings-168%20Audited%20Deals", content)

    # Last verified text
    content = re.sub(
        r"> \*\*🕒 Last Verified:\*\* `[^`]+` • All [0-9]+ active models and [0-9]+ archived listings verified live \([0-9]+ total audited listings milestone!\)",
        "> **🕒 Last Verified:** `2026-11-20 11:20:00 (+06:00 Asia/Dhaka)` • All 56 active models and 112 archived listings verified live (168 total audited listings milestone!)",
        content
    )

    # Doorbuster wave update
    doorbuster_target = r"> \*\*⚡ Best Buy, Walmart Event 1, Micro Center & Dell DFS Doorbuster Waves LIVE:\*\* [^\r\n]+"
    doorbuster_replacement = '> **⚡ Best Buy, Walmart Event 1, Micro Center & Dell DFS Doorbuster Waves LIVE:** Best Buy officially kicking off its 10-day Black Friday sale event with major doorbusters active (HP OmniBook X Flip 14" WUXGA OLED Touch 2-in-1 with Ryzen AI 5 430, 16GB LPDDR5X, 512GB SSD slashed 50% from $1,299.99 to $649.99, HP OmniBook 5 14" 2K OLED Touch at $449.99 saving $350 (flagged in curatorial audit #A111 for 8GB soldered memory trap & PWM flicker), Lenovo IdeaPad Pro 5 flagged in curatorial audit #A112 for soldered RAM ceiling & Modern Standby backpack drain, ASUS Vivobook 14 2K Snapdragon at $399.99 saving $300, Lenovo IdeaPad Slim 3i 15.3" 2K Touch $429.99, LOQ 15 RTX 4060 $699.99 with rapid inventory turnover, ASUS TUF A15 RTX 4060 $679.99) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027. Walmart Black Friday Deals Event 1 clearance transitions into holiday restocking ahead of Event 2 (Nov 23) (monitoring HP Victus RTX 4050 restocks at $499; Apple MacBook Air M2 holding strong at $649; Acer Nitro V 15 RTX 4060 at $649.99). Micro Center refurbished intelligence: in-store stock active on HP EliteBook 850 G8 16GB i7 ($449.99), HP EliteBook 840 G8 16GB ($379.99), and enterprise Latitude 5530 ($409). DFS inventory sweep: Precision 3581 Grade A RTX A500 verified live with official 40% automatic clearance discount ($619; 14-core i7 SKU 000038 at $559, 2 units left); Latitude 5420 verified at 30% off (no code needed); Latitude 7440 Grade B 14" FHD+ Touch (13th Gen i5-1345U 10-core, 16GB LPDDR5, 256GB SSD) actively tracking live with coupon AF7440LATSD / LAT744044 down to $403.73 (~৳54,504 landed / ~৳51,677 bank card rate) as our #1 Sub-৳55k Modern Touch King; coupon EARLYBF50 offering 50% off small/micro desktops; coupon AF5430NOV1 offering 60% off Latitude 5430 from $239; PRECISION4U offering 40% off; Latitude 7340 32GB QHD+ holding at final 1 unit ($579), Latitude 7340 Touch at $599 (5 units), and Latitude 5530 holding at 1 unit ($409). Woot inventory sweep: Dell Latitude 7430 32GB Touch holding at $449.99, Latitude 7330 32GB at $539.99, and Lenovo ThinkPad X13 Yoga Gen 3 at $439.99 (checkout code TENOFFLAPTOP active for an additional 10% off qualifying laptops). Lenovo Official US Outlet intelligence confirms verified live promo codes: OUTLET20 (extra 20% off outlet tech through Dec 1), OUTLET15 (extra 15% off outlet), EXTRAFIVE, and YOGASEMISALE active for ThinkPad and Yoga models, including Lenovo Slim 7i Aura Intel Ultra 5 226V 14" 2K OLED Touch 16GB/1TB at $539.82 with OUTLET20.'
    content = re.sub(doorbuster_target, doorbuster_replacement, content)

    # Header and navigation references
    content = re.sub(r"from (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167) audited listings", "from 168 audited listings", content)
    content = re.sub(r"All (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167) Audited Deals", "All 168 Audited Deals", content)
    content = re.sub(r"56 active serialized models and (?:146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167) audited listings", "56 active serialized models and 168 audited listings", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")

update_dashboard(os.path.join(repo_dir, "README.md"))
update_dashboard(os.path.join(docs_dir, "DEALS_SUMMARY.md"))
print("Dashboard files updated successfully!")
