from json_helper import write_json, remove_data_json

# "Database File Location"
filename = 'client_list.json'

class Client:
    def __init__(self, name = '', suburb = '', price = '', ID = ''):
        self.ID = 12345
        self.name = name
        self.suburb = suburb
        self.price = price
  
    def client_save(self):
        write_json(self.__dict__, filename)
    
    def client_remove(self):
        remove_data_json(self.ID, filename)




