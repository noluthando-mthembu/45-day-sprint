# Support Request Data Cleaner App

A defensive Python application built for Windows 11 that cleans customer support ticket CSV files by flagging duplicate ticket identifiers, missing values, and malformed rows.

---

## Key Features

* **Dual Interface (Single File):** Features an interactive Terminal CLI mode and a Desktop GUI App.
* **CSV Data Processing:** Utilises csv.DictReader and csv.DictWriter to process tabular ticket data.
* **Defensive Exception Handling:** Traps FileNotFoundError and empty file exceptions with traceback messages read from the bottom upwards.
* **Clean Output & Error Logging:** Generates clean_support_requests.csv for valid records and error_report.csv for flagged defects.
* **Full Variable Naming:** Written without shortcuts using full variable names (ticket_identifier, customer_name, issue_description, priority_level).

---

## File Overview

* **Script File:** support_cleaner.py
* **Input CSV File:** support_requests.csv
* **Clean CSV Output:** clean_support_requests.csv
* **Error CSV Output:** error_report.csv

---

## How to Run on Windows 11

1. Open VS Code terminal and navigate to folder:
   cd budget_project\support_cleaner

2. Run application:
   python support_cleaner.py

3. Select 1 for Terminal CLI Mode or 2 for Desktop GUI Mode.