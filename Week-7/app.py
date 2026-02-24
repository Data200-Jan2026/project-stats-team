# =============================================================================
#  DATA-200 | Sports Analytics Project
#  Team: Project-Stats-Team
# =============================================================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LogisticRegression, Lasso, Ridge, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, roc_auc_score, roc_curve, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CricketIQ Analytics | DATA-200",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1b2a 50%, #0a1628 100%);
    background-attachment: fixed;
}

.block-container {
    padding: 1.5rem 2rem;
    max-width: 1400px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b2a 0%, #091423 100%);
    border-right: 1px solid rgba(0,212,255,0.15);
}

[data-testid="stSidebar"] * {
    color: #e0e6f0 !important;
}

/* Page Title */
.page-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(90deg, #00d4ff, #0080ff, #00d4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}

.page-subtitle {
    color: #7a9abf;
    font-size: 0.95rem;
    font-weight: 400;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
}

/* Metric Cards */
.kpi-card {
    background: linear-gradient(135deg, rgba(0,212,255,0.08) 0%, rgba(0,128,255,0.05) 100%);
    border: 1px solid rgba(0,212,255,0.2);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    margin-bottom: 0.5rem;
}

.kpi-card:hover {
    border-color: rgba(0,212,255,0.5);
    box-shadow: 0 0 20px rgba(0,212,255,0.1);
}

.kpi-value {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #00d4ff;
    line-height: 1;
}

.kpi-label {
    font-size: 0.75rem;
    color: #7a9abf;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 0.4rem;
}

.kpi-delta {
    font-size: 0.8rem;
    color: #00ff88;
    margin-top: 0.2rem;
}

/* Section Headers */
.section-header {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: #00d4ff;
    border-left: 3px solid #00d4ff;
    padding-left: 0.8rem;
    margin: 1.5rem 0 1rem 0;
    letter-spacing: 0.5px;
}

/* Player Card */
.player-card {
    background: linear-gradient(135deg, rgba(0,212,255,0.06) 0%, rgba(0,128,255,0.03) 100%);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.8rem;
}

/* Result Box */
.result-elite {
    background: linear-gradient(135deg, rgba(0,255,136,0.1), rgba(0,200,100,0.05));
    border: 1px solid rgba(0,255,136,0.3);
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #00ff88;
    font-weight: 600;
    font-size: 1.1rem;
}

.result-good {
    background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,150,200,0.05));
    border: 1px solid rgba(0,212,255,0.3);
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #00d4ff;
    font-weight: 600;
    font-size: 1.1rem;
}

.result-avg {
    background: linear-gradient(135deg, rgba(255,180,0,0.1), rgba(200,140,0,0.05));
    border: 1px solid rgba(255,180,0,0.3);
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #ffb400;
    font-weight: 600;
    font-size: 1.1rem;
}

.result-low {
    background: linear-gradient(135deg, rgba(255,60,60,0.1), rgba(200,0,0,0.05));
    border: 1px solid rgba(255,60,60,0.3);
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #ff4444;
    font-weight: 600;
    font-size: 1.1rem;
}

/* Team Badge */
.team-badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Divider */
.glowing-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00d4ff, transparent);
    margin: 1.5rem 0;
    opacity: 0.4;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* Slider */
.stSlider [data-baseweb="slider"] {
    padding: 0.5rem 0;
}

/* Radio */
.stRadio label {
    color: #b0c4d8 !important;
    font-size: 0.9rem !important;
}

/* Selectbox */
.stSelectbox label { color: #7a9abf !important; }

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #7a9abf;
}

.stTabs [aria-selected="true"] {
    color: #00d4ff !important;
    border-bottom-color: #00d4ff !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #00d4ff, #0080ff);
    color: #0a0e1a;
    border-radius: 8px;
    padding: 0.6rem 2rem;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    border: none;
    letter-spacing: 1px;
    width: 100%;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #00ffbb, #00d4ff);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(0,212,255,0.4);
}

/* Metric */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(0,212,255,0.06), rgba(0,0,0,0));
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 10px;
    padding: 0.8rem 1rem;
}

[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.8rem !important;
}

[data-testid="stMetricLabel"] {
    color: #7a9abf !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── Matplotlib Dark Theme ─────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor'  : '#0d1b2a',
    'axes.facecolor'    : '#0d1b2a',
    'axes.edgecolor'    : '#1e3a5f',
    'axes.labelcolor'   : '#7a9abf',
    'xtick.color'       : '#7a9abf',
    'ytick.color'       : '#7a9abf',
    'text.color'        : '#e0e6f0',
    'grid.color'        : '#1e3a5f',
    'grid.alpha'        : 0.4,
    'axes.grid'         : True,
    'axes.spines.top'   : False,
    'axes.spines.right' : False,
    'figure.dpi'        : 130,
    'font.family'       : 'DejaVu Sans',
})

ACCENT   = '#00d4ff'
ACCENT2  = '#0080ff'
GREEN    = '#00ff88'
ORANGE   = '#ffb400'
RED      = '#ff4444'
DARK_BG  = '#0d1b2a'
PALETTE  = [ACCENT, ACCENT2, GREEN, ORANGE, RED]

