# Automated Deal-Tracker Specification & Multi-Tier Budget Protocol

## 🎯 Purpose & Scope
This specification defines the multi-tier financial framework and operational contract for the deal tracking suite. Deals are segmented into 4 distinct budget brackets to give a complete strategic picture—from ultra-budget workhorses to high-gravity outlier discounts.

---

## 💰 Multi-Tier Budget Brackets & Effective Currency Conversion Model

### 1. Exchange Rate & Landed Cost Breakdown
To accurately represent real purchasing cost in Bangladesh, we track three distinct rate layers:
* **Layer 1: Mid-Market Rate (`1 USD ≈ 124.0 BDT`):** Official Bangladesh Bank & Google/XE mid-market benchmark.
* **Layer 2: Bank Card Settlement Rate (`1 USD ≈ 128.0 BDT`):** Commercial bank card selling rate (~124.50 BDT) + 1.5%–2% cross-border FX markup + 15% VAT on service charges. Used when shipping to a tax-free US address (e.g. Delaware/Oregon) via traveler.
* **Layer 3: Realistic Landed Cost Rate (`1 USD ≈ 135.0 BDT`):** Bank settlement rate + US average state/city sales tax (~6%–8.875%) + transfer/handling buffer. **This is our primary realistic planning benchmark.**

### 2. Multi-Tier Financial Brackets

| Bracket | Price Envelope (USD) | Bank Settlement (1 USD ≈ 128 BDT) | Realistic Landed Cost (1 USD ≈ 135 BDT) | Hardware Target & Archetype |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 4: "Gravity" Stretchers** | **$550 – $699 USD** | **৳70,400 – ৳89,500 BDT** | **৳74,250 – ৳94,500 BDT** | **High-Gravity Outliers:** Laptops slashed 40%–50% from $1,000–$1,400 MSRP. Unlocks **NVIDIA RTX 4060 (8GB VRAM)**, 32GB RDNA3 Zen 4 ThinkPads, or MacBook Air M2. Worth breaking budget for. |
| **Tier 1: High Budget** | **$450 – $550 USD** | **৳57,600 – ৳70,400 BDT** | **৳60,750 – ৳74,250 BDT** | **Apex Powerhouse Tier:** Dedicated NVIDIA RTX 4050 / RTX 3050 GPUs, 10-core Core i7s, 16GB factory RAM, and un-soldered DDR5 SODIMM slots. |
| **Tier 2: Mid Budget** | **$350 – $450 USD** | **৳44,800 – ৳57,600 BDT** | **৳47,250 – ৳60,750 BDT** | **Touchscreen & 32GB RAM Sweet Spot:** Dell Inspiron 15 Touch with dual SODIMM slots, Dell Latitude 5320 2-in-1 with 32GB RAM, and 11th Gen Core i7 Latitudes with 40-50% coupons. |
| **Tier 3: Value / Under $350** | **$200 – $350 USD** | **৳25,600 – ৳44,800 BDT** | **৳27,000 – ৳47,250 BDT** | **Extreme Budget Bargains:** Precision workstations with dedicated Quadro GPUs, ThinkPad T14 Gen 1/2, and Latitude 5420 with 1-Year MAR warranty under ৳40,000 (beating local BD prices). |

---

## 📋 Evaluation Rules Across All Brackets

1. **Strict Floor Benchmark:** Must distinctly match or outperform an **HP EliteBook 840 G8 (Intel Core i5-1135G7, 8GB DDR4, 256GB SSD)**.
2. **RAM Upgradeability Protocol:** 
   * For clamshells: Dual SODIMM slots are mandatory unless pre-installed with ≥16GB RAM.
   * For 2-in-1 convertibles with soldered RAM: Must have 16GB+ pre-installed under $500, or if 8GB, must be priced under $350 for casual hand-down.
3. **GPU Evaluation for Local LLMs & Dev:**
   * RTX 4060 (8GB VRAM) = Gold Standard (Runs full 8B LLMs unquantized or Q8 at 50+ t/s).
   * RTX 4050 / 3050 (6GB VRAM) = Silver Standard (Runs quantized 8B Q4_K_M 100% on GPU at 35–45 t/s).
   * Integrated Iris Xe / Vega 7 = Bronze Standard (Requires 16GB–32GB system RAM for CPU inference).
