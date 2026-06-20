import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# ----------------------------------------------------------------------
# Business Process Mapping & Optimization Case Study
# Process under study: ORDER-TO-CASH (O2C) — e-commerce retail company
# ----------------------------------------------------------------------

departments = ["Sales", "Warehouse", "Logistics", "Finance", "Customer Service", "IT/Systems"]

dept_owners = {
    "Sales": ["Anita Sharma", "Rohan Mehta"],
    "Warehouse": ["Suresh Iyer", "Vikram Nair"],
    "Logistics": ["Deepak Rao", "Kavita Joshi"],
    "Finance": ["Neha Kapoor", "Sanjay Gupta"],
    "Customer Service": ["Priya Singh", "Arjun Verma"],
    "IT/Systems": ["Manoj Pillai", "Ritu Bhatia"],
}

resources = ["Order Mgmt System", "Warehouse Staff", "Courier Partner", "Finance Team",
             "Customer Support Agent", "ERP System", "CRM System", "Billing System",
             "Picking Robot/Staff", "Quality Check Staff", "Dispatch Team", "Collections Team"]

# Activity Name : (Process Name, Department, base_duration_minutes, variability, base_cost_per_task,
#                   sla_target_minutes, error_prone, rework_prone, waiting_heavy, approval_heavy)
activities = [
    ("Order Placement",            "Order-to-Cash", "Sales",             5,   3,   2,    15,  False, False, False, False),
    ("Order Validation",           "Order-to-Cash", "Sales",             10,  5,   3,    20,  True,  False, False, False),
    ("Credit Check",               "Order-to-Cash", "Finance",           20,  10,  5,    30,  False, False, True,  True),
    ("Inventory Allocation",       "Order-to-Cash", "Warehouse",         15,  8,   4,    25,  True,  True,  False, False),
    ("Order Approval",             "Order-to-Cash", "Sales",             30,  20,  3,    20,  False, False, True,  True),
    ("Picking",                    "Order-to-Cash", "Warehouse",         25,  10,  6,    30,  True,  True,  False, False),
    ("Packing",                    "Order-to-Cash", "Warehouse",         15,  6,   5,    20,  False, True,  False, False),
    ("Quality Check",              "Order-to-Cash", "Warehouse",         10,  5,   4,    15,  True,  True,  False, False),
    ("Dispatch Scheduling",        "Order-to-Cash", "Logistics",         20,  10,  4,    25,  False, False, True,  False),
    ("Courier Pickup",             "Order-to-Cash", "Logistics",         45,  25,  8,    60,  False, False, True,  False),
    ("In-Transit Tracking Update", "Order-to-Cash", "Logistics",         10,  4,   3,    15,  True,  False, False, False),
    ("Last-Mile Delivery",         "Order-to-Cash", "Logistics",         180, 90,  15,   240, True,  True,  True,  False),
    ("Delivery Confirmation",      "Order-to-Cash", "Customer Service",  8,   4,   2,    15,  False, False, False, False),
    ("Invoice Generation",         "Order-to-Cash", "Finance",           12,  6,   3,    15,  True,  True,  False, False),
    ("Invoice Approval",           "Order-to-Cash", "Finance",           25,  15,  3,    20,  False, False, True,  True),
    ("Payment Processing",         "Order-to-Cash", "Finance",           18,  9,   4,    25,  True,  True,  False, False),
    ("Payment Reconciliation",     "Order-to-Cash", "Finance",           22,  10,  5,    30,  True,  True,  False, False),
    ("Customer Query Handling",    "Order-to-Cash", "Customer Service",  15,  10,  4,    20,  False, True,  True,  False),
    ("Returns Processing",         "Order-to-Cash", "Customer Service",  30,  20,  7,    40,  True,  True,  True,  False),
    ("Refund Processing",          "Order-to-Cash", "Finance",           20,  10,  5,    30,  False, True,  True,  True,  ),
]

statuses = ["Completed", "Completed", "Completed", "Delayed", "Delayed", "In Progress", "Escalated"]

