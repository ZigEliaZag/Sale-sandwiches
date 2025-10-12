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

#data = sheet.sheet1.row_values(4)
sales = sheet.worksheet("sales")
data = sales.get_all_values()
print(data)