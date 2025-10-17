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
    sales_data = data_str.split(",") #the split() returns the broken up values as a list
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be cpnverted into int,
    or if there aren't exactly 6 values.
    """
    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values requireded, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")

get_sales_date()