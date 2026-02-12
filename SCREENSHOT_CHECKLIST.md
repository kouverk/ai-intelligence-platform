# Screenshot Checklist for Capstone Submission

## PART 1: Policy Signals (Astro - the impressive one)

### Setup
```bash
cd /Users/kouverbingham/development/data-expert-analytics/ai-intelligence-platform/policy-signals
astro dev start
# Wait for it to spin up (~1-2 min)
# Open http://localhost:8080
# Login: admin / admin
```

### Screenshots to take

| # | What | How |
|---|------|-----|
| 1 | DAG list view | Main page showing all 6 DAGs |
| 2 | ai_influence_pipeline Graph | Click DAG → Graph tab (shows 11 tasks, 5 groups) |
| 3 | snowflake_sync Graph | Click DAG → Graph tab (shows 3-task chain) |
| 4 | Run snowflake_sync | Trigger DAG → wait → screenshot green success |
| 5 | Run extract_lda_lobbying | Trigger DAG → wait → screenshot green success |

### When done
```bash
astro dev stop
```

---

## PART 2: Market Signals (Astro)

### Setup
```bash
cd /Users/kouverbingham/development/data-expert-analytics/ai-intelligence-platform/market-signals
astro dev start
# Wait for it to spin up (~1-2 min)
# Open http://localhost:8080
# Login: admin / admin
```

### Screenshots to take

| # | What | How |
|---|------|-----|
| 6 | DAG list view | Main page showing all 5 DAGs |
| 7 | dbt_transform Graph | Click DAG → Graph tab (shows 7-task chain) |
| 8 | Run dbt_transform | Trigger DAG → wait → screenshot green success |

### When done
```bash
astro dev stop
```

---

## Quick Notes

- If snowflake_sync fails (missing creds), just screenshot the Graph view anyway
- The Graph views alone show your architecture even without green runs
- extract_lda_lobbying is safest to actually run (just hits public API)
- Take screenshots with URL bar visible
