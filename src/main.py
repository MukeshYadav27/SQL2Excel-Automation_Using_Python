# main.py

import os
import subprocess
import sys
from database_explorer import show_database_objects
from query_manager import get_query, validate_query
from settings_manager import (
    save_job,
    list_jobs,
    delete_job,
    view_job
)
from scheduler import (
    create_schedule,
    delete_schedule
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------
# Clear Screen
# ------------------------------------------

def clear():

    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------
# Run Job Immediately
# ------------------------------------------

def run_job():

    job = input("\nEnter Job Name : ").strip()

    auto_run = os.path.join(BASE_DIR, "src", "auto_run.py")

    subprocess.run(
        [
         sys.executable,
         auto_run,
        job
        ]
    )


# ------------------------------------------
# Create Automation
# ------------------------------------------

def create_job():

    clear()

    print("="*70)

    print("CREATE NEW AUTOMATION")

    print("="*70)

    show_database_objects()

    query = get_query()

    if not validate_query(query):

        input("\nPress Enter...")

        return

    job_name = input("\nJob Name : ").strip()

    report_name = input("Report Name : ").strip()

    schedule = input(

        "Automation Time (Example : 11:50 AM) : "

    ).upper()

    if save_job(

        job_name,

        query,

        report_name,

        schedule

    ):

        create_schedule(

            job_name,

            schedule

        )

        print("\nAutomation Created Successfully")

    input("\nPress Enter...")


# ------------------------------------------
# View Jobs
# ------------------------------------------

def view_jobs():

    clear()

    list_jobs()

    choice = input(

        "\nView Job Details (Y/N): "

    ).upper()

    if choice == "Y":

        job = input("Enter Job Name : ")

        view_job(job)

    input("\nPress Enter...")


# ------------------------------------------
# Delete Job
# ------------------------------------------

def remove_job():

    clear()

    list_jobs()

    job = input("\nJob Name : ")

    delete_job(job)

    delete_schedule(job)

    input("\nPress Enter...")

# ------------------------------------------
# Main Menu
# ------------------------------------------

def main():

    while True:

        clear()

        print("=" * 70)
        print(" EMPLOYEE REPORT AUTOMATION SYSTEM ")
        print("=" * 70)

        print("1. Create Automation")
        print("2. View Jobs")
        print("3. Run Job Now")
        print("4. Delete Job")
        print("5. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            create_job()

        elif choice == "2":
            view_jobs()

        elif choice == "3":
            run_job()

        elif choice == "4":
            remove_job()

        elif choice == "5":
            print("\nThank You")
            break

        else:
            print("\nInvalid Choice")
            input("\nPress Enter...")


if __name__ == "__main__":
    main()