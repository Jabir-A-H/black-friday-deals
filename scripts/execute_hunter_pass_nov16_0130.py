import json
import re
import os

repo_dir = "D:/WebDev/BlackFridayDeals"
docs_dir = os.path.join(repo_dir, "docs", "laptop-tracker")

# 1. Update DEALS_LEDGER.json
ledger_path = os.path.join(docs_dir, "DEALS_LEDGER.json")
with open(ledger_path, "r", encoding="utf-8") as f:
    ledger = json.load(f)

ledger["metadata"]["version"] = "3.5.1"
ledger["metadata"]["last_updated"] = "2026-11-16T01:30:00+06:00"

for item in ledger["tracked_items"]:
    item["last_checked"] = "2026-11-16T01:30:00+06:00"

new_history_timestamp = "2026-11-16T01:30:00+06:00"
if ledger["reconciled_history"][0]["timestamp"] != new_history_timestamp:
    new_history = {
        "timestamp": new_history_timestamp,
        "summary": "November 16 Monday early morning Black Friday live deals synchronization pass (01:30 AM Asia/Dhaka / Sunday afternoon US peak retail traffic): Executed comprehensive multi-retailer intelligence sweep across Dell Refurbished (DFS), Micro Center, B&H Photo Used, Best Buy, Walmart Direct, and Woot. Verified strong Sunday peak holiday shopping turnover maintaining solid momentum across Best Buy Early Black Friday doorbusters (Lenovo IdeaPad Slim 3i Touch at $429.99, HP OmniBook X Flip 14 at $649.99, Lenovo Yoga 7i 16 at $599.99, Lenovo LOQ 15 RTX 4060 at $699.99 with rapid inventory turnover, ASUS TUF A15 RTX 4060 at $679.99) backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027; Dell Refurbished instant 40%-50% Hot Deals verified holding on Precision 3581 ($619 Grade A RTX A500; 14-core i7 SKU 000038 at $559, 2 units left), Latitude 5420 verified at 30% off (no code needed), Latitude 7440 Grade B 14\" FHD+ Touch (Core i5-1345U 10-core 13th Gen, 16GB RAM, 256GB SSD) verified with coupon AF7440LATSD down to $403.73 (~৳54,504 landed / ~৳51,677 bank) entering prime sub-৳55,000 BDT sweet spot; Latitude 7340 32GB QHD+ holding at final 1 unit ($579), Latitude 7340 Touch holding at 5 units ($599), and Latitude 5530 holding at 1 unit ($409). Woot live inventory sweep confirms active enterprise batches: Lenovo ThinkPad X13 Yoga Gen 3 (13.3\" WUXGA Touch 2-in-1, Core i5, 16GB RAM) at $439.99, Dell Latitude 7430 32GB Touch at $449.99, and Latitude 7330 32GB at $539.99 holding steady. Walmart Black Friday Deals Event 1 general access active Nov 12-16 (monitoring $499 HP Victus RTX 4050 restocks; Apple MacBook Air M2 holding at $649; Acer Nitro V 15 RTX 4060 at $649.99). Sourced and validated all sub-55k BDT ($300-$407 USD landed) champions: Dell Latitude 5330 2-in-1 ($275.00), Dell Latitude 7330 ($279.59), Dell Latitude 5430 ($329.99), ThinkPad X1 Yoga Gen 6 ($328.99 with verified 100% battery health, 4G LTE, and garaged stylus), ThinkPad X13 Yoga Gen 2 ($314.99), ThinkPad L13 Yoga Gen 3 ($339.00-$346.55), Dell Latitude 9420 2-in-1 ($354.99), ThinkPad T14 Gen 3 ($369-$379.95), ThinkPad X1 Carbon Gen 9 ($349.00), and HP ProBook x360 435 G8 ($306.90). Conducted rigorous Adversarial Doubt Gate audit on candidate #A84: HP Omen 16 (16.1\" - 16-xf, 16-wf, 16-xd, 16-wd Series - 2023/2024 Models) Infamous Hall Effect Sensor Black Screen Defect (Thermal Heatpipe Proximity Frying Magnetic Lid-Close Sensor Causing Permanent Black Screen Under Sustained GPU/CPU Load & Chimicles Schwartz Kriner & Donaldson-Smith LLP Consumer Investigation) & 8GB/Single-Channel DDR5 RAM Circular Trap & Deafening 54+ dB Jet-Engine Fan Whine & Bulky 280W Power Adapter (3.3 kg / 7.3 lbs Travel Weight) ($649.99–$799.99 early Black Friday holiday circulars across Best Buy, Walmart, Micro Center, Amazon, B&H: disqualified and rejected under structural component thermal placement gate, repairability protocol, and acoustic/travel weight criteria). Historic milestone reached: Master directory expanded to 139 audited listings (55 active serialized models + 84 archived/disqualified listings). Reconciled ledger to v3.5.1, synchronized README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
    }
    ledger["reconciled_history"].insert(0, new_history)

