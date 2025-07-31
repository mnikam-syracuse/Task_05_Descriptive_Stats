# Task 05: Descriptive Statistics and LLM Interaction

## Overview
This project demonstrates how to use a small dataset and interact with a Large Language Model (LLM) such as ChatGPT to answer natural language questions about that dataset. The primary goal is to evaluate LLM performance on structured data and determine its ability to provide accurate insights.

## Objectives
- Perform descriptive statistics on a sample dataset.
- Use an LLM to answer natural language questions about the dataset.
- Validate the correctness of LLM responses.
- Document the process, successes, and failures.
- Provide visualizations based on the dataset.

## Visual Output
Here is an example visualization generated from the sample dataset:

![Goals by Player](images/goals_chart.png)

## Steps
1. Clean and preprocess the dataset  
   (Dataset is not included in this repository as per assignment instructions.)
2. Compute basic descriptive statistics using Python (Pandas).
3. Design prompts to interact with an LLM.
4. Record LLM responses and analyze their accuracy.
5. Summarize findings in report.md.

## Tools and Libraries
- Python 3.x
- Pandas
- Matplotlib
- OpenAI API (or similar for LLM)

## How to Run
Install dependencies:
```
pip install -r requirements.txt
```

Run the analysis script:
```
python analysis.py
```

This will:
- Print summary statistics
- Identify the top scorer
- Generate a visualization (saved as images/goals_chart.png)

## Dataset Policy
The dataset is not included in this repository as per assignment requirements.  
To test the scripts:
- Use your own dataset (e.g., sports data in CSV format).
- Update file paths in clean_data.py and analysis.py.

## Files in This Repository
- README.md – Project documentation  
- analysis.py – Generates descriptive statistics and visualization  
- clean_data.py – Cleans and preprocesses raw data  
- prompts.md – LLM prompts used  
- llm_responses.md – LLM answers and evaluations  
- report.md – Research report and insights  
- requirements.txt – Dependencies  
- images/goals_chart.png – Visualization output  
