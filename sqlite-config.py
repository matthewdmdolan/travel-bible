import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('travel_info_database.sqlite3')
cursor = conn.cursor()

# Retrieve the list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print schema of each table
for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    for column in columns:
        print(column)
    print("-----\n")

# Close the connection
conn.close()