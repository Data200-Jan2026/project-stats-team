# Project Report Draft
## DATA-200 | Sports Analytics | Project-Stats-Team

### Introduction

For our DATA-200 project, our team chose Sports Analytics as the main topic. The goal was to work with a real-world sports dataset and find patterns that affect how players perform and whether a team wins or loses a match. We focused on cricket because it has rich performance data across batting, bowling, and fielding.

Our dataset includes 300 players from five international teams — India, Australia, England, South Africa, and New Zealand. Each player has 11 variables recorded including batting average, strike rate, wickets, fielding score, and an overall performance score.

### Problem Statement

Our team aims to analyze a real-world sports dataset to identify patterns and relationships that affect player performance and match outcomes. We apply statistical modeling and predictive techniques, including Linear Regression, ANOVA, and Logistic Regression, to generate actionable insights and support data-driven decision-making in sports.

### Dataset Overview

The dataset was built to simulate realistic cricket statistics. The key variables we worked with were batting average, strike rate, bowling average, wickets taken, fielding score, number of matches played, experience, an overall performance score, and a binary match outcome (win or loss). The performance score was calculated as a weighted combination of batting, bowling, and fielding contributions.

### Methodology

We followed a week-by-week approach throughout the project. Week 2 focused on reviewing existing literature on sports analytics and cricket data. Week 3 was exploratory data analysis where we looked at distributions, patterns, and initial relationships. Week 4 covered data cleaning and feature preparation. In Week 5 we ran all the main statistical tests and built our first regression models. Week 6 extended the modeling with regularization and ensemble methods and we began putting together this report.

### Week 5 Results

We started with descriptive statistics to understand the data. The average batting score across all players was 34.55 and the average performance score was 53.44. Most variables followed an approximately normal distribution which confirmed our data was suitable for parametric testing.

For hypothesis testing we ran two tests. The first was an independent samples t-test to check whether players with more experience performed significantly better. The result was t = 0.870 and p = 0.385 which means we failed to reject the null hypothesis. Experience alone does not significantly predict performance. The second test was a one-way ANOVA across the five teams. The result was F = 1.510 and p = 0.199 which again showed no significant difference between teams. This was an interesting finding because it means the team a player belongs to does not determine their individual performance level.

We also ran a Pearson correlation analysis. Batting average had the strongest positive correlation with performance score at r = 0.40 followed by wickets at r = 0.35. Bowling average had almost no correlation at r = -0.03.

For regression our linear regression model achieved an R² of 0.827 which means it explained 82.7% of the variance in performance score. The RMSE was 4.906. Batting average was the strongest predictor with a coefficient of +0.383 followed by wickets at +0.301. For classification logistic regression achieved 81.7% accuracy and an AUC of 0.972 when predicting match outcomes.

### Week 6 Results

In Week 6 we built on the Week 5 models by adding regularization and ensemble methods. We tested Ridge regression with alpha 10, Lasso regression with alpha 0.5, and a Random Forest regressor. Lasso performed the best with R² = 0.828 and RMSE = 4.894, a slight improvement over the base linear model. Random Forest actually performed worse at R² = 0.732 which suggests the linear relationship between features and performance score is strong enough that a simpler model works better here.

For classification we added Random Forest and Gradient Boosting classifiers. Logistic regression from Week 5 still came out on top with 88.3% accuracy and AUC = 0.972. Random Forest got 85.0% and Gradient Boosting got 80.0%. We also looked at feature importance from the Random Forest models which confirmed that batting average and wickets are consistently the most important features across both regression and classification tasks.

### Key Insights

The most important finding is that batting average is the single strongest driver of overall player performance. Players who bat well tend to have higher composite scores regardless of their team or experience level. Wickets came in second which highlights that all-round players who contribute both with the bat and ball are the most valuable.

We were surprised that team affiliation and experience had no significant statistical effect on performance. This tells us that individual skill matters far more than which team you play for or how long you have been playing.

Our best models were Lasso regression for predicting performance score and logistic regression for predicting match outcomes. Both performed consistently well across cross-validation which gives us confidence they would generalize to new data.

### Conclusions

This project showed that statistical modeling can effectively explain and predict sports performance. We achieved over 82% explained variance in performance prediction and over 88% accuracy in match outcome classification. The results support our original problem statement that data-driven approaches can generate meaningful insights for decision-making in sports.

Going forward we would like to validate these models on real IPL or ICC datasets, apply hyperparameter tuning using GridSearchCV, and expand the feature set to include match conditions like pitch type and weather.

*DATA-200 | Project-Stats-Team | February 2026*
