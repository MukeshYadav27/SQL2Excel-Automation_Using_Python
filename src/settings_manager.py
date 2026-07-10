# settings_manager.py

import json
import os

from config import JOB_FOLDER

# ---------------------------------------------
# Create Jobs Folder
# ---------------------------------------------

from config import BASE_DIR, JOB_FOLDER

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(JOB_FOLDER, exist_ok=True)


# ---------------------------------------------
# Job File Path
# ---------------------------------------------

def get_job_path(job_name):

    return os.path.join(JOB_FOLDER, f"{job_name}.json")


# ---------------------------------------------
# Save Job
# ---------------------------------------------

def save_job(job_name, query, report_name, schedule):

    filepath = get_job_path(job_name)

    if os.path.exists(filepath):

        print("\nJob already exists.")

        choice = input("Overwrite (Y/N): ").upper()

        if choice != "Y":

            print("Job not saved.")

            return False

    job = {

        "job_name": job_name,

        "query": query,

        "report_name": report_name,

        "schedule": schedule

    }

    with open(filepath, "w") as file:

        json.dump(job, file, indent=4)

    print("\nJob Saved Successfully")

    return True


# ---------------------------------------------
# Load Job
# ---------------------------------------------

def load_job(job_name):

    filepath = get_job_path(job_name)

    if not os.path.exists(filepath):

        return None

    with open(filepath, "r") as file:

        return json.load(file)


# ---------------------------------------------
# Delete Job
# ---------------------------------------------

def delete_job(job_name):

    filepath = get_job_path(job_name)

    if os.path.exists(filepath):

        os.remove(filepath)

        print("Job Deleted Successfully")

    else:

        print("Job Not Found")


# ---------------------------------------------
# List Jobs
# ---------------------------------------------

def list_jobs():

    print("\n" + "="*60)

    print("AVAILABLE AUTOMATION JOBS")

    print("="*60)

    files = [

        file for file in os.listdir(JOB_FOLDER)

        if file.endswith(".json")

    ]

    if len(files) == 0:

        print("No Jobs Found")

        return

    for i, file in enumerate(files, start=1):

        print(f"{i}. {file.replace('.json','')}")


# ---------------------------------------------
# View Job Details
# ---------------------------------------------

def view_job(job_name):

    job = load_job(job_name)

    if job is None:

        print("Job Not Found")

        return

    print("\n" + "="*60)

    print("JOB DETAILS")

    print("="*60)

    print(f"Job Name    : {job['job_name']}")

    print(f"Report Name : {job['report_name']}")

    print(f"Schedule    : {job['schedule']}")

    print(f"Query")

    print(job['query'])