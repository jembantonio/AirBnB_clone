#!/usr/bin/python3

''' Base Class module
'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    ''' BaseModel Class
    '''
    def __init__(self):
        ''' Initializes the BaseModel class
        '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Prints a BaseModel instance
        '''
        return ("[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        ''' Method that updates the public instance attribute updated_at with
            the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Method that returns a dictionary containing all key/value pairs of
            an instance
        '''
        dict = {}
        for key, val in self.__dict__.items():
            dict[key] = val 
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
