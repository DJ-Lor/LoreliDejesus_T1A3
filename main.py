import os
from property import Property
from client import Client
from helper import id_display, next_step
from input_helper import capture_name, capture_email, capture_suburb,\
     capture_price, capture_id, capture_confirm_action


user_input = ''

while True:
    user_input = input("""Welcome to RealSeller App!
Please choose one between the following options:
1. Manage Property List
2. Manage Client List
3. Prospective Opportunity Portal
4. Exit
Write the number, ie "2" if you wanted to go to Manage Client List.
Enter here: """)
    user_input = user_input.strip()
    os.system('cls||clear')

    # Manage Property option
    if user_input == '1':
        manage_prop_choice = input("""What would you like to do?
1. Add a new property to list
2. Edit a current property on the list
3. Delete a property on the list
4. Exit
Please enter a number: """)
        manage_prop_choice = manage_prop_choice.strip()
        os.system('cls||clear')

    # Add a new Property to the list
        if manage_prop_choice == '1':
            suburb = capture_suburb()
            suburb = suburb.lower()
            price = capture_price()
            p1 = Property(suburb, price)
            p1.property_save()
            os.system('cls||clear')
            print(f'Property in {suburb} priced at ${price} has been added!')
            print(f'Your property ID is {id_display()}!')
            next_step()
            os.system('cls||clear')

    # Edit a current Property from the list
        elif manage_prop_choice == '2':
            id = capture_id()
            p3 = Property('', 0, id)
            p3.property_edit()
            next_step()
            os.system('cls||clear')

    # Delete a current Property from the list
        elif manage_prop_choice == '3':
            id = capture_id()
            confirm_action = capture_confirm_action()

            if confirm_action == 'Y':
                p2 = Property('', 0, id)
                p2.property_remove()
                next_step()
                os.system('cls||clear')

            if confirm_action == 'N':
                print('No property deleted. Please choose again')
                continue

    # Exit option
        elif manage_prop_choice == '4':
            print('Good bye')
            break
        else:
            print('Invalid input. Please choose again')

    # Manage Client Option

    elif user_input == '2':
        user_input = user_input.strip()
        manage_client_choice = input("""What would you like to do?
1. Add a new client
2. Edit current client details on the list
3. Delete a client on the list
4. Exit
Please enter a number: """)
        manage_client_choice = manage_client_choice.strip()
        os.system('cls||clear')

    # Add a new client to the list
        if manage_client_choice == '1':
            name = capture_name()
            email = capture_email()
            suburb = capture_suburb()
            suburb = suburb.lower()
            price = capture_price()
            c1 = Client(name, email, suburb, price)
            c1.client_save()
            os.system('cls||clear')
            print('New client added!')
            print(f'Client name: {name}')
            print(f'Email: {email}')
            print(f'Looking for property in: {suburb}')
            print(f'Budget: ${price}')
            print(f'Your new client ID is {id_display()}!')
            print("""If this is incorrect, please go back to the main portal
and follow the prompts to edit client details.""")
            next_step()
            os.system('cls||clear')

    # Edit client details
        elif manage_client_choice == '2':
            id = capture_id()
            c3 = Client('', '', '', 0, id)
            c3.client_edit()
            next_step()
            os.system('cls||clear')

    # Delete client details
        elif manage_client_choice == '3':
            id = capture_id()
            confirm_action = capture_confirm_action()

            if confirm_action == 'Y':
                c2 = Client('', '', '', 0, id)
                c2.client_remove()
                next_step()
                os.system('cls||clear')

            elif confirm_action == 'N':
                print('No client deleted. Please choose again')
                continue

    # Exit option

        elif manage_client_choice == '4':
            print('Good bye!')
            break
        else:
            print('Invalid input. Please choose again')

    # Prospective opportunities view for client and property owners
    elif user_input == '3':
        opp_portal_choice = input("""Check out prospective opportunities.
Please select preferred view:
1. Client ID
2. Property ID
Enter here: """)
        if opp_portal_choice == '1':
            id = capture_id()
            c4 = Client('', '', '', 0, id)
            c4.client_search()
            next_step()
            os.system('cls||clear')

        elif opp_portal_choice == '2':
            id = capture_id()
            p4 = Property('', 0, id)
            p4.property_search()
            next_step()
            os.system('cls||clear')

        else:
            print('Invalid input. Please choose again.')

    elif user_input == '4':
        print('Good bye!')
        break

    else:
        print('Invalid input. Please choose a number from 1-4: ')
