import json
from os import path, system
from email_validator import validate_email, EmailNotValidError


# function to add to JSON
def write_json(new_data, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')

    # Read JSON file and load data into list
    # Append new dict to list
    # Point to top of file
    # Replace all objects in file with the updated list
    with open(filename, 'r+') as fp:
        list_obj = []
        list_obj = json.load(fp)
        list_obj.append(new_data)
        fp.seek(0)
        json.dump(list_obj, fp, indent=4, separators=(',', ': '))


def remove_data_json(id, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')

    # Read JSON file and load data into list
    list_obj = []
    with open(filename, 'r') as fp:
        list_obj = json.load(fp)

    has_deleted = False
    # Remove element from list
    for index, obj in enumerate(list_obj):
        if obj['id'] == id:
            list_obj.pop(index)
            has_deleted = True
            print(f'{id} has been deleted!')
            break
    if not has_deleted:
        print('Deletion failed, no match for ID')

    # Replace all objects in file with the updated list
    with open(filename, 'w') as wp:
        json.dump(list_obj, wp, indent=4, separators=(',', ': '))


def edit_data_json(id, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception('File not found')

    # Read JSON file and load data into list
    list_obj = []
    with open(filename, 'r') as fp:
        list_obj = json.load(fp)

    has_edited = False
    # Show elements from list
    for index, obj in enumerate(list_obj):
        if obj['id'] == id:
            print(f'Which detail would you like to edit?\n {list_obj[index]}')
            edit = input('Enter here: ')
            edit = edit.lower()
            if (edit == 'suburb' or edit == 'price'
                    or edit == 'name' or edit == 'email'):
                new_value = input(f'Please enter the new {edit}: ')
                new_value = new_value.lower()
                (list_obj[index])[edit] = new_value
                print(f'{edit} updated to {new_value}!')
                has_edited = True
            else:
                print('Invalid answer, not part of the editable options')
                has_edited = True

    if not has_edited:
        print('Update failed, no match for ID')

    # Replace all objects in file with the updated list
    with open(filename, 'w') as wp:
        json.dump(list_obj, wp, indent=4, separators=(',', ': '))


#  Search for client prospective properties based on location and price range \
# and using client id entered
def search_client_prosprop_data_json(id,
                                     filename1='./json_files/client_list.json',
                                     filename2='./json_files/property_list.json'
                                     ):
    # Check if file exists
    if path.isfile(filename1) is False:
        raise Exception('File not found')
    if path.isfile(filename2) is False:
        raise Exception('File not found')

    # Read JSON file and load data into list
    clients_list = []
    with open(filename1, 'r') as fp:
        clients_list = json.load(fp)

    found_client = None
    for cli in clients_list:
        if cli['id'] == id:
            found_client = cli
            break

    properties_list = []
    with open(filename2, 'r') as fp2:
        properties_list = json.load(fp2)

    if found_client is None:
        print('Client not found')

    if found_client is not None:
        print(found_client)

        matched_properties_list = []
        for pr in properties_list:
            if (pr)['suburb'] == (found_client)['suburb'] and \
                    (pr)['price'] <= (found_client)['price']:
                matched_properties_list.append(pr)

        if len(matched_properties_list) == 0:
            print('Sorry. There is no match at the moment.')
        else:
            print('Here are a list of properties for you:')
            for mtpr in matched_properties_list:
                print(mtpr)


#  Search for prospective clients for property owners based on location and\
#  price range and using property id entered
def search_prop_owner_data_json(id,
                                filename1='./json_files/client_list.json',
                                filename2='./json_files/property_list.json'):
    # Check if file exists
    if path.isfile(filename1) is False:
        raise Exception('File not found')
    if path.isfile(filename2) is False:
        raise Exception('File not found')

    clients_list = []
    with open(filename1, 'r') as fp:
        clients_list = json.load(fp)

    properties_list = []
    with open(filename2, 'r') as fp2:
        properties_list = json.load(fp2)

    found_property = None
    for pr in properties_list:
        if pr['id'] == id:
            found_property = pr
            break

    if found_property is None:
        print('Property not found')

    if found_property is not None:
        print(found_property)
        matched_clients_list = []
        for cli in clients_list:
            if (cli)['suburb'] == (found_property)['suburb'] and \
                    (cli)['price'] >= (found_property)['price']:
                matched_clients_list.append(cli)

        if len(matched_clients_list) == 0:
            print('Sorry. There is no match at the moment.')
        else:
            print('Here are a list of clients for you:')
            for mcl in matched_clients_list:
                print(mcl)


# ID generator for both client and property ID
def id_generate():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj = json.load(openfile)
        (id_obj)['id'] = (id_obj)['id']+1

    with open('json_files/id.json', 'w') as openfile:
        json.dump(id_obj, openfile, indent=4, separators=(',', ': '))
    return ((id_obj)['id'])


# Printing the ID once saved
def id_display():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj_r = json.load(openfile)
        return id_obj_r['id']


# Email Validator
def check_email(email):
    try:
        # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v['email']
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        # print(str(e))
        return False


# Next Step
def next_step():
    next_step = input("""Would you like to go back to the:
1. Main portal
2. Exit?
Choose a number: """)
    if next_step == '2':
        system('cls||clear')
        print('Good bye!')
        exit()
