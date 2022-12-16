from json_helper import write_json, remove_data_json, edit_data_json, search_client_prosprop_data_json, id_generate

# "Database File Location"
filename = 'client_list.json'

class Client:

    def __init__(self, NAME = '', EMAIL = '', SUBURB = '', PRICE = 0, ID = 0):
        self.ID = id_generate()
        self.NAME = NAME
        self.EMAIL = EMAIL
        self.SUBURB = SUBURB
        self.PRICE = PRICE
  
    def client_save(self):
        write_json(self.__dict__, filename)
    
    def client_remove(self):
        remove_data_json(self.ID, filename)
    
    def client_edit(self):
        edit_data_json(self.ID, filename)

    def client_search(self):
        search_client_prosprop_data_json(self.ID)

    # def client_add_ID(self):
    #     id_generate(self.__dict__)






