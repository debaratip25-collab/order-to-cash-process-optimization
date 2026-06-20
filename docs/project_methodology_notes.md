# Project Methodology Notes

## Step-by-Step Process Followed

### Step 1 — Define the Process and Build a Process Charter
Selected the Order-to-Cash (O2C) process as the subject of analysis because it spans nearly every department in an e-commerce business (Sales, Warehouse, Logistics, Finance, Customer Service, IT/Systems) and is a process every retail/e-commerce stakeholder can recognize. A Process Charter was drafted to fix scope, ownership, stakeholders, objectives, pain points, and success criteria before any data was collected. See `Process_Charter` sheet in the workbook.

### Step 2 — SIPOC Analysis
Before mapping the detailed flow, a SIPOC (Suppliers-Inputs-Process-Outputs-Customers) table was built to confirm the process boundary and the parties involved at each of the 9 high-level stages. See `SIPOC_Analysis` sheet and `process_maps/sipoc_map.png`.

### Step 3 — As-Is Process Mapping
The current-state workflow was mapped as a 12-node flowchart from Order Placement through Returns/Refund, with each node carrying a short annotation describing how the step is currently performed. Five nodes were flagged in red as likely bottlenecks based on initial stakeholder interviews (simulated for this case study) before the data confirmed it. See `process_maps/as_is_process_map.png`.

### Step 4 — Data Collection
A 130-record dataset was constructed to represent system-of-record exports (ERP/CRM/ticketing logs) across the 19 activities that make up the O2C process. Each record captures: Process ID, Process Name, Department, Process Owner, Activity Name, start/end timestamps, duration, resource assigned, task volume, tasks completed, error count, rework count, waiting time, approval time, process cost, SLA target, SLA achieved (Yes/No), customer complaint count, process status, and a mapped improvement opportunity. Distributions were deliberately built so that approval-heavy and waiting-heavy steps (Order Approval, Invoice Approval, Credit Check, Refund Processing, Courier Pickup) show materially worse SLA achievement — mirroring a realistic pattern of where manual processes break down. See `data/process_dataset_raw.csv`.

### Step 5 — KPI Analysis
Nine KPIs were calculated per activity, per department, and at the overall process level, using live Excel formulas (`AVERAGEIF`, `SUMIF`, `COUNTIFS`) referencing the raw dataset directly — not hardcoded values. This means the entire workbook recalculates automatically if the underlying dataset is updated. See `KPI_Analysis` and `Department_Performance` sheets.

### Step 6 — Bottleneck & Root Cause Analysis
All 19 activities were ranked by a weighted composite score: 40% average cycle time, 30% total cost, 15% error rate, 15% rework rate. Each of the top-ranked activities was paired with a root-cause hypothesis grounded in the nature of the step (e.g., "single approver dependency," "manual bank-statement matching"). See `Bottleneck_Analysis` sheet.

### Step 7 — To-Be Process Design
For each bottleneck, a corresponding automation or delegation lever was identified — RPA, API integration, auto-approval thresholds, real-time system sync, or self-service portals — and mapped back onto the same 12-node flowchart structure to produce a directly comparable To-Be process map. See `process_maps/to_be_process_map.png`.

### Step 8 — Impact Measurement (As-Is vs To-Be)
Projected To-Be values were modeled as percentage reductions/increases against the As-Is baseline (e.g., 45% cycle-time reduction, 25% cost reduction), informed by typical outcomes reported for comparable BPM/RPA initiatives. All comparisons and the annualized savings estimate are computed with live formulas referencing the KPI_Analysis summary row, so changing any assumption (e.g., monthly order volume) recalculates the savings estimate automatically. See `AsIs_vs_ToBe` sheet.

### Step 9 — Improvement Opportunity Matrix
All 19 improvement opportunities were scored on Impact (1–5) and Effort (1–5) and classified into Quick Win / Major Project / Fill-In / Reconsider quadrants using an Excel formula, then plotted as a scatter chart. See `Improvement_Opportunity_Matrix` sheet.

### Step 10 — Dashboard & Final Report
An executive dashboard was built as the first sheet of the workbook, combining KPI cards, six charts, a prioritized recommendations panel, and a filters/slicer guidance note for converting the static dashboard into a live PivotTable-driven one. The findings were then packaged into an 11-page Word recommendation report (cover page, table of contents, executive summary, process overview, KPI baseline, bottleneck analysis, To-Be design, KPI improvements/ROI, recommendations, dashboard preview, project facts, conclusion, and a KPI-definitions appendix).

## Notes on Reproducibility

- The dataset generation script uses a fixed random seed (42), so re-running it reproduces the exact same 130 records.
- All KPI, department, bottleneck, and As-Is/To-Be sheets use Excel formulas referencing `Raw_Dataset` directly; replacing the raw data with a real operational export and keeping the same column headers will cause the entire workbook to recalculate without any further changes.
- The workbook was validated with a formula-recalculation check confirming zero formula errors across 524 formulas.
