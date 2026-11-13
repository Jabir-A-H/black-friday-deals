import glob
import re

print("Searching for any 'ebay.com' across active markdown and json files...")
hits = 0
for f in glob.glob('D:/WebDev/BlackFridayDeals/**/*', recursive=True):
    if '_discarded' in f or '.git' in f or f.endswith('.py') or f.endswith('.ps1'):
        continue
    if not (f.endswith('.md') or f.endswith('.json')):
        continue
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
    except Exception as e:
        continue
    matches = re.findall(r'ebay\.com', content, re.IGNORECASE)
    if matches:
        print(f"FOUND in {f}: {len(matches)} occurrences")
        hits += len(matches)

print(f"Total 'ebay.com' occurrences in active docs/ledger: {hits}")
