# Top 1% Master Quantitative Finance Analytics & Machine Learning Portfolio

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub Org](https://img.shields.io/badge/github-bhupesh--debug-orange)](https://github.com/bhupesh-debug)
[![GitHub Pages](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-success)](https://bhupesh-debug.github.io/ml-portfolio-finance-analytics-hub/)

**Comprehensive End-to-End Enterprise Finance Suite: Regression, Forecasting, Uncertainty Quantification, Monte Carlo Simulation, Interactive HTML Dashboard, and Executive Solutions.**

**Lead Architect:** Bhupesh Chandra Dimri  
**Email:** [bhupesh7cd@gmail.com](mailto:bhupesh7cd@gmail.com)  
**GitHub:** [@bhupesh-debug](https://github.com/bhupesh-debug)  
**Live Interactive Dashboard:** [https://bhupesh-debug.github.io/ml-portfolio-finance-analytics-hub/](https://bhupesh-debug.github.io/ml-portfolio-finance-analytics-hub/)

---

## 🚀 Live Interactive HTML Dashboard & Project Labs

The repository includes a complete offline-first, client-side interactive executive dashboard and four project analytical labs with real-time mathematical simulation calculators and native SVG visualizations:

- **Executive Master Portal:** [index.html](index.html) *(Deployable on GitHub Pages)*
- **Pillar 1 (Budget Overrun):** [projects/budget-overrun.html](projects/budget-overrun.html) — Controller review capacity & avoided cost simulator
- **Pillar 2 (FP&A Rolling Forecast):** [projects/fpa-forecast.html](projects/fpa-forecast.html) — Macro driver shock & multi-horizon blending simulator
- **Pillar 3 (Liquidity Stress Forecaster):** [projects/liquidity-stress.html](projects/liquidity-stress.html) — Treasury buffer adequacy & run-off survival simulator
- **Pillar 4 (Reporting Data Quality):** [projects/data-quality.html](projects/data-quality.html) — Exception queue capacity & contra-account defect simulator

---

## Portfolio Overview & GitHub Repositories

This repository serves as the central hub for four enterprise quantitative finance projects. Each project is fully self-contained with its own runnable pipeline, automated `pytest` test suite, econometric regression analyses, 5,000-run Monte Carlo simulations, corporate finance business cases, comprehensive documentation, and executive PowerPoint presentations:

| # | Project Name | Domain | Focus Area | Champion Model | Interactive Lab | GitHub Repository |
|---|---|---|---|---|---|---|
| **P1** | `ml-project-budget-overrun-early-warning` | FP&A / Cost Variance | Predicts budget lines exceeding final allocation by >5% at mid-year | **Logistic Regression Scorecard (ROC-AUC 0.906)** | [Budget Lab](projects/budget-overrun.html) | [Repo Link](https://github.com/bhupesh-debug/ml-project-budget-overrun-early-warning) |
| **P2** | `ml-project-fpa-rolling-forecast-engine` | FP&A / Commercial | Multi-horizon monthly revenue forecasting across 8 business units | **Driver GBM + Dynamic Blending (0.061 WAPE 1m, 0.089 3m)** | [Forecast Lab](projects/fpa-forecast.html) | [Repo Link](https://github.com/bhupesh-debug/ml-project-fpa-rolling-forecast-engine) |
| **P3** | `ml-project-liquidity-stress-forecaster` | Treasury / Liquidity | Daily net cash outflow forecasting and 30-day buffer stress testing | **HistGBM (0.073 WAPE) + Conformal p95 (94.4% Coverage)** | [Liquidity Lab](projects/liquidity-stress.html) | [Repo Link](https://github.com/bhupesh-debug/ml-project-liquidity-stress-forecaster) |
| **P4** | `ml-project-reporting-data-quality-anomaly-detector` | Accounting / Controls | Catching broken journal transactions before reporting consolidation | **Enhanced Rules + Contra-Account + IF (93.7% Recall)** | [Data Quality Lab](projects/data-quality.html) | [Repo Link](https://github.com/bhupesh-debug/ml-project-reporting-data-quality-anomaly-detector) |

---

## Cumulative Financial Business Case Summary (Base Case)

| Project | Annual Quantified Benefit | Implementation Capex | Annual Opex | Year-1 Net Realized Benefit | Payback Runway | 3-Year NPV (@ 10%) | 3-Year ROI |
|---|---|---|---|---|---|---|---|
| **1. Budget Overrun Early Warning** | $3,070,000 | $240,000 | $60,000 | **$2,770,000** | 1.4 Months | **$7,245,424** | 3,019% |
| **2. FP&A Rolling Forecast Engine** | $3,070,000 | $240,000 | $60,000 | **$2,770,000** | 1.0 Month | **$7,245,424** | 3,019% |
| **3. Liquidity Stress Forecaster** | $3,362,500 | $260,000 | $65,000 | **$3,037,500** | 0.9 Months | **$7,940,394** | 3,054% |
| **4. Reporting Anomaly Detector** | $2,510,000 | $250,000 | $60,000 | **$2,200,000** | 1.2 Months | **$5,842,787** | 2,337% |
| **PORTFOLIO TOTALS** | **$12,012,500** | **$990,000** | **$245,000** | **$10,777,500** | **1.1 Months** | **$28,274,029** | **2,856%** |

---

## Master Deliverables & Reports Directory

### Consolidated Analytical Reports
- [Executive Summary & Business Decisions](reports/executive_summary.md)
- [Comprehensive Econometric & Technical Report](reports/technical_report.md)
- [Evidence-Backed Question & Answer Register (33 Questions)](reports/project_question_answer_register.md)
- [Prioritized Recommendations & Implementation Roadmap](reports/recommendations_and_action_plan.md)
- [Portfolio Executive Presentation Deck](PORTFOLIO_PRESENTATION.pptx)

### Machine-Readable Data Contracts (CSV)
- [Experiment Benchmark Results (20 Experiments)](reports/experiment_results.csv)
- [Regression Parameters & Diagnostics (42 Features)](reports/regression_results.csv)
- [Simulation Scenarios & Risk Measures](reports/simulation_results.csv)
- [Data Quality & Anomaly Findings](reports/data_quality_findings.csv)

---

## Reproduction & Verification

To reproduce all econometric models, backtests, simulations, charts, and test suites in a clean environment:

```bash
# 1. Clone the repository
git clone https://github.com/bhupesh-debug/ml-portfolio-finance-analytics-hub.git
cd ml-portfolio-finance-analytics-hub

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run master analytical pipeline
python run_analysis.py

# 4. Run automated test suite (25/25 tests passing)
python -m pytest tests/test_dashboard_contracts.py -v

# 5. Launch interactive executive portal locally
# Open index.html in any browser (Google Chrome, Edge, Safari, Firefox)
```
