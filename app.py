import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Tech Careers Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: "Inter", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(37,99,235,0.08), transparent 28%),
            radial-gradient(circle at top right, rgba(168,85,247,0.08), transparent 25%),
            linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 88%;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(24px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes shimmer {
        0% {
            background-position: -200% 0;
        }
        100% {
            background-position: 200% 0;
        }
    }

    .hero-wrap {
        background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1d4ed8 100%);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 28px;
        padding: 32px 34px;
        margin-bottom: 24px;
        color: white;
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.9s ease forwards;
        box-shadow: 0 16px 50px rgba(15,23,42,0.24);
    }

    .hero-wrap::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(
            120deg,
            rgba(255,255,255,0.00) 20%,
            rgba(255,255,255,0.08) 35%,
            rgba(255,255,255,0.00) 50%
        );
        background-size: 200% 100%;
        animation: shimmer 4.5s linear infinite;
        pointer-events: none;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        color: #dbeafe;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 16px;
        backdrop-filter: blur(10px);
    }

    .hero-title {
        font-size: 54px;
        line-height: 1.02;
        font-weight: 900;
        margin-bottom: 12px;
        letter-spacing: -1px;
    }

    .hero-sub {
        font-size: 18px;
        color: #dbeafe;
        max-width: 880px;
        line-height: 1.6;
        margin-bottom: 18px;
    }

    .hero-pills {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 8px;
    }

    .hero-pill {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.14);
        color: white;
        padding: 8px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
        backdrop-filter: blur(10px);
        transition: all 0.25s ease;
    }

    .hero-pill:hover {
        transform: translateY(-2px) scale(1.02);
        background: rgba(255,255,255,0.16);
    }

    .kpi-card {
        background: linear-gradient(180deg, #08122c 0%, #0f172a 100%);
        border: 1px solid rgba(30,41,59,0.95);
        border-radius: 24px;
        padding: 20px 20px 18px 20px;
        color: white;
        box-shadow: 0 12px 32px rgba(2,6,23,0.16);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        animation: fadeUp 0.7s ease forwards;
        opacity: 0;
        margin-bottom: 16px;
        height: 100%;
    }

    .kpi-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 18px 40px rgba(37,99,235,0.20);
        border-color: rgba(59,130,246,0.5);
    }

    .kpi-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }

    .kpi-label {
        color: #bfdbfe;
        font-size: 14px;
        font-weight: 600;
    }

    .kpi-icon {
        font-size: 20px;
        opacity: 0.95;
    }

    .kpi-value {
        font-size: 25px;
        line-height: 1.1;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 6px;
        letter-spacing: -0.5px;
        word-break: break-word;
    }

    .kpi-sub {
        color: #93c5fd;
        font-size: 13px;
    }

    .section-card {
        background: rgba(255,255,255,0.74);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(148,163,184,0.18);
        border-radius: 24px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(15,23,42,0.08);
        animation: fadeUp 0.7s ease forwards;
    }

    .section-title-dark {
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 10px;
        letter-spacing: -0.3px;
    }

    .insight-box {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        border: 1px solid rgba(59,130,246,0.22);
        border-radius: 18px;
        padding: 16px 18px;
        margin-top: 12px;
        color: #dbeafe;
        font-size: 14px;
        line-height: 1.6;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(15,23,42,0.96);
        color: white;
        border-radius: 14px 14px 0 0;
        padding: 10px 16px;
        transition: transform 0.2s ease, background 0.2s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-2px);
        background: #172554;
    }

    .stTabs [aria-selected="true"] {
        background-color: #2563eb !important;
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 14px !important;
        border: 1px solid rgba(148,163,184,0.25) !important;
        background: rgba(255,255,255,0.85) !important;
    }

    .stSlider [data-baseweb="slider"] {
        padding-top: 8px;
    }

    [data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid rgba(148,163,184,0.2);
        box-shadow: 0 8px 24px rgba(15,23,42,0.06);
    }

    /* ---------- Responsive tweaks ---------- */

    @media (max-width: 1200px) {
        .block-container {
            max-width: 94% !important;
        }

        .hero-title {
            font-size: 42px !important;
        }

        .hero-sub {
            font-size: 16px !important;
        }

        .kpi-value {
            font-size: 24px !important;
        }
    }

    @media (max-width: 992px) {
        .block-container {
            max-width: 96% !important;
            padding-top: 1.2rem !important;
            padding-bottom: 1.2rem !important;
        }

        .hero-wrap {
            padding: 24px 20px !important;
            border-radius: 22px !important;
        }

        .hero-title {
            font-size: 34px !important;
            line-height: 1.1 !important;
        }

        .hero-sub {
            font-size: 15px !important;
            max-width: 100% !important;
        }

        .hero-pill {
            font-size: 12px !important;
            padding: 7px 12px !important;
        }

        .kpi-card {
            padding: 16px !important;
            border-radius: 18px !important;
        }

        .kpi-label {
            font-size: 13px !important;
        }

        .kpi-value {
            font-size: 22px !important;
        }

        .kpi-sub {
            font-size: 12px !important;
        }

        .section-card {
            padding: 18px !important;
            border-radius: 18px !important;
        }

        .section-title-dark {
            font-size: 20px !important;
        }
    }

    @media (max-width: 768px) {
        .block-container {
            max-width: 100% !important;
            padding-left: 0.7rem !important;
            padding-right: 0.7rem !important;
        }

        .hero-wrap {
            padding: 18px 16px !important;
            margin-bottom: 16px !important;
        }

        .hero-badge {
            font-size: 11px !important;
            padding: 6px 10px !important;
            margin-bottom: 12px !important;
        }

        .hero-title {
            font-size: 28px !important;
            letter-spacing: -0.5px !important;
        }

        .hero-sub {
            font-size: 14px !important;
            line-height: 1.5 !important;
            margin-bottom: 14px !important;
        }

        .hero-pills {
            gap: 8px !important;
        }

        .hero-pill {
            font-size: 11px !important;
            padding: 6px 10px !important;
        }

        .kpi-card {
            padding: 14px !important;
            margin-bottom: 12px !important;
        }

        .kpi-top {
            margin-bottom: 8px !important;
        }

        .kpi-value {
            font-size: 20px !important;
        }

        .kpi-sub {
            font-size: 11px !important;
        }

        .section-card {
            padding: 14px !important;
            margin-bottom: 14px !important;
        }

        .section-title-dark {
            font-size: 18px !important;
        }

        .insight-box {
            font-size: 13px !important;
            padding: 12px 14px !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 6px !important;
            overflow-x: auto !important;
            flex-wrap: nowrap !important;
            scrollbar-width: none;
        }

        .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
            display: none;
        }

        .stTabs [data-baseweb="tab"] {
            padding: 8px 12px !important;
            font-size: 13px !important;
            white-space: nowrap !important;
        }

        [data-testid="stDataFrame"] {
            font-size: 12px !important;
        }
    }

    @media (max-width: 480px) {
        .hero-title {
            font-size: 24px !important;
        }

        .hero-sub {
            font-size: 13px !important;
        }

        .kpi-value {
            font-size: 18px !important;
        }

        .kpi-label {
            font-size: 12px !important;
        }

        .section-title-dark {
            font-size: 17px !important;
        }
    }

    header, #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)


