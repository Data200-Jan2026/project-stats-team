# Week 6: Statistical Modeling (Continued) + Report Draft
## DATA-200 | Sports Analytics Project | Project-Stats-Team

---

## Problem Statement
Our team aims to analyze a real-world sports dataset to identify patterns and relationships that affect player performance and match outcomes. We apply statistical modeling and predictive techniques, including **Linear Regression**, **ANOVA**, and **Logistic Regression**, to generate actionable insights and support data-driven decision-making in sports.

---

---

## Week 6 Tasks 

### 1. Advanced Regression (Building on Week 5)
- **Ridge Regression** (α=10) → R² = 0.827, RMSE = 4.906
- **Lasso Regression** (α=0.5) → R² = 0.828, RMSE = 4.894 ⭐ Best
- **Random Forest Regressor** → R² = 0.732, RMSE = 6.106
- Coefficient comparison: Linear vs Ridge vs Lasso

### 2. Advanced Classification (Building on Week 5)
- **Random Forest Classifier** → Accuracy = 85.0%, AUC = 0.928
- **Gradient Boosting Classifier** → Accuracy = 80.0%, AUC = 0.919
- Compared against Week 5 Logistic Regression (88.3%, AUC = 0.972)

### 3. ROC Curve Comparison
- All 3 classifiers plotted on single ROC graph
- Logistic Regression achieves best AUC = 0.972

### 4. Feature Importance Analysis
- Random Forest feature importance for both regression and classification
- Top features: Batting_Avg, Wickets, Strike_Rate

### 5. Confusion Matrices
- All 3 classifiers side-by-side comparison

### 6. Report Draft
- Full progress summary compiled in notebook (Step 9)
- Introduction, Methodology, Key Results, Conclusions

---

## Final Model Comparison

### Regression Models

| Model | R² | RMSE | CV R² |
|-------|----|------|-------|
| Linear Regression (Week 5) | 0.827 | 4.906 | 0.82 |
| Ridge (α=10) | 0.827 | 4.906 | 0.82 |
| **Lasso (α=0.5) ⭐** | **0.828** | **4.894** | **0.82** |
| Random Forest | 0.732 | 6.106 | 0.71 |

### Classification Models

| Model | Accuracy | AUC | CV Acc |
|-------|----------|-----|--------|
| **Logistic Regression ⭐** | **88.3%** | **0.972** | **86%** |
| Random Forest | 85.0% | 0.928 | 83% |
| Gradient Boosting | 80.0% | 0.919 | 80% |

---

## Key Insights
- **Batting Average** is the #1 driver of performance (coef=+0.383)
- **Wickets** is the #2 contributor (bowling matters!)
- **Team** and **Experience** → NOT significant predictors
- **Lasso** is the best regression model (slight improvement via regularization)
- **Logistic Regression** remains the best classifier (AUC=0.972)
- All-round players (bat + bowl) score highest consistently

---

## Tools & Libraries Used
- **Python 3.x** | **Jupyter Notebook** | **VS Code**
- `numpy` `pandas` `matplotlib` `seaborn`
- `scipy.stats`
- `scikit-learn` — Ridge, Lasso, RandomForest, GradientBoosting, cross_val_score, roc_auc_score

---

##  Next Steps (Final Report)
- Validate models on real IPL / ICC cricket datasets
- Hyperparameter tuning with GridSearchCV
- Write full discussion & recommendations
- Submit final project report
