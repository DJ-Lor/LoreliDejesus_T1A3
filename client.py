from json_helper import write_json, remove_data_json

# "Database File Location"
filename = 'client_list.json'

class Client:
    def __init__(self, suburb, price):
        self.property_ID = 12346
        self.suburb = suburb
        self.price = price
  
    def client_save(self):
        write_json(self.__dict__, filename)

    def client_remove(ID):
        remove_data_json(ID, filename)




