# Strategic Portfolio Recommendations & Executive Action Plan

**To**: Chief Financial Officer, Corporate Controller, and Head of Financial Operations  
**From**: Quantitative Analytics & Financial Machine Learning Architecture Team  

---

## 1. Executive Priority Ranking Matrix

| Strategic Action | Target Project | Expected Net Benefit (Yr 1) | Confidence Level | Implementation Effort | Risk Level | Priority Rank |
|---|---|---|---|---|---|---|
| **Deploy Mid-Year Budget Early-Warning Scorecard** | Project 1 (Budget Overrun) | $2,770,000 | **Very High (95%)** | **Low (4 Weeks)** | **Very Low** | **#1 Immediate Win** |
| **Implement Hybrid Horizon Rolling Revenue Engine** | Project 2 (FP&A Engine) | $2,770,000 | **High (85%)** | **Medium (8 Weeks)** | **Low** | **#2 High Impact** |
| **Establish Upstream Ingestion Gates & Contra Checks**| Project 4 (Reporting Quality) | $2,200,000 | **High (85%)** | **Medium (8 Weeks)** | **Low-Medium** | **#3 Close Control** |
| **Integrate Quantile Conformal Liquidity Stress Engine**| Project 3 (Liquidity Stress) | $3,037,500 | **Medium (75%)** | **Medium-High (10 Wks)**| **Medium (ALCO)** | **#4 Strategic ALM** |

---

## 2. Detailed Execution Recommendations

### Action 1: Deploy Logistic Scorecards for Q2 Mid-Year Budget Reviews (Project 1)
- **Why First**: The model is immediately deployable via standard database SQL scoring (`logit` formula). It captures 62.1% of overruns while requiring analysts to inspect only 20% of budget lines.
- **Immediate Step**: Connect the feature view to SAP General Ledger and Workday HR roster tables; generate the prioritized review queue for the upcoming fiscal Q2 close.

### Action 2: Operationalize Dynamic Blending in FP&A Rolling Closes (Project 2)
- **Why Second**: Generates $2.1M in working capital optimization by reducing 1-month forecast error from 10.5% to 6.1%.
- **Immediate Step**: Institute the recommended horizon blending policy (80/20 at 1m, 60/40 at 2m, 40/60 at 3m) across divisional planning meetings.

### Action 3: Implement Upstream Hard Gates and Normal-Balance Signs (Project 4)
- **Why Third**: Stops dirty data at the perimeter rather than cleaning it post-consolidation.
- **Immediate Step**: Implement database NOT NULL constraints and primary key deduplication in ETL staging. Map ERP chart of accounts to standard debit/credit normal postures to eliminate sign flips.

### Action 4: Formulate Two-Tier Treasury Buffer Policy (Project 3)
- **Why Fourth**: Protects against 100% buffer breaches during market liquidity contagion while avoiding excessive carry drag.
- **Immediate Step**: Establish a dynamic target buffer of 3,250 units, backed by pre-arranged credit lines for tail liquidity stress events.
