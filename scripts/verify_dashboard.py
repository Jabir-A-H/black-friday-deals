import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"

for filename in ["README.md", "docs/laptop-tracker/DEALS_SUMMARY.md"]:
    filepath = os.path.join(WORKSPACE, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"=== Checking {filename} ===")
    assert content.count("\ufffd") == 0, f"Found replacement chars in {filename}"
    
    # Check serial numbers in tables
    serials = re.findall(r'\|\s*\*\*#(\d+)\*\*\s*\|', content)
    print("Found table serials count:", len(serials))
    expected_serials = [f"{i:02d}" if i <= 10 else f"{i}" for i in range(1, 56)]
    assert len(serials) == 55, f"Expected 55 rows, got {len(serials)}"
    print("Min serial:", serials[0], "Max serial:", serials[-1])
    
    # Check champions table
    champions = re.findall(r'\|\s*(👑|✍️|🏆|💎|🛠️|🔄|☀️|🦄|🏗️|🎮)\s*\*\*.*?\*\*\s*\|', content)
    print("Found champions count:", len(champions))
    assert len(champions) == 10, f"Expected 10 champions, got {len(champions)}"

print("\nALL DASHBOARD VERIFICATIONS PASSED CLEANLY!")
