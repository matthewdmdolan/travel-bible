from google.oauth2 import service_account
import gspread
import json
import pandas as pd
import sqlite3

# Assuming cfg.json is in the same directory as this script.
# If it's elsewhere, provide the full path.
# Use the path to your service account JSON file
credentials_path = "cfg.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_with_scope = credentials.with_scopes(scope)
client = gspread.authorize(creds_with_scope)

spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1gNltmttsYy1lbFQgGRTx9RYy3ueUxYcv-7e-8a-RsPo/edit#gid=510460711')
worksheet = spreadsheet.get_worksheet(1)

travel_history_data = worksheet.get_all_records()

history_df = pd.DataFrame.from_dict(travel_history_data)

# Write to SQLite3 database
conn = sqlite3.connect('travel_info_database.sqlite3')
history_df .to_sql('travel_history_info', conn, if_exists='replace', index=False)
conn.close()

print("Data written to SQLite3 database.")



