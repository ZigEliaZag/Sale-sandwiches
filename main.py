import gspread 
from google.oauth2.service_account import Credentials 
from pprint import pprint
import math

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ") #The value that user provide will be returned as string
        sales_data = data_str.split(",") #the split() returns the broken up values as a list

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data 
                   
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be cpnverted into int,
    or if there aren't exactly 6 values.
    """
    try: 
        [int(value) for value in values] #convert value to a integer
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values requireded, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
    
    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = sheet.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

def calculate_surplus_data(sale_row):
    """ 
    Compare sales with stock and calculate the surplus for each item type.
    The surplas is defined as the sales figure subtracted from the stock:
    - positive surplus indecates waste.
    - Negative surplus indecates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = sheet.worksheet("stock").get_all_values()
    stock_row = stock[-1] # output one row from spreadsheet "stock row"
    
    surplus_data = []
    for stock, sales in zip(stock_row , sale_row):
        surplus = int(stock) - sales 
        surplus_data.append(surplus)
    
    return surplus_data

def main():
    """
    Run all program functions 
    """
    data = get_sales_date()
    sales_data = [int(num) for num in data] #convert the value to integer
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)

print("Welcome to Sale Sandwiches Data Automation")
main()