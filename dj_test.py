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
ID = int(input("Property ID: "))
# # Delete a property from file
p2 = Property(ID)
# print(p2)
# # Save updated file
p2.property_remove()

