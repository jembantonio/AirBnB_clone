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
        self.__file_path = 'file.json'
        self.__objects = {}

    def file_path(self):
        '''getter for file_path
        '''
        return self.__file_path

    def all(self):
        '''getter for the dict _objects
        '''
        return self.__objects

    def new(self, obj):
        '''setter for __objects
        '''
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        '''saves the base model
        '''
        from models.base_model import BaseModel
        dict_dict = {}
        for key, value in self.all().items():
            dict_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            json.dump(dict_dict, my_file)

    def reload(self):
        '''Reloads the base model
        '''
        from models.base_model import BaseModel
        import os
        if os.path.exists(self.__file_path):
            with open(
                    self.__file_path, mode='r', encoding='utf-8'
                    ) as my_file:
                temp_dict = json.loads(my_file.read())
                dict_obj = {}
                for key, value in temp_dict.items():
                    # use eval later instead of BaseModel
                    dict_obj[key] = BaseModel(**value)
                self.__objects = dict_obj
