# 🚢 Exploratory Data Analysis (EDA) on the Titanic Dataset
### Minor Project — Data Science & Statistical Analysis

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Data-Pandas-blue?logo=pandas)](https://pandas.pydata.org)
[![Visualization](https://img.shields.io/badge/Viz-Matplotlib%20%7C%20Seaborn-green)](https://matplotlib.org)

---

## 📌 Project Overview
This project performs an in-depth **Exploratory Data Analysis (EDA)** on the classic Titanic dataset. The goal is to clean and preprocess raw passenger information, calculate summary statistics, explore distributions, and identify key variables that determined a passenger's chance of survival.

---

## 📁 Project Structure
```
titanic-eda/
│
├── data/
│   └── titanic.csv               ← Raw Kaggle Titanic dataset
│
├── src/
│   ├── download_data.py          ← Python script to download dataset
│   ├── clean_data.py             ← Data cleaning and imputation script
│   └── visualize.py              ← Plot generation script
│
├── output/
│   ├── titanic_cleaned.csv       ← Processed clean dataset
│   └── charts/                   ← Exported visualization charts
│       ├── survival_ratio.png
│       ├── survival_by_gender.png
│       ├── survival_by_class.png
│       ├── age_distribution.png
│       └── correlation_heatmap.png
│
├── titanic_eda.ipynb             ← ⭐ Main Jupyter Notebook (Start Here)
├── requirements.txt              ← Python library dependencies
└── README.md                     ← Project documentation
```

---

## 🛠️ Key Steps & Methodology

### 1. Data Cleaning
* **Imputed Age:** Handled missing age records (177 missing) by replacing them with the **median age** of the passenger's specific socio-economic class (`Pclass`).
* **Imputed Embarked:** Replaced the 2 missing ports with the **mode** (most frequent boarding port, "S").
* **Dropped Redundancies:** Dropped the `Cabin` column due to a high missing rate (>77%) and removed non-predictive identifiers like `PassengerId` and `Ticket`.

### 2. Feature Engineering
* Created `FamilySize` by adding Sibling/Spouse (`SibSp`) and Parent/Child (`Parch`) counts + 1.
* Derived `IsAlone` (1 = traveling alone, 0 = with family).
* Grouped passenger names by social title (Mr, Mrs, Miss, Master, Rare).

### 3. Visual Analysis
* Generated charts examining the relation of Class, Gender, and Age with Survival rates.
* Visualized feature correlations using a Heatmap matrix.

---

## 📈 Key Insights & Findings

1. **Gender Bias:** Survival rate of **female passengers (74.2%)** was nearly 4 times higher than that of **males (18.9%)**.
2. **Socio-Economic Influence:** Passengers in **1st Class had a 63% survival rate**, while those in **3rd Class had only a 24.2% chance**.
3. **Age Priority:** Survival rates spike significantly for children aged **0 to 10 years**, validating the "women and children first" rescue protocol.
4. **Companionship Advantage:** Travelling alone (`IsAlone`) decreased a passenger's chance of survival compared to those with families.

---

## 🚀 How to Run the Project

1. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open and run the Jupyter notebook:
   ```bash
   jupyter notebook titanic_eda.ipynb
   ```
3. Run all cells (`Cell -> Run All`). All clean data and generated charts will be exported to the `output/` folder automatically.

---

## 👩‍💻 Author
**Minor Project - Exploratory Data Analysis**  
Submitted for evaluation.
