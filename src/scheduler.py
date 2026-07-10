# scheduler.py

import os
import sys
import subprocess

from config import BASE_DIR


# --------------------------------------------------
# Convert AM/PM to 24-Hour Format
# --------------------------------------------------

def convert_time(schedule):

    schedule = schedule.strip().upper()

    time_part, ampm = schedule.split()

    hour, minute = map(int, time_part.split(":"))

    if ampm == "PM" and hour != 12:
        hour += 12

    if ampm == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"


# --------------------------------------------------
# Create Windows Task
# --------------------------------------------------

def create_schedule(job_name, schedule):

    python_path = sys.executable

    auto_run = os.path.join(BASE_DIR, "src", "auto_run.py")

    schedule_time = convert_time(schedule)

    task_name = f"EmployeeAutomation_{job_name}"

    command = [

        "schtasks",

        "/create",

        "/f",

        "/sc", "daily",

        "/tn", task_name,

        "/tr",

        f'"{python_path}" "{auto_run}" "{job_name}"',

        "/st",

        schedule_time

    ]

    result = subprocess.run(

    command,

    capture_output=True,

    text=True

    )

    if result.returncode == 0:

        print("\nAutomation Created Successfully")

        print(f"Task Name : {task_name}")

    else:

        print("\nFailed To Create Automation")

        print(result.stderr)


# --------------------------------------------------
# Delete Task
# --------------------------------------------------

def delete_schedule(job_name):

    task_name = f"EmployeeAutomation_{job_name}"

    subprocess.run(

        [

            "schtasks",

            "/delete",

            "/tn",

            task_name,

            "/f"

        ],

        shell=True

    )

    print("\nAutomation Deleted")


# --------------------------------------------------
# Show Tasks
# --------------------------------------------------

def show_tasks():

    subprocess.run(

        [

            "schtasks",

            "/query",

            "/fo",

            "table"

        ],

        shell=True

    )