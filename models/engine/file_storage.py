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

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, obj):
        self.__objects = obj

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
        from models.base_model import BaseModel
        key = self.__class__.__name__ + ".id"
        return key

    def save(self):
        from models.base_model import BaseModel
        dict_dict = {}
        for key in self.all():
            turn_dict = self.all()
            dict_dict[self.new(turn_dict)] = key.to_dict()
        with open (self.file_path, mode='w', encoding='utf-8') as my_file: 
            json.dump(dict_dict, my_file)

    def reload(self):
        import os
        if os.path.exists(self.file_path):
            with open (self.file_path, mode='r', encoding='utf-8') as my_file:
                temp_dict = json.loads(my_file.read())
                from models.base_model import BaseModel
                dict_obj = BaseModel.to_dict(**temp_dict)
                self.objects = dict_obj
