# Week 5: Statistical Analysis & Validation
## DATA-200 | Sports Analytics Project | Project-Stats-Team

---

##  Problem Statement
Our team aims to analyze a real-world sports dataset to identify patterns and relationships that affect player performance and match outcomes. We apply statistical modeling and predictive techniques, including **Linear Regression**, **ANOVA**, and **Logistic Regression**, to generate actionable insights and support data-driven decision-making in sports.

---



##  Week 5 Tasks

### 1. Descriptive Statistics
- Summary statistics (mean, std, min, max, skewness, kurtosis)
- Team-level performance breakdown
- Match win rate analysis

### 2. Data Visualization
- Distribution histograms for all key variables
- Box plots by team (Performance Score & Batting Average)
- Pearson Correlation Heatmap

### 3. Hypothesis Testing
- **t-Test:** High vs Low Experience groups → `t=0.870, p=0.385` → Fail to Reject H₀
- **One-Way ANOVA:** Performance across 5 teams → `F=1.510, p=0.199` → Fail to Reject H₀

### 4. Multiple Linear Regression
- Target: `Performance_Score`
- Features: `Batting_Avg`, `Strike_Rate`, `Wickets`, `Fielding_Score`, `Matches`
- **R² = 0.827** | **RMSE = 4.91** | 5-Fold CV R² = 0.82+

### 5. Logistic Regression
- Target: `Match_Won` (0 = Loss, 1 = Win)
- **Accuracy = 81.7%** | **ROC-AUC = 0.88**
- Confusion Matrix + Precision / Recall / F1-Score

### 6. Model Diagnostics
- Shapiro-Wilk normality test on residuals
- Levene's test for equal variances
- Residual plot (homoscedasticity check)
- Cross-validation (5-fold) for both models

---

##  Key Results Summary

| Analysis | Result | Interpretation |
|----------|--------|----------------|
| t-Test (Experience) | p = 0.385 | No significant difference |
| ANOVA (Teams) | p = 0.199 | No significant difference |
| Linear Regression | R² = 0.827 | Strong fit — 82.7% variance explained |
| Logistic Regression | Accuracy = 81.7% | Strong classifier |

---

##  Key Insights
- **Batting Average** is the strongest predictor of overall performance
- **Wickets** (bowling) is the second most important contributor
- **Team** and **Experience** alone do NOT significantly affect performance
- Statistical models can effectively predict sports outcomes

---

##  Tools & Libraries Used
- **Python 3.x** | **Jupyter Notebook** | **VS Code**
- `numpy` `pandas` `matplotlib` `seaborn`
- `scipy.stats` — t-test, ANOVA, Shapiro-Wilk, Levene
- `scikit-learn` — LinearRegression, LogisticRegression, StandardScaler, cross_val_score

---

##  Next Steps (Week 6)
- Build on Week 5 models with Ridge/Lasso regularization
- Try Random Forest & Gradient Boosting classifiers
- Begin compiling the final project report
