from property import Property
from client import Client

user_input = ""

while True:
    user_input = input("Welcome to RealSeller App!\nPlease choose one between the following options:\n 1. Manage Property List\n 2. Manage Client List\n 3. Seller Portal\n 4. Exit\nWrite the number, ie '2' if you wanted to go to Manage Client List.\n Enter here: ")

    user_input = user_input.strip()

    if user_input == "1":
        manage_prop_choice = input("Would you like to\n 1. Add a new property to list\n 2. Edit a current property on the list\n 3. Delete a property on the list\n 4. Exit\n Please enter a number: ")
        manage_prop_choice = manage_prop_choice.strip()
        if manage_prop_choice == "1":
            suburb = input("Please enter the suburb of the new property: ") 
            price = int(input("Please enter the selling price of the new property: "))
            p1 = Property(suburb, price)
            p1.property_save()
            print(f"The new property located at {suburb} with a selling price of ${price} has been added!")
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break
        elif manage_prop_choice == "2":
            break
        elif manage_prop_choice == "3":
            ID = int(input("Property ID: "))
            confirm_action = input(f"Are you sure you want to delete property {ID} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                p2 = Property(ID)
                p2.property_remove()
                print(f"Property {ID} has been deleted!")
                next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number: ")
                if next_step == "1":
                    continue
                else:
                    break

            if confirm_action == "N":
                print("No property has been deleted. Please choose again from the following options")
                continue
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

