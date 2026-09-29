import urllib.parse
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="German Job Market Boolean Query Generator",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for Streamlit Controls
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
    }
    .sub-text {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 25px;
    }
    </style>
""",
    unsafe_allow_allow_html=True,
)

st.markdown(
    "<div class='main-header'> German Tech & Finance Boolean Query Generator</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='sub-text'>Construct optimized Boolean search strings for English-speaking, visa-sponsored, and remote-friendly Financial Data, Risk, and Governance roles in Germany.</div>",
    unsafe_allow_html=True,
)

# Sidebar - Preset Target Profiles
st.sidebar.header(" Preset Target Profiles")
preset = st.sidebar.selectbox(
    "Select a pre-filled configuration:",
    [
        "Financial Data Analyst",
        "Risk Analytics Specialist",
        "FinTech Audit & Governance",
        "Custom Configuration",
    ],
)

st.sidebar.markdown("---")
st.sidebar.header(" Filter Preferences")

# Remote Work Toggle in Sidebar
include_remote = st.sidebar.checkbox(
    "Include Remote / Flexible Keywords",
    value=True,
    help="Toggle off if you only want roles requiring immediate on-site relocation.",
)

st.sidebar.markdown(
    """
---
**Targeting Platforms:**
* LinkedIn Germany
* StepStone.de
* Google X-Ray Search
"""
)

# Preset Parameter Values Logic
if preset == "Financial Data Analyst":
    default_titles = "Financial Data Analyst, Senior Data Analyst Finance, Corporate Finance Analyst"
    default_skills = "Python, SQL, Tableau, Power BI, Streamlit"
    default_domain = "Financial Modeling, Corporate Governance, Auditing"
elif preset == "Risk Analytics Specialist":
    default_titles = "Risk Data Analyst, Quantitative Risk Analyst, Credit Risk Specialist"
    default_skills = "Python, SQL, R, Econometrics, Scikit-learn"
    default_domain = "Macroeconomics, Credit Decay, Risk Modeling"
elif preset == "FinTech Audit & Governance":
    default_titles = "Forensic Analytics Manager, Revenue Assurance Analyst, IT Auditor"
    default_skills = "SQL, Python, Forensic Accounting, Revenue Assurance"
    default_domain = "Regulatory Compliance, Financial Auditing, Banking Guidelines"
else:
    default_titles = "Financial Data Analyst, Risk Analytics Specialist"
    default_skills = "Python, SQL, Streamlit, Tableau"
    default_domain = "Auditing, Governance, Econometrics"

default_remote = "Remote, Work from Anywhere, Home Office, Distributed Team"
default_langs = "English, working language English"
default_visas = "Visa Sponsorship, Relocation"
default_excludes = "German Required, Fluent German, Internship, Student"

# Main Form Layout - 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Role & Core Competency Parameters")

    titles_input = st.text_area(
        "Job Titles (comma-separated)",
        value=default_titles,
        height=100,
        help="Primary job titles you are targeting.",
    )

    skills_input = st.text_area(
        "Technical Stack (comma-separated)",
        value=default_skills,
        height=100,
        help="Programming languages, visualization, and analytics tools.",
    )

    domain_input = st.text_area(
        "Domain Expertise (comma-separated)",
        value=default_domain,
        height=100,
        help="Subject-matter skills that differentiate your profile.",
    )

with col2:
    st.subheader("2. Work Rights, Remote & Language Constraints")

    if include_remote:
        remote_input = st.text_area(
            "Remote Keywords (comma-separated)",
            value=default_remote,
            height=80,
            help="Keywords to capture off-site and flexible working models.",
        )
    else:
        remote_input = ""
        st.info(" Remote keywords excluded. Query will focus strictly on relocation/on-site postings.")

    lang_input = st.text_area(
        "Working Language Keywords",
        value=default_langs,
        height=70,
        help="Keywords ensuring English is accepted as the working language.",
    )

    visa_input = st.text_area(
        "Visa & Relocation Support",
        value=default_visas,
        height=70,
        help="Keywords filtering for employers supporting international relocation.",
    )

    exclude_input = st.text_area(
        "Exclusion Keywords (NOT)",
        value=default_excludes,
        height=70,
        help="Keywords to eliminate non-qualifying listings.",
    )

# Logic to Process Inputs into Search Arrays
titles = [x.strip() for x in titles_input.split(",") if x.strip()]
skills = [x.strip() for x in skills_input.split(",") if x.strip()]
domain = [x.strip() for x in domain_input.split(",") if x.strip()]
remotes = [x.strip() for x in remote_input.split(",") if x.strip()] if include_remote else []
langs = [x.strip() for x in lang_input.split(",") if x.strip()]
visas = [x.strip() for x in visa_input.split(",") if x.strip()]
excludes = [x.strip() for x in exclude_input.split(",") if x.strip()]


def build_boolean_query(titles, skills, domain, remotes, langs, visas, excludes):
    """Dynamically generates a structured Boolean search query string."""
    blocks = []

    if titles:
        blocks.append(f"({' OR '.join([f'\"{t}\"' for t in titles])})")
    if skills:
        blocks.append(f"({' OR '.join([f'\"{s}\"' for s in skills])})")
    if domain:
        blocks.append(f"({' OR '.join([f'\"{d}\"' for d in domain])})")
    if remotes:
        blocks.append(f"({' OR '.join([f'\"{r}\"' for r in remotes])})")
    if langs:
        blocks.append(f"({' OR '.join([f'\"{l}\"' for l in langs])})")
    if visas:
        blocks.append(f"({' OR '.join([f'\"{v}\"' for v in visas])})")

    main_query = " AND ".join(blocks)

    if excludes:
        not_clause = " ".join([f'NOT "{e}"' for e in excludes])
        main_query = f"{main_query} {not_clause}"

    return main_query


# Generate Query Output
generated_query = build_boolean_query(
    titles, skills, domain, remotes, langs, visas, excludes
)

st.markdown("---")
st.subheader(" Generated Boolean Search Query")
st.code(generated_query, language="text")

# Dynamic Search Launchers
st.subheader(" One-Click Platform Search Launchers")

encoded_query = urllib.parse.quote(generated_query)

linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_query}&location=Germany"
google_xray_url = f"https://www.google.com/search?q=site:linkedin.com/in/+OR+site:stepstone.de+{encoded_query}"

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    st.link_button(" Run on LinkedIn Germany", linkedin_url, use_container_width=True)

with btn_col2:
    st.link_button(" Run Google X-Ray Search", google_xray_url, use_container_width=True)

# Footer Note
st.markdown("---")
st.caption(
    "Built for Finance, Risk, and Data Analytics professionals targeting English-speaking skilled worker roles in Germany."
)
