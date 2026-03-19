# FinTech Personal Finance Analysis (Tableau)

[Đọc bằng Tiếng Việt](README.vi.md)

## Table of Contents
- [Project Context](#project-context)
- [How we simulated the data](#how-we-simulated-the-data)
- [Key findings & Business Value](#key-findings--business-value)
- [Proposed Feature & A/B Test](#proposed-feature--ab-test)
- [Tools used](#tools-used)
- [How to run the project](#how-to-run-the-project)
- [Dashboard](#dashboard)

---

## Project Context
**Scenario:** Imagine working as a Data Analyst for a major US Digital Bank or FinTech app (similar to Chime, Mint, or a digital wallet). The **Product Team** wants to revamp the app's "Personal Financial Management (PFM)" feature to actually help users rather than just passively categorizing their past transactions.

To understand our user demographics and their pain points, we needed data. However, our initial user surveys lacked the volume needed for robust segmentation. To solve this, **we generated a highly realistic synthetic dataset of 20,000 users** modeled after real U.S. macroeconomic statistics. 

This Tableau dashboard is designed for the **Product Managers and Growth Team**, helping them uncover which demographics are struggling financially and *why*, so they can build better intervention features.

---

## How we simulated the data

Generating random numbers for spending categories independently would ignore real-world relationships (e.g., someone with high housing costs usually has different transport habits). To make the dataset as close to reality as possible, the data was simulated using a **multivariate normal distribution** to preserve category correlation.

1. **Base Demographics:** We started with a cleaned CSV of ~20,000 synthetic individuals based on initial survey profiles.
2. **Correlation Matrix:** We took reference data from the U.S. Bureau of Labor Statistics ([bls.gov](https://www.bls.gov/cex/tables.htm)), processed it, and computed the exact correlation matrix of spending habits across different age groups.
3. **Simulation:** A custom Python function applied this correlation matrix via log-normal and multivariate normal distributions to generate realistic, correlated spending vectors for each person.

*Reference:*
- **BaoCao_phu_Nhom_10.pdf** — Detailed explanation of the simulation mathematics.
- **Synthetic_data_generation.ipynb** — Python code for data generation.

---

## Key findings & Business Value

After running the computational analysis on our 20,000 synthetic users, we found critical insights for the Product Team:

| Age Group | Avg. Savings Rate | Financial Reality |
|-----------|------------------|-----------------|
| 18–25 | **–26.9%** | Spending more than they earn |
| 26–35 | +15.6% | Recovering — building stability |
| 36–45 | **+28.7%** | Best savers |
| 46–55 | +1.9% | Near-zero — likely peak family expenses |
| 56–65 | –86.6% | Drawing down savings (likely retired) |

**The crucial insight for the PFM feature:** 
Non-essential spending (dining out, entertainment, misc.) is only **~8%** of total spend across the board. 

> **Why this matters for the app:** Young users (18–25) aren't overspending because they buy too much coffee or entertainment. They go negative because **fixed costs (rent, insurance, transport) consume their income almost immediately**. A traditional budgeting app that only says "You spent too much on Dining" is useless to them.

---

## Proposed Feature & A/B Test

Based on the macro findings, here is the recommendation for the **PFM Product Team**:

### A/B Test: Proactive Fixed-Cost Alerts

**The problem:** The current standard in banking apps is to show users a pie chart at the end of the month (reactive). For our 18-25 demographic, their money is already gone to fixed costs early in the month.

**The proposed feature:** A proactive notification engine that warns users *before* they overspend their remaining disposable income, factoring in their heavy fixed costs.

| | Group A (Control) | Group B (Test) |
|---|---|---|
| Experience | Standard end-of-month spending summary | Proactive mid-month pacing alerts |
| Example | "You spent $2,000 this month." | "Rent just cleared. You only have $300 left for the next 15 days. Slow down!" |

**Hypothesis:** By shifting from a reactive "auto-categorization" feature (which users rarely review) to a proactive pacing alert, Group B will end the month with a higher average savings rate than Group A. This directly bridges the gap between macro-level insights and a micro-level product feature.

---

## Tools used

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy, SciPy) | Advanced statistical data simulation and cleaning |
| Tableau | Macro-level Dashboard design for Product stakeholders |
| Data Source | U.S. Bureau of Labor Statistics (BLS) |

---

## How to run the project

### Clone the repo
```bash
git clone https://github.com/hoangf384/pf-visualization.git
cd pf-visualization
```

### Set up the environment
```bash
# Create a virtual environment
python -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate
# Activate it (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Register the kernel for Jupyter
python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
```

---

## Dashboard

**Income Spending and Saving Overview.twbx** — Macro-level dashboard visualizing demographic behaviors for the Product Team.

![Dashboard Overview](Images/demographic.png)
[→ View General Dashboard on Tableau Public](https://public.tableau.com/app/profile/nguy.n.phan.ho.ng.ph.c/viz/Book1_17516920190310/General?publish=yes)
