import json

ledger_path = 'D:/WebDev/BlackFridayDeals/docs/laptop-tracker/DEALS_LEDGER.json'
with open(ledger_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update metadata
data['metadata']['version'] = '2.33.0'
data['metadata']['last_updated'] = '2026-11-05T06:20:00+06:00'

for item in data['tracked_items']:
    iid = item.get('id', '')
    if iid == 'dell-precision-3581-rtx-dfs':
        item['title'] = 'Dell Precision 3581 15.6" Mobile Workstation - Intel Core i5-13600H - 16GB DDR5 - NVIDIA RTX A500 4GB - 512GB SSD - Grade A'
        item['gpu'] = 'NVIDIA RTX A500 Laptop GPU (4GB GDDR6 dedicated, 2048 CUDA cores, 35W-50W TGP, Ampere GA107, ISV Certified)'
        item['notes'] = (
            "High-gravity workstation outlier: DFS Hot Deal provides 40% instant discount down to $619.00 (~৳83,565 landed). "
            "Equipped with an explicit NVIDIA RTX A500 Laptop GPU (4GB GDDR6, 2,048 CUDA cores, 64 Tensor cores, 16 RT cores, "
            "35W–50W TGP, Ampere GA107, ISV-certified drivers for SolidWorks/CAD/CATIA/Revit) paired with a 12-core 45W 13th Gen "
            "Core i5-13600H (up to 4.8 GHz). Hardware features include 16GB DDR5 RAM (2x un-soldered SODIMM slots upgradeable to 64GB DDR5-5200), "
            "dual M.2 PCIe Gen 4 SSD slots, dual Thunderbolt 4 ports (full 40Gbps eGPU ready), MicroSD card slot, Grade A condition, "
            "and free ground shipping. Stock update: 10 units remaining. Grade B alternative (SKU 000047) active at $549; 14-core i7-13700H "
            "variant (SKU 000029 with NVIDIA RTX A1000 6GB GDDR6) active at $639."
        )
        item['last_checked'] = '2026-11-05T06:20:00+06:00'

    elif iid == 'dell-precision-3550-workstation':
        item['title'] = 'Dell Precision 3550 15.6" Mobile Workstation - Intel Core i5 10th Gen - 8GB/16GB - NVIDIA Quadro P520 2GB - 256GB SSD'
        item['gpu'] = 'NVIDIA Quadro P520 (2GB GDDR5 dedicated, 384 CUDA cores, 64-bit bus, 18W TGP, ISV Certified)'
        item['last_checked'] = '2026-11-05T06:20:00+06:00'

    elif iid == 'msi-gf63-thin-rtx3050':
        item['title'] = 'MSI GF63 Thin 15.6" 144Hz Gaming Laptop - Intel Core i5 - 16GB RAM - NVIDIA GeForce RTX 3050 6GB - 512GB SSD'
        item['gpu'] = 'NVIDIA GeForce RTX 3050 Laptop GPU (6GB GDDR6 dedicated, 2048 CUDA cores, 45W TGP with Dynamic Boost)'
        item['last_checked'] = '2026-11-05T06:20:00+06:00'

    elif iid == 'hp-victus-15-rtx4050-walmart':
        item['gpu'] = 'NVIDIA GeForce RTX 4050 Laptop GPU (6GB GDDR6 dedicated, 2560 CUDA cores, 75W TGP, Ada Lovelace, DLSS 3)'
        item['last_checked'] = '2026-11-05T06:20:00+06:00'

    elif iid == 'acer-nitro-v15-rtx4060':
        item['gpu'] = 'NVIDIA GeForce RTX 4060 Laptop GPU (8GB GDDR6 dedicated, 3072 CUDA cores, 75W TGP, Ada Lovelace, DLSS 3)'
        item['last_checked'] = '2026-11-05T06:20:00+06:00'

history_entry = {
    'timestamp': '2026-11-05T06:20:00+06:00',
    'summary': (
        "Hardware spec precision audit & exact GPU telemetry reconciliation (06:20 AM): "
        "Audited all discrete and integrated GPU descriptions across the entire ledger. Completely eliminated "
        "vague references like 'dedicated NVIDIA RTX GPU' or 'NVIDIA RTX Workstation'. Explicitly specified "
        "the exact GPU for Dell Precision 3581 as NVIDIA RTX A500 Laptop GPU (4GB GDDR6 dedicated, 2,048 CUDA cores, "
        "64 Tensor cores, 16 RT cores, 35W–50W TGP, Ampere GA107, ISV-certified drivers) with full telemetry comparison "
        "against mobile RTX 3050, RTX 4050, and RTX 4060. Documented the i7-13700H variant (SKU 000029 at $639) carrying "
        "the NVIDIA RTX A1000 6GB GDDR6 GPU. Reconciled Dell Precision 3550 to NVIDIA Quadro P520 2GB, MSI GF63 Thin to "
        "NVIDIA GeForce RTX 3050 6GB (45W TGP), HP Victus 15 to RTX 4050 6GB (75W TGP), and Acer Nitro V 15 to RTX 4060 8GB (75W TGP). "
        "Synchronized all telemetry in README.md, DEALS_SUMMARY.md, and ALL_CHECKED_DEALS.md."
    )
}

data['reconciled_history'].insert(0, history_entry)

with open(ledger_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print("DEALS_LEDGER.json successfully updated with exact GPU specifications!")
