from helper import write_json, remove_data_json, edit_data_json, search_client_prosprop_data_json, id_generate

# 'Database File Location'
filename = 'json_files/client_list.json'

class Client:

    def __init__(self, name = '', email = '', suburb = '', price = 0, id = None):
        if id == None:
            self.id = id_generate()
        else:
            self.id = id
        self.name = name
        self.email = email
        self.suburb = suburb
        self.price = price
  
    def client_save(self):
        write_json(self.__dict__, filename)
    
    def client_remove(self):
        remove_data_json(self.id, filename)
    
    def client_edit(self):
        edit_data_json(self.id, filename)

    def client_search(self):
        search_client_prosprop_data_json(self.id)







