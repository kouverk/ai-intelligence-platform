# AI Intelligence Platform

**Comprehensive visibility into the AI industry through two independent data pipelines**

This platform contains **two separate analytics pipelines**, each with its own data sources, extraction logic, dbt models, and Airflow DAGs. They share infrastructure (Snowflake, Astronomer, Streamlit) but are architecturally independent.

| Pipeline | Question It Answers | Data Scale |
|----------|---------------------|------------|
| **Market Signals** | What's hot, growing, or dying in data/AI hiring? | 1.3M+ job posts |
| **Policy Signals** | Do AI companies practice what they preach? | 10K+ policy documents |

---

## Live Demo

**[AI Intelligence Platform Dashboard](https://ai-intelligence-platform-kouverk.streamlit.app/)**

Instead of looking at screenshots, you can see a live demo of the dashboard analytics here. The unified dashboard combines both pipelines with sidebar navigation.

For static screenshots, see the [screenshots/](screenshots/) folder.

---

## Documentation Guide

> **For Graders:** This README is an overview of the entire platform. Each pipeline has its own detailed documentation. For detailed technical documentation (architecture, data dictionaries, data quality tests, findings) please refer to these documents below:

| Documentation | Market Signals | Policy Signals |
|---------------|----------------|----------------|
| **Architecture & System Design** | [ARCHITECTURE.md](market-signals/docs/ARCHITECTURE.md) | [ARCHITECTURE.md](policy-signals/docs/ARCHITECTURE.md) |
| **Data Dictionary (all tables)** | [DATA_DICTIONARY.md](market-signals/docs/DATA_DICTIONARY.md) | [DATA_DICTIONARY.md](policy-signals/docs/DATA_DICTIONARY.md) |
| **Data Quality (dbt tests)** | [DATA_QUALITY.md](market-signals/docs/DATA_QUALITY.md) (77 tests) | [DATA_QUALITY.md](policy-signals/docs/DATA_QUALITY.md) (35 tests) |
| **Findings & Insights** | [INSIGHTS.md](market-signals/docs/INSIGHTS.md) | [INSIGHTS.md](policy-signals/docs/INSIGHTS.md) |
| **Module README** | [README.md](market-signals/README.md) | [README.md](policy-signals/README.md) |

---

## The Two Pipelines

### Pipeline 1: Market Signals

**Question:** What technologies and roles are trending in the AI/data job market?

| Aspect | Details |
|--------|---------|
| **Data Sources** | HN Who Is Hiring (93K posts), LinkedIn Jobs (1.3M snapshot), GitHub Repos (81 tracked) |
| **LLM Components** | Skill extraction from job posts, weekly trend insights |
| **Key Outputs** | Technology trends over time, role evolution, LLM vs regex extraction comparison |
| **dbt Models** | 21 models, 77 tests |
| **Airflow DAGs** | 4 DAGs |

### Pipeline 2: Policy Signals

**Question:** Do AI companies' public policy positions match their lobbying activity?

| Aspect | Details |
|--------|---------|
| **Data Sources** | AI Action Plan RFI submissions (10K PDFs), Senate LDA lobbying filings |
| **LLM Components** | Position extraction, discrepancy scoring, China rhetoric analysis, lobbying impact assessment |
| **Key Outputs** | Say-vs-do gap scores, quiet lobbying detection, cross-company comparisons |
| **dbt Models** | 16 models, 35 tests |
| **Airflow DAGs** | 6 DAGs |

---

## Architecture Overview

This diagram shows how the two pipelines share infrastructure while remaining independent:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AI INTELLIGENCE PLATFORM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────┐    ┌─────────────────────────────┐         │
│  │     MARKET SIGNALS          │    │     POLICY SIGNALS          │         │
│  │     (Pipeline 1)            │    │     (Pipeline 2)            │         │
│  │                             │    │                             │         │
│  │  Sources:                   │    │  Sources:                   │         │
│  │  • HN Who Is Hiring (93K)   │    │  • AI Policy Submissions    │         │
│  │  • LinkedIn Jobs (1.3M)     │    │  • Senate LDA Filings       │         │
│  │  • GitHub Repos (81)        │    │                             │         │
│  │                             │    │                             │         │
│  │  LLM Components:            │    │  LLM Components:            │         │
│  │  • Skill extraction         │    │  • Position extraction      │         │
│  │  • Weekly insights          │    │  • Discrepancy scoring      │         │
│  │                             │    │  • China rhetoric analysis  │         │
│  │                             │    │  • Lobbying impact scores   │         │
│  │                             │    │                             │         │
│  │  Outputs:                   │    │  Outputs:                   │         │
│  │  • Tech trends over time    │    │  • Say-vs-do gap scores     │         │
│  │  • Role evolution           │    │  • Quiet lobbying detection │         │
│  │  • LLM vs regex comparison  │    │  • Cross-company comparison │         │
│  └─────────────┬───────────────┘    └───────────────┬─────────────┘         │
│                │                                    │                       │
│                └────────────────┬───────────────────┘                       │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │                    SHARED INFRASTRUCTURE                        │        │
│  │                                                                 │        │
│  │   Orchestration: Airflow (Astronomer)                           │        │
│  │   Transformation: dbt (staging → intermediate → marts)          │        │
│  │   Warehouse: Snowflake                                          │        │
│  │   LLM: Claude API (Anthropic)                                   │        │
│  │   Presentation: Streamlit (unified dashboard)                   │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### For detailed architecture of each pipeline, see:

| Pipeline | Architecture Doc |
|----------|------------------|
| **Market Signals** | [ARCHITECTURE.md](market-signals/docs/ARCHITECTURE.md) |
| **Policy Signals** | [ARCHITECTURE.md](policy-signals/docs/ARCHITECTURE.md) |

---

## Combined Platform Metrics

| Metric | Market Signals | Policy Signals | **Combined** |
|--------|----------------|----------------|--------------|
| **Data Sources** | 3 | 2 | **5** |
| **Total Rows** | 1.3M+ | 5K+ | **1.3M+** |
| **dbt Models** | 21 | 16 | **37** |
| **dbt Tests** | 77 | 35 | **112** |
| **Airflow DAGs** | 4 | 6 | **10** |
| **LLM Scripts** | 2 | 6 | **8** |

---

## Key Findings

### Market Signals

| Finding | Evidence |
|---------|----------|
| **Snowflake overtook Redshift** | 1.6% vs 0.4% of HN posts in 2024 |
| **PyTorch dominates TensorFlow** | 2.0% vs 0.5% in 2025 (4x lead) |
| **OpenAI mentions exploded** | 0.4% (2022) to 2.7% (2025) |
| **LLM extracts 4x more skills** | 6.4 technologies/post vs 1.5 from regex |

### Policy Signals

| Finding | Evidence |
|---------|----------|
| **Anthropic is most consistent** | Lowest discrepancy (25/100), lowest concern (45/100) |
| **Google/Amazon have biggest say-vs-do gap** | Both score 72/100 discrepancy |
| **OpenAI most aggressive on China framing** | 85/100 rhetoric intensity |
| **Section 230 is the silent elephant** | 115 lobbying filings, ZERO public positions |

---

## Tech Stack

| Component | Technology | Why This Choice |
|-----------|------------|-----------------|
| **Orchestration** | Airflow (Astronomer) | Industry standard; managed deployment |
| **Data Lake** | Apache Iceberg + AWS S3 | Schema evolution for LLM outputs; ACID transactions |
| **Warehouse** | Snowflake | Native JSON handling; scalable |
| **Transformation** | dbt | Version-controlled SQL; built-in testing |
| **LLM** | Claude API (Anthropic) | Structured extraction; 200K context |
| **Dashboard** | Streamlit | Rapid prototyping; free hosting |

---

## Project Structure

```
ai-intelligence-platform/
├── README.md                    # This file (platform overview)
├── docs/
│   ├── CAPSTONE_PROPOSAL.md     # Original combined proposal
│   └── CAPSTONE_FEEDBACK.md     # Instructor feedback
│
├── market-signals/              # Pipeline 1: Job market intelligence
│   ├── README.md                # Module overview
│   ├── docs/                    # Detailed documentation
│   │   ├── ARCHITECTURE.md      # System design, DAGs, extraction logic
│   │   ├── DATA_DICTIONARY.md   # All tables and columns
│   │   ├── DATA_QUALITY.md      # 77 dbt tests
│   │   └── INSIGHTS.md          # Findings
│   ├── dashboard/
│   ├── dbt/
│   ├── extraction/
│   ├── include/
│   └── dags/
│
├── policy-signals/              # Pipeline 2: Lobbying/policy analysis
│   ├── README.md                # Module overview
│   ├── docs/                    # Detailed documentation
│   │   ├── ARCHITECTURE.md      # System design, LLM prompts, scoring
│   │   ├── DATA_DICTIONARY.md   # All tables and columns
│   │   ├── DATA_QUALITY.md      # 35 dbt tests
│   │   └── INSIGHTS.md          # Findings
│   ├── dashboard/
│   ├── dbt/ai_influence/
│   ├── include/scripts/
│   └── dags/
│
└── dashboard/                   # Unified dashboard entry point
    └── app.py
```

> **For detailed documentation**, see the `docs/` folder within each module. Each contains ARCHITECTURE.md, DATA_DICTIONARY.md, DATA_QUALITY.md, and INSIGHTS.md.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/kouverk/ai-intelligence-platform
cd ai-intelligence-platform

# Set up environment (each module has its own venv)
cd market-signals && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Or for policy-signals
cd policy-signals && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run the unified dashboard
cd dashboard && streamlit run app.py
```

---

## Repository History

This combined platform was developed as two parallel projects, later unified:

- **Market Signals:** [github.com/kouverk/data-ai-industry-index-tracker](https://github.com/kouverk/data-ai-industry-index-tracker)
- **Policy Signals:** [github.com/kouverk/ai-influence-monitor](https://github.com/kouverk/ai-influence-monitor)

Full git history for each module is preserved in their respective original repositories.

---

## Challenges & Solutions

### Market Signals

| Challenge | Solution |
|-----------|----------|
| **Unstructured job posting text** | Two-pronged extraction: regex taxonomy (152 technologies) for full dataset, LLM (Claude) on 10K sample for validation |
| **LLM extraction failures** | 1.8% failure rate handled with graceful error handling, `is_successful` flag, severity: warn in dbt tests |
| **LinkedIn single snapshot** | Used for cross-platform validation only; HN (2011-present) provides time-series |
| **Taxonomy vs LLM cost tradeoff** | LLM on sample (~$4.50) validates approach; regex on full 93K posts for cost efficiency |

### Policy Signals

| Challenge | Solution |
|-----------|----------|
| **Entity matching across datasets** | Built normalization layer with canonical name mappings (`config.py`) to match "Anthropic-AI" to "ANTHROPIC, PBC" |
| **LLM output consistency** | Pydantic validation + retry logic with structured prompts |
| **Taxonomy iteration** | Expanded from 12 to 30+ policy_ask codes based on actual document content |
| **"Quiet lobbying" definition** | Built bill-level coalition analysis matching LDA mentions to RFI positions |
| **Score clustering** | Updated prompts to request granular scoring (23, 47, 68 vs 25, 50, 75) |

---

## Future Enhancements

| Enhancement | Pipeline | Value |
|-------------|----------|-------|
| **Process all 10K+ policy submissions** | Policy | Complete industry coverage beyond priority companies |
| **Full LLM extraction on 93K posts** | Market | ~$37 for complete LLM-powered skill extraction |
| **Add FEC campaign finance data** | Policy | Correlate lobbying with political donations |
| **Temporal position tracking** | Policy | Track how company positions shift as regulations evolve |
| **Historical LinkedIn data** | Market | Currently single snapshot; would enable trend analysis |
| **Reddit subreddit tracking** | Market | Community sentiment signals |
| **Automated discrepancy alerts** | Policy | Notify when new filings contradict stated positions |

---

## Status

**Complete** - DataExpert.io Analytics Engineering Capstone

- [x] Market Signals pipeline complete
- [x] Policy Signals pipeline complete
- [x] Unified dashboard
- [x] Astronomer deployment: [PR #287](https://github.com/DataExpert-io/airflow-dbt-project/pull/287)

---

## License

MIT
