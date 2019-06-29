#!/usr/bin/python3

''' Base Class module
'''

from uuid import uuid4
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    ''' BaseModel Class
    '''
    def __init__(self, *args, **kwargs):
        ''' Initializes the BaseModel class
        '''
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(val,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(val,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'id':
                    self.id = val
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self, self.id)

    def __str__(self):
        ''' Prints a BaseModel instance
        '''
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                          self.id,
                                          self.__dict__))

    def save(self):
        ''' Method that updates the public instance attribute updated_at with
            the current datetime
        '''
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        ''' Method that returns a dictionary containing all key/value pairs of
            an instance
        '''
        my_dict = {}
        for key, val in self.__dict__.items():
            my_dict[key] = val
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
