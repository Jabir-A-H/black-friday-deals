import re

def update_file(path, is_summary=False):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update version badge
    content = content.replace('Ledger-v2.23.0', 'Ledger-v2.25.0')
    content = content.replace('Ledger-v2.24.0', 'Ledger-v2.25.0')

    # 2. Update header box
    old_header_pat = r'> \*\*🕒 Last Verified:\*\* `[^`]+` • Prices and stock verified live  \n> \*\*🎯 Strategic Focus Active:\*\* [^\n]+\n> \*\*🎃 Final Hours Alert:\*\* [^\n]+\n> \*\*🏷️ Best Buy DoorBOOsters Finale:\*\* [^\n]+\n> \*\*🎯 Target Holiday Kickoff:\*\* [^\n]+'

    new_header = (
        '> **🕒 Last Verified:** `2026-11-03 23:45:00 (+06:00 Asia/Dhaka)` • Prices and stock verified live  \n'
        '> **🎯 Strategic Focus Active:** 1) Deep research on sub-৳50k–৳55k BDT models • 2) Dedicated tracking of Touchscreen & 360° convertibles with 16GB RAM • 3) Radar on high-gravity outlier discounts (Tier 4).  \n'
        '> **🎯 48-Hour Alert (Target Early Black Friday):** Target\'s 3-day holiday electronic event launches **Thursday, Nov 5 through Nov 7** featuring rolling doorbusters.  \n'
        '> **🏷️ 72-Hour Alert (Best Buy Early Black Friday):** Official weekly doorbuster drops begin **Friday, Nov 6**, backed by Best Buy\'s Holiday Price Match Guarantee and extended holiday return window through January 15, 2027.  \n'
        '> **🏢 DFS Transition Alert:** Dell Refurbished Halloween coupon expired; instant 40%–50% Hot Deals active on Precision 3581 12-core RTX workstation ($619) and Latitude 7340 32GB QHD+ ($579).  \n'
        '> **🛒 Walmart Event 1 Confirmed:** Scheduled for **Nov 12–15** (online Nov 12 at 12:01 AM ET for Walmart+) — high alert for $499 HP Victus RTX 4050 restocks.'
    )

    content, n = re.subn(old_header_pat, new_header, content)
    if n == 0:
        print(f"Warning: header pattern not matched in {path}")

    # 3. Update Roadmap Phase 0
    old_phase0 = r'\| \*\*Phase 0: Outlet Transitions\*\* \| \*\*Nov 1 – Nov 5\*\* \*\([^\)]+\)\* \| [^|]+ \| Secure final-unit corporate clearance & doorbuster deals before coupon rotation\. \|'
    new_phase0 = (
        '| **Phase 0: Outlet Transitions** | **Nov 1 – Nov 5** *(Concluding)* | '
        '• Target 48-hr countdown to Early Black Friday (Nov 5–7).<br>'
        '• Dell Refurbished instant 40%–50% Hot Deals active post-Halloween.<br>'
        '• Best Buy 72-hr countdown to Early Black Friday wave kickoff (Nov 6).<br>'
        '• Extended holiday return windows active (Best Buy through Jan 15, 2027). | '
        'Secure enterprise clearance & prepare for Nov 5–6 major retail doorbuster drops. |'
    )
    content, n2 = re.subn(old_phase0, new_phase0, content)
    if n2 == 0:
        print(f"Warning: phase 0 pattern not matched in {path}")

    # 4. Insert Acer Swift Go 16 AI OLED into Tier 4 table if not already present
    if 'Acer Swift Go 16 AI OLED' not in content:
        swift_go_row = (
            '| **[Acer Swift Go 16 AI OLED](https://www.ebay.com/itm/257533096037)** <br>*(eBay Acer Outlet)* | '
            '**$577.88** <br>~~$999.99~~ | **~৳73,969** | **~৳78,014** | '
            'Core Ultra 5 125H (AI Boost NPU) • Intel Arc • 512GB SSD | '
            '**16GB LPDDR5X** • 71Whr Battery • Certified Refurb | '
            '**16.0" 2K/3.2K Touch OLED (100% DCI-P3 500 nits)** | `IN STOCK` *(42% Off OLED AI PC)* |\n'
        )
        # Insert after Dell Precision 3581 row
        target_marker = '| **[Dell Precision 3581]'
        idx = content.find(target_marker)
        if idx != -1:
            line_end = content.find('\n', idx)
            content = content[:line_end+1] + swift_go_row + content[line_end+1:]
        else:
            print(f"Warning: Precision 3581 marker not found in {path}")

    # 5. Update stock on Precision 3581 (10 available) and Latitude 7340 QHD+ (25 available)
    content = content.replace('*(11 Available)*', '*(10 Available)*')
    content = content.replace('*(30+ Available)*', '*(25 Available)*')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully synchronized {path}")

update_file('D:/WebDev/BlackFridayDeals/README.md', is_summary=False)
update_file('D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_SUMMARY.md', is_summary=True)
