from json_helper import write_json, remove_data_json, edit_data_json, search_prop_owner_data_json, id_generate

# "Database File Location"
filename = 'property_list.json'

class Property:
    def __init__(self, SUBURB = '', PRICE = 0, ID = None):
        if ID == None:
            self.ID = id_generate()
        else:
            self.ID = ID
        self.SUBURB = SUBURB
        self.PRICE = PRICE
  
    def property_save(self):
        write_json(self.__dict__, filename)
    
    def property_remove(self):
        remove_data_json(self.ID, filename)

    def property_edit(self):
        edit_data_json(self.ID, filename)

    def property_search(self):
        search_prop_owner_data_json(self.ID)




