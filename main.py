from property import Property
from client import Client
from helper import id_display, check_email, next_step

user_input = ""

while True:
    user_input = input("Welcome to RealSeller App!\nPlease choose one between the following options:\n 1. Manage Property List\n 2. Manage Client List\n 3. Prospective Opportunity Portal\n 4. Exit\nWrite the number, ie '2' if you wanted to go to Manage Client List.\n Enter here: ")

    user_input = user_input.strip()

    # Manage Property option
    if user_input == "1":
        manage_prop_choice = input("What would you like to do?\n 1. Add a new property to list\n 2. Edit a current property on the list\n 3. Delete a property on the list\n 4. Exit\n Please enter a number: ")
        manage_prop_choice = manage_prop_choice.strip()

    # Add a new Property to the list
        if manage_prop_choice == "1":
            SUBURB = input("Please enter the suburb of the new property: ") 
            PRICE = int(input("Please enter the selling price of the new property: "))
            p1 = Property(SUBURB, PRICE)
            p1.property_save()
            print(f"The new property located at {SUBURB} with a selling price of ${PRICE} has been added!")
            print(f"Your property ID is {id_display()}!")
            next_step()
            

    # Edit a current Property from the list
        elif manage_prop_choice == "2":
            ID = int(input("Property ID: "))
            p3 = Property('', 0, ID)
            p3.property_edit()
            next_step()

    # Delete a current Property from the list 
        elif manage_prop_choice == "3":
            ID = int(input("Property ID: "))
            confirm_action = input(f"Are you sure you want to delete property {ID} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                p2 = Property(ID)
                p2.property_remove()
                print(f"Property {ID} has been deleted!")
                next_step()

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
            NAME = input("Please enter the new client name: ")

            EMAIL = input("Please enter the client's email address: ")
            while(check_email(EMAIL) == False) :
                print('Invalid email. Please try again.')
                EMAIL = input("Please enter the client's email address: ")

            SUBURB = input("Please enter the client suburb of interest: ")
            PRICE = int(input("Please enter the client property budget: "))

            c1 = Client(NAME, EMAIL, SUBURB, PRICE)
            c1.client_save()
            print(f"New client added!\n Client name: {NAME}\n Email: {EMAIL}\n Looking for property in: {SUBURB}\n Budget: ${PRICE}\n Your client ID is {id_display()}!")
            print("If this is incorrect, please go back to the main portal and follow the prompts to edit client details.")
            next_step()

    # Edit client details
        elif manage_client_choice == "2":
            ID = int(input("Client ID: "))
            c3 = Client(ID)
            c3.client_edit()
            next_step()
    
    # Delete client details 

        elif manage_client_choice == "3":
            ID = int(input("Client ID: "))
            confirm_action = input(f"Are you sure you want to delete client {ID} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                c2 = Client(ID)
                c2.client_remove()
                print(f"Client {ID} has been deleted!")
                next_step()

            if confirm_action == "N":
                print("No client data has been deleted. Please choose again from the following options.")
                continue

    # Exit option

        elif manage_client_choice == "4":
            break
        else:
            print("Invalid input. Please choose again")

    # Prospective opportunities view for client and property owners
    elif user_input == "3":
        opp_portal_choice = input("Check out prospective business opportunities. Please select preferred view:\n 1. Client ID\n 2. Property ID\n Enter here: ")
        if opp_portal_choice == "1":
            ID = int(input("Please input the client ID. Enter here: "))
            c4 = Client('', '', '', 0, ID)
            c4.client_search()
            next_step()
            
        elif opp_portal_choice == "2":
            ID = int(input("Please input the property ID. Enter here: "))
            p4 = Property('', 0, ID)
            p4.property_search()
            next_step()

        else:
            print("Invalid input. Please choose again.")

    elif user_input == "4":
        print("Good bye!")
        break

    else:
        print("Invalid input. Please choose a number from 1-4: ")

