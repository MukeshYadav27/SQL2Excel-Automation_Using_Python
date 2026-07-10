# config.py

import os

# -----------------------------------
# SQL Server Configuration
# -----------------------------------

# Change these according to your SQL Server
SERVER = r"YOUR_SERVER_NAME"

DATABASE = "EmployeeDB1000"

DRIVER = "ODBC Driver 17 for SQL Server"

# -----------------------------------
# Project Paths (Automatic)
# -----------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

JOB_FOLDER = os.path.join(BASE_DIR, "jobs")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

SCREENSHOT_FOLDER = os.path.join(BASE_DIR, "screenshots")