load_css()


def short_text(text, limit=16):
    text = str(text)
    return text if len(text) <= limit else text[:limit] + "..."


def kpi_card(label, value, icon, subtitle):
    return f"""
    <div class="kpi-card">
        <div class="kpi-top">
            <div class="kpi-label">{label}</div>
            <div class="kpi-icon">{icon}</div>
        </div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-sub">{subtitle}</div>
    </div>
    """


@st.cache_data
def load_data():
    postings = pd.read_csv("data/postings_sample.csv")
    salaries = pd.read_csv("data/salaries.csv")
    job_skills = pd.read_csv("data/job_skills.csv")
    skills = pd.read_csv("data/skills.csv")
    job_industries = pd.read_csv("data/job_industries.csv")
    industries = pd.read_csv("data/industries.csv")
    benefits = pd.read_csv("data/benefits.csv")
    companies = pd.read_csv("data/companies.csv")
    employee_counts = pd.read_csv("data/employee_counts.csv")
    return postings, salaries, job_skills, skills, job_industries, industries, benefits, companies, employee_counts


postings, salaries, job_skills, skills, job_industries, industries, benefits, companies, employee_counts = load_data()

# -----------------------------
# Basic cleaning
# -----------------------------
postings = postings.copy()
postings.columns = postings.columns.str.strip()
skills.columns = skills.columns.str.strip()
job_skills.columns = job_skills.columns.str.strip()
industries.columns = industries.columns.str.strip()
job_industries.columns = job_industries.columns.str.strip()
benefits.columns = benefits.columns.str.strip()
companies.columns = companies.columns.str.strip()
employee_counts.columns = employee_counts.columns.str.strip()

