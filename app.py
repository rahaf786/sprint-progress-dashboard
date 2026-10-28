
import streamlit as st
import pandas as pd
from pathlib import Path

# Set up the dashboard
st.set_page_config(
    page_title="Sprint Progress Dashboard",
    layout="wide"
)

st.title("Sprint Progress Dashboard")
st.write("Track sprint tasks, progress, and blockers.")
st.caption("Demo dashboard using sample hotel booking project data.")

# Load task data
file_path = Path(__file__).with_name("sprint_tasks.csv")
df = pd.read_csv(file_path)

# Calculate sprint metrics
total_tasks = len(df)
completed_tasks = (df["status"] == "Completed").sum()
blocked_tasks = (df["status"] == "Blocked").sum()

completion_rate = (
    completed_tasks / total_tasks * 100
    if total_tasks > 0 else 0
)

# Display metrics
st.subheader("Sprint Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Blocked", blocked_tasks)
col4.metric("Completion Rate", f"{completion_rate:.1f}%")

# Create a chart
st.subheader("Task Status Breakdown")

status_counts = (
    df["status"]
    .value_counts()
    .rename_axis("Status")
    .reset_index(name="Tasks")
)

st.bar_chart(status_counts, x="Status", y="Tasks")

# Display all sprint tasks
st.subheader("All Sprint Tasks")
st.dataframe(df)

# Display blocked tasks
st.subheader("Blocked Tasks")

blocked_df = df[df["status"] == "Blocked"]

if blocked_df.empty:
    st.success("No blocked tasks!")
else:
    st.warning("Some tasks need attention.")
    st.dataframe(blocked_df)

# Deadline tracking
st.subheader("Deadline Tracking")

# Convert deadlines into dates
df["due_date"] = pd.to_datetime(df["due_date"])

today = pd.Timestamp.today().normalize()

# Find overdue tasks that are not completed
overdue_tasks = df[
    (df["due_date"] < today) &
    (df["status"] != "Completed")
]

# Display overdue task count
st.metric("Overdue Tasks", len(overdue_tasks))

if overdue_tasks.empty:
    st.success("No overdue tasks!")
else:
    st.error("These tasks are past their deadlines:")
    st.dataframe(overdue_tasks)

# Interactive Task Filters
st.subheader("Filter Sprint Tasks")

# Create dropdown filters
selected_status = st.multiselect(
    "Filter by Status",
    options=sorted(df["status"].unique())
)

selected_priority = st.multiselect(
    "Filter by Priority",
    options=sorted(df["priority"].unique())
)

selected_member = st.multiselect(
    "Filter by Team Member",
    options=sorted(df["assigned_to"].unique())
)

# Start with all tasks
filtered_df = df.copy()

# Apply filters only when something is selected
if selected_status:
    filtered_df = filtered_df[
        filtered_df["status"].isin(selected_status)
    ]

if selected_priority:
    filtered_df = filtered_df[
        filtered_df["priority"].isin(selected_priority)
    ]

if selected_member:
    filtered_df = filtered_df[
        filtered_df["assigned_to"].isin(selected_member)
    ]

# Display filtered results
st.subheader("Filtered Task Results")

st.write(f"Showing {len(filtered_df)} tasks")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# AI-Assisted Sprint Summary
st.subheader("AI-Assisted Sprint Summary")

st.write(
    "Generate a sprint report using ChatGPT."
)

# Prepare task information for the AI
task_data = df[
    ["task_name", "assigned_to", "status", "priority", "due_date"]
].to_string(index=False)

# Create a prompt with sprint metrics
ai_prompt = f"""
You are a technical program manager.

Analyze the following sprint data and create
a professional weekly sprint progress report.

Sprint Metrics:
- Total Tasks: {total_tasks}
- Completed Tasks: {completed_tasks}
- Blocked Tasks: {blocked_tasks}
- Completion Rate: {completion_rate:.1f}%
- Overdue Tasks: {len(overdue_tasks)}

Task Details:
{task_data}

Create a report containing:
1. Sprint progress summary
2. Completed work
3. Current blockers
4. Overdue tasks
5. Recommended next steps

Keep the report concise and professional.
Do not invent missing information.
"""

# Display the generated prompt
st.write("Copy this prompt into ChatGPT:")

st.code(ai_prompt, language=None)

# Download the prompt if needed
st.download_button(
    label="Download Sprint Report Prompt",
    data=ai_prompt,
    file_name="sprint_report_prompt.txt",
    mime="text/plain"
)

# Download Sample Sprint Report
st.subheader("Download Sprint Report")

report_path = Path(__file__).with_name(
    "sample_sprint_report.md"
)

if report_path.exists():
    report_text = report_path.read_text(
        encoding="utf-8"
    )

    st.download_button(
        label="Download Sprint Report",
        data=report_text,
        file_name="sprint_progress_report.md",
        mime="text/markdown"
    )
else:
    st.warning("Please create sample_sprint_report.md first.")
