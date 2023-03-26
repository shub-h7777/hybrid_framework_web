from utilities import read_utils

test_valid_login_data = [
    ("male", "Shubham", "Patel", "shuham122@gmail.com", "Demo@123", "Your registration completed"),
    ("female", "Riya", "Jaat", "riya1222@gmail.com", "Demo@123", "Your registration completed")
]

test_invalid_login_data = [
    ("male", "Shubham", "Patel", "shuham122@", "Demo@123", "Wrong email"),
    ("female", "Riya", "Jaat", "riya1222@", "Demo@123", "Wrong email")
]

test_case_3_data = read_utils.get_excel_as_list("../test_data/excel.xlsx", "Sheet1")
