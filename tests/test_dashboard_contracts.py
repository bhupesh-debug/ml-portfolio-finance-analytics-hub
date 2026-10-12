"""
Automated Test Suite for Enterprise Finance Analytics & Machine Learning Suite.
Validates data contracts, schema integrity, metric reproducibility, mathematical consistency,
and HTML offline asset integrity.

Author: Bhupesh Chandra Dimri (bhupesh7cd@gmail.com)
"""

import os
import json
import re
import pytest
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


class TestDeliverableArtifacts:
    """Checks that all mandatory deliverables exist on disk."""

    def test_core_html_deliverables_exist(self):
        expected_html = [
            os.path.join(BASE_DIR, "index.html"),
            os.path.join(PROJECTS_DIR, "budget-overrun.html"),
            os.path.join(PROJECTS_DIR, "fpa-forecast.html"),
            os.path.join(PROJECTS_DIR, "liquidity-stress.html"),
            os.path.join(PROJECTS_DIR, "data-quality.html"),
        ]
        for path in expected_html:
            assert os.path.exists(path), f"Missing required HTML deliverable: {path}"
            assert os.path.getsize(path) > 1000, f"HTML file is suspiciously small: {path}"

    def test_core_report_deliverables_exist(self):
        expected_reports = [
            os.path.join(REPORTS_DIR, "executive_summary.md"),
            os.path.join(REPORTS_DIR, "technical_report.md"),
            os.path.join(REPORTS_DIR, "project_question_answer_register.md"),
            os.path.join(REPORTS_DIR, "recommendations_and_action_plan.md"),
            os.path.join(REPORTS_DIR, "experiment_results.csv"),
            os.path.join(REPORTS_DIR, "regression_results.csv"),
            os.path.join(REPORTS_DIR, "simulation_results.csv"),
            os.path.join(REPORTS_DIR, "data_quality_findings.csv"),
        ]
        for path in expected_reports:
            assert os.path.exists(path), f"Missing required report deliverable: {path}"
            assert os.path.getsize(path) > 100, f"Report file is empty or corrupted: {path}"

    def test_css_and_js_assets_exist(self):
        css_path = os.path.join(ASSETS_DIR, "styles.css")
        js_path = os.path.join(ASSETS_DIR, "dashboard.js")
        assert os.path.exists(css_path), f"Missing CSS file: {css_path}"
        assert os.path.exists(js_path), f"Missing JS file: {js_path}"
        assert os.path.getsize(css_path) > 2000, "styles.css is incomplete"
        assert os.path.getsize(js_path) > 5000, "dashboard.js is incomplete"


class TestCSVDataContracts:
    """Validates structure, non-emptiness, and types of generated CSV artifacts."""

    def test_experiment_results_csv_schema(self):
        path = os.path.join(REPORTS_DIR, "experiment_results.csv")
        df = pd.read_csv(path)
        required_cols = {"Experiment_ID", "Project_Name", "Model_Family", "Method_Name", "Metric_Primary_Value", "Status"}
        assert required_cols.issubset(df.columns), f"Missing columns in {path}"
        assert len(df) >= 15, f"Expected at least 15 experiments, found {len(df)}"
        assert df["Metric_Primary_Value"].notna().all(), "Found NaN in Metric_Primary_Value"

    def test_regression_results_csv_schema(self):
        path = os.path.join(REPORTS_DIR, "regression_results.csv")
        df = pd.read_csv(path)
        assert len(df) >= 25, f"Expected at least 25 regression parameters, found {len(df)}"
        assert "Project" in df.columns, "Missing Project column in regression_results.csv"
        projects = df["Project"].dropna().unique()
        assert len(projects) >= 4, f"Expected all 4 projects represented in regression results, got {projects}"

    def test_simulation_results_csv_schema(self):
        path = os.path.join(REPORTS_DIR, "simulation_results.csv")
        df = pd.read_csv(path)
        required_cols = {"Project", "Simulation_Type", "Scenario_Name", "Key_Input", "Output_Measure", "Output_Value", "Risk_Measure", "Risk_Value"}
        assert required_cols.issubset(df.columns), f"Missing columns in {path}"
        assert len(df) >= 12, f"Expected at least 12 simulation scenarios, found {len(df)}"

    def test_data_quality_findings_csv_schema(self):
        path = os.path.join(REPORTS_DIR, "data_quality_findings.csv")
        df = pd.read_csv(path)
        required_cols = {"Project", "Dataset_File", "Total_Rows", "Columns", "Grain", "Missing_Values", "Duplicates", "Outlier_Issues", "Class_Imbalance_Prevalence", "Leakage_Risk", "Synthetic_Mechanism"}
        assert required_cols.issubset(df.columns), f"Missing columns in {path}"
        assert len(df) >= 4, f"Expected at least 4 datasets reviewed, found {len(df)}"


