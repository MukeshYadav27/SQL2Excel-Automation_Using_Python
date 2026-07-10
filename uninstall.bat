@echo off
title Employee Report Automation - Uninstall

echo ================================================
echo     EMPLOYEE REPORT AUTOMATION CLEANUP
echo ================================================
echo.

echo Removing Windows Scheduled Tasks...

for /f "tokens=1" %%i in ('schtasks /query /fo csv ^| findstr /I "EmployeeAutomation_"') do (
    schtasks /delete /tn %%~i /f >nul 2>&1
)

echo.
echo Deleting Generated Reports...

if exist reports (
    del /q reports\*.* >nul 2>&1
)

echo.
echo Deleting Log Files...

if exist logs (
    del /q logs\*.* >nul 2>&1
)

echo.
echo Deleting Job Files...

if exist jobs (
    del /q jobs\*.json >nul 2>&1
)

echo.
echo Cleanup Completed Successfully.

echo.
echo Your source code has NOT been deleted.
echo Only generated files and scheduled tasks were removed.

pause