for col in ["normalized_salary", "views", "applies", "remote_allowed"]:
    if col in postings.columns:
        postings[col] = pd.to_numeric(postings[col], errors="coerce")

if "title" in postings.columns:
    postings["title"] = postings["title"].astype(str).str.strip()

if "company_name" in postings.columns:
    postings["company_name"] = postings["company_name"].astype(str).str.strip()

if "location" in postings.columns:
    postings["location"] = postings["location"].astype(str).str.strip()

if "formatted_work_type" in postings.columns:
    postings["formatted_work_type"] = postings["formatted_work_type"].fillna("Unknown")

if "remote_allowed" not in postings.columns:
    postings["remote_allowed"] = 0

postings["remote_allowed"] = postings["remote_allowed"].fillna(0)
postings["is_remote"] = postings["remote_allowed"].apply(lambda x: "Remote" if x == 1 else "On-site / Hybrid")

postings = postings.dropna(subset=["title"])

# -----------------------------
# Tech filter
# -----------------------------
tech_keywords = [
    "engineer", "developer", "data", "analyst", "scientist", "software",
    "devops", "cloud", "security", "cyber", "frontend", "backend",
    "full stack", "machine learning", "ml", "ai", "web", "it",
    "systems", "network", "qa", "test", "automation", "database"
]

postings = postings[
    postings["title"].str.lower().apply(
        lambda x: any(keyword in x for keyword in tech_keywords)
    )
].copy()

# -----------------------------
# Skills merge
# -----------------------------
if "skill_abr" in skills.columns and "skill_abr" in job_skills.columns:
    job_skills_merged = job_skills.merge(skills, on="skill_abr", how="left")
else:
    job_skills_merged = job_skills.copy()

if "job_id" in postings.columns and "job_id" in job_skills_merged.columns:
    posting_skills = postings[["job_id", "title"]].merge(job_skills_merged, on="job_id", how="left")
else:
    posting_skills = pd.DataFrame()

if "skill_name" in posting_skills.columns:
    skills_count = (
        posting_skills["skill_name"]
        .dropna()
        .value_counts()
        .reset_index()
    )
    skills_count.columns = ["skill_name", "count"]
else:
    skills_count = pd.DataFrame(columns=["skill_name", "count"])

# -----------------------------
# Industries merge
# -----------------------------
if "industry_id" in job_industries.columns and "industry_id" in industries.columns:
    job_industries_merged = job_industries.merge(industries, on="industry_id", how="left")
else:
    job_industries_merged = job_industries.copy()

if "job_id" in postings.columns and "job_id" in job_industries_merged.columns:
    posting_industries = postings[["job_id", "title", "normalized_salary"]].merge(job_industries_merged, on="job_id", how="left")
else:
    posting_industries = pd.DataFrame()

if "industry_name" in posting_industries.columns:
    industry_counts = (
        posting_industries["industry_name"]
        .dropna()
        .value_counts()
        .reset_index()
    )
    industry_counts.columns = ["industry_name", "count"]
else:
    industry_counts = pd.DataFrame(columns=["industry_name", "count"])

# -----------------------------
# Benefits
# -----------------------------
benefit_col = None
for candidate in ["type", "inferred", "benefit_type"]:
    if candidate in benefits.columns:
        benefit_col = candidate
        break

if benefit_col:
    benefit_counts = (
        benefits[benefit_col]
        .dropna()
        .astype(str)
        .value_counts()
        .reset_index()
    )
    benefit_counts.columns = ["benefit_type", "count"]
else:
    benefit_counts = pd.DataFrame(columns=["benefit_type", "count"])

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.title("Dashboard Filters")

