# database.py

import pyodbc
from config import SERVER, DATABASE, DRIVER


def get_connection():
    """
    Create and return a SQL Server connection.
    Returns:
        pyodbc.Connection | None
    """

    connection_string = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    try:
        conn = pyodbc.connect(connection_string)

        print("✅ Connected to SQL Server Successfully.")

        return conn

    except pyodbc.Error as e:

        print("\n❌ Database Connection Failed")

        print(e)

        print("\nPlease check:")

        print("1. SQL Server Service is running.")
        print("2. Server Name is correct.")
        print("3. Database Name is correct.")
        print("4. ODBC Driver is installed.")

        return None