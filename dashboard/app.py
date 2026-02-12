"""
AI Intelligence Platform - Unified Dashboard

Combines Market Signals and Policy Signals modules into a single interface
with dynamic sidebar navigation.
"""

import streamlit as st
import sys
from pathlib import Path

# Add module paths for imports
platform_root = Path(__file__).parent.parent
sys.path.insert(0, str(platform_root / "market-signals" / "dashboard"))
sys.path.insert(0, str(platform_root / "policy-signals" / "dashboard"))

# Page config (must be first Streamlit call)
st.set_page_config(
    page_title="AI Intelligence Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import module dashboards
import importlib.util
from dotenv import load_dotenv

def load_module(name: str, path: Path):
    """Load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # Add module to sys.modules so relative imports work
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

# Load each module's .env explicitly before importing
# This ensures each module gets its correct schema settings

# Load market-signals .env first (for market dashboard)
load_dotenv(platform_root / "market-signals" / ".env", override=True)
market_dashboard = load_module(
    "market_dashboard",
    platform_root / "market-signals" / "dashboard" / "app.py"
)

# Load policy-signals .env (for policy dashboard) - must override market's settings
load_dotenv(platform_root / "policy-signals" / ".env", override=True)
policy_data_loader = load_module(
    "data_loader",
    platform_root / "policy-signals" / "dashboard" / "data_loader.py"
)
policy_dashboard = load_module(
    "policy_dashboard",
    platform_root / "policy-signals" / "dashboard" / "app.py"
)

# Apply policy CSS (has useful score coloring)
policy_dashboard.apply_custom_css()

# =============================================================================
# SIDEBAR NAVIGATION
# =============================================================================

st.sidebar.title("🤖 AI Intelligence Platform")
st.sidebar.markdown("*Comprehensive AI industry visibility*")
st.sidebar.divider()

# Module selection
module = st.sidebar.radio(
    "Select Module",
    ["📊 Market Signals", "🏛️ Policy Signals"],
    label_visibility="collapsed"
)

st.sidebar.divider()

# Dynamic page navigation based on module
if module == "📊 Market Signals":
    st.sidebar.subheader("📊 Market Signals")
    page = st.sidebar.radio(
        "Navigate",
        ["Executive Summary", "Technology Trends", "Role Trends",
         "GitHub & LinkedIn", "LLM vs Regex", "Data Explorer", "Methodology"],
        label_visibility="collapsed"
    )

    # Year range filter (for trend pages)
    st.sidebar.divider()
    st.sidebar.markdown("**Filters**")
    year_range = st.sidebar.slider(
        "Year Range",
        min_value=2011,
        max_value=2025,
        value=(2018, 2025)
    )

    st.sidebar.divider()
    st.sidebar.markdown("**Data Sources**")
    st.sidebar.caption("• HN Who Is Hiring (93K+ posts)")
    st.sidebar.caption("• LinkedIn Jobs (1.3M snapshot)")
    st.sidebar.caption("• GitHub Repos (81 tracked)")

else:  # Policy Signals
    st.sidebar.subheader("🏛️ Policy Signals")
    page = st.sidebar.radio(
        "Navigate",
        ["Executive Summary", "Company Deep Dive", "Cross-Company Comparison",
         "Bill-Level Analysis", "Position Explorer", "Methodology"],
        label_visibility="collapsed"
    )

    st.sidebar.divider()
    st.sidebar.markdown("**Data Sources**")
    st.sidebar.caption("• AI Action Plan RFI (17 companies)")
    st.sidebar.caption("• Senate LDA filings (2023+)")

# Footer
st.sidebar.divider()
st.sidebar.caption("DataExpert.io Capstone")
st.sidebar.caption("[GitHub](https://github.com/kouverk/ai-intelligence-platform)")

# =============================================================================
# MAIN CONTENT
# =============================================================================

if module == "📊 Market Signals":
    # Render Market Signals pages
    if page == "Executive Summary":
        market_dashboard.render_executive_summary()
    elif page == "Technology Trends":
        market_dashboard.render_technology_trends(year_range)
    elif page == "Role Trends":
        market_dashboard.render_role_trends(year_range)
    elif page == "GitHub & LinkedIn":
        market_dashboard.render_github_linkedin()
    elif page == "LLM vs Regex":
        market_dashboard.render_llm_analysis()
    elif page == "Data Explorer":
        market_dashboard.render_data_explorer()
    elif page == "Methodology":
        market_dashboard.render_methodology()

else:  # Policy Signals
    # Load policy data
    with st.spinner("Loading data..."):
        data = policy_dashboard.get_data()

    # Render Policy Signals pages
    if page == "Executive Summary":
        policy_dashboard.render_executive_summary(data)
    elif page == "Company Deep Dive":
        policy_dashboard.render_company_deep_dive(data)
    elif page == "Cross-Company Comparison":
        policy_dashboard.render_cross_company_comparison(data)
    elif page == "Bill-Level Analysis":
        policy_dashboard.render_bill_analysis(data)
    elif page == "Position Explorer":
        policy_dashboard.render_position_explorer(data)
    elif page == "Methodology":
        policy_dashboard.render_methodology()

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    AI Intelligence Platform | DataExpert.io Capstone |
    <a href='https://github.com/kouverk/ai-intelligence-platform'>GitHub</a>
</div>
""", unsafe_allow_html=True)
