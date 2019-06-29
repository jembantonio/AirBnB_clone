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
        key = self.__class__.__name__ + "." + self.id
        self.__objects[key] = obj

    def save(self):
        dict_dict = {}
        for key in self.all():
            turn_dict = self.all()
            dict_dict[self.new()] = turn_dict.to_dict()
        with open (self.file_path, mode='w', encoding='utf-8') as my_file: 
            json.dumps(dict_dict, my_file)

    def reload(self):
               
