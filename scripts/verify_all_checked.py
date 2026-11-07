import re
import os

WORKSPACE = "D:/WebDev/BlackFridayDeals"
filepath = os.path.join(WORKSPACE, "docs/laptop-tracker/ALL_CHECKED_DEALS.md")

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

print("=== Checking ALL_CHECKED_DEALS.md ===")
assert content.count("\ufffd") == 0, "Found replacement chars in ALL_CHECKED_DEALS.md"

active_items = re.findall(r'### (#\d+): \[(.*?)\]', content)
archived_items = re.findall(r'### (#A\d+): (.*)', content)

print("Active items count:", len(active_items))
print("Archived items count:", len(archived_items))
print("Total audited:", len(active_items) + len(archived_items))

assert len(active_items) == 55, f"Expected 55 active items, got {len(active_items)}"
assert len(archived_items) == 23, f"Expected 14 archived items, got {len(archived_items)}"

# Check badges
assert "Total%20Audited-78%20Listings" in content, "Missing Total Audited badge"
assert "Active%20Tracked-55%20Models" in content, "Missing Active Tracked badge"
assert "Archived%20%2F%20Filtered-23%20Listings" in content, "Missing Archived badge"

print("\nALL_CHECKED_DEALS.md VERIFICATION PASSED CLEANLY!")
