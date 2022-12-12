import json
from os import path

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
            edit = input(f"Which client detail would you like to edit?\n {listObj[index]}\n Enter here: ")
            edit = edit.upper()
            new_value = input(f"Please enter the new {edit}: ")
            (listObj[index])[edit] = new_value
            print(f"{edit} updated to {new_value}!")
          
                
                

      # Replace all objects in file with the updated list
    with open(filename, 'w') as wp:
        json.dump(listObj, wp, indent=4, separators=(',',': '))


            