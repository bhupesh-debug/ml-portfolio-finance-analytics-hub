# Master Technical Report: Econometrics, Machine Learning, Diagnostics & Validation

**Author**: Bhupesh Chandra Dimri ([bhupesh7cd@gmail.com](mailto:bhupesh7cd@gmail.com))  
**Repository**: [https://github.com/bhupesh-debug/ml-portfolio-finance-analytics-hub](https://github.com/bhupesh-debug/ml-portfolio-finance-analytics-hub)

---

## 1. Portfolio Architectural Design & Information Boundaries
To prevent data contamination, look-ahead bias, and target leakage across all experiments:
- **Project 1 (Budget Overrun)**: Chronological holdout using the final fiscal year (FY2025, $N=839$) strictly separated from training history ($N=2,361$).
- **Project 2 (FP&A Forecast)**: 9 sequential rolling origins ($t=48$ to $64$ in step 2) evaluating horizons $h \in \{1, 2, 3\}$. At each origin $o$, training is strictly bounded to periods where $t + h \le o$.
- **Project 3 (Liquidity Stress)**: Chronological holdout on the final 180 calendar days ($t=915$ to $1094$), with the training partition split 80/20 for out-of-fold conformal calibration.
- **Project 4 (Data Quality)**: Properly separated 60/40 train/test partition ($N=14,400$ train, $N=9,600$ test) with upstream anomaly generation artifacts strictly audited.

---

## 2. Econometric & Statistical Regression Modeling

### A. Project 1: Logistic Regression & OLS Variance Model
- **Logit Specification**:
  $$\text{logit}(P(\text{overrun}_i = 1)) = \beta_0 + \beta_1 \text{burn\_gap} + \beta_2 \text{prior\_year\_var} + \beta_3 \text{overtime\_share} + \beta_4 \text{change\_orders} + \beta_5 \text{vendor\_share} + \dots$$
- **Findings**:
  - `prior_year_variance_pct`: Odds Ratio = 4.36x ($z = 5.82, p < 0.001$)
  - `change_orders_ytd`: Odds Ratio = 2.95x ($z = 4.65, p < 0.001$)
  - `overtime_share`: Odds Ratio = 2.45x ($z = 3.91, p < 0.001$)
  - `type_non_labor`: Odds Ratio = 1.85x ($z = 3.12, p = 0.002$)
- **Diagnostics**:
  - Multicollinearity: VIF controlled below 3.5 across all non-redundant drivers.
  - Calibration: Brier score of **0.103**, demonstrating superior probabilistic calibration compared to heuristic rules (0.185).

### B. Project 2: Panel Regression & Driver Elasticities
- **OLS Specification with HC3 Heteroskedasticity-Consistent Errors**:
  $$\text{Rev}_{i, t+1} = \beta_0 + \beta_1 \text{rev\_lag0} + \beta_2 \text{same\_month\_last\_yr} + \beta_3 \text{sales\_hc} + \beta_4 \text{mkt\_spend} + \beta_5 \text{price\_idx} + \beta_6 \text{roll3} + \epsilon_{i, t+1}$$
- **Findings**:
  - $R^2 = 0.9791$, Adjusted $R^2 = 0.9788$, $F = 3,250.01$ ($p < 0.0001$).
  - `rev_lag0`: Coefficient = +0.928 ($t = 11.56, p < 0.0001$).
  - `same_month_last_year`: Coefficient = +0.485 ($t = 11.07, p < 0.0001$).
  - `sales_headcount`: Statistically significant commercial capacity driver ($t = -2.84, p = 0.0045$).
- **Diagnostics**: Autoregressive panel persistence induces high VIF on lags (72.2), but regularized Ridge ($\alpha=10.0$) and Lasso ($\alpha=0.1$) confirm stable generalization out-of-sample (0.044–0.045 WAPE at $h=1$).

### C. Project 3: Daily Time-Series Regression & Conformal Quantiles
- **OLS Specification**:
  $$\text{Outflow}_t = \beta_0 + \beta_1 \text{dow} + \beta_2 \text{dom} + \beta_3 \text{month\_end} + \beta_4 \text{market\_stress} + \beta_5 \text{lag1} + \beta_6 \text{lag7} + \dots$$
- **Findings**:
  - $R^2 = 0.9316$, $F = 1,572.42$ ($p < 0.0001$).
  - `month_end`: Coefficient = **+31.92 units** ($t = 20.70, p < 0.0001$), isolating the payroll and vendor clearing wall.
  - `market_stress`: Coefficient = **+17.84 units per index point** ($t = 18.11, p < 0.0001$).
- **Conformal Calibration Formulation**:
  $$\hat{y}_{t, \text{calibrated}}^{0.95} = \hat{q}_{0.95}(x_t) + \text{Quantile}_{0.95}\left(\{y_\tau - \hat{q}_{0.95}(x_\tau)\}_{\tau \in \mathcal{D}_{\text{cal}}}\right)$$
  - Empirical offset $\Delta = +7.03$ units restores out-of-sample test coverage from **87.8% to 94.4%**.

### D. Project 4: Supervised Logistic Regression & Anomaly Association
- **Logit Specification**:
  $$\text{logit}(P(\text{is\_break} = 1)) = \beta_0 + \beta_1 \text{log\_abs\_amount} + \beta_2 \text{acct\_z} + \beta_3 \text{ratio\_to\_median} + \beta_4 \text{sign\_vs\_acct} + \beta_5 \text{posting\_lag} + \dots$$
- **Findings**:
  - `missing_entity`: Odds Ratio = **1,089.3x** ($z = 17.58, p < 0.0001$).
  - `dup_key_count`: Odds Ratio = **42.0x** ($z = 37.95, p < 0.0001$).
  - `sign_vs_acct`: Odds Ratio = **4.44x** ($z = 6.73, p < 0.0001$).
  - `posting_lag_days`: Odds Ratio = **1.119x per day** ($z = 24.91, p < 0.0001$).

---

## 3. Comprehensive Model Validation & Benchmark Comparison

| Project | Benchmark Baseline | Candidate Models Evaluated | Champion Architecture | Validated Gain |
|---|---|---|---|---|
| **P1** | Spend-Burn Gap (0.686 ROC) | Logit, HistGBM | **Logistic Regression (0.906 ROC / 0.777 PR)** | **+32.1% ROC / +74.9% Recall@20** |
| **P2** | Seasonal Naive (0.105 WAPE) | Trend Naive, OLS, Ridge, Lasso, Driver GBM | **Driver GBM (1m) & Hybrid Blend (3m)** | **-41.0% Error (1m) / -14.9% (3m)** |
| **P3** | 28d Mean (0.379) / Lag-7 (0.105) | OLS, QuantReg p50, HistGBM p50, Calibrated p95 | **HistGBM p50 (0.073) + Calibrated p95 (94.4%)** | **-80.7% Error vs 28d / +6.6% Coverage** |
| **P4** | Control Rules (54.6% Recall) | Isolation Forest, Rules+IF, Supervised RF/Logit | **Enhanced Rules (Contra) + IF (93.7% Recall)** | **+71.6% Total Recall / +80.9% Sign Flips** |

---

## 4. Multi-Scenario Stress Testing & Monte Carlo Architecture
Every project executed a minimum of 5,000 stochastic Monte Carlo iterations with fixed random seeds (`seed=42`):
- **Project 1 ($N=5,000$)**: Evaluated parameter variance in contract overrun severity; established median portfolio exposure of **$168.88M** and median avoided overrun of **$17.48M**.
- **Project 2 ($N=5,000$)**: Perturbed commercial headcount, marketing spend, and pricing elasticity; established a **P05 downside liquidity floor of $241.91M** ($5.71M VaR corridor).
- **Project 3 ($N=5,000$)**: Stochastically modeled 30-day forward daily residual variance and stress clustering; proved that Severe Stress generates a median cumulative outflow of **3,335.1 units**, exhausting current buffers by Day 22.
- **Project 4 ($N=5,000$)**: Simulated daily Poisson exception arrivals (mean 800 transactions/day, Beta-distributed defect rates); proved that median daily triage load is **100 rows/day** with a **P95 peak load of 139 rows/day** ($4,865/day triage cost).

---

## 5. Technical Limitations & External Validity Caveats
1. **Synthetic Data Boundaries**: All four datasets were procedurally generated. Real-world corporate General Ledgers feature unrecorded liabilities, invoice disputations, and currency volatility not modeled here.
2. **Observational vs. Causal Interpretation**: Regression coefficients reflect empirical predictive associations. Reallocating marketing budgets or hiring sales reps does not causally guarantee revenue expansion without commercial market demand.
3. **Regulatory Non-Equivalence**: Project 3 is an internal operational cash ladder prototype and must never be represented as an approved regulatory LCR or NSFR calculation.
