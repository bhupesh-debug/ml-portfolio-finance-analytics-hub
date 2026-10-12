# Top 1% Master Quantitative Finance Analytics & Machine Learning Portfolio

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub Org](https://img.shields.io/badge/github-bhupesh--debug-orange)](https://github.com/bhupesh-debug)

**Comprehensive End-to-End Enterprise Finance Suite: Regression, Forecasting, Uncertainty Quantification, Monte Carlo Simulation, and Executive Solutions.**

**Lead Architect:** Bhupesh Chandra Dimri  
**Email:** [bhupesh7cd@gmail.com](mailto:bhupesh7cd@gmail.com)  
**GitHub:** [@bhupesh-debug](https://github.com/bhupesh-debug)

---

## Portfolio Overview & GitHub Repositories

This repository serves as the central hub for four enterprise quantitative finance projects. Each project is fully self-contained with its own runnable pipeline, automated `pytest` test suite, econometric regression analyses, 5,000-run Monte Carlo simulations, corporate finance business cases, comprehensive documentation, and executive PowerPoint presentations:

| # | Project Name | Domain | Focus Area | Champion Model | GitHub Repository |
|---|---|---|---|---|---|
| **P1** | `ml-project-budget-overrun-early-warning` | FP&A / Cost Variance | Predicts budget lines exceeding final allocation by >5% at mid-year | **Logistic Regression & HistGBM (ROC-AUC 0.906)** | [Repository Link](https://github.com/bhupesh-debug/ml-project-budget-overrun-early-warning) |
| **P2** | `ml-project-fpa-rolling-forecast-engine` | FP&A / Commercial | Multi-horizon monthly revenue forecasting across 8 business units | **Driver GBM + Dynamic Blending (0.061 WAPE 1m, 0.089 3m)** | [Repository Link](https://github.com/bhupesh-debug/ml-project-fpa-rolling-forecast-engine) |
| **P3** | `ml-project-liquidity-stress-forecaster` | Treasury / Liquidity | Daily net cash outflow forecasting and 30-day buffer stress testing | **HistGBM (0.073 WAPE) + Conformal p95 (94.4% Coverage)** | [Repository Link](https://github.com/bhupesh-debug/ml-project-liquidity-stress-forecaster) |
| **P4** | `ml-project-reporting-data-quality-anomaly-detector` | Accounting / Controls | Catching broken journal transactions before reporting consolidation | **Enhanced Rules + Contra-Account + IF (93.7% Recall)** | [Repository Link](https://github.com/bhupesh-debug/ml-project-reporting-data-quality-anomaly-detector) |

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

## Master Deliverables Directory
- [Portfolio Executive Summary](PORTFOLIO_EXECUTIVE_SUMMARY.md)
- [Portfolio Comparative Evaluation & Ranking](PORTFOLIO_COMPARISON.md)
- [Strategic Portfolio Recommendations](PORTFOLIO_RECOMMENDATIONS.md)
- [Portfolio Completion Matrix](PORTFOLIO_COMPLETION_MATRIX.csv)
- [Master Executive Slide Deck](PORTFOLIO_PRESENTATION.pptx)

---

## Reproduction Instructions

Each subproject can be executed independently from its respective root:

```bash
# Clone all repositories
git clone https://github.com/bhupesh-debug/ml-project-budget-overrun-early-warning.git
git clone https://github.com/bhupesh-debug/ml-project-fpa-rolling-forecast-engine.git
git clone https://github.com/bhupesh-debug/ml-project-liquidity-stress-forecaster.git
git clone https://github.com/bhupesh-debug/ml-project-reporting-data-quality-anomaly-detector.git

# Execute each project pipeline
cd ml-project-budget-overrun-early-warning && python run.py && python -m pytest tests/ && cd ..
cd ml-project-fpa-rolling-forecast-engine && python run.py && python -m pytest tests/ && cd ..
cd ml-project-liquidity-stress-forecaster && python run.py && python -m pytest tests/ && cd ..
cd ml-project-reporting-data-quality-anomaly-detector && python run.py && python -m pytest tests/ && cd ..
```
