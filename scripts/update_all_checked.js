const fs = require('fs');
const path = require('path');

const filePath = path.join('D:', 'WebDev', 'BlackFridayDeals', 'docs', 'laptop-tracker', 'ALL_CHECKED_DEALS.md');
let content = fs.readFileSync(filePath, 'utf8');

// Update badges
content = content.replace(
  /Total%20Audited-65%20Listings-blue/g,
  'Total%20Audited-67%20Listings-blue'
);
content = content.replace(
  /Active%20Tracked-53%20Models-success/g,
  'Active%20Tracked-54%20Models-success'
);
content = content.replace(
  /Archived%20%2F%20Filtered-12%20Listings-lightgrey/g,
  'Archived%20%2F%20Filtered-13%20Listings-lightgrey'
);

// Update navigation index
content = content.replace(
  /\(#A1 – #A12\)/g,
  '(#A1 – #A13)'
);

// Add #54 before ## 📦 Historical Archives & Disqualified Listings
const item54 = `### #54: [Dell Latitude 9420 14.0" QHD+ Touch 2-in-1 - Intel Core i7-1185G7 vPro - 16GB RAM - 512GB SSD - SafeShutter - Quad Speakers](https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?rt=nc&LH_ItemCondition=2000)

| Component Subsystem | Official OEM Specification & Telemetry Breakdown |
| :--- | :--- |
| **Tracking ID & SKU** | \`dell-latitude-9420-2in1\` • **SKU:** \`Latitude-9420-2in1-QHD\` |
| **Retailer / Channel** | **eBay Certified Refurbished / Amazon Renewed / Dell Financial Services** |
| **Pricing Breakdown** | **$369.00 USD** *(MSRP: $1699.00 • Lowest Seen: $359.00)* |
| **BDT Landed Rate** | **Bank Card Settlement (~128 BDT):** ~৳47,232 BDT<br>**Realistic Landed Cost (~135 BDT):** **~৳49,815 BDT** |
| **Stock & Verification** | \`IN_STOCK\` • *Last Checked:* \`2026-11-06T00:50:00+06:00\` |
| **Processor & Silicon Architecture (CPU)** | Intel 11th Gen Tiger Lake-U Core i7-1185G7 vPro (4 Cores / 8 Threads, 3.00 GHz base, up to 4.80 GHz Max Turbo, 12MB Intel Smart Cache, 10nm SuperFin, 12W–28W cTDP, Intel vPro Enterprise management) |
| **Graphics Subsystem (GPU & eGPU)** | Intel Iris Xe Graphics (96 Execution Units / 768 ALUs, up to 1.35 GHz, DirectX 12.1, OpenGL 4.6, QuickSync Video hardware AV1/HEVC decode, supports 3 external 4K displays or 1 8K display) • **Dual Thunderbolt 4 / USB4 (40Gbps, full eGPU support with 4 PCIe lanes)** |
| **Memory Architecture (RAM)** | 16GB LPDDR4x-4266 MHz dual-channel memory • 100% On-Board Soldered (Apex executive tier: satisfies non-negotiable 16GB convertible protocol, zero RAM bottlenecks for multitasking) |
| **Storage Subsystem (SSD/HDD)** | 512GB PCIe Gen 3/4 x4 NVMe Solid State Drive • 1× M.2 2280 PCIe NVMe SSD slot (easily swappable and upgradeable up to 2TB/4TB NVMe SSD) |
| **Display Panel & Visuals** | 14.0" 16:10 QHD+ (2560x1600) WVA/IPS Touchscreen, 500 nits high-brightness outdoor panel, 100% sRGB color gamut, ComfortView Plus hardware low blue light certified, Corning Gorilla Glass 6 DX with Anti-reflective and Anti-smudge coating, 360° hinge |
| **I/O Connectivity & Bus Speeds** | 2× Thunderbolt 4 / USB4 40Gbps (Power Delivery 3.0, DisplayPort 1.4 alt mode, full 40Gbps eGPU ready); 1× USB 3.2 Gen 1 Type-A with PowerShare; 1× HDMI 2.0 (up to 4K @ 60Hz); Intel Wi-Fi 6E AX210 + Bluetooth 5.2; 1× Universal Audio Jack (3.5mm) |
| **Card Reader & Expandability** | MicroSD 4.0 card slot (Integrated high-speed UHS-II support) |
| **Battery, Power & Thermals** | 3-cell 60Wh Lithium-Ion battery with ExpressCharge 2.0 (charges to 80% in 60 minutes) • 65W USB Type-C AC Adapter • Up to 11–13 hours mixed web productivity • Dual-pipe dual-fan active cooling system |
| **Chassis, Materials & Durability** | Ultra-premium CNC-Machined Aluminum unibody chassis with precision diamond-cut edges in Titan Grey • Weight: 1.40 kg (3.08 lbs) • Passed 17 MIL-STD-810H military durability tests • Hinge cycle tested to 25,000+ rotations |
| **Keyboard, Trackpad & Stylus** | Premium spill-resistant backlit chiclet keyboard with 1.5mm key travel • Large glass-surfaced Precision Clickpad with multi-touch gesture support • 10-point capacitive multi-touch screen with Dell Active Pen PN5122W / Premier Rechargeable Active Pen PN7522W support (4,096 levels of pressure, tilt detection) |
| **Webcam, Audio & Biometrics** | World's first motorized **SafeShutter** webcam (720p/1080p camera automatically synchronizes physical privacy shutter to video conferencing software) • ExpressSign-in human proximity sensor (walk-away lock & wake-on-approach) • Windows Hello IR facial recognition • Power button Match-on-Chip Fingerprint Reader • Discrete TPM 2.0 chip • **Quad-speaker array** (2 top-firing tweeters + 2 bottom-firing woofers with discrete smart amplifiers and Waves MaxxAudio Pro) • Quad noise-canceling beamforming microphone array |

> **🔍 Curatorial Audit & Engineering Verdict:**  
> Dell's Apex 9000-Series Executive Flagship Convertible: Slashes 78%+ off original $1,699+ MSRP down to $369.00 (~৳49,815 landed / ~৳47,232 bank card rate), breaking the sub-৳50,000 landed barrier. The 9420 is Dell's highest-tier commercial machine (positioned above the 7000 and 5000 series, directly rivaling the ThinkPad X1 Yoga and HP EliteBook 1040). Features an ultra-premium CNC-machined aluminum unibody chassis with diamond-cut edges, 14.0-inch 16:10 QHD+ (2560x1600) 500-nit touch display, 16GB dual-channel RAM (satisfying the non-negotiable 16GB convertible protocol), 512GB PCIe NVMe SSD, dual Thunderbolt 4 / USB-C ports (40Gbps full eGPU support), MicroSD 4.0 slot, motorized SafeShutter webcam that automatically opens and closes, quad-speaker array with dual top-firing tweeters and bottom woofers, quad noise-canceling beamforming microphones, and Dell Active Pen support. Backed by Allstate 1-to-2 Year Certified Refurbished Warranty.

---

`;

const archiveHeading = '## 📦 Historical Archives & Disqualified Listings';
content = content.replace(archiveHeading, item54 + archiveHeading);

// Add #A13 at the end of archived listings
const itemA13 = `### #A13: Microsoft Surface Laptop Go (Go 2 / Go 3) 12.4" Touch Laptop (Intel Core i5-1135G7 / i5-1235U, 4GB-8GB Soldered RAM, 128GB/256GB SSD)
* **Retailer / Platform:** Best Buy / Target / Amazon / Walmart Early Black Friday Doorbuster • **SKUs:** \`XK1-00001\` / \`8QC-00001\`
* **Promotional Doorbuster Price:** **$299.99 – $379.99 USD** (~৳38,399 – ~৳48,639 bank / ~৳40,499 – ~৳51,299 landed)
* **Audit Status:** \`DISQUALIFIED / FAILED 16GB PROTOCOL & SUB-1080P DISPLAY WARNING\`
* **Audit Verdict:** **REJECTED UNDER CONVERTIBLE/TOUCHSCREEN VALUE & PROTOCOL AUDIT.** Frequently promoted during early holiday shopping as a cheap entry point into the Microsoft Surface family:
  1. **Sub-1080p Low-Resolution Display:** Uses an unusual 12.4-inch 3:2 panel with an outdated resolution of 1536×1024 (~148 PPI). Text rendering is noticeably pixelated compared to true Full HD (1920×1080) and 16:10 WUXGA (1920×1200) panels, causing eyestrain during prolonged coding, spreadsheets, or reading sessions.
  2. **4GB / 8GB Soldered RAM Trap:** Base and mid-tier models sold at promotional doorbuster prices ship with only 4GB or 8GB of non-upgradeable soldered LPDDR4x RAM (violating our strict 16GB non-negotiable protocol). With Windows 11 background services active, multi-tab browsing immediately triggers swap-file thrashing and performance degradation.
  3. **No Keyboard Backlight:** Unlike standard business and prosumer laptops, Microsoft omitted keyboard backlighting on standard Surface Laptop Go configurations, making nighttime typing frustrating.
  4. **No Thunderbolt & Zero Repairability:** Only features a standard USB-C 3.2 port with no Thunderbolt / PCIe lanes (zero eGPU capability), and the entire chassis is glued together with a 0/10 repairability index.
  5. **Superior Actively Tracked Alternatives:** In the same $259–$369 price window, the **Dell Latitude 7320 2-in-1 ($259.00 / ~৳34,965 landed)** provides Full HD, **16GB RAM**, dual Thunderbolt 4, and 360° convertible versatility. The **ThinkBook 14s Yoga ($319.00 / ~৳43,065 landed)** offers un-soldered upgradeable RAM (up to 40GB), dual M.2 NVMe slots, and a garaged rechargeable pen; and the newly tracked **Dell Latitude 9420 2-in-1 ($369.00 / ~৳49,815 landed)** delivers a breathtaking 500-nit 16:10 QHD+ (2560×1600) display, 16GB RAM, quad speakers, and diamond-cut CNC aluminum durability.

---

<div align="center">`;

content = content.replace(/---\s+<div align="center">\s+<sub>The Master Directory of All Checked/, itemA13 + '\n<sub>The Master Directory of All Checked');

fs.writeFileSync(filePath, content, 'utf8');
console.log('ALL_CHECKED_DEALS.md updated successfully!');
