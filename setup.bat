@echo off
title Employee Report Automation - Setup

echo ==========================================================
echo        EMPLOYEE REPORT AUTOMATION SYSTEM SETUP
echo ==========================================================
echo.

:: Check Python
python --version >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python 3.11 or later.
    pause
    exit
)

echo [OK] Python Found
echo.

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

echo.

:: Install Required Packages
echo Installing Required Packages...
pip install -r requirements.txt

echo.

:: Create Required Folders
echo Creating Project Folders...

if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist jobs mkdir jobs
if not exist screenshots mkdir screenshots

echo.

:: Create config.py if it doesn't exist
if not exist src\config.py (
    copy src\config_example.py src\config.py
    echo config.py created from config_example.py
)

echo.

echo ==========================================================
echo Setup Completed Successfully
echo ==========================================================
echo.
echo Next Steps:
echo.
echo 1. Open src\config.py
echo 2. Update SERVER and DATABASE values
echo 3. Save the file
echo 4. Run run.bat
echo.
pause