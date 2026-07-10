# query_executor.py

import time
import pandas as pd
from database import get_connection


# ---------------------------------------------
# Execute SQL Query
# ---------------------------------------------

def execute_query(query):

    conn = get_connection()

    if conn is None:
        return None

    try:

        print("\nExecuting Query...")

        start = time.time()

        df = pd.read_sql(query, conn)

        end = time.time()

        conn.close()

        print("\nQuery Executed Successfully")

        print(f"Execution Time : {round(end-start,2)} Seconds")

        print(f"Rows Retrieved : {len(df)}")

        print(f"Columns : {len(df.columns)}")

        return df

    except Exception as e:

        print("\nQuery Execution Failed")

        print(e)

        conn.close()

        return None


# ---------------------------------------------
# Preview Data
# ---------------------------------------------

def preview_data(df):

    if df is None:

        print("\nNo Data Available")

        return

    print("\n" + "="*70)

    print("DATA PREVIEW")

    print("="*70)

    print(df.head())

    print("="*70)

    print(f"Total Rows : {len(df)}")

    print(f"Total Columns : {len(df.columns)}")