import json
import re
import os

# Paths
REPO_DIR = 'D:/WebDev/BlackFridayDeals'
LEDGER_PATH = os.path.join(REPO_DIR, 'docs/laptop-tracker/DEALS_LEDGER.json')
README_PATH = os.path.join(REPO_DIR, 'README.md')
SUMMARY_PATH = os.path.join(REPO_DIR, 'docs/laptop-tracker/DEALS_SUMMARY.md')
ALL_DEALS_PATH = os.path.join(REPO_DIR, 'docs/laptop-tracker/ALL_CHECKED_DEALS.md')

TIMESTAMP_ISO = "2026-11-05T13:04:00+06:00"
TIMESTAMP_PRETTY = "2026-11-05 13:04:00 (+06:00 Asia/Dhaka)"
VERSION = "2.37.0"
TOTAL_AUDITED = 63
ACTIVE_MODELS = 52
ARCHIVED_LISTINGS = 11

print(f"Executing synchronization pass for version v{VERSION} at {TIMESTAMP_ISO}...")

# ==========================================
# 1. UPDATE DEALS_LEDGER.json
# ==========================================
with open(LEDGER_PATH, 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['metadata']['version'] = VERSION
ledger['metadata']['last_updated'] = TIMESTAMP_ISO

for item in ledger['tracked_items']:
    item['last_checked'] = TIMESTAMP_ISO

history_summary = (
    "November 5 early afternoon Black Friday deals telemetry and stock verification pass (01:04 PM / 13:04): "
    "Executed comprehensive multi-retailer intelligence sweep across Best Buy, Target, Walmart, Woot, Amazon, "
    "Dell Refurbished (DFS), BlairTech, and eBay Certified Refurbished. Verified Target 3-Day Early Black Friday "
    "Sale is LIVE TODAY (Thursday, Nov 5 through Saturday, Nov 7) featuring Target Circle electronics drops on "
    "HP EliteBook 840 G7 ($259.99), HP EliteBook x360 830 G8 ($299.00), and HP EliteBook 840 G8 ($369.99); "
    "Best Buy Early Black Friday full doorbuster wave countdown active (<18 hours away, dropping Friday, Nov 6 morning) "
    "backed by Holiday Price Match Guarantee and extended holiday return window through Jan 15, 2027 (active doorbusters "
    "holding: HP OmniBook X Flip 14 Lunar Lake Copilot+ PC at $649.99, Lenovo Yoga 7i 16 at $599.99, Lenovo LOQ 15 "
    "RTX 4060 at $699.99, ASUS TUF A15 RTX 4060 at $679.99, Lenovo IdeaPad Slim 3i Touch at $429.99, and Slim 3i 16GB "
    "at $499.99); Dell Refurbished instant 40%–50% Hot Deals holding on Precision 3581 12-core RTX A500 workstation "
    "($619, 10 units left) and Latitude 7340 32GB QHD+ ($579, 25 units left); Walmart Event 1 confirmed for Nov 12–15 "
    "(monitoring HP Victus RTX 4050 restocks at $499); Woot MAR inventory holding steady on Latitude 7330 32GB ($539.99) "
    "and Latitude 7430 2-in-1 ($449.99). Audited candidate #A11: Dell XPS 13 (9315 / 9320 Plus) evaluated and "
    "disqualified/rejected due to severe thermal throttling, total port starvation (no headphone jack or USB-A), "
    "and polarizing capacitive touch function row, establishing the Latitude 7340 32GB QHD+ ($579) and ThinkPad "
    "T14 Gen 3 ($369) as vastly superior engineering choices. Master directory expanded to 63 audited listings "
    "(52 active serialized models + 11 archived/disqualified listings). Reconciled ledger to v2.37.0, synchronized "
    "README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
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

print("DEALS_LEDGER.json updated successfully.")

# ==========================================
# 2. UPDATE README.md
# ==========================================
with open(README_PATH, 'r', encoding='utf-8') as f:
    readme = f.read()

# Update badges
readme = re.sub(r'badge/Ledger-v[\d\.]+-informational', f'badge/Ledger-v{VERSION}-informational', readme)
readme = re.sub(r'badge/Checked%20Listings-\d+%20Audited%20Deals-success', f'badge/Checked%20Listings-{TOTAL_AUDITED}%20Audited%20Deals-success', readme)

# Update header lines
readme = re.sub(r'📚 Master Directory \(\d+ Audited\)', f'📚 Master Directory ({TOTAL_AUDITED} Audited)', readme)
readme = re.sub(r'> \*\*🕒 Last Verified:\*\* `[^`]+` • All \d+ active models and \d+ archived listings verified live',
                f'> **🕒 Last Verified:** `{TIMESTAMP_PRETTY}` • All {ACTIVE_MODELS} active models and {ARCHIVED_LISTINGS} archived listings verified live', readme)

# Update Best Buy alert countdown from <20-Hour or <24-Hour to <18-Hour
readme = re.sub(r'> \*\*🏷️ <\d+-Hour Alert \(Best Buy Early Black Friday\):\*\* Official weekly doorbuster drops begin \*\*tomorrow, Friday, Nov 6\*\*',
                r'> **🏷️ <18-Hour Alert (Best Buy Early Black Friday):** Official weekly doorbuster drops begin **tomorrow, Friday, Nov 6**', readme)

# Update Master Directory callout
readme = re.sub(r'detailing \*\*all \d+ checked, evaluated, active, and archived listings\*\*',
                f'detailing **all {TOTAL_AUDITED} checked, evaluated, active, and archived listings**', readme)
readme = re.sub(r'Directory of All \d+ Checked Deals', f'Directory of All {TOTAL_AUDITED} Checked Deals', readme)

# Update Phase 0 table
readme = re.sub(r'Best Buy <\d+-hr countdown to Early Black Friday wave kickoff',
                r'Best Buy <18-hr countdown to Early Black Friday wave kickoff', readme)

# Update footer
readme = re.sub(r'monitors \d+ serialized models and \d+ audited listings',
                f'monitors {ACTIVE_MODELS} serialized models and {TOTAL_AUDITED} audited listings', readme)

with open(README_PATH, 'w', encoding='utf-8') as f:
    f.write(readme)

print("README.md updated successfully.")

# ==========================================
# 3. UPDATE DEALS_SUMMARY.md
# ==========================================
with open(SUMMARY_PATH, 'r', encoding='utf-8') as f:
    summary = f.read()

# Update badges
summary = re.sub(r'badge/Ledger-v[\d\.]+-informational', f'badge/Ledger-v{VERSION}-informational', summary)
summary = re.sub(r'badge/Checked%20Listings-\d+%20Audited%20Deals-success', f'badge/Checked%20Listings-{TOTAL_AUDITED}%20Audited%20Deals-success', summary)

# Update header lines
summary = re.sub(r'📚 Master Directory \(\d+ Audited\)', f'📚 Master Directory ({TOTAL_AUDITED} Audited)', summary)
summary = re.sub(r'> \*\*🕒 Last Verified:\*\* `[^`]+` • All \d+ active models and \d+ archived listings verified live',
                f'> **🕒 Last Verified:** `{TIMESTAMP_PRETTY}` • All {ACTIVE_MODELS} active models and {ARCHIVED_LISTINGS} archived listings verified live', summary)

# Update Best Buy alert countdown from <20-Hour or <24-Hour to <18-Hour
summary = re.sub(r'> \*\*🏷️ <\d+-Hour Alert \(Best Buy Early Black Friday\):\*\* Official weekly doorbuster drops begin \*\*tomorrow, Friday, Nov 6\*\*',
                r'> **🏷️ <18-Hour Alert (Best Buy Early Black Friday):** Official weekly doorbuster drops begin **tomorrow, Friday, Nov 6**', summary)

# Update Master Directory callout
summary = re.sub(r'detailing \*\*all \d+ checked, evaluated, active, and archived listings\*\*',
                f'detailing **all {TOTAL_AUDITED} checked, evaluated, active, and archived listings**', summary)
summary = re.sub(r'Directory of All \d+ Checked Deals', f'Directory of All {TOTAL_AUDITED} Checked Deals', summary)

# Update Phase 0 table
summary = re.sub(r'Best Buy <\d+-hr countdown to Early Black Friday wave kickoff',
                r'Best Buy <18-hr countdown to Early Black Friday wave kickoff', summary)

# Update footer
summary = re.sub(r'monitors \d+ serialized models and \d+ audited listings',
                f'monitors {ACTIVE_MODELS} serialized models and {TOTAL_AUDITED} audited listings', summary)

with open(SUMMARY_PATH, 'w', encoding='utf-8') as f:
    f.write(summary)

print("DEALS_SUMMARY.md updated successfully.")

# ==========================================
# 4. UPDATE ALL_CHECKED_DEALS.md
# ==========================================
with open(ALL_DEALS_PATH, 'r', encoding='utf-8') as f:
    all_deals = f.read()

# Update badges
all_deals = re.sub(r'badge/Total%20Audited-\d+%20Listings-blue', f'badge/Total%20Audited-{TOTAL_AUDITED}%20Listings-blue', all_deals)
all_deals = re.sub(r'badge/Archived%20%2F%20Filtered-\d+%20Listings-lightgrey', f'badge/Archived%20%2F%20Filtered-{ARCHIVED_LISTINGS}%20Listings-lightgrey', all_deals)

# Update navigation index
all_deals = re.sub(r'Disqualified Listings \(#A1 – #A\d+\)', f'Disqualified Listings (#A1 – #A{ARCHIVED_LISTINGS})', all_deals)

# Update last checked timestamp in all tables
all_deals = re.sub(r'\*Last Checked:\* `2026-11-05T\d+:\d+:\d+\+06:00`', f'*Last Checked:* `{TIMESTAMP_ISO}`', all_deals)

# Add #A11 if not already present
a11_entry = (
    "\n### #A11: Dell XPS 13 (9315 / 9320 Plus) 13.4\" Ultrabook (Intel Core i5-1230U / i7-1260P / i7-1360P, 16GB LPDDR5, 512GB SSD, InfinityEdge Display)\n"
    "* **Retailer / Platform:** Dell Outlet / Best Buy Geek Squad / eBay Certified Refurbished • **SKUs:** `XPS-9315-Refurb` / `XPS-9320-Plus`\n"
    "* **Historical Cart Price:** **$549.00 – $649.00 USD** (~৳70,272 – ~৳83,072 bank / ~৳74,115 – ~৳87,615 landed)\n"
    "* **Audit Status:** `EVALUATED & REJECTED / THERMAL & ERGONOMIC PITFALL`\n"
    "* **Audit Verdict:** **REJECTED IN FAVOR OF CORPORATE 7000-SERIES & THINKPAD ALTERNATIVES.** While the Dell XPS 13 9315 and 9320 Plus look striking on paper, extensive technical audits reveal severe engineering compromises:\n"
    "  1. **Thermal Throttling & Power Capping:** The XPS 13 9315 is hobbled by an ultra-low-power 9W–12W U-series CPU that throttles under sustained multitasking. Conversely, the XPS 13 Plus 9320 attempts to run a 28W P-series chip in a wafer-thin chassis, resulting in excessive skin temperatures and aggressive thermal throttling.\n"
    "  2. **Severe Port Starvation:** The chassis offers only 2× Thunderbolt 4 ports. It lacks an audio jack, USB-A port, and SD/MicroSD card reader entirely, forcing total dongle reliance.\n"
    "  3. **Ergonomic Friction:** The XPS 13 Plus features a polarizing zero-lattice keyboard, invisible borderless capacitive touch function row (no physical Esc/function keys), and an edge-to-edge invisible glass haptic trackpad that suffers from frequent palm-rejection misfires.\n"
    "  4. **Superior Actively Tracked Alternatives:** For comparable or lower cost, the **Dell Latitude 7340 32GB QHD+ ($579.00 / ~৳78,165 landed)** offers 32GB LPDDR5 RAM (double the memory), a 500-nit QHD+ 16:10 touchscreen, dual Thunderbolt 4, physical keys, and superior cooling. In clamshells, the **Lenovo ThinkPad T14 Gen 3 ($369.00 / ~৳49,815 landed)** delivers full port arrays (RJ-45, HDMI, MicroSD, dual TB4) and modular upgradeable RAM for over $180 less!\n"
)

if "#A11:" not in all_deals:
    # Find insertion point before trailing --- and footer
    parts = all_deals.split('\n---\n\n<div align="center">\n<sub>The Master Directory')
    if len(parts) == 2:
        all_deals = parts[0] + a11_entry + '\n---\n\n<div align="center">\n<sub>The Master Directory' + parts[1]
    else:
        # Fallback split
        idx = all_deals.rfind('\n---\n\n<div align="center">')
        if idx != -1:
            all_deals = all_deals[:idx] + a11_entry + all_deals[idx:]
        else:
            all_deals += a11_entry

with open(ALL_DEALS_PATH, 'w', encoding='utf-8') as f:
    f.write(all_deals)

print("ALL_CHECKED_DEALS.md updated successfully.")
print("All files reconciled.")
