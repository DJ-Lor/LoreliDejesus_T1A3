from helper import check_email

# Mock email to test different conventions that may be entered by the user \
#  when adding a new client detail: Email


def test_check_email():
    assert check_email('loreli@gmail.com') is True  # Test case 1
    assert check_email('loreli.gmail.com') is False  # Test case 2
    assert check_email('loreli') is False  # Test case 3
    assert check_email('loreli@edu.org.au') is True  # Test case 4