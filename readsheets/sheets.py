import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

name = "Booki"

def readx():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(name).sheet1  # Open the spreadhseet
    data = sheet.get_all_records()  # Get a list of all records
    row = sheet.row_values(3)  # Get a specific row
    col = sheet.col_values(3)  # Get a specific column
    cell = sheet.cell(1,2).value  # Get the value of a specific cell
    numRows = sheet.row_count  # Get the number of rows in the sheet
    print(row)

readx()
