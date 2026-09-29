#  German Tech & Finance Job Market Boolean Query Generator

An interactive, production-ready Streamlit web application that dynamically constructs optimized Boolean search queries for **English-speaking, visa-sponsored, and remote-friendly** Financial Data Analytics, Risk, and Governance roles in Germany.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

##  Business & Executive Context

Finding specialized roles in the German labor market from abroad requires navigating complex employer requirements—such as language constraints, remote work eligibility, and work visa support under Germany's **Skilled Immigration Act** (*Fachkräfteeinwanderungsgesetz*).

Standard job board search bars often return noisy, irrelevant results (e.g., jobs requiring native German fluency or local-only residency). This tool automates the construction of **complex, multi-parameter Boolean search strings** tailored for platforms like **LinkedIn Germany, StepStone.de, and Google X-Ray Search**.

### Target Role Domains Covered:
1. **Financial Data Analytics:** Corporate Finance, Revenue Assurance, IGR Modeling, Tableau/Power BI Reporting.
2. **Quantitative Risk & Econometrics:** Credit Decay Modeling, Macroeconomic Risk Analysis, Systemic Banking Analytics.
3. **Forensic Accounting & Regulatory Audit:** Ledger Auditing, Regulatory Compliance, IT Governance.

---

##  Architecture & Core Logic

The application converts grouped string arrays into structured logical expressions with strict operational precedence:

$$\text{Query} = (\text{Titles}) \land (\text{Stack}) \land (\text{Domain}) \land [\text{Remote}] \land (\text{Language}) \land (\text{Visa}) \land \neg(\text{Exclusions})$$

### Core Python Query Function:
```python
def build_boolean_query(titles, skills, domain, remotes, langs, visas, excludes):
    """Dynamically generates structured Boolean logic strings for ATS and search engines."""
    blocks = []
    
    if titles:  blocks.append(f"({' OR '.join([f'\"{t}\"' for t in titles])})")
    if skills:  blocks.append(f"({' OR '.join([f'\"{s}\"' for s in skills])})")
    if domain:  blocks.append(f"({' OR '.join([f'\"{d}\"' for d in domain])})")
    if remotes: blocks.append(f"({' OR '.join([f'\"{r}\"' for r in remotes])})")
    if langs:   blocks.append(f"({' OR '.join([f'\"{l}\"' for l in langs])})")
    if visas:   blocks.append(f"({' OR '.join([f'\"{v}\"' for v in visas])})")
    
    main_query = " AND ".join(blocks)
    
    if excludes:
        not_clause = " ".join([f'NOT "{e}"' for e in excludes])
        main_query = f"{main_query} {not_clause}"
        
    return main_query
Key Features
Preset Profiles: One-click pre-fills for Financial Data Analysts, Risk Analytics Specialists, and Forensic Audit Managers.

Remote Flexibility Toggle: Dynamically injects or strips remote keywords (Remote, Work from Anywhere, Home Office) without breaking the core location strategy.

Instant Platform Launchers: Automatically formats URL-encoded parameters to launch live searches directly on LinkedIn Germany and Google X-Ray (LinkedIn/StepStone site search).

Copy-to-Clipboard Output: Clean syntax block ready to be pasted directly into job portal search bars.

Local Setup & Development
Prerequisites
Python 3.10 or higher

Git

Installation Steps
Clone the Repository:

Bash
git clone [https://github.com/bamideleadedji/german-boolean-query-builder.git](https://github.com/bamideleadedeji/german-boolean-query-builder.git)
cd german-boolean-query-builder
Set Up Virtual Environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Application:

Bash
streamlit run app.py
Project Structure
Plaintext
german-boolean-query-builder/
│
├── app.py                      # Main Streamlit web application
├── boolean_builder.ipynb        # Jupyter Notebook for algorithm testing & prototyping
├── requirements.txt            # App dependencies (Streamlit, Pandas)
├── .gitignore                  # Git tracking exclusion rules
└── README.md                   # Technical documentation
Sample Generated Output
Plaintext
("Financial Data Analyst" OR "Risk Analytics Specialist") 
AND ("Python" OR "SQL" OR "Streamlit" OR "Tableau") 
AND ("Auditing" OR "Governance" OR "Econometrics") 
AND ("Remote" OR "Home Office" OR "Work from Anywhere") 
AND ("English" OR "working language English") 
AND ("Visa Sponsorship" OR "Relocation") 
NOT "German Required" NOT "Internship"
Author & Expertise
Designed and built by Bamidele Adedeji

Senior Financial Consultant, Auditor, and Applied Data Scientist

GitHub: github.com/bamideleadedeji

Specializations: Financial Econometrics, Forensic Accounting, Machine Learning Pipelines, Streamlit Cloud Deployments.


---

### Step to Finalize on GitHub

Copy the raw Markdown text above into the `README.md` file in your project folder, save it, and run these terminal commands to commit and push:

```bash
git add README.md
git commit -m "Docs: Add comprehensive GitHub README documentation"
git push origin main