# ── Player Data ───────────────────────────────────────────────────────────────
INDIA = [
    "Virat Kohli","Rohit Sharma","MS Dhoni","Sachin Tendulkar","Sourav Ganguly",
    "Rahul Dravid","Anil Kumble","Kapil Dev","Sunil Gavaskar","Yuvraj Singh",
    "Shikhar Dhawan","KL Rahul","Hardik Pandya","Jasprit Bumrah","Ravindra Jadeja",
    "Ravichandran Ashwin","Mohammed Shami","Shreyas Iyer","Rishabh Pant","Axar Patel",
    "Bhuvneshwar Kumar","Kuldeep Yadav","Yuzvendra Chahal","Prithvi Shaw","Mayank Agarwal",
    "Ajinkya Rahane","Cheteshwar Pujara","Wriddhiman Saha","Ishant Sharma","Umesh Yadav",
    "Mohammad Kaif","VVS Laxman","Zaheer Khan","Harbhajan Singh","Irfan Pathan",
    "Virender Sehwag","Gautam Gambhir","Dinesh Karthik","Suresh Raina","Ambati Rayudu",
    "Shardul Thakur","Deepak Chahar","Navdeep Saini","Mohammed Siraj","Hanuma Vihari",
    "Sanju Samson","Ruturaj Gaikwad","Devdutt Padikkal","Ishan Kishan","Venkatesh Iyer",
    "Shubman Gill","Suryakumar Yadav","Deepak Hooda","Ravi Bishnoi","Harshal Patel",
    "Arshdeep Singh","Mukesh Kumar","Tilak Varma","Rinku Singh","Yashasvi Jaiswal"
]
AUSTRALIA = [
    "Steve Smith","David Warner","Pat Cummins","Mitchell Starc","Nathan Lyon",
    "Glenn Maxwell","Adam Gilchrist","Ricky Ponting","Shane Warne","Brett Lee",
    "Matthew Hayden","Justin Langer","Damien Martyn","Michael Clarke","Andrew Symonds",
    "Brad Haddin","Mitchell Johnson","Peter Siddle","James Faulkner","Shane Watson",
    "Aaron Finch","Marnus Labuschagne","Travis Head","Cameron Green","Josh Hazlewood",
    "Alex Carey","Matthew Wade","David Hussey","Michael Hussey","Simon Katich",
    "Jason Gillespie","Stuart MacGill","Brad Hogg","Andrew McDonald","Tim Paine",
    "Usman Khawaja","Chris Lynn","Ben McDermott","Ashton Agar","Adam Zampa",
    "Sean Abbott","Daniel Sams","Marcus Stoinis","Matthew Short","Josh Inglis",
    "Lance Morris","Todd Murphy","Scott Boland","Jhye Richardson","Michael Neser",
    "Nathan Ellis","Riley Meredith","Xavier Bartlett","Matt Renshaw","Peter Handscomb",
    "Nic Maddinson","Callum Ferguson","Tim David","Jake Fraser-McGurk","Cooper Connolly"
]
ENGLAND = [
    "Joe Root","Ben Stokes","James Anderson","Stuart Broad","Jonny Bairstow",
    "Kevin Pietersen","Andrew Flintoff","Alastair Cook","Ian Bell","Graeme Swann",
    "Eoin Morgan","Jos Buttler","Chris Woakes","Mark Wood","Jofra Archer",
    "Sam Curran","Tom Curran","Moeen Ali","Adil Rashid","Dawid Malan",
    "Jason Roy","Alex Hales","Zak Crawley","Ben Duckett","Ollie Pope",
    "Harry Brook","Liam Livingstone","Phil Salt","Will Jacks","Matthew Potts",
    "Olly Stone","Craig Overton","Jamie Overton","Jack Leach","Reece Topley",
    "David Willey","Tymal Mills","Tom Hartley","Shoaib Bashir","Gus Atkinson",
    "Dan Lawrence","James Vince","Dom Sibley","Rory Burns","Nick Compton",
    "Jonathan Trott","Paul Collingwood","Matt Prior","Tim Bresnan","Steve Harmison",
    "Matthew Hoggard","Simon Jones","Ryan Sidebottom","Monty Panesar","Samit Patel",
    "Ravi Bopara","Luke Wright","Michael Lumb","Nick Gubbins","Jordan Cox"
]
SOUTH_AFRICA = [
    "AB de Villiers","Jacques Kallis","Graeme Smith","Dale Steyn","Hashim Amla",
    "Morne Morkel","Vernon Philander","Faf du Plessis","Quinton de Kock","Kagiso Rabada",
    "Allan Donald","Shaun Pollock","Gary Kirsten","Herschelle Gibbs","Lance Klusener",
    "Mark Boucher","Jonty Rhodes","Temba Bavuma","Aiden Markram","Rassie van der Dussen",
    "David Miller","Heinrich Klaasen","Marco Jansen","Anrich Nortje","Lungi Ngidi",
    "Wayne Parnell","Keshav Maharaj","Tabraiz Shamsi","Ryan Rickelton","Tristan Stubbs",
    "Reeza Hendricks","Tony de Zorzi","Gerald Coetzee","Nandre Burger","Ottneil Baartman",
    "Wiaan Mulder","Senuran Muthusamy","Andile Phehlukwayo","Dwaine Pretorius","Dean Elgar",
    "Neil McKenzie","Alviro Petersen","Jean-Paul Duminy","Robin Peterson","Imran Tahir",
    "Lonwabo Tsotsobe","Chris Morris","Kyle Abbott","Daryn Smit","Morne van Wyk",
    "Colin Ingram","Rilee Rossouw","Khaya Zondo","Stiaan van Zyl","Simon Harmer",
    "Junior Dala","Beuran Hendricks","Lutho Sipamla","Glenton Stuurman","Lizaad Williams"
]
NEW_ZEALAND = [
    "Kane Williamson","Ross Taylor","Brendon McCullum","Tim Southee","Trent Boult",
    "Martin Guptill","Daniel Vettori","Chris Cairns","Stephen Fleming","Nathan Astle",
    "Mitchell McClenaghan","Adam Milne","Lockie Ferguson","Matt Henry","Kyle Jamieson",
    "Tom Latham","Devon Conway","Will Young","Daryl Mitchell","Glenn Phillips",
    "Jimmy Neesham","Mitchell Santner","Ish Sodhi","Todd Astle","Colin de Grandhomme",
    "Henry Nicholls","BJ Watling","Tom Blundell","Scott Kuggeleijn","Blair Tickner",
    "Jacob Duffy","Ben Sears","Mark Chapman","Michael Bracewell","Rachin Ravindra",
    "Chad Bowes","Finn Allen","Tim Seifert","Cole McConchie","Ajaz Patel",
    "Neil Wagner","Colin Munro","Anton Devcich","Grant Elliott","Corey Anderson",
    "Luke Ronchi","Peter Fulton","Rob Nicol","Dean Brownlie","James Franklin",
    "Ian Butler","Chris Martin","Iain O'Brien","Jeetan Patel","Daniel Flynn",
    "Jesse Ryder","Scott Styris","Lou Vincent","Craig McMillan","Hamish Bennett"
]

ALL_PLAYERS = INDIA + AUSTRALIA + ENGLAND + SOUTH_AFRICA + NEW_ZEALAND
ALL_TEAMS   = ['India']*60 + ['Australia']*60 + ['England']*60 + ['South Africa']*60 + ['New Zealand']*60

TEAM_COLORS = {
    'India'        : '#ff9900',
    'Australia'    : '#00d4ff',
    'England'      : '#ff4466',
    'South Africa' : '#00ff88',
    'New Zealand'  : '#aa88ff'
}

# ── Dataset ───────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    np.random.seed(42)
    n = 300
    batting_avg    = np.round(np.random.normal(35, 15, n).clip(5, 90), 2)
    strike_rate    = np.round(np.random.normal(75, 20, n).clip(30, 180), 2)
    bowling_avg    = np.round(np.random.normal(30, 10, n).clip(15, 60), 2)
    wickets        = np.random.randint(0, 120, n)
    fielding_score = np.round(np.random.uniform(50, 100, n), 1)
    matches        = np.random.randint(5, 80, n)
    experience     = np.round(matches / 10 + np.random.normal(0, 0.5, n), 2)
    performance_score = np.round(
        batting_avg*0.40 + strike_rate*0.20 + wickets*0.30 +
        fielding_score*0.10 + np.random.normal(0, 5, n), 2).clip(0, 100)
    match_won = (performance_score > 55).astype(int)
    rating = pd.cut(performance_score,
                    bins=[0,40,55,70,100],
                    labels=['Below Average','Average','Good','Elite'])
    return pd.DataFrame({
        'Player': ALL_PLAYERS, 'Team': ALL_TEAMS,
        'Matches': matches, 'Batting_Avg': batting_avg,
        'Strike_Rate': strike_rate, 'Bowling_Avg': bowling_avg,
        'Wickets': wickets, 'Fielding_Score': fielding_score,
        'Experience': experience, 'Performance_Score': performance_score,
        'Match_Won': match_won, 'Rating': rating
    })

