from json_helper import write_json, remove_data_json

# "Database File Location"
filename = 'property_list.json'

class Property:
    def __init__(self, ID= 12345, suburb = '', price = ''):
        self.ID = ID
        self.suburb = suburb
        self.price = price
  
    def property_save(self):
        write_json(self.__dict__, filename)
    
    def property_remove(self):
        remove_data_json(self.ID, filename)



