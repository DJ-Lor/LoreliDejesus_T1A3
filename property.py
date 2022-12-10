from json_helper import write_json

# "Database File Location"
filename = 'property_list.json'

class Property:
    def __init__(self, property_ID, suburb, price):
        self.property_ID = property_ID
        self.suburb = suburb
        self.price = price
  
    def property_add(self):
        user_input_data_p = {
            "client_ID": "",
            "suburb": "",
            "price": ""
        }

        user_input_data_p["suburb"] = input("Please enter the suburb of the new property: ")
        user_input_data_p["price"] = input(str(int("Please enter the selling price of the new property: ")))

        write_json(user_input_data_p, filename)



