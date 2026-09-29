import urllib.parse
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="German Job Market Boolean Query Generator",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
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
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='main-header'>🔍 German Tech & Finance Boolean Query Generator</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='sub-text'>Construct optimized Boolean search strings for English-speaking, visa-sponsored, and remote-friendly Financial Data, Risk, and Governance roles in Germany.</div>",
    unsafe_allow_html=True,
)

# Sidebar - Preset Profiles
st.sidebar.header("🎯 Preset Target Profiles")
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
st.sidebar.header("⚙️ Filter Preferences")

include_remote = st.sidebar.checkbox(
    "Include Remote / Flexible Keywords",
    value=True,
    help="Toggle off if you only want roles requiring immediate on-site relocation.",
)

# Preset Values
if preset == "Financial Data Analyst":
    default_titles = "Financial Data Analyst, Data Analyst Finance, Corporate Finance Analyst"
    default_skills = "Python, SQL, Tableau, Power BI"
    default_domain = "Financial Modeling, Governance, Auditing"
elif preset == "Risk Analytics Specialist":
    default_titles = "Risk Data Analyst, Quantitative Risk Analyst, Credit Risk Specialist"
    default_skills = "Python, SQL, R, Econometrics"
    default_domain = "Macroeconomics, Risk Modeling"
elif preset == "FinTech Audit & Governance":
    default_titles = "Forensic Analytics Manager, Revenue Assurance Analyst, IT Auditor"
    default_skills = "SQL, Python, Forensic Accounting"
    default_domain = "Regulatory Compliance, Auditing"
else:
    default_titles = "Financial Data Analyst, Risk Analytics Specialist"
    default_skills = "Python, SQL, Tableau"
    default_domain = "Auditing, Governance"

default_remote = "Remote, Home Office"
default_langs = "English"
default_visas = "Visa Sponsorship, Relocation"
default_excludes = "German Required, Internship"

# Main Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Role & Core Competency Parameters")
    titles_input = st.text_area("Job Titles (comma-separated)", value=default_titles, height=90)
    skills_input = st.text_area("Technical Stack (comma-separated)", value=default_skills, height=90)
    domain_input = st.text_area("Domain Expertise (comma-separated)", value=default_domain, height=90)

with col2:
    st.subheader("2. Work Rights, Remote & Language Constraints")
    if include_remote:
        remote_input = st.text_area("Remote Keywords", value=default_remote, height=70)
    else:
        remote_input = ""
        st.info("💡 Focus set to on-site/relocation roles.")

    lang_input = st.text_area("Working Language", value=default_langs, height=60)
    visa_input = st.text_area("Visa & Relocation Support", value=default_visas, height=60)
    exclude_input = st.text_area("Exclusion Keywords (NOT)", value=default_excludes, height=60)

# Parsing Inputs
titles = [x.strip() for x in titles_input.split(",") if x.strip()]
skills = [x.strip() for x in skills_input.split(",") if x.strip()]
domain = [x.strip() for x in domain_input.split(",") if x.strip()]
remotes = [x.strip() for x in remote_input.split(",") if x.strip()] if include_remote else []
langs = [x.strip() for x in lang_input.split(",") if x.strip()]
visas = [x.strip() for x in visa_input.split(",") if x.strip()]
excludes = [x.strip() for x in exclude_input.split(",") if x.strip()]


# Full Query Builder for Internal Job Board Search Bars (LinkedIn Job Search Bar)
def build_full_query(titles, skills, domain, remotes, langs, visas, excludes):
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

    main_q = " AND ".join(blocks)
    if excludes:
        main_q += " " + " ".join([f'NOT "{e}"' for e in excludes])
    return main_q


# High-Precision Lean Query for Google X-Ray Search
def build_xray_query(titles, skills, remotes):
    title_block = f"({' OR '.join([f'\"{t}\"' for t in titles[:2]])})" if titles else ""
    skill_block = f"({' OR '.join([f'\"{s}\"' for s in skills[:2]])})" if skills else ""
    
    # Target Google explicitly at German job pages
    query = f"site:de.linkedin.com/jobs/view OR site:stepstone.de/jobs {title_block} {skill_block} \"English\" \"Germany\""
    if remotes:
        query += " \"Remote\""
    return query


full_generated_query = build_full_query(titles, skills, domain, remotes, langs, visas, excludes)
xray_generated_query = build_xray_query(titles, skills, remotes)

st.markdown("---")
st.subheader("📋 Comprehensive ATS Search Query (For LinkedIn / Job Board Search Bar)")
st.code(full_generated_query, language="text")

# Dynamic Search Launchers
st.subheader("🚀 One-Click Job Search Launchers")

# Native LinkedIn Job Search URL
encoded_linkedin = urllib.parse.quote(f"({' OR '.join([f'\"{t}\"' for t in titles])}) AND English AND (Visa OR Relocation OR Remote)")
linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={encoded_linkedin}&location=Germany"

# Google X-Ray URL targeting job posting pages strictly
google_xray_url = f"https://www.google.com/search?q={urllib.parse.quote(xray_generated_query)}"

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    st.link_button("🔎 Open LinkedIn Germany Job Search", linkedin_url, use_container_width=True)

with btn_col2:
    st.link_button("🌐 Open Google X-Ray Job Search", google_xray_url, use_container_width=True)

st.markdown("---")
st.caption("Updated Engine: Targets job postings strictly (excluding candidate profiles) for English-speaking roles in Germany.")
