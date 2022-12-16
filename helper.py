import json
from os import path
from email_validator import validate_email, EmailNotValidError
 

# function to add to JSON
def write_json(new_data, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # Read JSON file and load data into list
    # Append new dict to list
    # Point to top of file
    # Replace all objects in file with the updated list
    with open(filename, 'r+') as fp:
        listObj = []
        listObj = json.load(fp)
        listObj.append(new_data)
        fp.seek(0)
        json.dump(listObj, fp, indent=4, separators=(',',': '))

def remove_data_json(ID, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # Read JSON file and load data into list
    listObj = []
    with open(filename, 'r') as fp:
        listObj = json.load(fp)

    # Remove element from list
    for index, obj in enumerate(listObj):
        if obj["ID"] == ID:
            listObj.pop(index)
            break
    
    # Replace all objects in file with the updated list
    with open(filename, 'w') as wp:
        json.dump(listObj, wp, indent=4, separators=(',',': '))



def edit_data_json(ID, filename):
    # Check if file exists
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # Read JSON file and load data into list
    listObj = []
    with open(filename, 'r') as fp:
        listObj = json.load(fp)

    # Show elements from list
    for index, obj in enumerate(listObj):
        if obj["ID"] == ID:
            edit = input(f"Which detail would you like to edit? \n {listObj[index]}\n Enter here: ")
            edit = edit.upper()
            new_value = input(f"Please enter the new {edit}: ")
            new_value = new_value.capitalize()
            (listObj[index])[edit] = new_value
            print(f"{edit} updated to {new_value}!")
            
    # Replace all objects in file with the updated list
    with open(filename, 'w') as wp:
        json.dump(listObj, wp, indent=4, separators=(',',': '))


#  Search for client prospective properties based on location and price range and using client id entered
def search_client_prosprop_data_json(ID, filename1= 'json_files/client_list.json', filename2 = 'json_files/property_list.json'):
    # Check if file exists
    if path.isfile(filename1) is False:
        raise Exception("File not found")
    if path.isfile(filename2) is False:
        raise Exception("File not found")

    # Read JSON file and load data into list
    clients_list = []
    with open(filename1, 'r') as fp:
        clients_list = json.load(fp)

    found_client = None
    for cli in clients_list:
        if cli["ID"] == ID:
            found_client = cli
            break
    
    if found_client is None:
        raise Exception("Client not found")


    properties_list = []
    with open(filename2, 'r') as fp2:
        properties_list = json.load(fp2)

    print(found_client)
        
    matched_properties_list = []
    for pr in properties_list:
        if (pr)["SUBURB"] == (found_client)["SUBURB"] and (pr)["PRICE"] <= (found_client)["PRICE"]:
            matched_properties_list.append(pr)

    print('Here are a list of properties for you:')
    for mtpr in matched_properties_list:
        print(mtpr)


#  Search for prospective clients for property owners based on location and price range and using property id entered
def search_prop_owner_data_json(ID, filename1= 'json_files/client_list.json', filename2 = 'json_files/property_list.json'):
    # Check if file exists
    if path.isfile(filename1) is False:
        raise Exception("File not found")
    if path.isfile(filename2) is False:
        raise Exception("File not found")

    clients_list = []
    with open(filename1, 'r') as fp:
        clients_list = json.load(fp)

    properties_list = []
    with open(filename2, 'r') as fp2:
        properties_list = json.load(fp2)

    found_property = None
    for pr in properties_list:
        if pr["ID"] == ID:
            found_property = pr
            break
    
    if found_property is None:
        raise Exception("Property not found")

    print(found_property)

    matched_clients_list = []
    for cli in clients_list:
        if (cli)["SUBURB"] == (found_property)["SUBURB"] and (cli)["PRICE"] >= (found_property)["PRICE"]:
            matched_clients_list.append(cli)

    print('Here are a list of clients for you:')
    for mcl in matched_clients_list:
        print(mcl)


# ID generator for both client and property ID 
def id_generate():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj = json.load(openfile)
        (id_obj)["ID"] = (id_obj)["ID"]+1

    with open('json_files/id.json', 'w') as openfile:
        json.dump(id_obj, openfile, indent=4, separators=(',',': '))
    return ((id_obj)["ID"])


# Printing the ID once saved
def id_display():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj_r = json.load(openfile)
        return id_obj_r["ID"]


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