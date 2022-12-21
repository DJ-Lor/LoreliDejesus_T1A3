from helper import write_json, remove_data_json, edit_data_json,\
     search_prop_owner_data_json, id_generate

# 'Database File Location'
filename = 'json_files/property_list.json'


class Property:
    def __init__(self, suburb='', price=0, id=None):
        if id is None:
            self.id = id_generate()
        else:
            self.id = id
        self.suburb = suburb
        self.price = price

    def property_save(self):
        write_json(self.__dict__, filename)

    def property_remove(self):
        remove_data_json(self.id, filename)

    def property_edit(self):
        edit_data_json(self.id, filename)

    def property_search(self):
        search_prop_owner_data_json(self.id)
