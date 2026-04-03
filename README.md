
# 📈 YouTube FBR Tax Compliance Tracker (2026 Edition)

A Python-based Business Intelligence (BI) dashboard designed to help Pakistani content creators navigate the **SRO 545 & 546(I)/2026** tax regulations issued in April 2026. This tool uses live data from the YouTube Data API to calculate "Assessed Revenue" vs. "Actual Liability."

## 🚀 The Problem
In April 2026, the Federal Board of Revenue (FBR) introduced a new "Presumptive Tax" benchmark for social media creators:
* **Benchmark:** PKR 195 per 1,000 views.
* **Expense Allowance:** 30% flat deduction.
* **Taxable Threshold:** PKR 600,000 per annum.

Many creators are unsure when they actually hit the "Tax Wall." This tool automates that calculation.

## ✨ Features
* **Real-time API Integration:** Fetches live view counts and subscriber data using **YouTube Data API v3**.
* **FBR Logic Engine:** Automatically applies the 195 PKR/1000 views rule and the 30% expense deduction.
* **Growth Simulator:** An interactive Plotly chart that predicts exactly which month you will cross the 600k taxable limit based on your growth rate.
* **Compliance Status:** Instant feedback on whether you need to file a "Nil Return" (for 50k+ subs) or pay actual income tax.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Frontend:** Streamlit (UI/UX)
* **Data Viz:** Plotly Express
* **Backend:** Google API Client Library
* **Security:** Python-Dotenv (Environment Variable Management)

## 📦 Installation & Setup

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/FBR-YouTube-Tax-Tracker.git](https://github.com/YOUR_USERNAME/FBR-YouTube-Tax-Tracker.git)
   cd FBR-YouTube-Tax-Tracker
