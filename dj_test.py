#Import my property class that has CRUD functions
from property import Property
from client import Client
from helper import id_generate, id_display, next_step
import json
from os import path

# # Ask for user input
# suburb = input("Please enter the suburb of the new property: ")
# price = int(input("Please enter the selling price of the new property: "))

# # # Create property
# p1 = Property(suburb, price)
# # # Save property to file
# p1.property_save()

# Ask for user input
# ID = int(input("Property ID: "))
# # # Delete a property from file
# p2 = Property(ID)
# # print(p2)
# # # Save updated file
# p2.property_remove()




# # # # Ask for user input
# name = input("Please enter the new client name: ")
# email = input("Please enter the client's email address: ")
# suburb = input("Please enter the client suburb of interest: ")
# price = int(input("Please enter the client property budget: "))

# # # # Create client
# c1 = Client(name, email, suburb, price)
# # # # # Save client to file
# # c1.client_save()

# # # Ask for user input
# ID = int(input("Client ID: "))

# # # # # Delete a client ID from file
# c2 = Client(ID)
# # # # print(c2)
# # # # # Save updated file
# c2.client_remove()

# Ask for user input

# ID = int(input("Client ID: "))
# c3 = Client(ID)
# c3.client_edit()

# ID = int(input("Property ID: "))
# p3 = Property(ID)
# p3.property_edit()

# ID = int(input("Client ID: "))
# c4 = Client('', '', '', 0, ID)
# c4.client_search()
   



# Read JSON file and load data into list
# Append new dict to list
# Point to top of file
# # Replace all objects in file with the updated list

# def id_generate():

#     with open('id.json', 'r') as openfile:
#         # Reading from json file
#         id_obj = json.load(openfile)
#         (id_obj)["ID"] = (id_obj)["ID"] + 1

#     with open('id.json', 'w') as openfile:
#         json.dump(id_obj, openfile, indent=4, separators=(',',': '))
#     return ((id_obj)["ID"])

# print(id_generate())


  
    # id_list =+ 
    # id_list.append(new_data)
    # fp.seek(0)
    # json.dump(id_list, fp, indent=4, separators=(',',': '))

# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)



# print(Client.ID())


# c4 = Client('', '', '', 0, ID)
# c4.client_search()


print(next_step())



