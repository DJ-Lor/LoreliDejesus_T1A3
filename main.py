from property import Property
from client import Client

user_input = ""

while True:
    user_input = input("Welcome to RealSeller App!\nPlease choose one between the following options:\n 1. Manage Property List\n 2. Manage Client List\n 3. Seller Portal\n 4. Exit\nWrite the number, ie '2' if you wanted to go to Manage Client List.\n Enter here: ")

    user_input = user_input.strip()

    # Manage Property option
    if user_input == "1":
        manage_prop_choice = input("What would you like to do?\n 1. Add a new property to list\n 2. Edit a current property on the list\n 3. Delete a property on the list\n 4. Exit\n Please enter a number: ")
        manage_prop_choice = manage_prop_choice.strip()

    # Add a new Property to the list
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

    # Edit a current Property from the list
        elif manage_prop_choice == "2":
            ID = int(input("Property ID: "))
            p3 = Property(ID)
            p3.property_edit()
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break

    # Delete a current Property from the list 
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
                print("No property data has been deleted. Please choose again from the following options")
                continue
    
    # Exit option
        elif manage_prop_choice == "4":
            break
        else:
            print("Invalid input. Please choose again")

    # Manage Client Option

    elif user_input == "2":

        user_input = user_input.strip()

        manage_client_choice = input("What would you like to do?\n 1. Add a new client\n 2. Edit current client details on the list\n 3. Delete a client on the list\n 4. Exit\n Please enter a number: ")
        manage_client_choice = manage_client_choice.strip()

    # Add a new client to the list 
        if manage_client_choice == "1":
            name = input("Please enter the new client name: ")
            email = input("Please enter the client's email address: ")
            suburb = input("Please enter the client suburb of interest: ")
            price = int(input("Please enter the client property budget: "))

            c1 = Client(name, email, suburb, price)
            c1.client_save()
            print(f"New client added!\n Client name: {name}\n Email: {email}\n Looking for property in: {suburb}\n Budget: ${price}\nIf this is incorrect, please go back to the main portal and follow the prompts to edit client details.")
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break

    # Edit client details
        elif manage_client_choice == "2":
            ID = int(input("Client ID: "))
            c3 = Client(ID)
            c3.client_edit()
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break
    
    # Delete client details 

        elif manage_client_choice == "3":
            ID = int(input("Client ID: "))
            confirm_action = input(f"Are you sure you want to delete client {ID} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                c2 = Client(ID)
                c2.client_remove()
                print(f"Client {ID} has been deleted!")
                next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number: ")
                if next_step == "1":
                    continue
                else:
                    break

            if confirm_action == "N":
                print("No client data has been deleted. Please choose again from the following options")
                continue

    # Exit option

        elif manage_client_choice == "4":
            break
        else:
            print("Invalid input. Please choose again")

    # Prospective opportunities view for client and property owners
    elif user_input == "3":
        seller_portal_choice = input("Check out prospective business opportunities. Please select preferred view:\n 1. Client ID\n 2. Property ID\n Enter here: ")
        if seller_portal_choice == "1":
            ID = int(input("Please input the client ID. Enter here: "))
            c4 = Client('', '', '', 0, ID)
            c4.client_search()
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break
            
        elif seller_portal_choice == "2":
            ID = int(input("Please input the property ID. Enter here: "))
            p4 = Property('', 0, ID)
            p4.property_search()
            next_step = input("Would you like to go back to the 1. Main portal or 2. Exit?\n Choose a number. ")
            if next_step == "1":
                continue
            else:
                break

        else:
            print("Invalid input. Please choose again")

    elif user_input == "4":
        break

    else:
        print("Invalid input. Please choose a number from 1-4: ")