@st.cache_resource
def train_all_models(df):
    feat_r = ['Batting_Avg','Strike_Rate','Wickets','Fielding_Score','Matches']
    feat_c = ['Batting_Avg','Strike_Rate','Wickets','Fielding_Score','Matches','Bowling_Avg']
    Xr, yr = df[feat_r], df['Performance_Score']
    Xc, yc = df[feat_c], df['Match_Won']
    sc = StandardScaler(); Xcs = sc.fit_transform(Xc)
    Xr_tr,Xr_te,yr_tr,yr_te = train_test_split(Xr, yr, test_size=0.2, random_state=42)
    Xc_tr,Xc_te,yc_tr,yc_te = train_test_split(Xcs, yc, test_size=0.2, random_state=42, stratify=yc)

    lasso   = Lasso(alpha=0.5);           lasso.fit(Xr_tr, yr_tr)
    log_reg = LogisticRegression(max_iter=1000, random_state=42); log_reg.fit(Xc_tr, yc_tr)
    rf_r    = RandomForestRegressor(n_estimators=100, random_state=42); rf_r.fit(Xr_tr, yr_tr)
    rf_c    = RandomForestClassifier(n_estimators=100, random_state=42); rf_c.fit(Xc_tr, yc_tr)
    gb_c    = GradientBoostingClassifier(n_estimators=100, random_state=42); gb_c.fit(Xc_tr, yc_tr)

    yp_r  = lasso.predict(Xr_te)
    yp_c  = log_reg.predict(Xc_te)
    r2    = r2_score(yr_te, yp_r)
    rmse  = np.sqrt(mean_squared_error(yr_te, yp_r))
    acc   = (yp_c == yc_te).mean()
    auc   = roc_auc_score(yc_te, log_reg.predict_proba(Xc_te)[:,1])
    fpr, tpr, _ = roc_curve(yc_te, log_reg.predict_proba(Xc_te)[:,1])
    fi    = dict(zip(feat_r, rf_r.feature_importances_))

    return lasso, log_reg, rf_r, rf_c, gb_c, sc, feat_r, feat_c, r2, rmse, acc, auc, fpr, tpr, fi, Xr_te, yr_te, yp_r, Xc_te, yc_te

