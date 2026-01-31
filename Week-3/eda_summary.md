# Week 3: Exploratory Data Analysis (EDA) Summary

## 1. Data Preprocessing
- **Missing Values**: Checked all columns for missing data. No missing entries were found, so no imputation was needed.
- **Duplicates**: There were no duplicate rows in the dataset.
- **Outliers**: Box plots were used to identify extreme values in `Economy_Rate` and `Runs`. These outliers were retained since they represent actual variations in player performance.
- **Data Types**: Columns such as `Runs`, `Strike_Rate`, and `Economy_Rate` were confirmed to be numeric for proper calculations.

## 2. Descriptive Statistics

| Metric        | Mean  | Median | Min  | Max   |
|---------------|-------|--------|------|-------|
| Runs          | 45.7  | 42     | 0    | 120   |
| Strike Rate   | 112.4 | 110.5  | 98.6 | 145.4 |
| Economy Rate  | 5.2   | 5.0    | 2.1  | 12.1  |

**Observations:**
- Most players score between 20 and 70 runs per match.
- Strike rates are mostly in the 100–130 range.
- Economy rates are generally between 4 and 6, with a few high values showing occasional poor bowling performance.

## 3. Visualizations and Insights
- **Histograms**: Show the distribution of `Runs`, `Strike_Rate`, and `Economy_Rate`.
  - Most players score under 70 runs, and most bowlers have economy rates between 4 and 6.
- **Box Plots**: Helped identify outliers and the spread of the data.
  - Some high economy rates (>10) indicate occasional bad performances, while a few high run scores represent top-performing players.
- **Scatter Plots**: Used to check relationships between metrics:
  - `Runs vs Strike Rate`: Players scoring more runs tend to have higher strike rates.
  - `Economy Rate vs Wickets` (if available): Lower economy rates usually correspond to better bowling performance.

## 4. Key Takeaways
- The dataset is clean and ready for further analysis.
- Most players’ performance falls within expected ranges, with a few outliers showing exceptional results.
- Visualizations confirm trends like higher runs linking with higher strike rates.
- The data is suitable for predictive modeling and statistical tests in future analysis.
