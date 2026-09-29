# Data Cleaning & Reporting Automation

## Overview

This project automates the process of cleaning sales data and generating a summary report using Python. It handles missing values, duplicate records, inconsistent text values, data type conversion, and calculates total sales automatically.

The project also generates an Excel report and a sales visualization to make the cleaned data easier to analyze.

## Objectives

* Clean raw sales data automatically
* Handle missing values
* Remove duplicate records
* Standardize inconsistent categories and regions
* Convert data into appropriate data types
* Calculate total sales
* Generate an automated Excel report
* Generate a visual sales summary

## Technologies Used

* Python
* Pandas
* Matplotlib
* OpenPyXL
* CSV
* Excel

## Project Structure

```text
thiranex-task-04-data-cleaning-reporting/
│
├── data/
│   └── raw_sales_data.csv
│
├── output/
│   ├── cleaned_sales_data.csv
│   ├── sales_report.xlsx
│   └── sales_by_region.png
│
├── main.py
├── requirements.txt
└── README.md
```

## Data Cleaning Operations

The automation performs the following operations:

1. Loads the raw CSV dataset.
2. Removes duplicate records.
3. Removes unnecessary spaces from text fields.
4. Standardizes category and region names.
5. Handles missing customer names.
6. Handles missing quantity values.
7. Handles missing price values using the median price.
8. Converts the date column into a proper date format.
9. Calculates total sales using quantity × price.
10. Saves the cleaned dataset.

## Reporting

The program automatically creates an Excel report containing:

* Cleaned Data
* Summary
* Region Report

It also generates a bar chart showing total sales by region.

## How to Run

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the automation

```bash
python main.py
```

## Expected Output

After successful execution, the `output` folder contains:

* `cleaned_sales_data.csv`
* `sales_report.xlsx`
* `sales_by_region.png`

## Result

The automation successfully cleans the input sales dataset and produces structured reporting outputs. This reduces manual data preparation and improves the efficiency and consistency of the reporting workflow.
