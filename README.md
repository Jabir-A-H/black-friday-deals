# 🛒 Black Friday Laptop Deal Tracker & Multi-Tier Intelligence Suite

An automated, data-driven tracker monitoring US Black Friday and seasonal doorbusters across major retailers (Walmart, Best Buy, Woot, Dell Refurbished DFS, Target Restored, eBay Certified Outlets). 

Tracked deals are reconciled into a persistent structured JSON ledger and presented in a live markdown dashboard with dual currency conversions: **Bank Card Settlement (`1 USD ≈ 128 BDT`)** and **Realistic Landed Cost (`1 USD ≈ 135 BDT`)**.

---

## 📑 Core Documentation & Data

* **Live Dashboard:** [`docs/laptop-tracker/DEALS_SUMMARY.md`](docs/laptop-tracker/DEALS_SUMMARY.md)
* **Structured JSON Database:** [`docs/laptop-tracker/DEALS_LEDGER.json`](docs/laptop-tracker/DEALS_LEDGER.json)
* **Operational Spec & Budget Protocol:** [`docs/laptop-tracker/TRACKER_SPEC.md`](docs/laptop-tracker/TRACKER_SPEC.md)

---

## 💰 Multi-Tier Budget Architecture

| Bracket | Price Envelope (USD) | Bank Settlement (~128 BDT) | Real Landed (~135 BDT) | Hardware Target & Archetype |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 4: "Gravity" Stretchers** | **$550 – $699 USD** | **৳70,400 – ৳89,500** | **৳74,250 – ৳94,500** | **High-Gravity Outliers:** 40%–50% off $1,000+ MSRP. Unlocks **NVIDIA RTX 4060 (8GB VRAM)** or Apple M2. |
| **Tier 1: High Budget** | **$450 – $550 USD** | **৳57,600 – ৳70,400** | **৳60,750 – ৳74,250** | **Apex Powerhouse Tier:** Dedicated NVIDIA RTX 4050/3050 GPUs, 10-core CPUs, un-soldered DDR5 SODIMM slots. |
| **Tier 2: Mid Budget** | **$350 – $450 USD** | **৳44,800 – ৳57,600** | **৳47,250 – ৳60,750** | **Touchscreens & 32GB RAM:** Dell Latitude 5320 2-in-1 (32GB pre-installed), Dell Inspiron 15 Touch (dual SODIMM slots). |
| **Tier 3: Value Under $350** | **$200 – $350 USD** | **৳25,600 – ৳44,800** | **৳27,000 – ৳47,250** | **Extreme Budget Workhorses:** Precision workstations with Quadro GPU ($207), ThinkPad T14 Gen 2 ($299). |

---

## 🎯 Benchmark Floor & Evaluation Protocol

1. **Strict Baseline Floor:** Must distinctly outperform a standard 11th Gen business baseline machine (**Intel Core i5-1135G7, 8GB DDR4, 256GB SSD**).
2. **RAM Upgradeability Protocol:** 
   * **Clamshells:** Dual un-soldered SODIMM slots are mandatory unless factory-equipped with $\ge 16\text{GB}$ RAM.
   * **Convertibles (2-in-1):** Soldered memory accepted only if pre-installed with $\ge 16\text{GB}$ under \$500.
3. **GPU Compute Evaluation:**
   * **RTX 4060 (8GB VRAM):** Unlocks unquantized 8B local LLMs, full Ray Tracing/DLSS 3, 1080p Ultra gaming.
   * **RTX 4050 / 3050 (6GB VRAM):** Unlocks quantized 8B LLMs (Q4_K_M) 100% on GPU at 35–45 tokens/sec.
   * **Intel Iris Xe 96EU / Radeon 680M:** Minimum floor for general dev, Docker, and dual external displays.

---

## 🤖 Automation Architecture

The repository is continuously updated via two automated cron agents:
1. **Routine 2-Hour Web Tracker (`laptop-deal-tracker`):** Runs every 2 hours via native web search, monitoring live doorbuster prices and stock changes across Walmart, Best Buy, Amazon, and Target.
2. **Daily Deep Deal Hunter (`firecrawl-deep-deal-hunter`):** Runs daily at 9:00 AM (Asia/Dhaka) using Firecrawl MCP to deep-crawl Slickdeals forums, Woot, Dell DFS, and eBay Certified Refurbished outlets.
3. **Auto-Push Sync:** Commits and pushes the reconciled `DEALS_LEDGER.json` and `DEALS_SUMMARY.md` directly to GitHub after every run.
