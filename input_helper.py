from email_validator import validate_email, EmailNotValidError
 
# Input ID 
def capture_id():
    
    while True:
        try:
            input_id = int(input('Enter ID: '))
            if input_id < 100:
                raise
            break
        except:
            print('Invalid input. Please enter the correct ID')
    return input_id


# Input name function and error handling
def capture_name():
    input_name = input("Please enter the new client name: ")
    while (len(input_name) <= 1):
        print('Invalid name. Please try again.')
        input_name = input("Please enter the new client name: ")
    return input_name


# Email Validator
def check_email(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v["email"] 
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        # print(str(e))
        return False

# Input email function and error handling
def capture_email():
    input_email = input("Please enter the client's email address: ")
    while(check_email(input_email) == False) :
        print('Invalid email. Please try again.')
        input_email = input("Please enter the client's email address: ")
    return input_email


# Input suburb function and error handling
def capture_suburb():
    input_suburb = input("Please enter the suburb name: ")
    while (len(input_suburb) <= 3):
        print('Invalid name. Please try again.')
        input_suburb = input("Please enter the suburb name: ")
    return input_suburb


# Input price function and error handling
def capture_price():
    
    while True:
        try:
            input_price = int(input("Please enter the property price/budget: "))
            break

        except ValueError:
            print('Invalid Input. Please enter an integer and try again.')

    return input_price


