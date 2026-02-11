"""
AI Intelligence Platform - Unified Dashboard

Combines Market Signals and Policy Signals modules into a single interface.
"""

import streamlit as st
import sys
from pathlib import Path

# Add module paths for imports
platform_root = Path(__file__).parent.parent
sys.path.insert(0, str(platform_root / "market-signals" / "dashboard"))
sys.path.insert(0, str(platform_root / "policy-signals" / "dashboard"))

st.set_page_config(
    page_title="AI Intelligence Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🤖 AI Intelligence Platform")
st.markdown("**Comprehensive visibility into the AI industry**")

# Module selection tabs
tab1, tab2 = st.tabs(["📊 Market Signals", "🏛️ Policy Signals"])

with tab1:
    st.header("Market Signals")
    st.markdown("""
    **What's hot, growing, or dying in data/AI?**

    Tracks job market trends, skill demand, and technology adoption across the data/AI ecosystem.

    | Metric | Value |
    |--------|-------|
    | HN Job Posts | 93K |
    | LinkedIn Jobs | 1.3M |
    | GitHub Repos | 81 |
    | dbt Models | 21 |
    | dbt Tests | 77 |
    """)

    st.info("👉 For the full Market Signals dashboard, run: `streamlit run market-signals/dashboard/app.py`")

    # Key findings preview
    st.subheader("Key Findings")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Snowflake vs Redshift (2024)", "1.6% vs 0.4%", "Snowflake overtook in 2022")
        st.metric("PyTorch vs TensorFlow (2025)", "2.0% vs 0.5%", "4x lead")
    with col2:
        st.metric("OpenAI Mentions", "2.7%", "+575% since 2022")
        st.metric("LLM vs Regex Extraction", "6.4 vs 1.5", "4x more skills found")

with tab2:
    st.header("Policy Signals")
    st.markdown("""
    **Do AI companies practice what they preach?**

    Analyzes policy positions from government submissions and compares them to lobbying activity.

    | Metric | Value |
    |--------|-------|
    | AI Submissions | 10,068 PDFs |
    | LDA Filings | 970 |
    | Companies Analyzed | 30 |
    | dbt Models | 16 |
    | dbt Tests | 35 |
    """)

    st.info("👉 For the full Policy Signals dashboard, run: `streamlit run policy-signals/dashboard/app.py`")

    # Key findings preview
    st.subheader("Key Findings")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Most Consistent Company", "Anthropic", "25/100 discrepancy")
        st.metric("Biggest Say-vs-Do Gap", "Google/Amazon", "72/100 discrepancy")
    with col2:
        st.metric("Heaviest China Rhetoric", "OpenAI", "85/100 intensity")
        st.metric("Quiet Lobbying Example", "Section 230", "115 filings, 0 positions")

# Sidebar
st.sidebar.title("AI Intelligence Platform")
st.sidebar.markdown("---")
st.sidebar.markdown("""
### Quick Links

**Market Signals**
- [Full Dashboard](../market-signals/dashboard/app.py)
- [Documentation](../market-signals/docs/)

**Policy Signals**
- [Full Dashboard](../policy-signals/dashboard/app.py)
- [Documentation](../policy-signals/docs/)
""")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### About

This platform provides 360-degree visibility into the AI industry:

1. **Market Signals** - Job trends, skill demand, technology adoption
2. **Policy Signals** - Lobbying patterns, say-vs-do analysis

Built as a DataExpert.io capstone project.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    AI Intelligence Platform | DataExpert.io Capstone |
    <a href='https://github.com/kouverk/ai-intelligence-platform'>GitHub</a>
</div>
""", unsafe_allow_html=True)
