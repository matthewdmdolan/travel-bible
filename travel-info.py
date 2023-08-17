from google.oauth2 import service_account
import pandas as pd
import gspread
import json
import os

credentials = service_account.Credentials.from_service_account_info("cfg.json")
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds_with_scope = credentials.with_scopes(scope)

client = gspread.authorize(creds_with_scope)