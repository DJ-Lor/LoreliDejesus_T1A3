from helper import check_email

# Mock email to test different conventions that may be entered by the user when adding a new client detail: Email
def check_email():
    assert check_email(loreli@gmail.com) == True # Test case 1
    assert check_email(loreli.gmail.com) == False # Test case 2
    assert check_email(loreli) == False # Test case 3
    assert check_email(loreli@edu.au.org) == False # Test case 4