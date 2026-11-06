import os
import re

FILE_PATH = "D:/WebDev/BlackFridayDeals/docs/laptop-tracker/ALL_CHECKED_DEALS.md"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update badges
content = re.sub(r"Total%20Audited-\d+%20Listings-blue", "Total%20Audited-70%20Listings-blue", content)
content = re.sub(r"Active%20Tracked-\d+%20Models-success", "Active%20Tracked-56%20Models-success", content)
content = re.sub(r"Archived%20%2F%20Filtered-\d+%20Listings-lightgrey", "Archived%20%2F%20Filtered-14%20Listings-lightgrey", content)

# 2. Update navigation index
content = re.sub(r"\(#A1 – #A\d+\)", "(#A1 – #A14)", content)

# 3. Add #56 before ## 📦 Historical Archives & Disqualified Listings
item56 = """### #56: [Lenovo ThinkPad X1 Carbon Gen 9 14.0" 16:10 WUXGA Laptop - Intel Core i5-1145G7 vPro / i7-1185G7 - 16GB RAM - 512GB SSD - Dual TB4 - Ultralight 1.13kg](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)

| Component Subsystem | Official OEM Specification & Telemetry Breakdown |
| :--- | :--- |
| **Tracking ID & SKU** | `thinkpad-x1-carbon-gen9-ebay` • **SKU:** `ThinkPad-X1-Carbon-G9` |
| **Retailer / Channel** | **eBay Certified Refurbished / Amazon Renewed** |
| **Pricing Breakdown** | **$349.00 USD** *(MSRP: $1,699.00 • Lowest Seen: $349.00)* |
| **BDT Landed Rate** | **Bank Card Settlement (~128 BDT):** ~৳44,672 BDT<br>**Realistic Landed Cost (~135 BDT):** **~৳47,115 BDT** |
| **Stock & Verification** | `IN_STOCK` • *Last Checked:* `2026-11-06T13:10:00+06:00` |
| **Processor & Silicon Architecture (CPU)** | Intel 11th Gen Tiger Lake-U Core i5-1145G7 vPro / i7-1185G7 (4 Cores / 8 Threads, 2.60 GHz base, up to 4.80 GHz Max Turbo, 12MB Intel Smart Cache, 10nm SuperFin, 12W–28W cTDP, Intel vPro Enterprise management) |
| **Graphics Subsystem (GPU & eGPU)** | Intel Iris Xe Graphics (96 Execution Units / 768 ALUs, up to 1.35 GHz, DirectX 12.1, OpenGL 4.6, QuickSync Video hardware AV1/HEVC decode, supports up to 3 external displays) • **Dual Thunderbolt 4 / USB4 (40Gbps, full eGPU support with 4 PCIe lanes)** |
| **Memory Architecture (RAM)** | 16GB LPDDR4x-4266 MHz dual-channel memory • 100% On-Board Soldered (Apex executive tier: satisfies non-negotiable 16GB protocol, zero RAM bottlenecks for multitasking) |
| **Storage Subsystem (SSD/HDD)** | 512GB PCIe Gen 4 x4 NVMe Solid State Drive • 1× M.2 2280 PCIe NVMe SSD slot (easily swappable and upgradeable up to 2TB/4TB NVMe SSD) |
| **Display Panel & Visuals** | 14.0" 16:10 WUXGA (1920x1200) Low Power IPS Anti-glare Display, 400 nits high-brightness panel, 100% sRGB color gamut, TÜV Rheinland Eyesafe hardware low blue light certified, Anti-reflective coating |
| **I/O Connectivity & Bus Speeds** | 2× Thunderbolt 4 / USB4 40Gbps (Power Delivery 3.0, DisplayPort 1.4a, full 40Gbps eGPU ready); 2× USB 3.2 Gen 1 Type-A (1 Always On); 1× HDMI 2.0b (up to 4K @ 60Hz); Intel Wi-Fi 6 AX201 + Bluetooth 5.2; 1× 3.5mm headphone/microphone combo jack |
| **Card Reader & Expandability** | None (Requires external USB-C hub / dongle) |
| **Battery, Power & Thermals** | 57Wh Lithium-Polymer battery with Rapid Charge (charges to 80% in 60 minutes) • 65W USB Type-C AC Adapter • Up to 14+ hours mixed productivity battery life • Dual-fan rear-exhaust thermal system |
| **Chassis, Materials & Durability** | Carbon fiber reinforced top cover with magnesium-aluminum unibody bottom in Deep Black / Storm Grey • Ultralight Weight: 1.13 kg (2.49 lbs) • Passed 12 MIL-STD-810H military durability methods and 26 rigorous procedures |
| **Keyboard, Trackpad & Stylus** | Legendary spill-resistant ThinkPad backlit keyboard with ergonomic dished keycaps, 1.5mm key travel • TrackPoint pointing stick with physical click buttons + large glass-surface multi-touch TrackPad • Non-touch clamshell (No stylus required) |
| **Webcam, Audio & Biometrics** | FHD 1080p + IR hybrid webcam with physical Privacy Shutter, human presence sensing (walk-away lock & wake-on-approach), Windows Hello facial recognition • Match-on-Chip Fingerprint Reader integrated into power key • Discrete TPM 2.0 chip • Dolby Atmos 4-speaker sound system (2 upward-firing tweeters + 2 downward-firing woofers) • Quad 360-degree far-field microphones |

> **🔍 Curatorial Audit & Engineering Verdict:**  
> Sub-৳48k 1.13kg Carbon Fiber Ultralight Flagship: Slashes 79%+ off original $1,699 enterprise MSRP down to $349.00 USD (~৳47,115 landed / ~৳44,672 bank card rate), entering directly into our prime sub-৳48,000 BDT sweet spot. The apex 9th-generation ThinkPad X1 Carbon features an ultralight 1.13 kg (2.49 lbs) carbon fiber and magnesium-aluminum chassis, 11th Gen Intel Core i5-1145G7 vPro / i7-1185G7 processor, 16GB LPDDR4x-4266 dual-channel memory (satisfies 16GB minimum protocol), 512GB PCIe Gen 4 NVMe SSD, modern 16:10 WUXGA 400-nit low-power 100% sRGB display, dual Thunderbolt 4 / USB4 ports (40Gbps full eGPU support), 57Wh battery with Rapid Charge (up to 14+ hours), Dolby Atmos quad speakers, quad 360-degree far-field microphones, Match-on-Chip fingerprint reader, and MIL-STD-810H durability. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty.

---

"""

