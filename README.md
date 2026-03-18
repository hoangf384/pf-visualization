# Personal Finance Dashboard (Tableau)

## Table of Contents
- [Project Overview](#project-overview)
- [Key Learnings](#key-learnings)
- [Context](#context)
- [Methodology (STAR Framework)](#methodology-star-framework)
- [Key Insights](#key-insights)
- [Tools & Skills](#tools--skills)
- [Future Developments](#future-developments)
- [Getting Started](#getting-started)
  - [How to Clone the Project](#how-to-clone-the-project)
  - [How to Install the Project](#how-to-install-the-project)
- [Screenshots](#screenshots)

---

## Project Overview

[README in Vietnamese](README.vi.md)

This project analyzes synthetic personal finance data to understand patterns in income, spending, and saving across different demographic groups and over time. It includes both the data generation process and the data visualization stage using Tableau.

To fully understand the project, please follow this order:

1. **BaoCao_phu_Nhom_10.pdf** - Explains how the dataset was adjusted and generated.
2. **Synthetic_data_generation.ipynb** - Jupyter Notebook describing the synthetic data generation process (sampling, noise, validation).
3. **BaoCao_Nhom_10.pdf** - Main analytical report summarizing workflow, dashboard design, and insights.
4. **Income Spending and Saving Overview.twbx** - Tableau dashboard visualizing population-level financial behavior.
5. **Actual Spending Behavior Analysis.twbx** - Tableau dashboard analyzing individual spending and saving patterns.

Repository structure:
```text
nhom_10
├── Reports/
│   ├── main_report.pdf 
│   └── other_report.pdf
│
├── Notebooks/
│   ├── Datacleaned_Nhom_10.ipynb
│   └── Synthetic_data_generation.ipynb
│
├── Dashboards/
│   ├── Income Spending and Saving Overview.twbx
│   └── Actual Spending Behavior Analysis.twbx
│
└── Data/
    ├── synthetic_data_output.csv
    ├── [1] Personal_Finance_Dataset.csv
    ├── [1] financial-literacy-data.csv
    └── reference-person-age-ranges-2023.xlsx
```

## Key Learnings

- **End-to-End Data Workflow:** Gained a comprehensive understanding of data generation, statistical noise addition, and data validation using Python.
- **Data Visualization Expertise:** Developed advanced, interactive dashboards in Tableau to communicate complex financial metrics to diverse audiences.
- **Behavioral Analysis:** Enhanced analytical capabilities by identifying and breaking down demographic spending patterns to extract actionable insights.
- **Business Communication:** Improved skills in data storytelling through the creation of detailed, structured analytical reports.

## Context

The project simulates financial literacy and personal finance behaviors to:
- Identify demographic differences in income and saving potential.
- Detect inefficient spending patterns and provide improvement suggestions.
- Demonstrate how data-driven visualization can support financial decision-making.

## Methodology (STAR Framework)

### Situation
Analyzed two synthetic datasets representing population-level and individual financial activities.

### Task
Build interactive Tableau dashboards to visualize saving and spending patterns, and deliver actionable insights.

### Action
- Generated and validated synthetic data using Python.
- Cleaned and structured datasets (20K and 1.5K rows).
- Built dashboards with KPI cards, heatmaps, and trend analyses in Tableau.
- Compared demographic-level and personal-level insights to identify behavioral patterns.

### Result
- Created two interactive dashboards summarizing key metrics:
  - Average income: $74,503, spending: $66,196, saving: $8,307 (11%).
- Identified Transport & Insurance as major expense drivers.
- Discovered that non-essential expenses made up 58% of total spending in the personal data dataset.
- Proposed strategies for improving saving habits and optimizing spending categories.

## Key Insights

| Category | Observation | Implication |
|-----------|--------------|--------------|
| **Age 18–25** | Lowest saving rate | Need for early financial education |
| **Transport & Insurance** | Top spending categories | Potential for optimization |
| **Non-essential spending (58%)** | Exceeds income growth | Encourage automated budgeting |

## Tools & Skills

- **Python (Pandas, NumPy)** - Synthetic data generation
- **Tableau** - Dashboard design, KPI visualization
- **Excel / Google Sheets** - Data cleaning and validation
- **Data Storytelling** - Insight communication and report writing

## Future Developments

- **Real-Time Data Integration:** Connect to personal finance APIs or actual bank exports to analyze live data.
- **Predictive Analytics:** Implement machine learning models to forecast future expenses and estimate saving rates based on current trends.
- **Enhanced Personalization:** Introduce customizable financial goal tracking components into the Tableau dashboards.
- **Automated Data Pipelines:** Refactor the existing Python notebooks into a streamlined data pipeline using workflow orchestration tools.

## Getting Started

### How to Clone the Project

Run the following command in your terminal to clone the repository to your local machine:

```bash
git clone https://github.com/hoangf384/pf-visualization.git
cd pf-visualization
```

### How to Install the Project

Follow these steps to set up the development environment required for running the Python notebooks:

```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 3. Install necessary Python libraries
pip install -r requirements.txt

# 4. Register the virtual environment kernel with Jupyter
python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
```

By completing the final step, you have successfully registered the new kernel. When you open any Jupyter Notebooks (`.ipynb`), be sure to select the `Python (.venv)` kernel to utilize the correctly isolated environment!

## Screenshots

![Dashboard Overview](images/demographic.png)
[Demographic Overview](https://public.tableau.com/app/profile/nguy.n.phan.ho.ng.ph.c/viz/Book1_17516920190310/General?publish=yes)

![Spending Behavior](images/Behaviors.png)
[Spending Behavior Analysis](https://public.tableau.com/app/profile/nguyen.nhi8170/viz/CuoiKy_17519870918010/Dashboard1?publish=yes)