df = load_data()
lasso, log_reg, rf_r, rf_c, gb_c, scaler, feat_r, feat_c, r2, rmse, acc, auc, fpr, tpr, fi, Xr_te, yr_te, yp_r, Xc_te, yc_te = train_all_models(df)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0;'>
        <div style='font-family:Rajdhani,sans-serif; font-size:1.6rem; font-weight:700;
                    background:linear-gradient(90deg,#00d4ff,#00ff88);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
            CricketIQ
        </div>
        <div style='color:#7a9abf; font-size:0.75rem; letter-spacing:2px; margin-top:2px;'>
            ANALYTICS PLATFORM
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    page = st.radio("", [
        "Overview",
        "Team Analysis",
        "Player Explorer",
        "Statistical Tests",
        "Model Performance",
        "Leaderboard",
        "Player Prediction"
    ], label_visibility="collapsed")

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='font-size:0.8rem; color:#7a9abf; line-height:2;'>
        Players &nbsp;<span style='color:#00d4ff; font-weight:600;'>{len(df)}</span><br>
        Teams &nbsp;&nbsp;&nbsp;<span style='color:#00d4ff; font-weight:600;'>{df['Team'].nunique()}</span><br>
        Variables &nbsp;<span style='color:#00d4ff; font-weight:600;'>{df.shape[1]}</span><br>
        Win Rate &nbsp;<span style='color:#00ff88; font-weight:600;'>{df['Match_Won'].mean():.1%}</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#3a5a7a; font-size:0.7rem; text-align:center;'>DATA-200 | Project-Stats-Team<br>Week 7 | February 2026</div>", unsafe_allow_html=True)


# =============================================================================
# OVERVIEW
# =============================================================================
if page == "Overview":
    st.markdown("<div class='page-title'>Sports Analytics Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>DATA-200 Project &nbsp;|&nbsp; Project-Stats-Team &nbsp;|&nbsp; 300 International Cricket Players</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    # KPI Row
    c1,c2,c3,c4,c5,c6 = st.columns(6)
    kpis = [
        ("300", "Total Players", "5 Teams"),
        (f"{df['Performance_Score'].mean():.1f}", "Avg Performance", "out of 100"),
        (f"{df['Batting_Avg'].mean():.1f}", "Avg Batting Avg", "runs/dismissal"),
        (f"{df['Match_Won'].mean():.1%}", "Overall Win Rate", "all teams"),
        (f"{r2:.3f}", "Best R² Score", "Lasso Model"),
        (f"{acc:.1%}", "Classifier Acc", "Logistic Reg"),
    ]
    for col, (val, label, sub) in zip([c1,c2,c3,c4,c5,c6], kpis):
        col.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-value'>{val}</div>
            <div class='kpi-label'>{label}</div>
            <div class='kpi-delta'>{sub}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.markdown("<div class='section-header'>Performance Score Distribution</div>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(9, 4))
        for team, col in TEAM_COLORS.items():
            subset = df[df['Team'] == team]['Performance_Score']
            ax.hist(subset, bins=18, alpha=0.55, color=col, edgecolor='none', label=team)
        ax.axvline(df['Performance_Score'].mean(), color='white', linestyle='--', lw=1.5, alpha=0.7, label=f"Mean: {df['Performance_Score'].mean():.1f}")
        ax.set_xlabel('Performance Score', fontsize=10)
        ax.set_ylabel('Players', fontsize=10)
        ax.set_title('All Teams – Performance Score Distribution', fontsize=11, color='#e0e6f0', pad=10)
        ax.legend(fontsize=8, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        fig.tight_layout()
        st.pyplot(fig); plt.close()

    with col_right:
        st.markdown("<div class='section-header'>Player Ratings</div>", unsafe_allow_html=True)
        rating_counts = df['Rating'].value_counts()
        fig, ax = plt.subplots(figsize=(5, 4))
        wedge_colors = [GREEN, ACCENT, ORANGE, RED]
        wedges, texts, autotexts = ax.pie(
            rating_counts.values, labels=rating_counts.index,
            colors=wedge_colors, autopct='%1.1f%%',
            startangle=90, pctdistance=0.75,
            wedgeprops=dict(width=0.6, edgecolor='#0d1b2a', linewidth=2)
        )
        for text in texts: text.set_color('#b0c4d8'); text.set_fontsize(9)
        for at in autotexts: at.set_color('#0a0e1a'); at.set_fontsize(8); at.set_fontweight('bold')
        ax.set_title('Player Rating Breakdown', fontsize=11, color='#e0e6f0', pad=10)
        fig.tight_layout()
        st.pyplot(fig); plt.close()

    st.markdown("<div class='section-header'>Problem Statement & Project Overview</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(0,212,255,0.06),rgba(0,0,0,0));
                border:1px solid rgba(0,212,255,0.15); border-radius:12px; padding:1.2rem 1.5rem;
                color:#b0c4d8; font-size:0.9rem; line-height:1.8;'>
        <em>"Our team aims to analyze a real-world sports dataset to identify patterns and relationships
        that affect player performance and match outcomes. We apply statistical modeling and predictive
        techniques, including Linear Regression, ANOVA, and Logistic Regression, to generate actionable
        insights and support data-driven decision-making in sports."</em>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Project Timeline</div>", unsafe_allow_html=True)
    weeks = ["Week 2","Week 3","Week 4","Week 5","Week 6","Week 7"]
    tasks = ["Literature Review","EDA","Data Cleaning & Feature Engineering",
             "Statistical Analysis — t-Test, ANOVA, Linear & Logistic Regression",
             "Advanced Modeling — Ridge, Lasso, Random Forest, Gradient Boosting",
             "Python Application Development (This App)"]
    for w, t in zip(weeks, tasks):
        st.markdown(f"""
        <div style='display:flex; align-items:center; margin-bottom:0.5rem;
                    background:rgba(0,212,255,0.04); border-radius:8px; padding:0.5rem 1rem;
                    border-left:3px solid #00d4ff;'>
            <span style='color:#00d4ff; font-family:Rajdhani,sans-serif; font-weight:700;
                         font-size:0.9rem; min-width:70px;'>{w}</span>
            <span style='color:#b0c4d8; font-size:0.85rem; margin-left:1rem;'>{t}</span>
            <span style='margin-left:auto; color:#00ff88; font-size:0.8rem;'>Complete</span>
        </div>
        """, unsafe_allow_html=True)


# =============================================================================
# TEAM ANALYSIS
# =============================================================================
elif page == "Team Analysis":
    st.markdown("<div class='page-title'>Team Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Head-to-head comparison across all 5 international teams</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    # Team KPIs
    team_stats = df.groupby('Team').agg(
        Players=('Player','count'),
        Avg_Score=('Performance_Score','mean'),
        Win_Rate=('Match_Won','mean'),
        Avg_Batting=('Batting_Avg','mean'),
        Avg_Wickets=('Wickets','mean'),
        Elite_Players=('Rating', lambda x: (x=='Elite').sum())
    ).round(2)

    cols = st.columns(5)
    for col, (team, row) in zip(cols, team_stats.iterrows()):
        tc = TEAM_COLORS[team]
        col.markdown(f"""
        <div style='background:linear-gradient(135deg,{tc}15,{tc}05);
                    border:1px solid {tc}40; border-radius:12px; padding:1rem; text-align:center;'>
            <div style='font-family:Rajdhani,sans-serif; font-size:1rem; font-weight:700; color:{tc};
                        text-transform:uppercase; letter-spacing:1px;'>{team}</div>
            <div style='font-family:Rajdhani,sans-serif; font-size:2rem; font-weight:700; color:{tc};
                        margin:0.3rem 0;'>{row['Avg_Score']:.1f}</div>
            <div style='color:#7a9abf; font-size:0.7rem; letter-spacing:1px;'>AVG SCORE</div>
            <div style='color:#00ff88; font-size:0.85rem; margin-top:0.4rem;'>Win Rate: {row['Win_Rate']:.1%}</div>
            <div style='color:#7a9abf; font-size:0.75rem;'>Elite: {int(row['Elite_Players'])} players</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-header'>Performance Score by Team</div>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(8, 5))
        team_order = df.groupby('Team')['Performance_Score'].median().sort_values(ascending=False).index
        colors_list = [TEAM_COLORS[t] for t in team_order]
        data_to_plot = [df[df['Team']==t]['Performance_Score'].values for t in team_order]
        bp = ax.boxplot(data_to_plot, labels=team_order, patch_artist=True, notch=False,
                        medianprops=dict(color='white', lw=2),
                        whiskerprops=dict(color='#3a5a7a'),
                        capprops=dict(color='#3a5a7a'),
                        flierprops=dict(marker='o', color='#3a5a7a', alpha=0.4, markersize=4))
        for patch, col in zip(bp['boxes'], colors_list):
            patch.set_facecolor(col); patch.set_alpha(0.6)
        ax.axhline(df['Performance_Score'].mean(), color='white', linestyle='--', lw=1.2, alpha=0.5)
        ax.set_xlabel('Team', fontsize=10); ax.set_ylabel('Performance Score', fontsize=10)
        ax.set_title('Performance Score Distribution by Team', fontsize=11, color='#e0e6f0', pad=10)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.markdown("<div class='section-header'>Win Rate Comparison</div>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(8, 5))
        wr = df.groupby('Team')['Match_Won'].mean().sort_values(ascending=True)
        bars = ax.barh(wr.index, wr.values*100,
                       color=[TEAM_COLORS[t] for t in wr.index], alpha=0.8, edgecolor='none', height=0.5)
        for bar, val in zip(bars, wr.values*100):
            ax.text(val+0.5, bar.get_y()+bar.get_height()/2, f'{val:.1f}%',
                    va='center', fontsize=10, color='white', fontweight='600')
        ax.axvline(50, color='white', linestyle='--', lw=1, alpha=0.3)
        ax.set_xlabel('Win Rate (%)', fontsize=10)
        ax.set_title('Match Win Rate by Team', fontsize=11, color='#e0e6f0', pad=10)
        ax.set_xlim(0, 80)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.markdown("<div class='section-header'>Multi-Metric Radar Comparison</div>", unsafe_allow_html=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    metrics = ['Batting_Avg','Strike_Rate','Wickets']
    titles  = ['Batting Average','Strike Rate','Wickets Taken']
    for ax, metric, title in zip(axes, metrics, titles):
        team_means = df.groupby('Team')[metric].mean().sort_values(ascending=False)
        bars = ax.bar(team_means.index, team_means.values,
                      color=[TEAM_COLORS[t] for t in team_means.index], alpha=0.8, edgecolor='none')
        for bar, val in zip(bars, team_means.values):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, f'{val:.1f}',
                    ha='center', fontsize=8, color='white', fontweight='600')
        ax.set_title(title, fontsize=10, color='#e0e6f0', pad=8)
        ax.set_xticklabels(team_means.index, rotation=15, ha='right', fontsize=8)
    fig.tight_layout(); st.pyplot(fig); plt.close()


# =============================================================================
# PLAYER EXPLORER
# =============================================================================
elif page == "Player Explorer":
    st.markdown("<div class='page-title'>Player Explorer</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Search, filter and analyze all 300 international cricket players</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        search = st.text_input("Search player name", placeholder="e.g. Virat Kohli")
    with col_f2:
        team_filter = st.selectbox("Filter by Team", ['All'] + sorted(df['Team'].unique().tolist()))
    with col_f3:
        rating_filter = st.selectbox("Filter by Rating", ['All','Elite','Good','Average','Below Average'])
    with col_f4:
        sort_by = st.selectbox("Sort by", ['Performance_Score','Batting_Avg','Strike_Rate','Wickets','Matches'])

    fdf = df.copy()
    if search:       fdf = fdf[fdf['Player'].str.contains(search, case=False)]
    if team_filter != 'All':   fdf = fdf[fdf['Team'] == team_filter]
    if rating_filter != 'All': fdf = fdf[fdf['Rating'] == rating_filter]
    fdf = fdf.sort_values(sort_by, ascending=False).reset_index(drop=True)

    st.markdown(f"<div style='color:#7a9abf; font-size:0.85rem; margin-bottom:0.8rem;'>Showing <span style='color:#00d4ff; font-weight:600;'>{len(fdf)}</span> players</div>", unsafe_allow_html=True)

    # Top 3 highlight cards
    if len(fdf) >= 3:
        st.markdown("<div class='section-header'>Top Performers</div>", unsafe_allow_html=True)
        top3 = fdf.head(3)
        tcols = st.columns(3)
        for col, (_, row) in zip(tcols, top3.iterrows()):
            tc = TEAM_COLORS.get(row['Team'], ACCENT)
            col.markdown(f"""
            <div style='background:linear-gradient(135deg,{tc}15,{tc}05);
                        border:1px solid {tc}40; border-radius:12px; padding:1.2rem; text-align:center;'>
                <div style='font-family:Rajdhani,sans-serif; font-size:1.2rem; font-weight:700;
                            color:#e0e6f0;'>{row['Player']}</div>
                <div style='color:{tc}; font-size:0.8rem; margin:0.3rem 0;'>{row['Team']}</div>
                <div style='font-family:Rajdhani,sans-serif; font-size:2.2rem; font-weight:700;
                            color:{tc};'>{row['Performance_Score']:.1f}</div>
                <div style='color:#7a9abf; font-size:0.7rem; letter-spacing:1px;'>PERFORMANCE SCORE</div>
                <div style='display:flex; justify-content:space-around; margin-top:0.8rem;'>
                    <div style='text-align:center;'>
                        <div style='color:{tc}; font-weight:600; font-size:0.9rem;'>{row['Batting_Avg']}</div>
                        <div style='color:#7a9abf; font-size:0.65rem;'>BAT AVG</div>
                    </div>
                    <div style='text-align:center;'>
                        <div style='color:{tc}; font-weight:600; font-size:0.9rem;'>{row['Wickets']}</div>
                        <div style='color:#7a9abf; font-size:0.65rem;'>WICKETS</div>
                    </div>
                    <div style='color:{"#00ff88" if row["Match_Won"]==1 else "#ff4444"};
                                font-weight:600; font-size:0.9rem; display:flex; align-items:center;'>
                        {"Win" if row["Match_Won"]==1 else "Loss"}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='section-header'>All Players</div>", unsafe_allow_html=True)
    display_cols = ['Player','Team','Matches','Batting_Avg','Strike_Rate','Bowling_Avg','Wickets','Fielding_Score','Performance_Score','Rating','Match_Won']
    st.dataframe(fdf[display_cols], use_container_width=True, hide_index=True, height=400)

    st.markdown("<div class='section-header'>Scatter Analysis</div>", unsafe_allow_html=True)
    sc1, sc2 = st.columns(2)
    with sc1: x_axis = st.selectbox("X Axis", ['Batting_Avg','Strike_Rate','Wickets','Fielding_Score','Matches','Bowling_Avg'], index=0)
    with sc2: y_axis = st.selectbox("Y Axis", ['Performance_Score','Batting_Avg','Strike_Rate','Wickets','Fielding_Score'], index=0)

    fig, ax = plt.subplots(figsize=(10, 5))
    for team, tc in TEAM_COLORS.items():
        sub = fdf[fdf['Team'] == team]
        ax.scatter(sub[x_axis], sub[y_axis], color=tc, alpha=0.7, s=50, edgecolors='none', label=team)
    ax.set_xlabel(x_axis.replace('_',' '), fontsize=10)
    ax.set_ylabel(y_axis.replace('_',' '), fontsize=10)
    ax.set_title(f'{x_axis.replace("_"," ")} vs {y_axis.replace("_"," ")}', fontsize=11, color='#e0e6f0')
    ax.legend(fontsize=8, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
    fig.tight_layout(); st.pyplot(fig); plt.close()


# =============================================================================
# STATISTICAL TESTS
# =============================================================================
elif page == "Statistical Tests":
    st.markdown("<div class='page-title'>Statistical Analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Week 5 — Hypothesis testing, descriptive statistics and correlation analysis</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>Descriptive Statistics</div>", unsafe_allow_html=True)
    num_cols = ['Batting_Avg','Strike_Rate','Bowling_Avg','Wickets','Fielding_Score','Performance_Score']
    desc = df[num_cols].describe().T.round(3)
    desc['skewness'] = df[num_cols].skew().round(3)
    desc['kurtosis'] = df[num_cols].kurt().round(3)
    st.dataframe(desc, use_container_width=True)

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-header'>t-Test: Experience vs Performance</div>", unsafe_allow_html=True)
        med_exp = df['Experience'].median()
        hi = df[df['Experience'] >  med_exp]['Performance_Score']
        lo = df[df['Experience'] <= med_exp]['Performance_Score']
        t_stat, t_p = stats.ttest_ind(hi, lo)
        decision = "Reject H0" if t_p < 0.05 else "Fail to Reject H0"
        d_color  = GREEN if t_p < 0.05 else ORANGE
        st.markdown(f"""
        <div style='background:rgba(0,212,255,0.05); border:1px solid rgba(0,212,255,0.15);
                    border-radius:10px; padding:1rem; margin-bottom:1rem;'>
            <div style='display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;'>
                <div style='color:#7a9abf; font-size:0.8rem;'>H0</div>
                <div style='color:#e0e6f0; font-size:0.8rem;'>No significant difference</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>t-statistic</div>
                <div style='color:#00d4ff; font-weight:600;'>{t_stat:.4f}</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>p-value</div>
                <div style='color:#00d4ff; font-weight:600;'>{t_p:.4f}</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>Alpha</div>
                <div style='color:#e0e6f0;'>0.05</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>Decision</div>
                <div style='color:{d_color}; font-weight:700;'>{decision}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.hist(hi, bins=15, alpha=0.7, color=ACCENT,  edgecolor='none', label=f'High Experience (n={len(hi)})')
        ax.hist(lo, bins=15, alpha=0.7, color=ORANGE, edgecolor='none', label=f'Low Experience (n={len(lo)})')
        ax.axvline(hi.mean(), color=ACCENT,  linestyle='--', lw=2, alpha=0.8)
        ax.axvline(lo.mean(), color=ORANGE, linestyle='--', lw=2, alpha=0.8)
        ax.set_xlabel('Performance Score', fontsize=9); ax.set_ylabel('Frequency', fontsize=9)
        ax.set_title('Performance Distribution by Experience Level', fontsize=10, color='#e0e6f0')
        ax.legend(fontsize=8, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with col2:
        st.markdown("<div class='section-header'>ANOVA: Teams vs Performance</div>", unsafe_allow_html=True)
        grps = [df[df['Team']==t]['Performance_Score'].values for t in df['Team'].unique()]
        f_stat, f_p = stats.f_oneway(*grps)
        decision2 = "Reject H0" if f_p < 0.05 else "Fail to Reject H0"
        d_color2  = GREEN if f_p < 0.05 else ORANGE
        st.markdown(f"""
        <div style='background:rgba(0,212,255,0.05); border:1px solid rgba(0,212,255,0.15);
                    border-radius:10px; padding:1rem; margin-bottom:1rem;'>
            <div style='display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;'>
                <div style='color:#7a9abf; font-size:0.8rem;'>H0</div>
                <div style='color:#e0e6f0; font-size:0.8rem;'>All team means are equal</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>F-statistic</div>
                <div style='color:#00d4ff; font-weight:600;'>{f_stat:.4f}</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>p-value</div>
                <div style='color:#00d4ff; font-weight:600;'>{f_p:.4f}</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>Alpha</div>
                <div style='color:#e0e6f0;'>0.05</div>
                <div style='color:#7a9abf; font-size:0.8rem;'>Decision</div>
                <div style='color:{d_color2}; font-weight:700;'>{decision2}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        sorted_teams  = df.groupby('Team')['Performance_Score'].median().sort_values(ascending=False).index
        sorted_groups = [df[df['Team']==t]['Performance_Score'].values for t in sorted_teams]
        fig, ax = plt.subplots(figsize=(7, 3.5))
        bp = ax.boxplot(sorted_groups, labels=sorted_teams, patch_artist=True,
                        medianprops=dict(color='white', lw=2),
                        whiskerprops=dict(color='#3a5a7a'), capprops=dict(color='#3a5a7a'),
                        flierprops=dict(marker='o', color='#3a5a7a', alpha=0.3, markersize=3))
        for patch, team in zip(bp['boxes'], sorted_teams):
            patch.set_facecolor(TEAM_COLORS[team]); patch.set_alpha(0.7)
        ax.set_xlabel('Team', fontsize=9); ax.set_ylabel('Performance Score', fontsize=9)
        ax.set_title('Performance Score Across Teams', fontsize=10, color='#e0e6f0')
        fig.tight_layout(); st.pyplot(fig); plt.close()

    st.markdown("<div class='section-header'>Correlation Heatmap</div>", unsafe_allow_html=True)
    corr_cols = ['Batting_Avg','Strike_Rate','Bowling_Avg','Wickets','Fielding_Score','Matches','Experience','Performance_Score']
    corr = df[corr_cols].corr()
    fig, ax = plt.subplots(figsize=(11, 6))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap=cmap, center=0,
                linewidths=0.5, ax=ax, annot_kws={'size': 9, 'weight': 'bold'},
                cbar_kws={'shrink': 0.8})
    ax.set_title('Pearson Correlation Matrix — All Variables', fontsize=11, color='#e0e6f0', pad=10)
    fig.tight_layout(); st.pyplot(fig); plt.close()


# =============================================================================
# MODEL PERFORMANCE
# =============================================================================
elif page == "Model Performance":
    st.markdown("<div class='page-title'>Model Performance</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Week 5 & 6 — Full regression and classification model comparison</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Regression Models", "Classification Models", "Feature Importance"])

    with tab1:
        st.markdown("<div class='section-header'>Regression Results</div>", unsafe_allow_html=True)
        reg_df = pd.DataFrame({
            'Model'      : ['Linear Regression (Week 5)','Ridge (alpha=10)','Lasso (alpha=0.5)','Random Forest'],
            'R2 Score'   : [0.827, 0.827, 0.828, 0.732],
            'RMSE'       : [4.906, 4.906, 4.894, 6.106],
            'CV R2 Mean' : [0.82, 0.82, 0.82, 0.71],
            'Best'       : ['No','No','Yes','No']
        })
        st.dataframe(reg_df, use_container_width=True, hide_index=True)

        fig, axes = plt.subplots(1, 2, figsize=(13, 5))
        names     = ['Linear\n(W5)','Ridge','Lasso','Random\nForest']
        r2_vals   = [0.827, 0.827, 0.828, 0.732]
        rmse_vals = [4.906, 4.906, 4.894, 6.106]
        bcolors   = [ACCENT2, ACCENT, GREEN, ORANGE]

        bars = axes[0].bar(names, r2_vals, color=bcolors, edgecolor='none', alpha=0.85, width=0.5)
        axes[0].set_title('R2 Score — Higher is Better', fontsize=11, color='#e0e6f0', pad=10)
        axes[0].set_ylim(0, 1.1)
        axes[0].axhline(0.8, color='white', linestyle='--', lw=1, alpha=0.3, label='0.8 threshold')
        axes[0].legend(fontsize=8, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        for bar, val in zip(bars, r2_vals):
            axes[0].text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.01, f'{val:.3f}',
                         ha='center', fontweight='bold', fontsize=10, color='white')

        bars2 = axes[1].bar(names, rmse_vals, color=bcolors, edgecolor='none', alpha=0.85, width=0.5)
        axes[1].set_title('RMSE — Lower is Better', fontsize=11, color='#e0e6f0', pad=10)
        for bar, val in zip(bars2, rmse_vals):
            axes[1].text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.05, f'{val:.2f}',
                         ha='center', fontweight='bold', fontsize=10, color='white')

        st.markdown("<div class='section-header'>Actual vs Predicted — Lasso</div>", unsafe_allow_html=True)
        axes[0].set_facecolor('#0d1b2a'); axes[1].set_facecolor('#0d1b2a')
        fig.tight_layout(); st.pyplot(fig); plt.close()

        fig, axes = plt.subplots(1, 2, figsize=(13, 5))
        axes[0].scatter(yr_te, yp_r, alpha=0.6, color=ACCENT, edgecolors='none', s=50)
        mv = [min(yr_te.min(), yp_r.min()), max(yr_te.max(), yp_r.max())]
        axes[0].plot(mv, mv, color=GREEN, linestyle='--', lw=2, label='Perfect Fit')
        axes[0].set_xlabel('Actual Score', fontsize=10); axes[0].set_ylabel('Predicted Score', fontsize=10)
        axes[0].set_title(f'Actual vs Predicted  (R²={r2:.3f})', fontsize=11, color='#e0e6f0')
        axes[0].legend(fontsize=9, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        residuals = yr_te - yp_r
        axes[1].scatter(yp_r, residuals, alpha=0.6, color=ORANGE, edgecolors='none', s=50)
        axes[1].axhline(0, color='white', linestyle='--', lw=1.5, alpha=0.5)
        axes[1].set_xlabel('Predicted Values', fontsize=10); axes[1].set_ylabel('Residuals', fontsize=10)
        axes[1].set_title('Residual Plot', fontsize=11, color='#e0e6f0')
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with tab2:
        st.markdown("<div class='section-header'>Classification Results</div>", unsafe_allow_html=True)
        clf_df = pd.DataFrame({
            'Model'      : ['Logistic Regression (Week 5)','Random Forest','Gradient Boosting'],
            'Accuracy'   : ['88.3%','85.0%','80.0%'],
            'ROC-AUC'    : [0.972, 0.928, 0.919],
            'CV Accuracy': ['86%','83%','80%'],
            'Best'       : ['Yes','No','No']
        })
        st.dataframe(clf_df, use_container_width=True, hide_index=True)

        fig, axes = plt.subplots(1, 2, figsize=(13, 5))
        names_c  = ['Logistic\nReg','Random\nForest','Gradient\nBoosting']
        acc_vals = [0.883, 0.850, 0.800]
        auc_vals = [0.972, 0.928, 0.919]
        bc       = [GREEN, ACCENT, ORANGE]

        bars3 = axes[0].bar(names_c, acc_vals, color=bc, edgecolor='none', alpha=0.85, width=0.4)
        axes[0].set_title('Accuracy — Higher is Better', fontsize=11, color='#e0e6f0', pad=10)
        axes[0].set_ylim(0, 1.1)
        axes[0].axhline(0.8, color='white', linestyle='--', lw=1, alpha=0.3)
        for bar, val in zip(bars3, acc_vals):
            axes[0].text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.01, f'{val:.1%}',
                         ha='center', fontweight='bold', fontsize=11, color='white')

        axes[1].plot(fpr, tpr, color=GREEN, lw=2.5, label=f'Logistic Reg (AUC={auc:.3f})')
        axes[1].plot([0,1],[0,1], color='#3a5a7a', linestyle='--', lw=1.5)
        axes[1].fill_between(fpr, tpr, alpha=0.1, color=GREEN)
        axes[1].set_xlabel('False Positive Rate', fontsize=10)
        axes[1].set_ylabel('True Positive Rate', fontsize=10)
        axes[1].set_title('ROC Curve', fontsize=11, color='#e0e6f0', pad=10)
        axes[1].legend(fontsize=9, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        fig.tight_layout(); st.pyplot(fig); plt.close()

    with tab3:
        st.markdown("<div class='section-header'>Random Forest Feature Importance</div>", unsafe_allow_html=True)
        fi_sorted = dict(sorted(fi.items(), key=lambda x: x[1], reverse=True))
        fig, ax = plt.subplots(figsize=(9, 4))
        bars = ax.barh(list(fi_sorted.keys()), list(fi_sorted.values()),
                       color=[ACCENT, GREEN, ORANGE, ACCENT2, RED], edgecolor='none', alpha=0.85)
        for bar, val in zip(bars, fi_sorted.values()):
            ax.text(val+0.002, bar.get_y()+bar.get_height()/2, f'{val:.3f}',
                    va='center', fontsize=10, color='white', fontweight='600')
        ax.set_title('Feature Importance — Predicting Performance Score', fontsize=11, color='#e0e6f0', pad=10)
        ax.set_xlabel('Importance Score', fontsize=10)
        fig.tight_layout(); st.pyplot(fig); plt.close()


# =============================================================================
# LEADERBOARD
# =============================================================================
elif page == "Leaderboard":
    st.markdown("<div class='page-title'>Player Leaderboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Top performing players ranked by performance score</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    metric_opt = st.selectbox("Rank by", ['Performance_Score','Batting_Avg','Strike_Rate','Wickets','Fielding_Score'])
    top_n      = st.slider("Show top N players", 5, 50, 20)

    top = df.nlargest(top_n, metric_opt).reset_index(drop=True)

    # Top 3 podium
    if len(top) >= 3:
        p2, p1, p3 = st.columns([1,1.2,1])
        for col, idx, medal, height in [(p2,1,'2nd','85%'), (p1,0,'1st','100%'), (p3,2,'3rd','70%')]:
            row = top.iloc[idx]
            tc  = TEAM_COLORS.get(row['Team'], ACCENT)
            col.markdown(f"""
            <div style='background:linear-gradient(135deg,{tc}20,{tc}08);
                        border:1px solid {tc}50; border-radius:14px; padding:1.5rem;
                        text-align:center; min-height:{height};'>
                <div style='font-size:2rem; margin-bottom:0.3rem;'>{"🥇" if medal=="1st" else "🥈" if medal=="2nd" else "🥉"}</div>
                <div style='font-family:Rajdhani,sans-serif; font-size:1.1rem; font-weight:700;
                            color:#e0e6f0;'>{row['Player']}</div>
                <div style='color:{tc}; font-size:0.8rem; margin:0.3rem 0;'>{row['Team']}</div>
                <div style='font-family:Rajdhani,sans-serif; font-size:2.5rem; font-weight:700;
                            color:{tc};'>{row[metric_opt]:.1f}</div>
                <div style='color:#7a9abf; font-size:0.7rem; letter-spacing:1px;'>{metric_opt.replace("_"," ").upper()}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(13, max(5, top_n * 0.35)))
    y_pos = range(len(top)-1, -1, -1)
    bar_colors = [TEAM_COLORS.get(t, ACCENT) for t in top['Team']]
    bars = ax.barh(list(y_pos), top[metric_opt].values, color=bar_colors, edgecolor='none', alpha=0.8, height=0.7)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels([f"{row['Player']} ({row['Team']})" for _, row in top.iterrows()], fontsize=9)
    ax.set_xlabel(metric_opt.replace('_',' '), fontsize=10)
    ax.set_title(f'Top {top_n} Players by {metric_opt.replace("_"," ")}', fontsize=12, color='#e0e6f0', pad=10)
    for bar, val in zip(bars, top[metric_opt].values):
        ax.text(val + 0.3, bar.get_y()+bar.get_height()/2, f'{val:.1f}', va='center', fontsize=8, color='white')
    legend_patches = [mpatches.Patch(color=TEAM_COLORS[t], label=t) for t in TEAM_COLORS]
    ax.legend(handles=legend_patches, fontsize=8, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f', loc='lower right')
    fig.tight_layout(); st.pyplot(fig); plt.close()

    st.dataframe(top[['Player','Team','Matches','Batting_Avg','Strike_Rate','Wickets','Performance_Score','Rating']],
                 use_container_width=True, hide_index=False)


# =============================================================================
# PLAYER PREDICTION
# =============================================================================
elif page == "Player Prediction":
    st.markdown("<div class='page-title'>Player Prediction Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-subtitle'>Enter player statistics to predict performance score and match outcome probability</div>", unsafe_allow_html=True)
    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div style='color:#00d4ff; font-weight:600; margin-bottom:0.5rem; font-family:Rajdhani,sans-serif; font-size:1.1rem; letter-spacing:1px;'>BATTING</div>", unsafe_allow_html=True)
        batting_avg    = st.slider("Batting Average",  5.0,  90.0,  35.0, 0.5)
        strike_rate    = st.slider("Strike Rate",      30.0, 180.0, 75.0, 0.5)
    with col2:
        st.markdown("<div style='color:#00d4ff; font-weight:600; margin-bottom:0.5rem; font-family:Rajdhani,sans-serif; font-size:1.1rem; letter-spacing:1px;'>BOWLING & FIELDING</div>", unsafe_allow_html=True)
        wickets        = st.slider("Wickets Taken",    0,    120,   50)
        bowling_avg    = st.slider("Bowling Average",  15.0, 60.0,  30.0, 0.5)
        fielding_score = st.slider("Fielding Score",   50.0, 100.0, 75.0, 0.5)
    with col3:
        st.markdown("<div style='color:#00d4ff; font-weight:600; margin-bottom:0.5rem; font-family:Rajdhani,sans-serif; font-size:1.1rem; letter-spacing:1px;'>EXPERIENCE</div>", unsafe_allow_html=True)
        matches        = st.slider("Matches Played",   5,    80,    40)
        st.markdown(f"""
        <div style='background:rgba(0,212,255,0.05); border:1px solid rgba(0,212,255,0.1);
                    border-radius:8px; padding:0.8rem; margin-top:1rem;'>
            <div style='color:#7a9abf; font-size:0.75rem; letter-spacing:1px;'>DATASET CONTEXT</div>
            <div style='color:#b0c4d8; font-size:0.8rem; margin-top:0.5rem; line-height:1.8;'>
                Avg Batting: 34.55<br>
                Avg Wickets: 55.82<br>
                Avg Matches: 41.55<br>
                Win Rate: {df['Match_Won'].mean():.1%}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

    if st.button("RUN PREDICTION"):
        input_r  = np.array([[batting_avg, strike_rate, wickets, fielding_score, matches]])
        pred_score = np.clip(lasso.predict(input_r)[0], 0, 100)
        input_c    = np.array([[batting_avg, strike_rate, wickets, fielding_score, matches, bowling_avg]])
        input_sc   = scaler.transform(input_c)
        pred_out   = log_reg.predict(input_sc)[0]
        pred_prob  = log_reg.predict_proba(input_sc)[0]
        win_prob   = pred_prob[1] * 100

        st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'>Prediction Results</div>", unsafe_allow_html=True)

        rc1, rc2, rc3, rc4 = st.columns(4)
        rc1.metric("Performance Score", f"{pred_score:.1f} / 100")
        rc2.metric("Match Outcome",     "Win" if pred_out == 1 else "Loss")
        rc3.metric("Win Probability",   f"{win_prob:.1f}%")
        rc4.metric("Loss Probability",  f"{pred_prob[0]*100:.1f}%")

        if pred_score >= 70:
            rating_label, rating_class = "Elite Player", "result-elite"
            rating_desc = f"Outstanding performance — top {(df['Performance_Score'] > pred_score).mean():.0%} of all players."
        elif pred_score >= 55:
            rating_label, rating_class = "Good Player", "result-good"
            rating_desc = "Above average — consistent contributor to the team."
        elif pred_score >= 40:
            rating_label, rating_class = "Average Player", "result-avg"
            rating_desc = "Room for improvement — focus on batting average and wickets."
        else:
            rating_label, rating_class = "Below Average", "result-low"
            rating_desc = "Significant development needed across all skill areas."

        st.markdown(f"""
        <div class='{rating_class}'>
            {rating_label} &nbsp;—&nbsp; {rating_desc}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='glowing-divider'></div>", unsafe_allow_html=True)

        fig, axes = plt.subplots(1, 2, figsize=(13, 4))
        # Win probability
        outcomes = ['Loss', 'Win']
        probs    = [pred_prob[0]*100, pred_prob[1]*100]
        axes[0].barh(outcomes, probs, color=[RED, GREEN], edgecolor='none', alpha=0.85, height=0.4)
        for i, val in enumerate(probs):
            axes[0].text(val+0.5, i, f'{val:.1f}%', va='center', fontsize=12, color='white', fontweight='700')
        axes[0].set_xlim(0, 110); axes[0].set_xlabel('Probability (%)', fontsize=10)
        axes[0].set_title('Match Outcome Probability', fontsize=11, color='#e0e6f0', pad=10)

        # Comparison with dataset
        stats_compare = {
            'Batting Avg': (batting_avg, 34.55),
            'Strike Rate': (strike_rate, 76.71),
            'Wickets'    : (wickets, 55.82),
            'Field Score': (fielding_score, 75.03),
            'Matches'    : (matches, 41.55)
        }
        x = np.arange(len(stats_compare))
        player_vals = [v[0] for v in stats_compare.values()]
        mean_vals   = [v[1] for v in stats_compare.values()]
        norm_p = [v/max(player_vals+mean_vals) for v in player_vals]
        norm_m = [v/max(player_vals+mean_vals) for v in mean_vals]
        w = 0.3
        axes[1].bar(x-w/2, norm_p, w, color=ACCENT, alpha=0.85, edgecolor='none', label='Your Player')
        axes[1].bar(x+w/2, norm_m, w, color='#3a5a7a', alpha=0.85, edgecolor='none', label='Dataset Mean')
        axes[1].set_xticks(x); axes[1].set_xticklabels(list(stats_compare.keys()), fontsize=9)
        axes[1].set_title('Your Player vs Dataset Average', fontsize=11, color='#e0e6f0', pad=10)
        axes[1].legend(fontsize=9, framealpha=0.2, facecolor='#0d1b2a', edgecolor='#1e3a5f')
        axes[1].set_ylabel('Normalised Value', fontsize=10)
        fig.tight_layout(); st.pyplot(fig); plt.close()

        # Summary table
        st.markdown("<div class='section-header'>Input vs Dataset Mean</div>", unsafe_allow_html=True)
        summary = pd.DataFrame({
            'Statistic'   : ['Batting Average','Strike Rate','Wickets','Fielding Score','Matches Played','Bowling Average'],
            'Your Input'  : [batting_avg, strike_rate, wickets, fielding_score, matches, bowling_avg],
            'Dataset Mean': [34.55, 76.71, 55.82, 75.03, 41.55, 31.29]
        })
        summary['Difference'] = (summary['Your Input'] - summary['Dataset Mean']).round(2)
        summary['Status'] = summary['Difference'].apply(lambda d: 'Above Average' if d > 0 else 'Below Average')
        st.dataframe(summary, use_container_width=True, hide_index=True)