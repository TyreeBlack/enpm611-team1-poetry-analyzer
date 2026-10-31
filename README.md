# Poetry Issue Analyzer

## Project Description

The Poetry Issue Analyzer is a Python application that analyzes GitHub issues from the Poetry project. It processes issue data and provides summaries and visualizations to help understand issue activity.

## Features

### Feature 1: Issue Overview
- Displays the total number of issues.
- Shows the number of open and closed issues.
- Identifies the top 10 issue creators.
- Identifies the most common issue labels.

### Feature 2: Issue Creation Trends
- Analyzes issue creation activity over time.
- Groups issues by month and year.
- Generates a line chart showing the number of issues created each month.

## Requirements

- Python 3
- Matplotlib

## Running the Application

1. Clone or download the project repository.
2. Open a terminal in the project directory.
3. Make sure the required Python dependencies are installed.
4. Run the desired feature using the following commands:

**Feature 1:**
```bash
python run.py --feature 1
```

**Feature 2:**
```bash
python run.py --feature 2
```

The application loads issue data from `poetry_issues.json` and executes the selected analysis.

## Data Source

The application uses GitHub issue data from the Poetry project, stored in `poetry_issues.json`.
