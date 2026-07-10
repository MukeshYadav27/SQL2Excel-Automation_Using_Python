# database_explorer.py

from database import get_connection


# ----------------------------------------
# Execute Query
# ----------------------------------------

def fetch_objects(query):

    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    cursor.execute(query)

    data = [row[0] for row in cursor.fetchall()]

    conn.close()

    return data


# ----------------------------------------
# Get Tables
# ----------------------------------------

def get_tables():

    query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE='BASE TABLE'
        ORDER BY TABLE_NAME
    """

    return fetch_objects(query)


# ----------------------------------------
# Get Views
# ----------------------------------------

def get_views():

    query = """
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.VIEWS
        ORDER BY TABLE_NAME
    """

    return fetch_objects(query)


# ----------------------------------------
# Get Stored Procedures
# ----------------------------------------

def get_procedures():

    query = """
        SELECT name
        FROM sys.procedures
        ORDER BY name
    """

    return fetch_objects(query)


# ----------------------------------------
# Get Functions
# ----------------------------------------

def get_functions():

    query = """
        SELECT name
        FROM sys.objects
        WHERE type IN ('FN','TF','IF')
        ORDER BY name
    """

    return fetch_objects(query)


# ----------------------------------------
# Display Database Objects
# ----------------------------------------

def show_database_objects():

    print("\n" + "="*60)
    print("DATABASE OBJECTS")
    print("="*60)

    tables = get_tables()
    views = get_views()
    procedures = get_procedures()
    functions = get_functions()

    print(f"\nTables ({len(tables)})")
    print("-"*60)

    if tables:
        for i, table in enumerate(tables, start=1):
            print(f"{i}. {table}")
    else:
        print("No Tables Found")

    print(f"\nViews ({len(views)})")
    print("-"*60)

    if views:
        for i, view in enumerate(views, start=1):
            print(f"{i}. {view}")
    else:
        print("No Views Found")

    print(f"\nStored Procedures ({len(procedures)})")
    print("-"*60)

    if procedures:
        for i, procedure in enumerate(procedures, start=1):
            print(f"{i}. {procedure}")
    else:
        print("No Stored Procedures Found")

    print(f"\nFunctions ({len(functions)})")
    print("-"*60)

    if functions:
        for i, function in enumerate(functions, start=1):
            print(f"{i}. {function}")
    else:
        print("No Functions Found")

    print("\n" + "="*60)