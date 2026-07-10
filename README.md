# 📊 Employee Report Automation System

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![SQL Server](https://img.shields.io/badge/SQL%20Server-SSMS-red)
![Windows](https://img.shields.io/badge/Windows-Task%20Scheduler-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Project Overview

The **Employee Report Automation System** is a Python-based automation project that connects to **Microsoft SQL Server (SSMS)**, executes SQL queries, generates formatted Excel reports, and automates report generation using **Windows Task Scheduler**.

Instead of manually opening SQL Server every day and exporting reports, the user creates an automation job once. The application automatically executes the SQL query at the scheduled time, generates an Excel report, stores it in the reports folder, writes logs, and displays a desktop notification.

---

# 🚀 Features

- ✅ SQL Server Integration
- ✅ Connect using **pyodbc**
- ✅ Display Database Tables
- ✅ Display Views
- ✅ Display Stored Procedures
- ✅ Display Functions
- ✅ Suggested SQL Queries
- ✅ Custom SQL Queries
- ✅ SQL Query Validation
- ✅ Excel Report Generation
- ✅ Professional Excel Formatting
- ✅ Multiple Automation Jobs
- ✅ Windows Task Scheduler Integration
- ✅ Desktop Notifications
- ✅ Logging
- ✅ JSON Job Configuration
- ✅ Modular Python Project
- ✅ GitHub Ready

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| SQL Server (SSMS) | Database |
| pyodbc | Database Connection |
| pandas | Data Processing |
| openpyxl | Excel Report Generation |
| plyer | Desktop Notifications |
| JSON | Store Automation Jobs |
| Windows Task Scheduler | Scheduling |

---

# 📁 Folder Structure

```text
Employee_Automation_Project
│
├── src/
│   ├── main.py
│   ├── auto_run.py
│   ├── config.py
│   ├── config_example.py
│   ├── database.py
│   ├── database_explorer.py
│   ├── query_manager.py
│   ├── query_executor.py
│   ├── report_generator.py
│   ├── scheduler.py
│   ├── settings_manager.py
│   ├── notifier.py
│   ├── logger.py
│   ├── utils.py
│
├── jobs/
├── reports/
├── logs/
├── sql/
├── screenshots/
├── docs/
│
├── README.md
├── requirements.txt
├── LICENSE
├── run.bat
├── setup.bat
├── install_requirements.bat
└── .gitignore
```

---

# ⚙ Prerequisites

Before running this project, install:

- Python 3.11 or later
- Microsoft SQL Server
- SQL Server Management Studio (SSMS)
- ODBC Driver 17 (or newer) for SQL Server

---

# 📥 Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Employee_Report_Automation_System.git
```

---

## Step 2

Open the project

```bash
cd Employee_Report_Automation_System
```

---

## Step 3

Install required packages

```bash
pip install -r requirements.txt
```

---

## Step 4

Open

```
src/config.py
```

Update

```python
SERVER = r"YOUR_SERVER_NAME"

DATABASE = "EmployeeDB1000"

DRIVER = "ODBC Driver 17 for SQL Server"
```

---

## Step 5

Run

```bash
python src/main.py
```

or

Double-click

```
run.bat
```

---

# 💻 How It Works

## Create Automation

```
Run main.py
```

↓

Display Database Objects

↓

Choose Suggested Query

OR

Write Custom Query

↓

Enter Job Name

↓

Enter Report Name

↓

Enter Automation Time

↓

Save Job

↓

Windows Task Scheduler Created

↓

Exit

---

## At Scheduled Time

Windows Task Scheduler

↓

Runs auto_run.py

↓

Loads Job Configuration

↓

Connects SQL Server

↓

Executes SQL Query

↓

Generates Excel Report

↓

Stores Report in reports/

↓

Writes Log

↓

Displays Desktop Notification

↓

Shows Report Location

---

# 📄 Example Excel Report

```
reports/

Attendance_Report_2026-07-11_11-50-00.xlsx
```

---

# 📝 Logging

Logs are stored inside

```
logs/

automation.log
```

Example

```
[2026-07-11 11:50:00] Attendance Started

[2026-07-11 11:50:03] Excel Generated

[2026-07-11 11:50:05] Notification Sent
```

---

# 🖼 Screenshots

Add screenshots here

- Home Screen

- Database Objects

- Query Selection

- Excel Report

- Notification

- Windows Task Scheduler

---

# 📂 SQL Scripts

Inside

```
sql/
```

- CreateTables.sql
- InsertData.sql
- SampleQueries.sql

---

# 🛡 Error Handling

The application handles:

- Database Connection Errors
- Invalid SQL Queries
- Missing Tables
- Missing Jobs
- Invalid Time Format
- Windows Task Scheduler Errors
- Excel Generation Errors

---

# 📈 Future Enhancements

- Email Reports
- PDF Report Generation
- Charts
- Dashboard
- REST API
- Flask / Django Web Version
- User Login System
- Cloud Database Support

---

# 👨‍💻 Author

** P.MUKESH **
---

# ⭐ If you like this project

Please ⭐ Star this repository.

---

# 📜 License

This project is licensed under the **MIT License**.