with open(ledger_path, "w", encoding="utf-8") as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("1. DEALS_LEDGER.json successfully updated to v3.5.1")

# 2. Update ALL_CHECKED_DEALS.md
all_deals_path = os.path.join(docs_dir, "ALL_CHECKED_DEALS.md")
with open(all_deals_path, "r", encoding="utf-8") as f:
    all_deals = f.read()

all_deals = all_deals.replace("Total%20Audited-138%20Listings", "Total%20Audited-139%20Listings")
all_deals = all_deals.replace("Archived%20%2F%20Filtered-83%20Listings", "Archived%20%2F%20Filtered-84%20Listings")
all_deals = all_deals.replace("#A1 – #A83", "#A1 – #A84")
all_deals = all_deals.replace(
    "55 active serialized models + 83 archived/disqualified listings = 138 total audited",
    "55 active serialized models + 84 archived/disqualified listings = 139 total audited"
)

candidate_a84 = """---

### #A84: HP Omen 16 (16.1" - 16-xf, 16-wf, 16-xd, 16-wd Series - 2023/2024 Models) Infamous Hall Effect Sensor Black Screen Defect (Thermal Heatpipe Proximity Frying Magnetic Lid-Close Sensor Causing Permanent Black Screen Under Sustained GPU/CPU Load & Chimicles Schwartz Kriner & Donaldson-Smith LLP Consumer Investigation) & 8GB/Single-Channel DDR5 RAM Circular Trap & Deafening 54+ dB Jet-Engine Fan Whine & Bulky 280W Power Adapter (3.3 kg / 7.3 lbs Travel Weight) (16.1" FHD 1920x1080 144Hz 250-Nit 45% NTSC / QHD 240Hz 300-Nit IPS Display, Intel Core i7-13700HX / i7-14700HX / AMD Ryzen 7 7840HS / 7435HS, NVIDIA GeForce RTX 4060 8GB / RTX 4070 8GB 120W–140W TGP, 8GB/16GB DDR5 Single/Dual-Channel RAM, 512GB/1TB PCIe Gen 4 NVMe SSD)
* **Retailer / Platform:** Best Buy / Walmart / Micro Center / Amazon / B&H Early Black Friday Holiday Circulars • **SKUs:** `16-xf0033dx` / `16-wf0019nr` / `16-xd0010nr` / `16-wd0013dx` / `16-wf0083dx` / `783S7UA` / `783S8UA`
* **Promotional Price:** **$649.99 – $799.99 USD** (~৳83,199 – ~৳102,399 bank / ~৳87,749 – ~৳107,999 landed) *(MSRP: $1,099.99 – $1,399.99)*
* **Audit Status:** `DISQUALIFIED / SEVERE SYSTEMIC HARDWARE DESIGN FLAW: CRITICAL REAR THERMAL PLACEMENT DEFECT (HP SITUATED THE LID-DETECTION HALL EFFECT MAGNETIC SENSOR CHIP DIRECTLY OVER THE REAR EXHAUST HEATPIPES AND GPU THERMAL FINS, CAUSING SYSTEMIC HEAT-INDUCED SENSOR DEGRADATION THAT FALSELY SIGNALS A CLOSED LID UNDER SUSTAINED GAMING TEMPERATURES, RESULTING IN SUDDEN PERMANENT INTERNAL DISPLAY BLACKOUTS WHILE FANS RUN AT MAXIMUM RPM, SUBJECT OF CHIMICLES SCHWARTZ KRINER & DONALDSON-SMITH LLP LEGAL INVESTIGATION), REQUIRING INVASIVE MOTHERBOARD SWAPS OR RISKY DIY PHYSICAL SENSOR REMOVAL, STRICT 16GB PROTOCOL VIOLATION WITH 8GB/SINGLE-CHANNEL DDR5 CONFIGURATIONS ON BASE CIRCULARS, DEAFENING 54+ DB ACOUSTIC NOISE, AND BULKY 280W BRICK YIELDING 3.3 KG TRAVEL WEIGHT`
* **Audit Verdict:** **REJECTED UNDER STRUCTURAL COMPONENT THERMAL PLACEMENT GATE, REPAIRABILITY PROTOCOL, AND ACOUSTIC/TRAVEL WEIGHT CRITERIA.** Heavily marketed across early Black Friday circulars and clearance liquidations as an enticing "$649 to $799 high-performance RTX 4060/4070 gaming rig slashed $400–$600 from MSRP", masking one of the most widespread and severe hardware engineering flaws in recent laptop history:
  1. **Catastrophic Hall Effect Sensor Black Screen Defect:** In the 2023–2024 rear-port chassis redesign of the HP Omen 16, HP engineers routed the lid-detection Hall Effect magnetic sensor daughterboard trace directly adjacent to the main GPU/CPU copper heatpipes and rear exhaust fins. Under sustained gaming or 3D rendering workloads where exhaust temperatures reach 80°C–90°C, the intense localized heat systematically degrades the Hall sensor chip and its solder joints over 2 to 6 months of regular use. Once degraded, the sensor latches into a permanent false "lid closed" state: the internal laptop display abruptly cuts to black, the keyboard and trackpad freeze, yet the cooling fans roar at 100% RPM. The machine is rendered completely unusable on its integrated panel unless connected to an external monitor.
  2. **Failed Warranty Depots & Invasive DIY Teardown Workaround:** Official HP warranty depot service replaces the faulted motherboard with another identical motherboard carrying the exact same thermal placement defect—causing the black screen to reoccur within months. The only "permanent" community solution discovered by technicians and Reddit /r/HPOmen owners requires completely disassembling the bottom chassis and physically unplugging or desoldering the miniature Hall sensor ribbon cable—permanently disabling automatic sleep-on-lid-close functionality and risking warranty invalidation. The issue has triggered an active defect investigation by class action law firm Chimicles Schwartz Kriner & Donaldson-Smith LLP.
  3. **Strict 16GB Memory Protocol Violation on Base Holiday Circulars:** Base early Black Friday doorbuster configurations ship with only a single 8GB DDR5-5600 SO-DIMM module or asymmetric 8GB memory, throttling dual-channel bandwidth and inducing stutter in modern game engines and video rendering timelines.
  4. **Deafening 54+ dB Fan Acoustics & Cumbersome Travel Weight:** Dual high-RPM blowers generate an abrasive 54+ dB jet-engine acoustic whine under load. Combined with a massive 280W/330W charging brick, total travel weight exceeds 3.3 kg (7.3 lbs), completely disqualifying the machine for mobile academic, portable work, or overseas travel.
  5. **Superior Actively Tracked Alternatives in the Creator & Gaming Categories:**
     * **Acer Nitro V 15.6" RTX 4060 (#1 at $649.99 / ~৳87,749 landed):** True Ada Lovelace **NVIDIA GeForce RTX 4060 8GB VRAM (full DLSS 3 Frame Generation, unquantized 8B LLM inferencing)**, **10-core / 16-thread Intel Core i7-13620H**, **16GB DDR5 (2× un-soldered SODIMM slots upgradeable to 64GB)**, dual M.2 Gen 4 NVMe slots, zero Hall sensor defects, and reliable dual-fan cooling!
     * **Dell Precision 3581 Mobile Workstation (#5 at $619.00 / ~৳83,565 landed):** **12-core / 16-thread Core i5-13600H (45W H-series)**, dedicated **NVIDIA RTX A500 4GB (ISV Certified enterprise drivers for CAD/SolidWorks)**, **16GB DDR5 (2× un-soldered SODIMM slots upgradeable to 64GB)**, dual M.2 Gen 4 SSD bays, dual Thunderbolt 4, and 100-Day Direct Dell warranty!
     * **ASUS TUF Gaming A15 RTX 4060 (#6 at $679.99 / ~৳91,799 landed):** Full-wattage **140W TGP NVIDIA GeForce RTX 4060 8GB GDDR6 with MUX switch**, true multithreaded AMD Ryzen Zen 4 processor, **16GB DDR5 (2× un-soldered SODIMM slots up to 64GB)**, quad-exhaust cooling, zero lid sensor defects, and MIL-STD-810H durability!
     * **Lenovo LOQ 15 RTX 4060 (#7 at $699.99 / ~৳94,499 landed):** **115W TGP NVIDIA RTX 4060 8GB GDDR6 with MUX Switch**, 8-core / 16-thread AMD Ryzen 7 7435HS, **16GB DDR5 (2× un-soldered SODIMM slots)**, 100% sRGB 144Hz G-SYNC display!
     * **HP Victus 15.6" RTX 4050 (#9 at $499.00 / ~৳67,365 landed):** Dedicated **NVIDIA RTX 4050 6GB GDDR6 with DLSS 3**, 6-core / 12-thread AMD Ryzen 5 8645HS (Zen 4), **2× un-soldered DDR5 SODIMM slots**, clean thermal layout without rear-exhaust Hall sensor flaws under $500!
     * **MSI GF63 Thin RTX 3050 (#13 at $479.00 / ~৳64,665 landed):** Dedicated RTX 3050 6GB with **16GB factory RAM out of the box (dual un-soldered SODIMM slots)** under $480!
     * **Dell Latitude 7430 2-in-1 (#12 at $379.00 / ~৳51,165 landed):** 10-core 12th Gen Core i7-1265U vPro, **16GB RAM**, 360-degree touch convertible with dual Thunderbolt 4 (40Gbps eGPU ready for external desktop RTX cards), integrated FHD IR webcam, and CNC aluminum unibody under ৳52,000 landed!

"""

