import gspread 
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json', scopes=SCOPE)
client = gspread.authorize(CREDS)
sheet_id = "1pqXmgvomFqOWzbPYIQ98lN_r4N07CtYyY3JlzzieIVo"
sheet = client.open_by_key(sheet_id)

""" 
-> this is code to check that API is working
data = sheet.sheet1.row_values(4) 
sales = sheet.worksheet("sales")
data = sales.get_all_values()
print(data) 
"""

def get_sales_date():
    """
    Get sales figures input from the user 
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ") #The value that user provide will be returned as string
    print(f"The data provided is {data_str}")

get_sales_date()