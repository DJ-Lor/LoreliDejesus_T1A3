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
    # Remove element from list
    # Point to top of file
    # Replace all objects in file with the updated list
    with open(filename, 'r+') as fp:
        listObj = []
        listObj = json.load(fp)
        # listObj. delete object that has the same ID - WRITE
        fp.seek(0)
        json.dump(listObj, fp, indent=4, separators=(',',': '))