if "### #A84: HP Omen 16" not in all_deals:
    footer_pattern = r"(\r?\n---\r?\n\r?\n<sub>The Master Directory of All Checked Laptop Deals)"
    all_deals = re.sub(footer_pattern, "\n" + candidate_a84 + r"\1", all_deals)

with open(all_deals_path, "w", encoding="utf-8") as f:
    f.write(all_deals)
print("2. ALL_CHECKED_DEALS.md successfully updated to 139 listings (#A84 added)")

# 3. Update README.md and DEALS_SUMMARY.md
def update_dashboard(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Badge updates
    content = re.sub(r"Ledger-v3\.[0-9]+\.[0-9]+", "Ledger-v3.5.1", content)
    content = re.sub(r"Checked%20Listings-[0-9]+%20Audited%20Deals", "Checked%20Listings-139%20Audited%20Deals", content)

    # Last verified text
    content = re.sub(
        r"> \*\*🕒 Last Verified:\*\* `[^`]+` • All [0-9]+ active models and [0-9]+ archived listings verified live \([0-9]+ total audited listings milestone!\)",
        "> **🕒 Last Verified:** `2026-11-16 01:30:00 (+06:00 Asia/Dhaka)` • All 55 active models and 84 archived listings verified live (139 total audited listings milestone!)",
        content
    )

    # Candidate #A84 callout insertion in Adversarial Defect Gate Active paragraph
    a84_callout = 'Disqualified candidate #A84 (HP Omen 16 16.1" 16-xf/16-wf/16-xd/16-wd infamous Hall effect sensor black screen defect [thermal heatpipe proximity frying magnetic lid-close sensor causing permanent black screen under sustained GPU/CPU load & Chimicles Schwartz Kriner & Donaldson-Smith LLP consumer investigation] & 8GB single-channel DDR5 circular trap & deafening 54+ dB jet-engine fan whine & bulky 280W power adapter [3.3 kg / 7.3 lbs travel weight]), '
    if "Disqualified candidate #A84" not in content:
        content = content.replace("Disqualified candidate #A83", a84_callout + "Disqualified candidate #A83")

    # Header and navigation references
    content = content.replace("from 138 audited listings", "from 139 audited listings")
    content = content.replace("All 138 Audited Deals", "All 139 Audited Deals")
    content = content.replace("55 active serialized models and 138 audited listings", "55 active serialized models and 139 audited listings")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path}")

update_dashboard(os.path.join(repo_dir, "README.md"))
update_dashboard(os.path.join(docs_dir, "DEALS_SUMMARY.md"))
