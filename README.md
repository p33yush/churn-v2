# Customer Churn Analysis

## 📌 About
A data analytics project focused on identifying why customers leave a subscription-based business and which customer segments have higher churn rates.

## 🎯 Objective
- Analyze customer data to uncover patterns behind churn
- Identify high-risk customer segments with the highest churn rates
- Calculate key business metrics like churn rate, retention rate, and revenue at risk
- Build an interactive Power BI dashboard to present actionable insights
- Help the business improve customer retention and reduce revenue loss

## 🛠️ Tools & Technologies
| Tool | Purpose |
|------|---------|
| **Python** (Pandas, NumPy, Matplotlib, Seaborn) | Data cleaning, EDA, and visualization |
| **SQL** (SQLite) | Churn metrics, customer segmentation, revenue analysis |
| **Power BI** | Interactive dashboard with business insights |
| **Git & GitHub** | Version control |

## 📁 Project Structure

```
churn-analysis/ 
├── data/                  # All datasets
│   ├── raw/               # Original datasets
│   └── cleaned/           # Cleaned & processed data
├── notebooks/             # Jupyter notebooks
│   ├── 01-eda.ipynb       # Exploratory Data Analysis
│   ├── 02-churn-metrics.ipynb  # Churn metric calculations
│   └── 03-segmentation.ipynb   # Customer segmentation
├── sql/                   # SQL scripts
│   ├── churn_metrics.sql    # Churn rate & retention calculations
│   ├── segmentation.sql     # Customer segmentation logic
│   └── revenue_analysis.sql # Revenue impact analysis
├── reports/               # Power BI files & outputs
│   ├── churn_dashboard.pbix  # Main Power BI dashboard
│   ├── churn_metrics.pdf     # Exported metrics report
│   └── segmentation.pdf    # Segmentation analysis report
├── images/                # Visual outputs
│   ├── churn_distribution.png
│   ├── churn_by_region.png
│   ├── revenue_at_risk.png
│   └── segmentation_heatmap.png
├── src/                   # Reusable Python modules
│   ├── data_loader.py     # Data loading & preprocessing
│   ├── churn_calculator.py  # Metric calculation functions
│   └── visualizer.py      # Visualization utilities
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```


## 🚀 Status
🚧 **In Progress** — Currently in the data exploration phase.
