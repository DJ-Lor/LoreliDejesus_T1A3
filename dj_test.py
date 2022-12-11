# Import my property class that has CRUD functions
from property import Property
from client import Client

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
# suburb = input("Please enter the client suburb of interest: ")
# price = int(input("Please enter the client property budget: "))

# # # # Create client
# c1 = Client(name, suburb, price)
# # # # # Save client to file
# c1.client_save()

# # Ask for user input
ID = int(input("Client ID: "))
# # # # Delete a client ID from file
c2 = Client(ID)
# # # print(c2)
# # # # Save updated file
c2.client_remove()