import sqlite3

# Connect to the database
conn = sqlite3.connect('travel_info_database.sqlite3')
cursor = conn.cursor()

# Step 1: Fetch the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Step 2: For each table, fetch its structure using PRAGMA
for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    for column in columns:
        print(column)
    print("-----")


# Close the connection
conn.close()