title_options = sorted(postings["title"].dropna().unique().tolist())
location_options = sorted(postings["location"].dropna().unique().tolist()) if "location" in postings.columns else []

selected_titles = st.sidebar.multiselect("Job Title", title_options)
selected_locations = st.sidebar.multiselect("Location", location_options[:300])
remote_only = st.sidebar.checkbox("Remote only")

salary_min = 0
salary_max = 300000

if "normalized_salary" in postings.columns and not postings["normalized_salary"].dropna().empty:
    detected_min = int(postings["normalized_salary"].dropna().min())
    detected_max = int(postings["normalized_salary"].dropna().max())
    salary_min = max(0, detected_min)
    salary_max = max(detected_max, salary_min + 1000)

selected_salary = st.sidebar.slider(
    "Salary Range",
    min_value=salary_min,
    max_value=salary_max,
    value=(salary_min, salary_max)
)

filtered = postings.copy()

if selected_titles:
    filtered = filtered[filtered["title"].isin(selected_titles)]

if selected_locations:
    filtered = filtered[filtered["location"].isin(selected_locations)]

if remote_only:
    filtered = filtered[filtered["remote_allowed"] == 1]

if "normalized_salary" in filtered.columns:
    filtered = filtered[
        (filtered["normalized_salary"].isna()) |
        (
            (filtered["normalized_salary"] >= selected_salary[0]) &
            (filtered["normalized_salary"] <= selected_salary[1])
        )
    ]

# -----------------------------
# Filtered helpers
# -----------------------------
filtered_top_titles = (
    filtered["title"]
    .value_counts()
    .head(12)
    .reset_index()
)
filtered_top_titles.columns = ["title", "count"]

filtered_salary_by_title = (
    filtered.dropna(subset=["normalized_salary"])
    .groupby("title")["normalized_salary"]
    .mean()
    .reset_index()
    .sort_values("normalized_salary", ascending=False)
    .head(12)
)

if not posting_skills.empty and "job_id" in filtered.columns:
    filtered_skills = filtered[["job_id", "title"]].merge(job_skills_merged, on="job_id", how="left")
else:
    filtered_skills = pd.DataFrame()

if "skill_name" in filtered_skills.columns:
    filtered_skills_count = (
        filtered_skills["skill_name"]
        .dropna()
        .value_counts()
        .head(15)
        .reset_index()
    )
    filtered_skills_count.columns = ["skill_name", "count"]
else:
    filtered_skills_count = pd.DataFrame(columns=["skill_name", "count"])

if not posting_industries.empty and "job_id" in filtered.columns:
    filtered_industries = filtered[["job_id", "title", "normalized_salary"]].merge(job_industries_merged, on="job_id", how="left")
else:
    filtered_industries = pd.DataFrame()

if "industry_name" in filtered_industries.columns:
    filtered_industry_counts = (
        filtered_industries["industry_name"]
        .dropna()
        .value_counts()
        .head(12)
        .reset_index()
    )
    filtered_industry_counts.columns = ["industry_name", "count"]

    filtered_salary_by_industry = (
        filtered_industries.dropna(subset=["industry_name", "normalized_salary"])
        .groupby("industry_name")["normalized_salary"]
        .mean()
        .reset_index()
        .sort_values("normalized_salary", ascending=False)
        .head(12)
    )
else:
    filtered_industry_counts = pd.DataFrame(columns=["industry_name", "count"])
    filtered_salary_by_industry = pd.DataFrame(columns=["industry_name", "normalized_salary"])

company_jobs = (
    filtered.groupby("company_name")
    .size()
    .reset_index(name="job_count")
    .sort_values("job_count", ascending=False)
    .head(12)
)