improvement_lib = {
    "Order Validation": "Automate validation rules via RPA to reduce manual review time",
    "Credit Check": "Integrate real-time credit scoring API to remove manual waiting time",
    "Inventory Allocation": "Implement real-time inventory sync between CRM and ERP",
    "Order Approval": "Introduce auto-approval thresholds and delegation rules to cut approval delay",
    "Picking": "Deploy barcode/RFID-guided picking to reduce errors and rework",
    "Packing": "Standardize packing SOPs and add packing-station checklists",
    "Quality Check": "Add automated weight/dimension QC sensors to reduce manual QC errors",
    "Dispatch Scheduling": "Use route optimization software to auto-schedule dispatch",
    "Courier Pickup": "Negotiate fixed pickup windows with courier partners",
    "In-Transit Tracking Update": "Automate tracking updates via courier API webhook integration",
    "Last-Mile Delivery": "Partner with hyperlocal delivery fleet for high-density pin codes",
    "Delivery Confirmation": "Enable automated OTP/SMS-based delivery confirmation",
    "Invoice Generation": "Auto-generate invoices via ERP trigger on dispatch confirmation",
    "Invoice Approval": "Set auto-approval limits for invoices below threshold value",
    "Payment Processing": "Integrate automated payment gateway reconciliation",
    "Payment Reconciliation": "Use RPA bots for automated bank-statement matching",
    "Customer Query Handling": "Deploy chatbot for L1 query resolution to reduce queue time",
    "Returns Processing": "Simplify returns workflow with self-service return portal",
    "Refund Processing": "Automate refund triggers tied to return-approval status",
}

n_records = 130
records = []
start_date = datetime(2025, 1, 6)

for i in range(1, n_records + 1):
    act = random.choice(activities)
    (activity_name, process_name, dept, base_dur, var_dur, base_cost,
     sla_target, error_prone, rework_prone, waiting_heavy, approval_heavy) = act

    owner = random.choice(dept_owners[dept])
    resource = random.choice(resources)

    day_offset = random.randint(0, 119)
    start_dt = start_date + timedelta(days=day_offset, hours=random.randint(8, 17), minutes=random.randint(0, 59))

    duration = max(2, int(np.random.normal(base_dur, var_dur)))
    waiting_time = int(np.random.exponential(25 if waiting_heavy else 6))
    waiting_time = min(waiting_time, 240)
    approval_time = int(np.random.exponential(20 if approval_heavy else 3)) if approval_heavy or random.random() < 0.15 else int(np.random.exponential(3))
    approval_time = min(approval_time, 180)

    end_dt = start_dt + timedelta(minutes=duration + waiting_time + approval_time)

    task_volume = random.randint(20, 200)
    error_rate_base = 0.12 if error_prone else 0.03
    error_count = int(np.random.binomial(task_volume, error_rate_base))
    rework_rate_base = 0.10 if rework_prone else 0.02
    rework_count = int(np.random.binomial(task_volume, rework_rate_base))

    completion_rate = np.random.uniform(0.88, 1.0)
    tasks_completed = int(task_volume * completion_rate)

    cost_per_task = round(base_cost + np.random.uniform(-0.5, 1.5), 2)
    process_cost = round(cost_per_task * task_volume, 2)

    sla_achieved_minutes = duration + waiting_time + approval_time
    sla_met = "Yes" if sla_achieved_minutes <= sla_target * 1.1 else "No"

    complaint_base = 0.06 if (waiting_heavy or error_prone) else 0.015
    complaint_count = int(np.random.binomial(task_volume, complaint_base))

    if sla_met == "No" and random.random() < 0.4:
        status = "Delayed"
    elif rework_count > task_volume * 0.15:
        status = "Escalated"
    elif random.random() < 0.05:
        status = "In Progress"
    else:
        status = "Completed"

    improvement = improvement_lib.get(activity_name, "Review process for automation opportunity")

    records.append({
        "Process ID": f"PROC-{i:04d}",
        "Process Name": process_name,
        "Department": dept,
        "Process Owner": owner,
        "Activity Name": activity_name,
        "Activity Start Time": start_dt.strftime("%Y-%m-%d %H:%M"),
        "Activity End Time": end_dt.strftime("%Y-%m-%d %H:%M"),
        "Activity Duration (mins)": duration,
        "Resource Assigned": resource,
        "Task Volume": task_volume,
        "Tasks Completed": tasks_completed,
        "Error Count": error_count,
        "Rework Count": rework_count,
        "Waiting Time (mins)": waiting_time,
        "Approval Time (mins)": approval_time,
        "Process Cost ($)": process_cost,
        "SLA Target (mins)": sla_target,
        "SLA Achieved": sla_met,
        "Customer Complaint Count": complaint_count,
        "Process Status": status,
        "Improvement Opportunity": improvement,
    })

df = pd.DataFrame(records)
df.to_csv("/home/claude/project/data/process_dataset_raw.csv", index=False)
print(df.shape)
print(df.head(3).to_string())
print(df["Activity Name"].value_counts())
