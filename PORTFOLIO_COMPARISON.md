# Quantitative Portfolio Comparison & Methodological Ranking

**Objective**: Rigorously benchmark the four projects based on statistical evidence, business applicability, implementation complexity, model validation risks, and production readiness.

---

## 1. Multi-Dimensional Portfolio Ranking Matrix

| Evaluation Dimension | Project 1: Budget Overrun Early Warning | Project 2: FP&A Rolling Forecast Engine | Project 3: Liquidity Stress Forecaster | Project 4: Reporting Anomaly Detector |
|---|---|---|---|---|
| **Primary Domain** | FP&A / Cost Variance | Corporate FP&A / Commercial | Treasury / Liquidity Risk | Accounting / Financial Reporting |
| **Statistical Robustness** | High ($ROC=0.906$, Logit & GBM parity) | High ($R^2=0.979$, 9-origin backtest) | High ($R^2=0.932$, Conformal calibration) | Moderate (Synthetic label dependence) |
| **Quantified Annual Benefit** | $3.07M (Base Case) | $3.07M (Base Case) | $3.36M (Base Case) | $2.51M (Base Case) |
| **Implementation Complexity** | Low (Tabular batch inference) | Moderate (Multi-horizon panel lags) | Moderate (Quantile + Conformal + Stress) | Low-Moderate (ETL rules + IF pipeline) |
| **Validation / Leakage Risk** | Low (Strict mid-year cutoff) | Low (Chronological rolling origins) | Low-Moderate (Non-regulatory prototype) | Moderate-High (Label availability in prod) |
| **Production Readiness** | **85% (Immediate Pilot)** | **80% (Shadow Run)** | **75% (ALCO Operational Use)** | **70% (Requires Upstream ERP Mapping)**|
| **Evidence-Based Rank** | **Rank 2 (Easiest Win)** | **Rank 1 (Strongest Core ML)** | **Rank 3 (Highest Risk Exposure)**| **Rank 4 (Highest Governance Work)** |

---

## 2. Evidence-Based Project Diagnoses

### A. Strongest Project: Project 2 (FP&A Rolling Forecast Engine)
- **Why It Ranks Strongest**:
  1. Methodologically flawless 9-origin rolling backtest without look-ahead bias across 8 autonomous divisions over 72 months.
  2. Discovered non-trivial econometric insight: seasonal naive suffers from systematic negative growth bias (-10.4%), while ML driver forecasts win at short horizons but require dynamic blending at longer horizons.
  3. Direct connection to tangible operational value: $2.1M working capital release and $850k logistics expediting savings.

### B. Easiest Implementation Win: Project 1 (Budget Overrun Early Warning)
- **Why It Ranks as Easiest Win**:
  1. Tabular mid-year checkpoint features are directly accessible in existing SAP/Workday ERP schemas.
  2. Logistic Regression (ROC-AUC 0.906) perfectly matches gradient boosting, meaning it can be implemented directly via SQL scorecard scoring inside enterprise databases without complex microservice infrastructure.
  3. Captures 62.1% of overruns by reviewing only the top 20% highest-risk budget lines.

### C. Project with Greatest Validation Risks: Project 3 (Liquidity Stress Forecaster)
- **Validation Risks & Caveats**:
  1. Regulatory Non-Equivalence: Treasury models face heavy regulatory scrutiny. The model must not be confused with Basel III LCR/NSFR statutory reporting.
  2. Conformal Calibration Drift: The +7.03 unit offset was calibrated on synthetic data. Real-world liquidity crunches involve regime shifts where historical residuals may underestimate tail contagion.
  3. Behavioral Assumptions: Assumes static cash drain without active liquidity management responses.

### D. Project with Highest Operational Dependencies: Project 4 (Reporting Anomaly Detector)
- **Operational Dependencies & Caveats**:
  1. Synthetic Prevalence Distortion: Injected 13.0% anomaly rate is 20-50x higher than real production feeds (typically 0.1%-0.5%). Real deployment will experience lower precision unless upstream hard gates filter structural duplicates.
  2. Contra-Account Mapping: Catching sign flips depends entirely on maintaining accurate normal-balance charts of accounts in ERP master data.
  3. Supervised Ceiling: Supervised Random Forest results assume labels exist; true production day-1 must rely on unsupervised Isolation Forest + Rules.

---

## 3. Prioritized Portfolio Improvement Trajectory
1. **Priority 1 (Project 1)**: Deploy Logistic Regression scorecard directly into ERP for upcoming Q2 mid-year reviews.
2. **Priority 2 (Project 2)**: Initiate 3-cycle parallel shadow forecasting against FP&A spreadsheet models with dynamic horizon blending.
3. **Priority 3 (Project 4)**: Implement upstream database constraints blocking duplicates and missing keys before deploying Isolation Forest.
4. **Priority 4 (Project 3)**: Formalize ALCO amber/red liquidity triggers and validate conformal bands against historical Fedwire settlement logs.
