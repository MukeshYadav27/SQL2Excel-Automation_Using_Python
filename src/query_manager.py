# query_manager.py

from database_explorer import get_tables

# --------------------------------------------------
# Show Suggested Queries
# --------------------------------------------------

def show_queries():

    tables = get_tables()

    queries = []

    print("\n" + "=" * 60)
    print("SUGGESTED SQL QUERIES")
    print("=" * 60)

    for table in tables:

        queries.append(f"SELECT * FROM {table}")
        queries.append(f"SELECT TOP 10 * FROM {table}")
        queries.append(f"SELECT COUNT(*) AS TotalRecords FROM {table}")

    for i, query in enumerate(queries, start=1):

        print(f"{i}. {query}")

    return queries


# --------------------------------------------------
# Custom Query
# --------------------------------------------------

def custom_query():

    print("\nWrite Your SQL Query")

    query = input("SQL> ")

    return query


# --------------------------------------------------
# Query Validation
# --------------------------------------------------

def validate_query(query):

    query = query.strip()

    if query == "":

        print("\nQuery cannot be empty.")

        return False

    if not query.lower().startswith("select"):

        print("\nOnly SELECT queries are allowed.")

        return False

    blocked = [

        "delete",

        "drop",

        "truncate",

        "update",

        "insert",

        "alter",

        "create",

        "exec",

        "execute"

    ]

    for word in blocked:

        if word in query.lower():

            print(f"\n'{word.upper()}' is not allowed.")

            return False

    return True


# --------------------------------------------------
# Get Query
# --------------------------------------------------

def get_query():

    queries = show_queries()

    print("\n1. Use Suggested Query")
    print("2. Write My Own Query")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        try:

            number = int(input("Enter Query Number : "))

            if 1 <= number <= len(queries):

                print("\nSelected Query")

                print(queries[number - 1])

                return queries[number - 1]

            else:

                print("\nInvalid Query Number")

                return get_query()

        except ValueError:

            print("\nPlease enter a valid number.")

            return get_query()

    elif choice == "2":

        query = custom_query()

        if validate_query(query):

            return query

        else:

            return get_query()

    else:

        print("\nInvalid Choice")

        return get_query()