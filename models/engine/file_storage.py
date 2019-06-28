#!/urs/bin/python3
'''Stores files as JSON file type
'''

import json

class FileStorage:
    '''stores files
    '''
    def __init__(self):
        '''inits the file storage attributes
        '''
        __file_path = 'file.json'
        __objects = {}

    @property
    def file_path(self):
        '''getter for file_path
        '''
        return self.__file_path

    @property
    def all(self):
        '''getter for the dict _objects
        '''
        return self.__objects

    @new.setter
    def new(self, obj):
        '''setter for __objects
        '''
        self.__objects = obj
    
    @classmethod
    def save(self):
        with open (self.file_path, mode='w', encoding='utf-8') as my_file: 
            f = {}
            for my_dict in file_data:
                dict_obj = BaseModel.to_dict(**my_dict)
               f.append(dict_obj)
            my_file.write(json.dumps(self.all))

    @classmethod
    def reload(self):
        import os
        from #import base_model.py
        if os.path.exists(self.file_path):
            with open (self.file_path, mode='r', encoding='utf-8') as my_file:
              # file_data = json.loads(my_file.read())
               