archive_heading = "## 📦 Historical Archives & Disqualified Listings"
if "### #56:" not in content:
    content = content.replace(archive_heading, item56 + archive_heading)
    print("Added #56 before archives.")

# 4. Add #A14 under Historical Archives
itemA14 = """### #A14: Dell Inspiron 15 (3525 / 3535 / 3511) Budget Retail Configurations (AMD Ryzen 3 7320U / Intel Core i3, 8GB Single-Channel RAM, 256GB SSD)
* **Retailer / Platform:** Best Buy / Dell / Walmart Early Black Friday Doorbuster • **SKUs:** `i3525-3914BLK` / `i3535-A309BLK`
* **Promotional Doorbuster Price:** **$249.99 – $299.99 USD** (~৳31,999 – ~৳38,399 bank / ~৳33,749 – ~৳40,499 landed)
* **Audit Status:** `DISQUALIFIED / WEAK CHASSIS & 220-NIT TN PANEL WARNING`
* **Audit Verdict:** **REJECTED UNDER ADVERSARIAL HARDWARE & VALUE EVALUATION.** Frequently promoted during early Black Friday sales as an entry-level 15.6" notebook under $300:
  1. **Fragile Plastic Resin Hinge Mounts:** Built with thin textured plastic palmrests where metal hinge brackets are anchored into fragile plastic standoffs using single short screws. Under everyday opening/closing torque, these anchors routinely crack and separate, causing display lid failure.
  2. **Abysmal 220-Nit 45% NTSC TN Display:** Uses an inferior Twisted Nematic (TN) panel with severely washed-out colors (~60% sRGB) and terrible viewing angles where colors invert if viewed slightly off-axis, causing eyestrain during prolonged use.
  3. **No USB-C Power Delivery / DisplayPort:** Budget 3000-series motherboards lack USB-C charging, forcing users to carry proprietary 4.5mm barrel chargers. Display output is capped at HDMI 1.4 (restricted to 1080p @ 60Hz or 4K @ 30Hz), with zero Thunderbolt / eGPU capability.
  4. **8GB Single-Channel RAM & Dual/Quad-Core CPUs:** Ships with 8GB single-channel RAM and entry-level quad-core Ryzen 3 or dual/quad-core Core i3 silicon that fail our mandatory HP EliteBook 840 G8 baseline benchmark.
  5. **Superior Actively Tracked Alternatives:** For the identical $259–$299 price, the **HP EliteBook 840 G7 ($259.99 / ~৳35,099 landed)** and **Dell Latitude 7320 2-in-1 ($259.00 / ~৳34,965 landed)** offer CNC all-aluminum / carbon fiber unibody construction, 16GB dual-channel RAM, dual Thunderbolt ports (40Gbps eGPU ready), and military durability. The **HP ProBook 445 G8 ($272.99 / ~৳36,854 landed)** and **ThinkPad T14 Gen 2 ($294.27 / ~৳39,726 landed)** deliver 6-core Zen 3 compute and dual un-soldered SODIMM slots for under $300!

---
"""

if "### #A14:" not in content:
    # Insert right before footer
    footer_pattern = re.compile(r"(---\s+<div align=\"center\">\s+<sub>The Master Directory of All Checked)", re.MULTILINE)
    content = footer_pattern.sub(itemA14 + "\n<div align=\"center\">\n<sub>The Master Directory of All Checked", content)
    print("Added #A14 under archives.")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("ALL_CHECKED_DEALS.md updated successfully!")
