# auto_run.py

import os
import sys
import traceback

from settings_manager import load_job
from query_executor import execute_query
from report_generator import generate_excel
from notifier import show_notification
from logger import write_log, log_error


def main():

    # ----------------------------------------
    # Set Project Directory
    # ----------------------------------------

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    os.chdir(BASE_DIR)

    print("=" * 70)
    print("      EMPLOYEE REPORT AUTOMATION SYSTEM")
    print("=" * 70)

    # ----------------------------------------
    # Get Job Name
    # ----------------------------------------

    if len(sys.argv) < 2:

        print("\nJob Name Missing!")

        print("\nUsage:")

        print("python auto_run.py Attendance")

        input("\nPress Enter To Exit...")

        return

    job_name = sys.argv[1]

    print(f"\nJob Name : {job_name}")

    # ----------------------------------------
    # Load Job
    # ----------------------------------------

    job = load_job(job_name)

    if job is None:

        print("\nJob Not Found!")

        input("\nPress Enter To Exit...")

        return

    query = job["query"]
    report_name = job["report_name"]
    schedule = job["schedule"]

    print("\nJob Loaded Successfully")

    write_log(f"{job_name} Started")

    # ----------------------------------------
    # Execute Query
    # ----------------------------------------

    try:

        print("\nConnecting to SQL Server...")

        df = execute_query(query)

        if df is None:

            write_log("Query Execution Failed")

            input("\nPress Enter To Exit...")

            return

        print(f"\nRows Retrieved : {len(df)}")

        # ----------------------------------------
        # Generate Excel
        # ----------------------------------------

        print("\nGenerating Excel Report...")

        excel_path = generate_excel(
            df,
            report_name
        )

        print("\nExcel Generated Successfully")

        print("\nExcel Location")

        print(excel_path)

        write_log(f"Excel Generated : {excel_path}")

        # ----------------------------------------
        # Desktop Notification
        # ----------------------------------------

        show_notification(

            "Employee Report Automation",

            f"{report_name} Generated Successfully"

        )

        print("\nDesktop Notification Sent")

        write_log("Notification Sent")

        print("\nAutomation Completed Successfully")

    except Exception as e:

        print("\nUnexpected Error\n")

        traceback.print_exc()

        log_error(str(e))

    print("\n" + "=" * 70)

    input("Press Enter To Close...")


# ----------------------------------------
# Program Entry Point
# ----------------------------------------

if __name__ == "__main__":
    main()