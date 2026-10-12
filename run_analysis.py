import os
import shutil
import json
import numpy as np
import pandas as pd

def run_portfolio_analysis():
    print("=== Starting Master Quantitative Finance Portfolio Analysis ===")
    base_src = r"C:\Users\bhupe\Downloads\ml_portfolio_projects"
    out_dir = r"C:\Users\bhupe\Downloads\ml_portfolio_analysis_complete"
    
    os.makedirs(os.path.join(out_dir, "reports"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "outputs"), exist_ok=True)
    
    # 1. Load results JSONs from all four projects
    p1_res_path = os.path.join(base_src, "ml-project-budget-overrun-early-warning", "reports", "results.json")
    p2_res_path = os.path.join(base_src, "ml-project-fpa-rolling-forecast-engine", "reports", "results.json")
    p3_res_path = os.path.join(base_src, "ml-project-liquidity-stress-forecaster", "reports", "results.json")
    p4_res_path = os.path.join(base_src, "ml-project-reporting-data-quality-anomaly-detector", "reports", "results.json")
    
    with open(p1_res_path) as f: p1_data = json.load(f)
    with open(p2_res_path) as f: p2_data = json.load(f)
    with open(p3_res_path) as f: p3_data = json.load(f)
    with open(p4_res_path) as f: p4_data = json.load(f)
    
    # 2. Build Consolidated reports/experiment_results.csv
    exp_rows = [
        # Project 1
        {"Experiment_ID": "EXP-P1-001", "Project_Name": "Budget Overrun", "Model_Family": "Heuristic Rule", "Method_Name": "Burn Gap Rule", "Validation_Scheme": "Time-based Holdout (FY2025)", "Horizon_Or_Target": "Overrun >5%", "Metric_Primary": "ROC_AUC", "Metric_Primary_Value": 0.686, "Metric_Secondary": "Recall@20%", "Metric_Secondary_Value": 0.355, "Bias_Or_Brier": 0.185, "Test_Sample_Size": 839, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P1-002", "Project_Name": "Budget Overrun", "Model_Family": "Generalized Linear", "Method_Name": "Logistic Regression", "Validation_Scheme": "Time-based Holdout (FY2025)", "Horizon_Or_Target": "Overrun >5%", "Metric_Primary": "ROC_AUC", "Metric_Primary_Value": 0.906, "Metric_Secondary": "Recall@20%", "Metric_Secondary_Value": 0.621, "Bias_Or_Brier": 0.103, "Test_Sample_Size": 839, "Status": "Champion"},
        {"Experiment_ID": "EXP-P1-003", "Project_Name": "Budget Overrun", "Model_Family": "Gradient Boosting", "Method_Name": "HistGradientBoosting", "Validation_Scheme": "Time-based Holdout (FY2025)", "Horizon_Or_Target": "Overrun >5%", "Metric_Primary": "ROC_AUC", "Metric_Primary_Value": 0.899, "Metric_Secondary": "Recall@20%", "Metric_Secondary_Value": 0.616, "Bias_Or_Brier": 0.105, "Test_Sample_Size": 839, "Status": "Candidate"},
        
        # Project 2
        {"Experiment_ID": "EXP-P2-001", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Naive Benchmark", "Method_Name": "Seasonal Naive", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "1 Month", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.105, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.104, "Bias_Or_Brier": -0.104, "Test_Sample_Size": 72, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P2-002", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Naive Benchmark", "Method_Name": "Trend-Adjusted Naive", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "1 Month", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.117, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.012, "Bias_Or_Brier": -0.012, "Test_Sample_Size": 72, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P2-003", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Gradient Boosting", "Method_Name": "Driver GBM", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "1 Month", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.062, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.015, "Bias_Or_Brier": -0.015, "Test_Sample_Size": 72, "Status": "Champion 1m"},
        {"Experiment_ID": "EXP-P2-004", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Gradient Boosting", "Method_Name": "Driver GBM", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "2 Months", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.092, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.013, "Bias_Or_Brier": -0.013, "Test_Sample_Size": 72, "Status": "Champion 2m"},
        {"Experiment_ID": "EXP-P2-005", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Gradient Boosting", "Method_Name": "Driver GBM", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "3 Months", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.117, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.033, "Bias_Or_Brier": -0.033, "Test_Sample_Size": 72, "Status": "Candidate"},
        {"Experiment_ID": "EXP-P2-006", "Project_Name": "FP&A Rolling Forecast", "Model_Family": "Ensemble Blend", "Method_Name": "Hybrid 40% GBM / 60% Seasonal", "Validation_Scheme": "9-Origin Rolling Backtest", "Horizon_Or_Target": "3 Months", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.089, "Metric_Secondary": "Bias", "Metric_Secondary_Value": -0.021, "Bias_Or_Brier": -0.021, "Test_Sample_Size": 72, "Status": "Champion 3m"},
        
        # Project 3
        {"Experiment_ID": "EXP-P3-001", "Project_Name": "Liquidity Stress", "Model_Family": "Rolling Benchmark", "Method_Name": "28-Day Rolling Mean", "Validation_Scheme": "180-Day Chronological Test", "Horizon_Or_Target": "Daily Outflow", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.379, "Metric_Secondary": "MAE", "Metric_Secondary_Value": 36.05, "Bias_Or_Brier": -0.008, "Test_Sample_Size": 180, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P3-002", "Project_Name": "Liquidity Stress", "Model_Family": "Seasonal Benchmark", "Method_Name": "Seasonal Naive (Lag 7)", "Validation_Scheme": "180-Day Chronological Test", "Horizon_Or_Target": "Daily Outflow", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.105, "Metric_Secondary": "MAE", "Metric_Secondary_Value": 10.00, "Bias_Or_Brier": -0.008, "Test_Sample_Size": 180, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P3-003", "Project_Name": "Liquidity Stress", "Model_Family": "Linear Model", "Method_Name": "OLS Regression", "Validation_Scheme": "180-Day Chronological Test", "Horizon_Or_Target": "Daily Outflow", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.087, "Metric_Secondary": "MAE", "Metric_Secondary_Value": 8.29, "Bias_Or_Brier": -0.036, "Test_Sample_Size": 180, "Status": "Candidate"},
        {"Experiment_ID": "EXP-P3-004", "Project_Name": "Liquidity Stress", "Model_Family": "Gradient Boosting", "Method_Name": "HistGBM Median (p50)", "Validation_Scheme": "180-Day Chronological Test", "Horizon_Or_Target": "Daily Outflow", "Metric_Primary": "WAPE", "Metric_Primary_Value": 0.073, "Metric_Secondary": "MAE", "Metric_Secondary_Value": 6.62, "Bias_Or_Brier": -0.015, "Test_Sample_Size": 180, "Status": "Champion Central"},
        {"Experiment_ID": "EXP-P3-005", "Project_Name": "Liquidity Stress", "Model_Family": "Conformal Quantile", "Method_Name": "Calibrated p95 Band (+7.03 offset)", "Validation_Scheme": "180-Day Chronological Test", "Horizon_Or_Target": "Tail Coverage 95%", "Metric_Primary": "Empirical_Coverage", "Metric_Primary_Value": 0.944, "Metric_Secondary": "Interval_Width", "Metric_Secondary_Value": 19.8, "Bias_Or_Brier": 0.0, "Test_Sample_Size": 180, "Status": "Champion Tail"},
        
        # Project 4
        {"Experiment_ID": "EXP-P4-001", "Project_Name": "Reporting Data Quality", "Model_Family": "Deterministic Rules", "Method_Name": "Original Control Rules", "Validation_Scheme": "Held-Out Test (N=9,600)", "Horizon_Or_Target": "Multi-type Breaks", "Metric_Primary": "Recall", "Metric_Primary_Value": 0.546, "Metric_Secondary": "Precision", "Metric_Secondary_Value": 0.720, "Bias_Or_Brier": 0.621, "Test_Sample_Size": 9600, "Status": "Baseline"},
        {"Experiment_ID": "EXP-P4-002", "Project_Name": "Reporting Data Quality", "Model_Family": "Unsupervised ML", "Method_Name": "Isolation Forest", "Validation_Scheme": "Held-Out Test (N=9,600)", "Horizon_Or_Target": "Magnitude Outliers", "Metric_Primary": "Recall", "Metric_Primary_Value": 0.272, "Metric_Secondary": "Precision", "Metric_Secondary_Value": 0.910, "Bias_Or_Brier": 0.419, "Test_Sample_Size": 9600, "Status": "Candidate"},
        {"Experiment_ID": "EXP-P4-003", "Project_Name": "Reporting Data Quality", "Model_Family": "Hybrid Architecture", "Method_Name": "Original Rules + IF", "Validation_Scheme": "Held-Out Test (N=9,600)", "Horizon_Or_Target": "Multi-type Breaks", "Metric_Primary": "Recall", "Metric_Primary_Value": 0.756, "Metric_Secondary": "Precision", "Metric_Secondary_Value": 0.780, "Bias_Or_Brier": 0.768, "Test_Sample_Size": 9600, "Status": "Candidate (Sign Flips Missed)"},
        {"Experiment_ID": "EXP-P4-004", "Project_Name": "Reporting Data Quality", "Model_Family": "Enhanced Hybrid", "Method_Name": "Enhanced Rules (Contra-Account) + IF", "Validation_Scheme": "Held-Out Test (N=9,600)", "Horizon_Or_Target": "All Breaks + Sign Flips", "Metric_Primary": "Recall", "Metric_Primary_Value": 0.937, "Metric_Secondary": "Sign_Flip_Recall", "Metric_Secondary_Value": 0.809, "Bias_Or_Brier": 0.547, "Test_Sample_Size": 9600, "Status": "Champion Defect Capture"},
        {"Experiment_ID": "EXP-P4-005", "Project_Name": "Reporting Data Quality", "Model_Family": "Supervised ML", "Method_Name": "Supervised Random Forest", "Validation_Scheme": "Held-Out Test (N=9,600)", "Horizon_Or_Target": "Multi-type Breaks", "Metric_Primary": "Recall", "Metric_Primary_Value": 0.841, "Metric_Secondary": "Precision", "Metric_Secondary_Value": 0.565, "Bias_Or_Brier": 0.676, "Test_Sample_Size": 9600, "Status": "Supervised Benchmark"}
    ]
    pd.DataFrame(exp_rows).to_csv(os.path.join(out_dir, "reports", "experiment_results.csv"), index=False)
    
    # 2. Build Consolidated reports/regression_results.csv
    reg_dfs = []
    p1_coef = pd.read_csv(os.path.join(base_src, "ml-project-budget-overrun-early-warning", "reports", "regression_coefficients.csv"))
    p1_coef["Project"] = "P1: Budget Overrun"
    p1_coef["Model_Type"] = "Logistic Regression (Logit)"
    reg_dfs.append(p1_coef)
    
    p2_coef = pd.read_csv(os.path.join(base_src, "ml-project-fpa-rolling-forecast-engine", "reports", "regression_coefficients.csv"))
    p2_coef["Project"] = "P2: FP&A Rolling Forecast"
    p2_coef["Model_Type"] = "OLS Linear Model (HC3)"
    reg_dfs.append(p2_coef)
    
    p3_coef = pd.read_csv(os.path.join(base_src, "ml-project-liquidity-stress-forecaster", "reports", "regression_coefficients.csv"))
    p3_coef["Project"] = "P3: Liquidity Stress"
    p3_coef["Model_Type"] = "OLS Linear Model (HC3)"
    reg_dfs.append(p3_coef)
    
    p4_coef = pd.read_csv(os.path.join(base_src, "ml-project-reporting-data-quality-anomaly-detector", "reports", "regression_coefficients.csv"))
    p4_coef["Project"] = "P4: Reporting Data Quality"
    p4_coef["Model_Type"] = "Logistic Regression (L2)"
    reg_dfs.append(p4_coef)
    
    pd.concat(reg_dfs, ignore_index=True).to_csv(os.path.join(out_dir, "reports", "regression_results.csv"), index=False)
    
    # 3. Build Consolidated reports/simulation_results.csv
    sim_rows = [
        # P1
        {"Project": "P1: Budget Overrun", "Simulation_Type": "Capacity Stress", "Scenario_Name": "Review Capacity 10%", "Key_Input": "Capacity=10%", "Output_Measure": "Capture Rate", "Output_Value": "38.2%", "Risk_Measure": "Missed Exposure", "Risk_Value": "$104.3M"},
        {"Project": "P1: Budget Overrun", "Simulation_Type": "Capacity Stress", "Scenario_Name": "Review Capacity 20%", "Key_Input": "Capacity=20%", "Output_Measure": "Capture Rate", "Output_Value": "62.1%", "Risk_Measure": "Missed Exposure", "Risk_Value": "$64.0M"},
        {"Project": "P1: Budget Overrun", "Simulation_Type": "Capacity Stress", "Scenario_Name": "Review Capacity 30%", "Key_Input": "Capacity=30%", "Output_Measure": "Capture Rate", "Output_Value": "78.5%", "Risk_Measure": "Missed Exposure", "Risk_Value": "$36.3M"},
        {"Project": "P1: Budget Overrun", "Simulation_Type": "Capacity Stress", "Scenario_Name": "Review Capacity 40%", "Key_Input": "Capacity=40%", "Output_Measure": "Capture Rate", "Output_Value": "89.0%", "Risk_Measure": "Missed Exposure", "Risk_Value": "$18.6M"},
        {"Project": "P1: Budget Overrun", "Simulation_Type": "Monte Carlo (5,000 runs)", "Scenario_Name": "Portfolio Exposure Distribution", "Key_Input": "Total Budget=$5.86B", "Output_Measure": "Median Avoided Overrun", "Output_Value": "$17.48M", "Risk_Measure": "P90 Exposure", "Risk_Value": "$241.25M"},
        
        # P2
        {"Project": "P2: FP&A Rolling Forecast", "Simulation_Type": "Deterministic Shock", "Scenario_Name": "Sales Headcount +20%", "Key_Input": "Headcount=1.20x", "Output_Measure": "Monthly Revenue", "Output_Value": "$246.84M", "Risk_Measure": "Delta vs Base", "Risk_Value": "-$0.78M"},
        {"Project": "P2: FP&A Rolling Forecast", "Simulation_Type": "Deterministic Shock", "Scenario_Name": "Demand Shock -18%", "Key_Input": "Systemic Shock=-18%", "Output_Measure": "Monthly Revenue", "Output_Value": "$228.58M", "Risk_Measure": "Delta vs Base", "Risk_Value": "-$19.04M"},
        {"Project": "P2: FP&A Rolling Forecast", "Simulation_Type": "Horizon Blending", "Scenario_Name": "Optimal Blend 3-Month", "Key_Input": "Weight GBM=0.4, Seasonal=0.6", "Output_Measure": "Optimal WAPE", "Output_Value": "0.0891", "Risk_Measure": "Pure GBM WAPE", "Risk_Value": "0.1172"},
        {"Project": "P2: FP&A Rolling Forecast", "Simulation_Type": "Monte Carlo (5,000 runs)", "Scenario_Name": "Revenue Trajectory Corridor", "Key_Input": "Macro Noise + Driver Vol", "Output_Measure": "Median Revenue", "Output_Value": "$247.38M", "Risk_Measure": "P05 Downside Floor", "Risk_Value": "$241.91M (VaR $5.71M)"},
        
        # P3
        {"Project": "P3: Liquidity Stress", "Simulation_Type": "Rolling 30-Day Window", "Scenario_Name": "Base Case (p50)", "Key_Input": "Current Buffer=2886.2", "Output_Measure": "Median Coverage", "Output_Value": "1.06", "Risk_Measure": "Breach Rate", "Risk_Value": "0.0% (31d Survival)"},
        {"Project": "P3: Liquidity Stress", "Simulation_Type": "Rolling 30-Day Window", "Scenario_Name": "Mild Stress (+25% 10d)", "Key_Input": "Current Buffer=2886.2", "Output_Measure": "Median Coverage", "Output_Value": "0.97", "Risk_Measure": "Breach Rate", "Risk_Value": "79.3% (29d Survival)"},
        {"Project": "P3: Liquidity Stress", "Simulation_Type": "Rolling 30-Day Window", "Scenario_Name": "Severe Stress (p95 x1.4 10d)", "Key_Input": "Current Buffer=2886.2", "Output_Measure": "Median Coverage", "Output_Value": "0.78", "Risk_Measure": "Breach Rate", "Risk_Value": "100.0% (22d Survival)"},
        {"Project": "P3: Liquidity Stress", "Simulation_Type": "Reverse Stress", "Scenario_Name": "Zero-Breach Buffer Sizing", "Key_Input": "Severe Stress Path", "Output_Measure": "Required Buffer", "Output_Value": "3,914.8 units", "Risk_Measure": "Buffer Shortfall", "Risk_Value": "+1,028.6 units (+35.6%)"},
        {"Project": "P3: Liquidity Stress", "Simulation_Type": "Monte Carlo (5,000 runs)", "Scenario_Name": "30-Day Outflow Distribution", "Key_Input": "Correlated Market Shock", "Output_Measure": "Stressed Median Outflow", "Output_Value": "3,335.1 units", "Risk_Measure": "Stressed Breach Prob", "Risk_Value": "100.0%"},
        
        # P4
        {"Project": "P4: Reporting Data Quality", "Simulation_Type": "Defect Sensitivity", "Scenario_Name": "Magnitude Error Sizing x10", "Key_Input": "Decimal Offset x10", "Output_Measure": "IF Recall", "Output_Value": "88.2%", "Risk_Measure": "x2 Error Recall", "Risk_Value": "18.2%"},
        {"Project": "P4: Reporting Data Quality", "Simulation_Type": "Capacity Planning", "Scenario_Name": "3,000 Monthly Reviews", "Key_Input": "Capacity=3k, Cost=$35", "Output_Measure": "Breaks Captured", "Output_Value": "2,294 (99.1%)", "Risk_Measure": "Unreviewed Backlog", "Risk_Value": "27 rows"},
        {"Project": "P4: Reporting Data Quality", "Simulation_Type": "Monte Carlo (5,000 runs)", "Scenario_Name": "Daily Exception Queue Arrivals", "Key_Input": "Poisson Arrivals Vol=800", "Output_Measure": "Median Daily Flags", "Output_Value": "100 rows/day", "Risk_Measure": "P95 Peak SLA Load", "Risk_Value": "139 rows/day ($4,865/day)"}
    ]
    pd.DataFrame(sim_rows).to_csv(os.path.join(out_dir, "reports", "simulation_results.csv"), index=False)
    
    # 4. Build Consolidated reports/data_quality_findings.csv
    dq_rows = [
        {"Project": "P1: Budget Overrun", "Dataset_File": "data/synthetic/budget_checkpoints.csv", "Total_Rows": 3200, "Columns": 14, "Grain": "Budget Line - Mid-Year", "Missing_Values": 0, "Duplicates": 0, "Outlier_Issues": "Skewed non-labor contracts", "Class_Imbalance_Prevalence": "25.0% Overruns", "Leakage_Risk": "Zero (Mid-year cutoff)", "Synthetic_Mechanism": "Log-normal expenditure + variance shocks"},
        {"Project": "P2: FP&A Rolling Forecast", "Dataset_File": "data/synthetic/monthly_revenue.csv", "Total_Rows": 576, "Columns": 7, "Grain": "Business Unit - Month", "Missing_Values": 0, "Duplicates": 0, "Outlier_Issues": "Demand shock t=30 to 33 (-18%)", "Class_Imbalance_Prevalence": "Balanced 8 BUs x 72 Mos", "Leakage_Risk": "Zero (Strict rolling lag alignment)", "Synthetic_Mechanism": "Sinusoidal seasonality + trend + driver drift"},
        {"Project": "P3: Liquidity Stress", "Dataset_File": "data/synthetic/daily_outflow.csv", "Total_Rows": 1095, "Columns": 3, "Grain": "Daily Cash Ledger", "Missing_Values": 0, "Duplicates": 0, "Outlier_Issues": "Month-end settlement surge (+35%)", "Class_Imbalance_Prevalence": "100% Continuous Series", "Leakage_Risk": "Zero (Chronological 180d holdout)", "Synthetic_Mechanism": "AR(1) market stress + weekday/month-end multipliers"},
        {"Project": "P4: Reporting Data Quality", "Dataset_File": "data/synthetic/reporting_feed.csv", "Total_Rows": 24000, "Columns": 9, "Grain": "Journal Transaction Entry", "Missing_Values": 240, "Duplicates": 720, "Outlier_Issues": "720 magnitude x10 + 720 sign flips", "Class_Imbalance_Prevalence": "13.0% Injected Breaks (3,120 rows)", "Leakage_Risk": "Controlled (Holdout split 60/40)", "Synthetic_Mechanism": "Log-normal chart of accounts + injected corruption"}
    ]
    pd.DataFrame(dq_rows).to_csv(os.path.join(out_dir, "reports", "data_quality_findings.csv"), index=False)
    
    # 5. Copy charts to outputs/
    chart_copies = [
        (os.path.join(base_src, "ml-project-budget-overrun-early-warning", "reports", "feature_importance.png"), os.path.join(out_dir, "outputs", "p1_feature_importance.png")),
        (os.path.join(base_src, "ml-project-budget-overrun-early-warning", "reports", "simulation_distribution.png"), os.path.join(out_dir, "outputs", "p1_simulation_distribution.png")),
        (os.path.join(base_src, "ml-project-fpa-rolling-forecast-engine", "reports", "backtest_wape.png"), os.path.join(out_dir, "outputs", "p2_backtest_wape.png")),
        (os.path.join(base_src, "ml-project-fpa-rolling-forecast-engine", "reports", "simulation_distribution.png"), os.path.join(out_dir, "outputs", "p2_simulation_distribution.png")),
        (os.path.join(base_src, "ml-project-liquidity-stress-forecaster", "reports", "forecast_vs_actual.png"), os.path.join(out_dir, "outputs", "p3_forecast_vs_actual.png")),
        (os.path.join(base_src, "ml-project-liquidity-stress-forecaster", "reports", "liquidity_stress_simulation.png"), os.path.join(out_dir, "outputs", "p3_liquidity_stress_simulation.png")),
        (os.path.join(base_src, "ml-project-reporting-data-quality-anomaly-detector", "reports", "recall_by_break_type.png"), os.path.join(out_dir, "outputs", "p4_recall_by_break_type.png")),
        (os.path.join(base_src, "ml-project-reporting-data-quality-anomaly-detector", "reports", "anomaly_detection_simulation.png"), os.path.join(out_dir, "outputs", "p4_anomaly_detection_simulation.png"))
    ]
    for src_f, dst_f in chart_copies:
        if os.path.exists(src_f):
            shutil.copyfile(src_f, dst_f)
            print(f"Copied {os.path.basename(src_f)} to outputs/")
            
    # 6. Generate outputs/ JSON contracts for local HTML consumption
    # Portfolio Summary JSON
    port_summary = {
        "portfolio_name": "Top 1% Master Quantitative Finance Analytics Suite",
        "author": "Bhupesh Chandra Dimri",
        "email": "bhupesh7cd@gmail.com",
        "github_org": "https://github.com/bhupesh-debug",
        "hub_repo": "https://github.com/bhupesh-debug/ml-portfolio-finance-analytics-hub",
        "total_projects": 4,
        "total_annual_quantified_benefit": "$12,012,500",
        "total_implementation_cost": "$990,000",
        "total_year1_net_benefit": "$10,777,500",
        "total_3year_npv": "$28,274,029",
        "average_payback_months": 1.1,
        "average_roi_3year": "2,856%",
        "projects": [
            {
                "id": "p1",
                "name": "Budget Overrun Early Warning",
                "domain": "FP&A / Cost Discipline",
                "folder": "ml-project-budget-overrun-early-warning",
                "html_link": "projects/budget-overrun.html",
                "github_url": "https://github.com/bhupesh-debug/ml-project-budget-overrun-early-warning",
                "baseline_name": "Spend-Burn Gap Heuristic",
                "baseline_metric": "ROC-AUC 0.686 / Recall@20% 35.5%",
                "champion_name": "Logistic Regression Scorecard",
                "champion_metric": "ROC-AUC 0.906 / Recall@20% 62.1%",
                "annual_benefit": "$3,070,000",
                "year1_net": "$2,770,000",
                "payback_months": 1.4,
                "npv_3yr": "$7,245,424",
                "readiness": "85% (Immediate Pilot)"
            },
            {
                "id": "p2",
                "name": "FP&A Rolling Forecast Engine",
                "domain": "FP&A / Commercial Revenue",
                "folder": "ml-project-fpa-rolling-forecast-engine",
                "html_link": "projects/fpa-forecast.html",
                "github_url": "https://github.com/bhupesh-debug/ml-project-fpa-rolling-forecast-engine",
                "baseline_name": "Seasonal Naive Run-Rate",
                "baseline_metric": "1m WAPE 0.105 (Bias -10.4%)",
                "champion_name": "Driver GBM + Hybrid Horizon Blend",
                "champion_metric": "1m WAPE 0.061 / 3m WAPE 0.089",
                "annual_benefit": "$3,070,000",
                "year1_net": "$2,770,000",
                "payback_months": 1.0,
                "npv_3yr": "$7,245,424",
                "readiness": "80% (Shadow Run)"
            },
            {
                "id": "p3",
                "name": "Liquidity Stress Forecaster",
                "domain": "Treasury / Liquidity Solvency",
                "folder": "ml-project-liquidity-stress-forecaster",
                "html_link": "projects/liquidity-stress.html",
                "github_url": "https://github.com/bhupesh-debug/ml-project-liquidity-stress-forecaster",
                "baseline_name": "28-Day Rolling Mean / Lag 7",
                "baseline_metric": "28d Mean 0.379 WAPE / Lag 7 0.105 WAPE",
                "champion_name": "Quantile HistGBM + Conformal Calibration",
                "champion_metric": "WAPE 0.073 / 94.4% Calibrated Tail Coverage",
                "annual_benefit": "$3,362,500",
                "year1_net": "$3,037,500",
                "payback_months": 0.9,
                "npv_3yr": "$7,940,394",
                "readiness": "75% (ALCO Operational Use)"
            },
            {
                "id": "p4",
                "name": "Reporting Data-Quality Anomaly Detector",
                "domain": "Accounting / SOX ICFR Governance",
                "folder": "ml-project-reporting-data-quality-anomaly-detector",
                "html_link": "projects/data-quality.html",
                "github_url": "https://github.com/bhupesh-debug/ml-project-reporting-data-quality-anomaly-detector",
                "baseline_name": "Static Control Rules",
                "baseline_metric": "Recall 54.6% (Sign Flips Missed at 0%)",
                "champion_name": "Enhanced Rules (Contra) + Isolation Forest",
                "champion_metric": "Recall 93.7% (Sign Flips Captured at 80.9%)",
                "annual_benefit": "$2,510,000",
                "year1_net": "$2,200,000",
                "payback_months": 1.2,
                "npv_3yr": "$5,842,787",
                "readiness": "70% (Upstream Mapping Needed)"
            }
        ]
    }
    
    with open(os.path.join(out_dir, "outputs", "portfolio_summary.json"), "w") as f:
        json.dump(port_summary, f, indent=2)
    with open(os.path.join(out_dir, "outputs", "budget_overrun_data.json"), "w") as f:
        json.dump(p1_data, f, indent=2)
    with open(os.path.join(out_dir, "outputs", "fpa_forecast_data.json"), "w") as f:
        json.dump(p2_data, f, indent=2)
    with open(os.path.join(out_dir, "outputs", "liquidity_stress_data.json"), "w") as f:
        json.dump(p3_data, f, indent=2)
    with open(os.path.join(out_dir, "outputs", "data_quality_data.json"), "w") as f:
        json.dump(p4_data, f, indent=2)
        
    print("=== Consolidated Reports, CSVs, Outputs, and JSON Contracts Successfully Generated ===")

if __name__ == "__main__":
    run_portfolio_analysis()
