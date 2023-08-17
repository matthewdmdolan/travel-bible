import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('travel_info_database.sqlite3')
cursor = conn.cursor()

# Execute the SQL JOIN query
cursor.execute("""
SELECT 
    a.*, b.*, c.*
FROM 
    country_info a
LEFT JOIN 
    travel_plans_info b ON a.Name = b.[Country ]
LEFT JOIN 
    travel_history_info c ON a.Name = c.[Country ]
""")

results = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

# Write to a CSV file
with open('joined_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header (column names)
    writer.writerow(column_names)

    # Write the results
    writer.writerows(results)

print("Data written to joined_data.csv")

# Close the connection
conn.close()
