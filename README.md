# Order-to-Cash Process Optimization

A complete, consulting-style Business Analyst case study: mapping a real-world Order-to-Cash workflow, quantifying its bottlenecks with a 130-record operational dataset, and designing an optimized "To-Be" process — backed by a live, formula-driven Excel dashboard and a full recommendation report.

## Business Problem

NorthBridge Retail's Order-to-Cash process — from order placement to payment reconciliation — averaged **37.6 minutes of cycle time** per task touchpoint, hit SLA targets only **48.8%** of the time, carried a **7.12% error rate**, and generated **$74,661** in tracked process cost across the sampled activities. Customer complaints clustered around returns, refunds, and delivery delays.

## What's Inside

- **130-record dataset** — 19 activities, 6 departments, 4 months of simulated operational data (cycle time, waiting time, approval time, cost, errors, rework, SLA, complaints)
- **9-sheet Excel workbook** — Dashboard, Raw Dataset, KPI Analysis, Department Performance, Bottleneck Analysis, As-Is vs To-Be, Improvement Opportunity Matrix, Process Charter, SIPOC — 524 live formulas, zero errors
- **As-Is and To-Be process maps** + SIPOC diagram
- **11-page recommendation report** (Word) — executive summary, root-cause analysis, ROI, prioritized recommendations
- **Power BI build guide** — DAX measures and report layout to rebuild the dashboard as a fully interactive model

## Methodology

Process Charter → SIPOC → As-Is Mapping → Data Collection → KPI Analysis → Bottleneck & Root Cause Analysis → To-Be Design → Impact Measurement → Improvement Opportunity Matrix (Impact vs Effort) → Dashboard & Reporting

## Key Findings

- **Picking, Courier Pickup, and Payment Reconciliation** are the highest-impact bottlenecks — driven by manual, single-point-of-failure steps, not task complexity
- **Approval-heavy steps** (Order Approval, Invoice Approval, Credit Check, Refund Processing) show 0–20% SLA achievement — the cheapest, fastest wins via auto-approval thresholds
- Projected optimization lifts SLA achievement from **48.8% → 85%+**, cuts cycle time by **~45%**, and reduces process cost by **25–35%**

## Tools Used

Excel (openpyxl-generated, formula-driven dashboard) · Python (pandas, dataset generation) · Power BI (DAX measures, interactive report) · Word (recommendation report)

## Repository Structure

```
order-to-cash-process-optimization/
├── README.md
├── data/
│   └── process_dataset_raw.csv
├── dashboard/
│   └── Business_Process_Case_Study_Workbook.xlsx
│   └── dashboard.pbix
├── process_maps/
│   ├── as_is_process_map.png
│   ├── to_be_process_map.png
│   └── sipoc_map.png
├── reports/
│   └── Business_Process_Optimization_Recommendation_Report.docx
├── screenshots/
│   └── excel_dashboard_1.png
│   └── excel_dashboard_2.png
│   └── excel_dashboard_3.png
│   └── power bi_dashboard_1.png
│   └── power bi_dashboard_2.png
│   └── power bi_dashboard_3.png
│   └── power bi_dashboard_4.png
├── scripts/
    └── generate_dataset.py

```

## Author

Debarati Pal

Business Analyst portfolio project — built as a practical, job-ready demonstration of process mapping, KPI analysis, and optimization consulting.