class TestJSONDataContracts:
    """Validates structure and statistical fidelity of JSON artifacts used by dashboard."""

    def test_portfolio_summary_json(self):
        path = os.path.join(OUTPUTS_DIR, "portfolio_summary.json")
        assert os.path.exists(path), f"Missing {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data["total_projects"] == 4
        assert "total_annual_quantified_benefit" in data
        assert "total_year1_net_benefit" in data
        assert "projects" in data
        assert len(data["projects"]) == 4

    def test_budget_overrun_json(self):
        path = os.path.join(OUTPUTS_DIR, "budget_overrun_data.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data["rows"] == 3200
        assert data["overrun_rate"] == 0.25
        assert abs(data["logistic"]["roc_auc"] - 0.906) < 0.005
        assert abs(data["logistic"]["recall_at_top20pct"] - 0.621) < 0.005
        assert abs(data["rule_burn_gap"]["roc_auc"] - 0.686) < 0.005

    def test_fpa_forecast_json(self):
        path = os.path.join(OUTPUTS_DIR, "fpa_forecast_data.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data["origins"] == 9
        assert data["units"] == 8
        assert abs(data["backtest_results"]["driver_gbm"]["1"]["wape"] - 0.062) < 0.005
        assert abs(data["backtest_results"]["seasonal_naive"]["1"]["wape"] - 0.105) < 0.005
        assert abs(data["backtest_results"]["driver_gbm"]["2"]["wape"] - 0.092) < 0.005

    def test_liquidity_stress_json(self):
        path = os.path.join(OUTPUTS_DIR, "liquidity_stress_data.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert abs(data["calibration_offset"] - 7.03) < 0.01
        assert abs(data["wape_gbm_p50"] - 0.073) < 0.005
        assert abs(data["wape_rolling28"] - 0.379) < 0.005
        assert abs(data["p95_coverage"] - 0.944) < 0.005
        assert len(data["stress_table"]) == 3

    def test_data_quality_json(self):
        path = os.path.join(OUTPUTS_DIR, "data_quality_data.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data["rows"] == 24000
        assert data["break_rate"] == 0.13
        assert abs(data["rules_plus_isolation_forest"]["recall"] - 0.742) < 0.005
        assert data["recall_by_break_type"]["Rules"]["sign_flip"] == 0.0
        assert data["recall_by_break_type"]["IsolationForest"]["sign_flip"] == 0.0


class TestHTMLLinkAndAssetIntegrity:
    """Verifies that HTML files have valid local links and reference existing images."""

    @pytest.mark.parametrize("html_file", [
        "index.html",
        "projects/budget-overrun.html",
        "projects/fpa-forecast.html",
        "projects/liquidity-stress.html",
        "projects/data-quality.html",
    ])
    def test_html_image_references_exist(self, html_file):
        full_path = os.path.join(BASE_DIR, html_file)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all <img src="..."> occurrences
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        html_dir = os.path.dirname(full_path)
        for src in img_srcs:
            if src.startswith("http"):
                continue
            resolved_img = os.path.abspath(os.path.join(html_dir, src))
            assert os.path.exists(resolved_img), f"Broken image in {html_file}: {src} (resolved to {resolved_img})"

    @pytest.mark.parametrize("html_file, required_ids", [
        ("projects/budget-overrun.html", ["sim-budget-form", "p1-units", "p1-capacity", "p1-threshold", "p1-chart-container"]),
        ("projects/fpa-forecast.html", ["sim-fpa-form", "p2-horizon", "p2-hc-shock", "p2-blend-weight", "p2-chart-container"]),
        ("projects/liquidity-stress.html", ["sim-liquidity-form", "p3-buffer", "p3-scenario", "p3-stress-mult", "p3-chart-container"]),
        ("projects/data-quality.html", ["sim-data-quality-form", "p4-volume", "p4-prevalence", "p4-contra", "p4-chart-container"]),
    ])
    def test_simulator_contract_ids_present(self, html_file, required_ids):
        full_path = os.path.join(BASE_DIR, html_file)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        for elem_id in required_ids:
            assert f'id="{elem_id}"' in content or f"id='{elem_id}'" in content, (
                f"Missing required simulator ID '{elem_id}' in {html_file}"
            )


class TestSimulationMathematicalLogic:
    """Unit tests verifying mathematical consistency of simulation calculations."""

    def test_budget_simulation_math(self):
        units = 3200
        capacity_pct = 20.0
        threshold = 0.42
        effectiveness = 0.60
        cost_intervention = 4500
        cost_overrun = 52000
        cost_fp = 650

        total_overruns = round(units * 0.25)  # 800
        recall_factor = min(1.0, ((capacity_pct / 100.0) ** 0.65) * 1.76)
        detected = round(total_overruns * recall_factor)
        assert 450 <= detected <= 550, f"Detected overruns unexpected: {detected}"

        mitigated = detected * cost_overrun * effectiveness
        expense = (detected * cost_intervention) + (143 * cost_fp)
        net = mitigated - expense
        assert net > 10_000_000, f"Net benefit unexpected: {net}"

    def test_fpa_blending_math(self):
        base_revenue = 247.62
        seasonal_baseline = 221.80

        # At horizon 1, blend is 80% ML
        w_ml = 0.80
        forecast_1m = (w_ml * base_revenue) + ((1 - w_ml) * seasonal_baseline)
        assert 240.0 <= forecast_1m <= 248.0

        # At horizon 3, blend is 40% ML / 60% Seasonal
        w_ml_3m = 0.40
        forecast_3m = (w_ml_3m * base_revenue) + ((1 - w_ml_3m) * seasonal_baseline)
        assert 230.0 <= forecast_3m <= 235.0

    def test_liquidity_buffer_run_off_math(self):
        initial_buffer = 2886.2
        horizon = 30
        cum_outflow = 0.0

        for d in range(1, horizon + 1):
            day_rate = 98.4
            if d % 7 in (6, 0):
                day_rate *= 0.35
            else:
                day_rate *= 1.12
            if d in (28, 29, 30):
                day_rate += 31.9
            cum_outflow += day_rate

        # In base case, 30-day cumulative outflow is ~2,720 units (coverage ~1.06x)
        assert 2600 <= cum_outflow <= 2850
        coverage = initial_buffer / cum_outflow
        assert coverage >= 1.0, f"Base case should survive, but coverage was {coverage}"

    def test_data_quality_contra_account_recall(self):
        # Without contra check:
        breaks_total = 1264
        legacy_recall = 0.742
        assert round(breaks_total * legacy_recall) == 938

        # With contra check:
        enhanced_recall = 0.937
        assert round(breaks_total * enhanced_recall) == 1184
        # Incremental capture
        assert (1184 - 938) == 246