# -----------------------------
# KPIs
# -----------------------------
total_jobs = len(filtered)
avg_salary = filtered["normalized_salary"].dropna().mean() if "normalized_salary" in filtered.columns else np.nan
remote_pct = (filtered["remote_allowed"].fillna(0).eq(1).mean() * 100) if len(filtered) > 0 else 0
top_job_title = filtered["title"].mode()[0] if not filtered["title"].mode().empty else "N/A"
top_skill = filtered_skills_count.iloc[0]["skill_name"] if not filtered_skills_count.empty else "N/A"
top_industry = filtered_industry_counts.iloc[0]["industry_name"] if not filtered_industry_counts.empty else "N/A"

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">LIVE MARKET INTELLIGENCE</div>
    <div class="hero-title">Tech Careers Intelligence Dashboard</div>
    <div class="hero-sub">
        Explore hiring demand, salary signals, skills, industries, companies, and benefits across the tech job market through a polished interactive experience.
    </div>
    <div class="hero-pills">
        <div class="hero-pill">Salary Trends</div>
        <div class="hero-pill">Skills Demand</div>
        <div class="hero-pill">Remote Roles</div>
        <div class="hero-pill">Industry Insights</div>
    </div>
</div>
""", unsafe_allow_html=True)

kpi_cols_top = st.columns([1, 1, 1], gap="small")
with kpi_cols_top[0]:
    st.markdown(kpi_card("Total Jobs", f"{total_jobs:,}", "📌", "Active filtered listings"), unsafe_allow_html=True)
with kpi_cols_top[1]:
    st.markdown(kpi_card("Avg Salary", f"${avg_salary:,.0f}" if pd.notnull(avg_salary) else "N/A", "💰", "Average normalized salary"), unsafe_allow_html=True)
with kpi_cols_top[2]:
    st.markdown(kpi_card("Remote Jobs %", f"{remote_pct:.1f}%", "🌍", "Share of remote-friendly roles"), unsafe_allow_html=True)

kpi_cols_bottom = st.columns([1, 1, 1], gap="small")
with kpi_cols_bottom[0]:
    st.markdown(kpi_card("Top Job Title", short_text(top_job_title, 16), "🧠", "Most common role right now"), unsafe_allow_html=True)
with kpi_cols_bottom[1]:
    st.markdown(kpi_card("Top Skill", short_text(top_skill, 16), "🛠️", "Most requested skill"), unsafe_allow_html=True)
with kpi_cols_bottom[2]:
    st.markdown(kpi_card("Top Industry", short_text(top_industry, 16), "🏢", "Leading industry segment"), unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview",
    "Salary Insights",
    "Skills Demand",
    "Industries",
    "Companies & Benefits",
    "Explore Jobs"
])

# -----------------------------
# Tab 1: Overview
# -----------------------------
with tab1:
    col1, col2 = st.columns([1.2, 1], gap="medium")

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Top Tech Job Titles</div>', unsafe_allow_html=True)

        fig_titles = px.bar(
            filtered_top_titles,
            x="count",
            y="title",
            orientation="h",
            template="plotly_white",
            text="count"
        )
        fig_titles.update_layout(
            height=460,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Openings",
            yaxis_title="",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_titles, use_container_width=True)
        st.markdown(
            f'<div class="insight-box">The filtered dataset currently contains <b>{total_jobs:,}</b> tech-related jobs, with <b>{short_text(top_job_title, 25)}</b> appearing most often.</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Work Type Distribution</div>', unsafe_allow_html=True)

        work_type_counts = filtered["formatted_work_type"].fillna("Unknown").value_counts().reset_index()
        work_type_counts.columns = ["work_type", "count"]

        fig_work = px.pie(
            work_type_counts,
            names="work_type",
            values="count",
            hole=0.5,
            template="plotly_white"
        )
        fig_work.update_layout(
            height=460,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_work, use_container_width=True)
        st.markdown(
            f'<div class="insight-box"><b>{remote_pct:.1f}%</b> of the filtered tech roles are marked as remote, showing how location flexibility varies across this slice of the market.</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 2: Salary Insights
# -----------------------------
with tab2:
    col1, col2 = st.columns([1.15, 1], gap="medium")

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Average Salary by Role</div>', unsafe_allow_html=True)

        fig_salary = px.bar(
            filtered_salary_by_title,
            x="normalized_salary",
            y="title",
            orientation="h",
            template="plotly_white",
            text_auto=".2s"
        )
        fig_salary.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Average Salary (USD)",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_salary, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Salary Distribution</div>', unsafe_allow_html=True)

        salary_dist = filtered.dropna(subset=["normalized_salary"]).copy()
        fig_hist = px.histogram(
            salary_dist,
            x="normalized_salary",
            nbins=35,
            template="plotly_white"
        )
        fig_hist.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title="Salary (USD)",
            yaxis_title="Count",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_hist, use_container_width=True)

        if pd.notnull(avg_salary):
            st.markdown(
                f'<div class="insight-box">The current filtered average salary is <b>${avg_salary:,.0f}</b>. Use the sidebar to compare titles, locations, and remote roles.</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 3: Skills Demand
# -----------------------------
with tab3:
    col1, col2 = st.columns([1.15, 1], gap="medium")

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Top Skills in Demand</div>', unsafe_allow_html=True)

        fig_skills = px.bar(
            filtered_skills_count,
            x="count",
            y="skill_name",
            orientation="h",
            template="plotly_white",
            text="count"
        )
        fig_skills.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Mentions",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_skills, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Demand Snapshot</div>', unsafe_allow_html=True)

        if not filtered_skills_count.empty:
            top_5 = filtered_skills_count.head(5)["skill_name"].tolist()
            skill_text = ", ".join(top_5)
            st.markdown(
                f'<div class="insight-box">The most requested skills in the current filtered dataset are <b>{skill_text}</b>. These skills can help shape which tools and technologies deserve priority in your portfolio.</div>',
                unsafe_allow_html=True
            )
        else:
            st.info("No skill data available for the current filters.")

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 4: Industries
# -----------------------------
with tab4:
    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Top Industries by Job Count</div>', unsafe_allow_html=True)

        fig_ind = px.bar(
            filtered_industry_counts,
            x="count",
            y="industry_name",
            orientation="h",
            template="plotly_white",
            text="count"
        )
        fig_ind.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Job Count",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ind, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Average Salary by Industry</div>', unsafe_allow_html=True)

        fig_ind_salary = px.bar(
            filtered_salary_by_industry,
            x="normalized_salary",
            y="industry_name",
            orientation="h",
            template="plotly_white",
            text_auto=".2s"
        )
        fig_ind_salary.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Average Salary (USD)",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ind_salary, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 5: Companies & Benefits
# -----------------------------
with tab5:
    col1, col2 = st.columns([1.1, 1], gap="medium")

    with col1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Top Hiring Companies</div>', unsafe_allow_html=True)

        fig_comp = px.bar(
            company_jobs,
            x="job_count",
            y="company_name",
            orientation="h",
            template="plotly_white",
            text="job_count"
        )
        fig_comp.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Openings",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_comp, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title-dark">Most Common Benefits</div>', unsafe_allow_html=True)

        fig_benefits = px.bar(
            benefit_counts.head(12),
            x="count",
            y="benefit_type",
            orientation="h",
            template="plotly_white",
            text="count"
        )
        fig_benefits.update_layout(
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis={"categoryorder": "total ascending"},
            xaxis_title="Frequency",
            yaxis_title="",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_benefits, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 6: Explore Jobs
# -----------------------------
with tab6:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title-dark">Explore Job Listings</div>', unsafe_allow_html=True)

    display_cols = [
        "title",
        "company_name",
        "location",
        "formatted_work_type",
        "normalized_salary",
        "views",
        "applies",
        "job_posting_url"
    ]

    available_cols = [c for c in display_cols if c in filtered.columns]

    sort_option = st.selectbox(
        "Sort by",
        options=[
            "Highest Salary",
            "Most Views",
            "Most Applies",
            "Job Title A-Z"
        ]
    )

    table_df = filtered.copy()

    if sort_option == "Highest Salary" and "normalized_salary" in table_df.columns:
        table_df = table_df.sort_values("normalized_salary", ascending=False, na_position="last")
    elif sort_option == "Most Views" and "views" in table_df.columns:
        table_df = table_df.sort_values("views", ascending=False, na_position="last")
    elif sort_option == "Most Applies" and "applies" in table_df.columns:
        table_df = table_df.sort_values("applies", ascending=False, na_position="last")
    elif sort_option == "Job Title A-Z":
        table_df = table_df.sort_values("title", ascending=True)

    st.dataframe(
        table_df[available_cols].head(500),
        use_container_width=True,
        hide_index=True
    )

    st.markdown('</div>', unsafe_allow_html=True)