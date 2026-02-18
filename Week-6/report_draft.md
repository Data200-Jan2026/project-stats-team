#  Project Report Draft
## DATA-200 | Sports Analytics Project
### Team: Project-Stats-Team

## 1. Introduction

Sports analytics has become a critical field in modern cricket, enabling teams to make data-driven decisions on player selection, match strategy, and performance optimization.

This project analyzes a **300-player cricket dataset** across **5 international teams** to:
- Identify key factors that drive player performance
- Build predictive models for match outcomes
- Apply statistical techniques to generate actionable insights

**Project Topic:** Sports Analytics  
**Dataset:** Cricket Player Performance Dataset (300 players, 11 variables)  
**Tools:** Python, Jupyter Notebook, VS Code, GitHub  

## 2. Problem Statement

> *Our team aims to analyze a real-world sports dataset to identify patterns and relationships that affect player performance and match outcomes. We apply statistical modeling and predictive techniques, including Linear Regression, ANOVA, and Logistic Regression, to generate actionable insights and support data-driven decision-making in sports.*

## 3. Dataset Description

| Variable | Description |
|----------|-------------|
| Player | Unique player identifier |
| Team | One of 5 international cricket teams |
| Matches | Total matches played |
| Batting_Avg | Batting average (runs per dismissal) |
| Strike_Rate | Batting strike rate |
| Bowling_Avg | Bowling average |
| Wickets | Total wickets taken |
| Fielding_Score | Composite fielding score (50–100) |
| Experience | Experience index |
| Performance_Score | Overall composite score (target variable) |
| Match_Won | Binary outcome: 1 = Win, 0 = Loss |

## 4. Methodology

| Week | Task |
|------|------|
| Week 2 | Literature Review |
| Week 3 | Exploratory Data Analysis (EDA) |
| Week 4 | Data Cleaning & Feature Engineering |
| Week 5 | Descriptive Stats, t-Test, ANOVA, Linear & Logistic Regression |
| Week 6 | Ridge, Lasso, Random Forest, Gradient Boosting, Model Comparison |


## 5. Week 5 – Statistical Analysis Results

### 5.1 Descriptive Statistics

| Variable | Mean | Std Dev | Min | Max |
|----------|------|---------|-----|-----|
| Batting_Avg | 34.55 | 15.30 | 5.00 | 81.18 |
| Strike_Rate | 76.71 | 19.00 | 30.00 | 127.65 |
| Bowling_Avg | 31.29 | 9.63 | 15.00 | 55.80 |
| Wickets | 55.82 | 35.21 | 0 | 119 |
| Performance_Score | 53.44 | 13.77 | 18.97 | 90.88 |

### 5.2 Correlation Analysis

| Variable Pair | Pearson r | Strength |
|---------------|-----------|----------|
| Batting_Avg ↔ Performance_Score | +0.40 | Moderate Positive |
| Wickets ↔ Performance_Score | +0.35 | Moderate Positive |
| Strike_Rate ↔ Performance_Score | +0.22 | Weak-Moderate |
| Bowling_Avg ↔ Performance_Score | -0.03 | Negligible |

### 5.3 Hypothesis Testing

#### t-Test (Experience vs Performance)
- **H₀:** No significant difference between experience groups
- **H₁:** Significant difference exists
- **Result:** t = 0.870, p = 0.385 → **Fail to Reject H₀**
- **Conclusion:** Experience alone does NOT significantly predict performance

#### One-Way ANOVA (Teams vs Performance)
- **H₀:** All team means are equal
- **H₁:** At least one team differs
- **Result:** F = 1.510, p = 0.199 → **Fail to Reject H₀**
- **Conclusion:** No significant performance difference across teams

### 5.4 Linear Regression

| Metric | Value |
|--------|-------|
| R² Score | 0.827 |
| RMSE | 4.906 |
| CV R² (5-fold) | 0.82 ± 0.04 |
| Top Predictor | Batting_Avg (coef = +0.383) |

### 5.5 Logistic Regression

| Metric | Value |
|--------|-------|
| Accuracy | 81.7% |
| ROC-AUC | 0.972 |
| F1-Score (Win) | 0.84 |


## 6. Week 6 – Advanced Modeling Results

### 6.1 Regression Model Comparison

| Model | R² | RMSE | CV R² |
|-------|----|------|-------|
| Linear Regression (Week 5) | 0.827 | 4.906 | 0.82 |
| Ridge (α=10) | 0.827 | 4.906 | 0.82 |
| **Lasso (α=0.5) ⭐ Best** | **0.828** | **4.894** | **0.82** |
| Random Forest | 0.732 | 6.106 | 0.71 |

### 6.2 Classification Model Comparison

| Model | Accuracy | AUC | CV Acc |
|-------|----------|-----|--------|
| **Logistic Regression ⭐ Best** | **88.3%** | **0.972** | **86%** |
| Random Forest | 85.0% | 0.928 | 83% |
| Gradient Boosting | 80.0% | 0.919 | 80% |

### 6.3 Feature Importance (Random Forest)

| Feature | Importance |
|---------|------------|
| Batting_Avg | Highest |
| Wickets | 2nd |
| Strike_Rate | 3rd |
| Fielding_Score | 4th |
| Matches | 5th |

## 7. Key Insights

1. **Batting Average** is the single strongest predictor of performance (coef = +0.383)
2. **Wickets (Bowling)** is the second most important contributor
3. **Team affiliation** does NOT significantly affect performance (ANOVA p = 0.199)
4. **Experience alone** does NOT predict performance (t-test p = 0.385)
5. **Lasso Regression** is the best regression model (R² = 0.828)
6. **Logistic Regression** is the best classifier (Accuracy = 88.3%, AUC = 0.972)
7. **All-round players** (high batting + high wickets) score highest consistently
8. Statistical models **can reliably predict** match outcomes

---

## 8. Conclusions

- Individual skill (batting + bowling) drives player performance, not team or experience
- Statistical modeling is highly effective for sports performance prediction
- Lasso regularization slightly improves regression generalization
- The project validates the hypothesis that data-driven insights support better decision-making in sports


## 9. Next Steps (Final Report)

- [ ] Validate models on real IPL / ICC cricket datasets
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Write full discussion & recommendations section
- [ ] Add all visualizations to the final report document
- [ ] Submit final project report


*Report Draft – DATA-200 | Project-Stats-Team | February 2026*
