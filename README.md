
# AI-Assisted Sprint Progress Dashboard

A Python-based dashboard designed to help software development
teams monitor Agile sprint progress, identify blockers, track
deadlines, and prepare AI-assisted progress reports.

## Project Overview

Managing sprint progress often requires manually reviewing
tasks, checking deadlines, and preparing status reports.

This project explores how data analytics and AI-assisted
workflows can simplify sprint tracking and reporting.

## Features

- Sprint progress metrics and completion rates
- Task status visualization
- Automatic overdue task detection
- Blocked task identification
- Interactive filters for status, priority, and team members
- AI-assisted sprint report prompts
- Downloadable sample progress reports

## Technologies Used

- Python
- Pandas
- Streamlit
- Git and GitHub
- ChatGPT (manual AI-assisted reporting)

## How It Works

1. Loads sample sprint task data from a CSV file.
2. Uses Pandas to calculate completion rates and task metrics.
3. Displays interactive charts and tables with Streamlit.
4. Identifies blocked and overdue tasks.
5. Generates a structured prompt for an AI-assisted report.
6. Allows users to download a sample progress report.

## Running Locally

Install the required packages:

    pip install pandas streamlit

Run the application:

    streamlit run app.py

Open the local URL displayed in the terminal.

## AI Integration

The current prototype creates structured report prompts
that can be copied into ChatGPT.

AI report generation is currently a manual step, not
an automated API integration.

## Data

This project uses fictional demonstration task data
inspired by an Agile hotel booking application.

No real customer or private team data is included.

## Future Improvements

- Connect to GitHub and Linear APIs
- Automate AI-generated progress summaries
- Add historical sprint performance tracking
- Measure reporting time saved
- Improve dashboard usability through user feedback

## Project Purpose

This project demonstrates Python programming, data
analysis, workflow improvement, Agile project tracking,
and AI-assisted reporting.
