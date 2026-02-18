# Week 7: Python Application Development
## DATA-200 | Sports Analytics Project | Project-Stats-Team

### What is this?

This is a locally running Streamlit web application built to demonstrate the full Sports Analytics project. It combines everything from Week 5 and Week 6 into an interactive dashboard with live predictions.

### Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |

### How to Run

Step 1 — Install Streamlit if you don't have it

```bash
pip install streamlit
```

Step 2 — Run the app

```bash
streamlit run app.py
```

Step 3 — It will open automatically in your browser at `http://localhost:8501`

### Libraries Used

- `streamlit` — web application framework
- `pandas` — data manipulation
- `numpy` — numerical computing
- `matplotlib` — charts and plots
- `seaborn` — statistical visualizations
- `scipy` — statistical tests
- `scikit-learn` — machine learning models

### App Pages

**Home** — Project overview, timeline, dataset preview and key metrics

**Dashboard and EDA** — Filter by team, view distributions, correlation heatmap, boxplots and raw data table

**Statistical Analysis** — t-Test and ANOVA results with visualizations from Week 5

**Model Results** — Full comparison of all regression and classification models from Week 5 and Week 6

**Predict Player** — Enter any player stats using sliders and get a live Performance Score prediction and Match Win/Loss prediction with probability

### Models Inside the App

| Task | Model | Performance |
|------|-------|-------------|
| Performance Score | Lasso Regression | R² = 0.828 |
| Match Outcome | Logistic Regression | Accuracy = 88.3%, AUC = 0.972 |

*DATA-200 | Project-Stats-Team | February 2026*
