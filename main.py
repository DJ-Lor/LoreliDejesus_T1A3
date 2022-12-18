from property import Property
from client import Client
from helper import id_display, next_step
from input_helper import capture_name, capture_email, capture_suburb, capture_price, capture_id


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
            suburb = capture_suburb()
            price = capture_price()
            p1 = Property(suburb, price)
            p1.property_save()
            print(f"The new property located at {suburb} with a selling price of ${price} has been added!")
            print(f"Your property ID is {id_display()}!")
            next_step()
            

    # Edit a current Property from the list
        elif manage_prop_choice == "2":
            id = capture_id()
            p3 = Property('', 0, id)
            p3.property_edit()
            next_step()

    # Delete a current Property from the list 
        elif manage_prop_choice == "3":
            id = capture_id()
            confirm_action = input(f"Are you sure you want to delete property {id} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                p2 = Property(id)
                p2.property_remove()
                print(f"Property {id} has been deleted!")
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
            name = capture_name()
            email = capture_email()
            suburb = capture_suburb()
            price = capture_price()

            c1 = Client(name, email, suburb, price)
            c1.client_save()
            print(f"New client added!\n Client name: {name}\n Email: {email}\n Looking for property in: {suburb}\n Budget: ${price}\n Your client ID is {id_display()}!")
            print("If this is incorrect, please go back to the main portal and follow the prompts to edit client details.")
            next_step()

    # Edit client details
        elif manage_client_choice == "2":
            id = capture_id()
            c3 = Client(id)
            c3.client_edit()
            next_step()
    
    # Delete client details 
        elif manage_client_choice == "3":
            id = capture_id()
            confirm_action = input(f"Are you sure you want to delete client {ID} from the list? Y/N:  ")
            confirm_action = confirm_action.capitalize()
            if confirm_action == "Y":
                c2 = Client(id)
                c2.client_remove()
                print(f"Client {id} has been deleted!")
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
            id = capture_id()
            c4 = Client('', '', '', 0, id)
            c4.client_search()
            next_step()
            
        elif opp_portal_choice == "2":
            id = capture_id()
            p4 = Property('', 0, id)
            p4.property_search()
            next_step()

        else:
            print("Invalid input. Please choose again.")

    elif user_input == "4":
        print("Good bye!")
        break

    else:
        print("Invalid input. Please choose a number from 1-4: ")

