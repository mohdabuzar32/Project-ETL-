# 🏦 Bluestock Mutual Fund Analytics — ETL Capstone Project

A complete data analytics pipeline for the Indian Mutual Fund industry built during the Bluestock Internship Program.

## 📁 Project Structure

Project-ETL-/
├── data/                  # Raw CSV datasets
├── notebooks/             # Jupyter analysis notebooks
├── dashboard/             # Power BI dashboard (.pbix)
├── reports/               # Output charts and CSV reports
├── data_ingestion.py      # Fetch NAV data from mfapi.in
├── clean_data.py          # Clean and merge datasets
├── recommender.py         # Fund recommendation engine
├── run_pipeline.py        # Master script — runs full ETL
├── queries.sql            # SQL analysis queries
├── schema.sql             # Database schema
├── bluestock_mf.db        # SQLite database
└── requirements.txt       # Python dependencies

## ⚙️ Setup Instructions

git clone https://github.com/mohdabuzar32/Project-ETL-.git
cd Project-ETL-
pip install -r requirements.txt
python run_pipeline.py

## 📊 How to Open the Dashboard

1. Install Power BI Desktop
2. Open dashboard/ folder
3. Open the .pbix file

## 🗂️ Dataset Descriptions

| File | Description |
|------|-------------|
| alpha_beta.csv | Alpha & Beta risk metrics per fund |
| fund_scorecard.csv | Composite performance scorecard |
| tracking_error.csv | Benchmark tracking error analysis |

## 🔧 How to Run ETL

python data_ingestion.py   # Step 1: Fetch data
python clean_data.py       # Step 2: Clean & transform
python recommender.py      # Step 3: Get recommendations
python run_pipeline.py     # OR: Run all at once

## 👥 Team
Abuzar | Saireddy | Vardhan | Kartik | Shruthi

## 🏢 Organization
Bluestock Fintech — Internship Capstone, June 2026
