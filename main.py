
# ***Main View***
# 1. Options shown and require user input too choose
# * Manage Property List
# * Manage Client List
# * Seller Portal
# * Exit

user_input = ""

while True:
    user_input = input("Welcome to RealSeller App!\nPlease choose one between the following options:\n 1. Manage Property List\n 2. Manage Client List\n 3. Seller Portal\n 4. Exit\nWrite the number, ie '2' if you wanted to go to Manage Client List.\n Enter here: ")

    user_input = user_input.strip()

    if user_input == "1":
        manage_prop_choice = input("Would you like to\n1. Add a new property list\n 2. Edit a current property on the list\n 3. Delete a property on the list\n 4. Exit\n Please enter a number: ")
        if manage_prop_choice == "1":
            break
        elif manage_prop_choice == "2":
            break
        elif manage_prop_choice == "3":
            break
        elif manage_prop_choice == "4":
            break
        else:
            print("Invalid input. Please choose again")

    elif user_input == "2":
        manage_client_choice = input("Would you like to\n 1. Add a new client\n 2. Edit current client details on the list\n 3. Delete a client on the list\n 4. Exit\n Please enter a number: ")
        if manage_client_choice == "1":
            break
        elif manage_client_choice == "2":
            break
        elif manage_client_choice == "3":
            break
        elif manage_client_choice == "4":
            break
        else:
            print("Invalid input. Please choose again")

    elif user_input == "3":
        seller_portal_choice = input("Would you like to enter the\n 1. Client ID\n 2. Client Name")
        if seller_portal_choice == "1":
            seller_portal_choice = input("Please input the client ID. Enter here: ")
        elif seller_portal_choice == "2":
            break
        else:
            print("Invalid input. Please choose again")

    elif user_input == "4":
        break

    else:
        print("INVALID ANSWER. Please choose a number from 1-4: ")

