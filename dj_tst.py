#Import my property class that has CRUD functions
from property import Property
from client import Client
from helper import id_generate, id_display, next_step
import json
from os import path
from input_helper import capture_confirm_action, capture_suburb

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




# # # # # Ask for user input
# # name = input("Please enter the new client name: ")
# # email = input("Please enter the client's email address: ")
# # suburb = input("Please enter the client suburb of interest: ")
# # price = int(input("Please enter the client property budget: "))

# # # # # Create client
# # c1 = Client(name, email, suburb, price)
# # # # # # Save client to file
# # # c1.client_save()

# # # # Ask for user input
# # ID = int(input("Client ID: "))

# # # # # # Delete a client ID from file
# # c2 = Client(ID)
# # # # # print(c2)
# # # # # # Save updated file
# # c2.client_remove()

# # Ask for user input

# # ID = int(input("Client ID: "))
# # c3 = Client(ID)
# # c3.client_edit()

# # ID = int(input("Property ID: "))
# # p3 = Property(ID)
# # p3.property_edit()

# # ID = int(input("Client ID: "))
# # c4 = Client('', '', '', 0, ID)
# # c4.client_search()
   



# # Read JSON file and load data into list
# # Append new dict to list
# # Point to top of file
# # # Replace all objects in file with the updated list

# # def id_generate():

# #     with open('id.json', 'r') as openfile:
# #         # Reading from json file
# #         id_obj = json.load(openfile)
# #         (id_obj)["ID"] = (id_obj)["ID"] + 1

# #     with open('id.json', 'w') as openfile:
# #         json.dump(id_obj, openfile, indent=4, separators=(',',': '))
# #     return ((id_obj)["ID"])

# # print(id_generate())


  
#     # id_list =+ 
#     # id_list.append(new_data)
#     # fp.seek(0)
#     # json.dump(id_list, fp, indent=4, separators=(',',': '))

# # with open("sample.json", "w") as outfile:
# #     json.dump(dictionary, outfile)



# # print(Client.ID())


# # c4 = Client('', '', '', 0, ID)
# # c4.client_search()


# # print(next_step())




# #  Search for prospective clients for property owners based on location and price range and using property id entered
# def search_prop_owner_data_json(ID, filename1= 'json_files/client_list.json', filename2 = 'json_files/property_list.json'):
#     # Check if file exists
#     if path.isfile(filename1) is False:
#         raise Exception("File not found")
#     if path.isfile(filename2) is False:
#         raise Exception("File not found")

#     clients_list = []
#     with open(filename1, 'r') as fp:
#         clients_list = json.load(fp)

#     properties_list = []
#     with open(filename2, 'r') as fp2:
#         properties_list = json.load(fp2)

#     found_property = None
#     for pr in properties_list:
#         if pr["ID"] == ID:
#             found_property = pr
#             break
    
#     if found_property is None:
#         raise Exception("Property not found")

#     print(found_property)

#     matched_clients_list = []
#     for cli in clients_list:
#         if (cli)["SUBURB"] == (found_property)["SUBURB"] and (cli)["PRICE"] >= (found_property)["PRICE"]:
#             matched_clients_list.append(cli)

#     print(matched_clients_list)

#     print('Here are a list of clients for you:')
#     for mcl in matched_clients_list:
#         length = len(matched_clients_list)
#         if length == 0:
#             print("Sorry. There is no match at the moment.")
#         else:
#             print(mcl)

    

# onfired_action = 'n'

# if onfired_action != "Y":
#     print('not Y')
# else:
#     print('correct')


capture_suburb()

