# Food Delivery Fleet Efficiency & Delivery Lag Diagnostics

**AICTE | IBM SkillsBuild Data Analytics with AI Academic Internship Program 2026**  
**Conducted by:** BharatCares in association with AICTE  
**Candidate Name:** Nandini Priyadarshini  
**Institution:** Institute of Technical Education and Research (ITER), Bhubaneswar  

---

## 1. Project Overview

In quick-commerce and hyper-local food logistics, maintaining the **30-minute Service Level Agreement (SLA)** is vital for customer retention, app-store ratings, and unit economics. When deliveries exceed 30 minutes, platforms incur direct costs through refund vouchers, support escalations, and cascaded fleet queuing.

This project delivers an end-to-end data analytics and diagnostics system analyzing **45,593 delivery records** to uncover the operational root causes of delivery delay. Through geodesic feature engineering, statistical bottleneck diagnostics, and interactive telemetry simulation, this project formulates data-grounded policies that reduce overall SLA breach rates by an estimated **20% to 35%**.

---

## 2. Dataset Information

- **Dataset Name:** Food Delivery Dataset
- **Dataset Source Link:** [Kaggle Food Delivery Dataset (Gaurav Malik)](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset)
- **Primary Raw Data File:** `train.csv` (45,593 records across 20 attributes)
- **Processed Data File:** `cleaned_delivery_data.csv` (43,799 validated deliveries with engineered geodesic features)

### Core Features Analyzed:
- `Delivery_person_ID`, `Delivery_person_Age`, `Delivery_person_Ratings`
- `Restaurant_latitude`, `Restaurant_longitude`, `Delivery_location_latitude`, `Delivery_location_longitude`
- `Weather_conditions` (Sunny, Cloudy, Fog, Sandstorms, Stormy, Windy)
- `Road_traffic_density` (Low, Medium, High, Jam)
- `Type_of_vehicle` (bicycle, electric_scooter, scooter, motorcycle)
- `multiple_deliveries` (0, 1, 2, 3 orders)
- **Engineered Metrics:** `Distance_km` (Haversine formula), `Speed_kmh`, `Is_Delayed` (1 if Time > 30 min), `Distance_Band` (`0-3 km`, `3-7 km`, `7-15 km`, `15+ km`)

---

## 3. Technologies Used

- **Programming Language:** Python 3.10+
- **Data Processing & Feature Engineering:** Pandas 2.2+, NumPy 2.2+
- **Statistical Visualization:** Matplotlib 3.7+, Seaborn 0.12+
- **Interactive Operations Dashboard:** Streamlit 1.30+, Plotly 5.18+
- **Report & Documentation Automation:** python-docx 1.1+

---

## 4. Submission Files

| Required Submission File | File Name in Repository | Description |
|---|---|---|
| **Code File** (`.ipynb`) | `NandiniPriyadarshini_Food_Delivery_Fleet_Efficiency_and_Delivery_Lag_Diagnostics.ipynb` | Complete end-to-end pipeline (Data Cleaning, Feature Engineering, 4 Diagnostic Visual Analyses, Recommendations) with all charts pre-computed. |
| **Requirements File** (`.txt`) | `requirements.txt` | Complete list of all Python libraries and dependencies needed to run the project. |
| **Project Report** (`.docx`) | `NandiniPriyadarshini_ProjectReport.docx` | Comprehensive formal project documentation covering Executive Summary, Methodology, Empirical Diagnostics, Dashboard Architecture, and Policy Roadmap. |
| **README File** (`.md`) | `README.md` | Project overview, dataset link, setup/run instructions, technologies used, and key findings. |

---

## 5. Setup & Execution Instructions

### Step 1: Clone / Navigate to Project Directory
```bash
cd "c:\Users\NANDINI\Desktop\DD\PROJECTS\DataAnalytics-Internship"
```

### Step 2: Set Up Virtual Environment (Recommended)
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 4: Run Data Cleaning & Feature Engineering Pipeline
```bash
python 01_data_cleaning_and_feature_engineering.py
```
*Outputs `cleaned_delivery_data.csv` with cleaned coordinate features, Haversine distances, calculated transit speeds, and operational SLA targets.*

### Step 5: Launch the Interactive Operations Dashboard
```bash
streamlit run 03_dashboard_app.py
```
*Opens the web dashboard in your browser at `http://localhost:8501` featuring global KPI cards, multi-facet sidebar filtering, and 5 analytical deep-dive tabs.*

### Step 6: Review the Diagnostic Jupyter Notebook
```bash
jupyter notebook NandiniPriyadarshini_Food_Delivery_Fleet_Efficiency_and_Delivery_Lag_Diagnostics.ipynb
```
*(Or open directly in VS Code / Cursor to inspect the pre-rendered heatmaps, stacked bar charts, and boxplots).*

---

## 6. Key Empirical Findings

1. **Weather x Traffic Compounding:** Adverse weather (Fog, Stormy) combined with congested traffic (High, Jam) increases median delivery time to **35–36 minutes** (157% higher than baseline 14 min), systematically breaching the 30-minute SLA.
2. **The 7 km Distance Tipping Point:** While hyper-local orders (0–3 km) maintain an SLA breach rate of **19.3%**, breaches escalate sharply to **30.6%** for 7–15 km and reach **36.4%** on 15+ km deliveries.
3. **Multi-Delivery Stacking Degradation:** Transitioning from 1 to 2 concurrent deliveries adds **+12 to +14 minutes** to delivery turnaround. For 3 concurrent orders, median delivery time climbs to **44–48 minutes**. Bicycles cannot support triple stacking, and electric scooters suffer severe battery-load drag.
4. **Driver Competence vs. Age:** Courier rating correlates positively with speed ($r = +0.105$) and negatively with total delivery duration ($r = -0.339$). Driver age displays negligible correlation with transit velocity ($r = +0.012$), proving demographic age is not a performance bottleneck.

---

## 7. Strategic Business Recommendations

- **Dynamic ETA Buffers (+8 to +12 min):** Automatically extend advertised customer delivery windows during severe weather/traffic pairings to eliminate SLA breach surprises and cut customer refund claims by **15% to 25%**.
- **Multi-Order Stacking Route Distance Cap (5 km Threshold):** Impose an algorithmic limit restricting multi-order batching (`multiple_deliveries > 1`) strictly to routes within a 5 km geodesic radius.
- **Short-Haul Modality Allocation:** Restrict bicycles and electric scooters to micro-delivery zones (< 3 km) where they operate competitively with motorized vehicles, cutting bicycle SLA breaches by **~50%**.
