# AI Intelligence Platform

**Comprehensive visibility into the AI industry through two complementary lenses**

A dual-module analytics platform that combines job market intelligence with policy/lobbying analysis to provide 360-degree visibility into the AI industry.

---

## The Two Lenses

| Module | Question | Data Sources | Key Outputs |
|--------|----------|--------------|-------------|
| **[Market Signals](market-signals/)** | What's hot, growing, or dying in data/AI? | HN jobs (93K), LinkedIn (1.3M), GitHub (81 repos) | Technology trends, role evolution, skill demand |
| **[Policy Signals](policy-signals/)** | Do AI companies practice what they preach? | AI RFI submissions (10K PDFs), Senate LDA API | Lobbying analysis, say-vs-do scores, China rhetoric |

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

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      AI INTELLIGENCE PLATFORM                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────┐    ┌─────────────────────────────┐         │
│  │     MARKET SIGNALS          │    │     POLICY SIGNALS          │         │
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
│  │  Outputs:                   │    │                             │         │
│  │  • Tech trends over time    │    │  Outputs:                   │         │
│  │  • Role evolution           │    │  • Say-vs-do gap scores     │         │
│  │  • LLM vs regex comparison  │    │  • Quiet lobbying detection │         │
│  └─────────────┬───────────────┘    └───────────────┬─────────────┘         │
│                │                                    │                        │
│                └────────────────┬───────────────────┘                        │
│                                 │                                            │
│                                 ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │                    SHARED INFRASTRUCTURE                         │        │
│  │                                                                  │        │
│  │   Orchestration: Airflow (Astronomer)                           │        │
│  │   Transformation: dbt (staging → intermediate → marts)          │        │
│  │   Warehouse: Snowflake                                          │        │
│  │   LLM: Claude API (Anthropic)                                   │        │
│  │   Presentation: Streamlit (unified dashboard)                   │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

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
├── README.md                    # This file
├── docs/
│   ├── CAPSTONE_PROPOSAL.md     # Original combined proposal
│   └── CAPSTONE_FEEDBACK.md     # Instructor feedback
│
├── market-signals/              # Job market intelligence module
│   ├── README.md
│   ├── dashboard/
│   ├── dbt/
│   ├── extraction/
│   ├── airflow/dags/
│   └── docs/
│       ├── ARCHITECTURE.md
│       ├── DATA_DICTIONARY.md
│       ├── DATA_QUALITY.md
│       └── INSIGHTS.md
│
├── policy-signals/              # Lobbying/policy analysis module
│   ├── README.md
│   ├── dashboard/
│   ├── dbt/ai_influence/
│   ├── include/scripts/
│   ├── dags/
│   └── docs/
│       ├── ARCHITECTURE.md
│       ├── DATA_DICTIONARY.md
│       ├── DATA_QUALITY.md
│       └── INSIGHTS.md
│
└── dashboard/                   # Unified dashboard entry point
    └── app.py
```

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

## Module Documentation

Each module maintains its own detailed documentation:

### Market Signals
- [README](market-signals/README.md) - Module overview
- [ARCHITECTURE](market-signals/docs/ARCHITECTURE.md) - System design
- [DATA_DICTIONARY](market-signals/docs/DATA_DICTIONARY.md) - Schema reference
- [DATA_QUALITY](market-signals/docs/DATA_QUALITY.md) - 77 dbt tests
- [INSIGHTS](market-signals/docs/INSIGHTS.md) - Findings

### Policy Signals
- [README](policy-signals/README.md) - Module overview
- [ARCHITECTURE](policy-signals/docs/ARCHITECTURE.md) - System design, scoring methodology
- [DATA_DICTIONARY](policy-signals/docs/DATA_DICTIONARY.md) - Schema reference
- [DATA_QUALITY](policy-signals/docs/DATA_QUALITY.md) - 35 dbt tests
- [INSIGHTS](policy-signals/docs/INSIGHTS.md) - Findings

---

## Live Demos

- **Market Signals:** [data-ai-industry-tracker.streamlit.app](https://data-ai-industry-tracker.streamlit.app/)
- **Policy Signals:** [ai-influence-tracker.streamlit.app](https://ai-influence-monitor-kouverk.streamlit.app/)

---

## Repository History

This combined platform was developed as two parallel projects, later unified:

- **Market Signals:** [github.com/kouverk/data-ai-industry-index-tracker](https://github.com/kouverk/data-ai-industry-index-tracker)
- **Policy Signals:** [github.com/kouverk/ai-influence-monitor](https://github.com/kouverk/ai-influence-monitor)

Full git history for each module is preserved in their respective original repositories.

---

## Status

**Complete** - DataExpert.io Analytics Engineering Capstone

- [x] Market Signals module complete
- [x] Policy Signals module complete
- [x] Unified dashboard
- [x] Astronomer deployment ready

---

## License

MIT
