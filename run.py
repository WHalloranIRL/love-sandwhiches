# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """"
    Get data from the users input
    """
    while True:
        print("Please enter data from the last sales day")
        print("Data should be 6 numbers serperated by ,")
        print("Example: 1,2,3,4,5,6")

        data_str = input("Enter your sales data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid\n")
            break

    return sales_data

def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) !=6:
            raise ValueError(
                f"Exactly 6 values needed, you submitted {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e} is not valid, plaease try again \n")    
        return False

    return True


def update_sales_data(data):
    """
    Update the sales worksheet, add a new row with the data values
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales sheet updated \n")

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_data(sales_data)