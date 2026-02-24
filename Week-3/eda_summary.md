# EDA Summary — 300 International Cricket Players
**Course:** DATA-200 | Project-Stats-Team | **Week 3**

> Exploratory Data Analysis using descriptive statistics and visualizations to understand data patterns, relationships, and data quality.

---

## 1. Dataset Overview

| Property | Value |
|----------|-------|
| **Source File** | `cricket_players_300.csv` |
| **Shape** | 300 rows × 12 columns |
| **Unique Players** | 300 (no duplicates) |
| **Teams** | 5 international teams |
| **Target Variable** | `Performance_Score` |

### Columns & Data Types

| Column | Dtype | Description |
|--------|-------|-------------|
| `Player` | object | Player name |
| `Team` | object | National team |
| `Matches` | int64 | Matches played |
| `Batting_Avg` | float64 | Batting average |
| `Strike_Rate` | float64 | Strike rate |
| `Bowling_Avg` | float64 | Bowling average |
| `Wickets` | int64 | Total wickets |
| `Fielding_Score` | float64 | Fielding score |
| `Experience` | float64 | Years of experience |
| `Performance_Score` | float64 | Overall performance score |
| `Match_Won` | int64 | Match won indicator (binary) |
| `Rating` | object | Categorical rating label |

---

## 2. Data Quality

### 2.1 Missing Values
**Result: Zero missing values across all 12 columns** — the dataset is completely clean and requires no imputation.

### 2.2 Duplicates
**Result: No duplicate rows detected.** All 300 player entries are unique.

### 2.3 Outlier Detection (IQR Method)

| Feature | Q1 | Q3 | IQR | Lower Fence | Upper Fence | Outliers |
|---------|-----|-----|-----|-------------|-------------|---------|
| Batting_Avg | 24.75 | 44.40 | 19.65 | -4.72 | 73.88 | **2** |
| Strike_Rate | 60.92 | 87.32 | 26.41 | 21.30 | 126.94 | **1** |
| Bowling_Avg | 24.28 | 37.12 | 12.83 | 5.03 | 56.36 | 0 |
| Wickets | 26.75 | 87.00 | 60.25 | -63.62 | 177.38 | 0 |
| Fielding_Score | 62.40 | 86.05 | 23.65 | 26.93 | 121.52 | 0 |
| Matches | 20.00 | 56.00 | 36.00 | -34.00 | 110.00 | 0 |
| Experience | 2.06 | 5.73 | 3.67 | -3.45 | 11.24 | 0 |
| Performance_Score | 44.76 | 62.28 | 17.53 | 18.46 | 88.58 | 0 |

> **Takeaway:** Only 3 outliers total across 8 numeric features — the dataset is remarkably clean. `Batting_Avg` (2 outliers) and `Strike_Rate` (1 outlier) are the only affected features.

---

## 3. Descriptive Statistics

| Feature | Mean | Std | Min | Median | Max | Skewness | Kurtosis |
|---------|------|-----|-----|--------|-----|----------|----------|
| Batting_Avg | 35.00 | 14.48 | 5.00 | 35.89 | ~74 | — | — |
| Strike_Rate | 74.59 | 19.19 | 30.00 | 74.63 | ~127 | — | — |
| Bowling_Avg | 31.00 | 9.62 | 15.00 | 30.43 | ~56 | — | — |
| Wickets | — | — | — | — | — | — | — |
| Fielding_Score | — | — | — | — | — | — | — |
| Experience | — | — | — | — | — | — | — |
| Performance_Score | ~55 | — | — | — | — | slight right skew | — |

> `Performance_Score` is approximately normally distributed with a mean near 55 and a slight positive skew.

---

## 4. Categorical Feature Analysis

### Team Distribution

| Team | Players |
|------|---------|
| India | 60 |
| Australia | 60 |
| England | 60 |
| South Africa | 60 |
| New Zealand | 60 |

> **Perfectly balanced** — each of the 5 teams contributes exactly 60 players (20% each). No sampling bias by team.

### Rating Distribution

| Rating | Count | Share |
|--------|-------|-------|
| Good | 122 | ~40.7% |
| Average | 107 | ~35.7% |
| Below Average | 45 | ~15.0% |
| Elite | 26 | ~8.7% |

> Most players fall in the **Good** and **Average** bands. Only ~8.7% are rated Elite (Performance Score > 70), while ~15% are Below Average.

### Win Rate
**Overall Win Rate: 49.3%** — nearly balanced, with a very slight lean toward losses.

---

## 5. Visualizations Produced

| # | Chart | Purpose |
|---|-------|---------|
| 5.1 | Histograms (2×4 grid) | Distribution of all 8 numeric features |
| 5.2 | Box Plots (2×4 grid) | Outlier visualization per feature |
| 5.3 | Scatter Plots (1×4) | Relationships between key features and Performance Score, color-coded by team |
| 5.4 | Pearson Correlation Heatmap | Feature inter-correlations (lower triangle) |
| 5.5 | Box + Bar Plot | Performance Score distribution by team |
| 5.6 | Bar Chart + Pie Chart | Player rating breakdown |

---

## 6. Key Insights & Findings

| Finding | Detail |
|---------|--------|
| ✅ **Missing Values** | No missing values — dataset is completely clean |
| ✅ **Duplicates** | No duplicate rows detected |
| ⚠️ **Outliers** | Only 3 outliers across all features — negligible impact |
| 📊 **Performance Score** | Approximately normally distributed (mean ≈ 55, slight positive skew) |
| 🔗 **Top Correlates** | Wickets & Batting Average are most strongly correlated with Performance Score |
| ⚖️ **Team Balance** | Each team has exactly 60 players — perfectly balanced dataset |
| 🏆 **Win Rate** | ~49.3% overall win rate — nearly balanced (slight imbalance) |
| 🌟 **Elite Players** | ~8.7% rated Elite (26 players); ~27% rated Elite if threshold is Performance Score > 70 |
| 📈 **Rating Majority** | ~76% of players rated Good or Average — healthy mid-tier concentration |

---

## 7. Next Steps

Based on these EDA findings, the recommended statistical analyses are:

- **t-Test** — Compare Performance Scores between two groups (e.g., Elite vs. non-Elite)
- **ANOVA** — Test whether Performance Score differs significantly across all 5 teams
- **Linear Regression** — Predict Performance Score using Batting Avg, Wickets, Strike Rate, etc.
- **Logistic Regression** — Predict `Match_Won` (binary) using player performance features

---

