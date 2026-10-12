# Master Recommendations, Solutions & Implementation Action Plan

**Target Audience**: Executive Steering Committee, FP&A Leadership, Corporate Treasurer, Chief Accounting Officer  
**Author**: Quantitative Analytics & Financial Machine Learning Team  

---

## 1. Prioritized Strategic Recommendations Matrix

| Strategic Action | Focus Project | Financial Net Benefit (Yr 1) | Confidence | Complexity | Implementation Owner | Time to Value | Priority Rank |
|---|---|---|---|---|---|---|---|
| **1. Deploy Budget Overrun SQL Scorecard** | P1: Budget Overrun | $2,770,000 | Very High (95%) | Low (4 Wks) | Lead FP&A Director | Immediate (Q2 Close) | **#1 Immediate Win** |
| **2. Embed 3-Horizon Blending in Rolling Closes** | P2: FP&A Rolling Forecast | $2,770,000 | High (85%) | Medium (8 Wks) | Commercial Finance VP | Near-Term (60 Days) | **#2 High Impact** |
| **3. Implement Upstream Hard Gates & Contra Rules** | P4: Reporting Data Quality | $2,200,000 | High (85%) | Medium (8 Wks) | Financial Controller / ETL Ops | Near-Term (60 Days) | **#3 SOX Control** |
| **4. Operationalize Dynamic Two-Tier Buffer Sizing** | P3: Liquidity Stress | $3,037,500 | Medium (75%) | Med-High (10 Wks) | Head of Treasury / ALCO | Strategic (90 Days) | **#4 Solvency Shield** |

---

## 2. Phased 12-Week Portfolio Deployment Roadmap

```
Week 1-4: Foundation & Quick Wins
├── Deploy Project 1 Logistic Scorecard directly into SAP/Oracle ERP SQL views for Q2 mid-year reviews.
├── Enforce database NOT NULL and primary key deduplication constraints in Project 4 ETL ingestion pipelines.
└── Connect automated feeds for commercial sales headcount (Workday) and pricing indices.

Week 5-8: Parallel Shadow Runs & Operational Alignment
├── Initiate 3-cycle parallel shadow forecasting for Project 2 with dynamic horizon blending (80/20 at 1m, 60/40 at 2m, 40/60 at 3m).
├── Deploy daily morning 07:30 EST liquidity outflow forecasting for Project 3 Money Market Desk.
└── Configure ERP chart of accounts normal debit/credit balance mapping to activate contra-account anomaly detection.

Week 9-12: Full Production Cutover & SOX Governance
├── ALCO formal review and adoption of the 3,250-unit dynamic buffer policy backed by contingent credit facilities.
├── Rollout of controller exception triage queue in SAP/Oracle with auto-generated variance waterfalls.
└── Establish automated quarterly retraining triggers (WAPE > 8.5%, tail coverage < 93%, defect drift > 3.0%).
```

---

## 3. Detailed Solution Specifications

### Solution 1: Budget Overrun Early-Warning Controller Queue (Project 1)
- **Problem**: Spend-burn gap heuristics miss 64.5% of overruns, causing $168.9M in unmonitored risk exposure.
- **Action**: Implement Logistic Regression log-odds scoring in ERP database views. Filter the top 20% highest-risk lines into a dedicated controller review queue.
- **Success Metric**: Capture rate $\ge 60\%$ of eventual overruns in the top 20% review volume.
- **Resource Requirement**: 1 Data Engineer (80 hrs), 1 Financial Analyst (40 hrs).

### Solution 2: FP&A Dynamic Rolling Horizon Forecast Workflow (Project 2)
- **Problem**: Seasonal naive run-rates miss corporate growth (-10.4% bias), while pure ML degrades at 3 months (0.117 WAPE).
- **Action**: Institutionalize automated driver ML for near-term 30-day and 60-day closes; blend 40% ML with 60% seasonal naive for 90-day closes.
- **Success Metric**: 1-month portfolio WAPE $< 0.070$; 3-month portfolio WAPE $< 0.095$.
- **Resource Requirement**: 1 Data Scientist (120 hrs), FP&A planning leads (60 hrs).

### Solution 3: Two-Tier Liquidity Buffer & Stress Early-Warning Framework (Project 3)
- **Problem**: Holding excess idle cash costs $2.4M in carry drag; current 2,886-unit buffer breaches 100% under severe stress.
- **Action**: Size operational baseline buffer to 3,250 units; automate Amber (Coverage $< 1.10$) and Red (Coverage $< 1.00$) ALCO contingency alerts.
- **Success Metric**: 30-day baseline coverage $\ge 1.10$; empirical test coverage $\ge 94.0\%$.
- **Resource Requirement**: Treasury Quantitative Analyst (100 hrs), ALCO stakeholder time.

### Solution 4: Multi-Tier Reporting Integrity Gate (Project 4)
- **Problem**: Corrupt transactions reach audited financial consolidation; amount-only methods catch 0% of sign flips.
- **Action**: Deploy upstream hard rejection gates for duplicates and null entities; implement contra-account normal-sign validation rules alongside Isolation Forest.
- **Success Metric**: Capture rate $\ge 90\%$ of corrupt transactions with precision $\ge 75\%$.
- **Resource Requirement**: ETL Data Engineer (100 hrs), Senior Accounting Controller (50 hrs).
