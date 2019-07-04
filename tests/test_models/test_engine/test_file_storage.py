#!/usr/bin/python3
''' file_storage class unittest module
'''

import unittest
from models.engine.file_storage import FileStorage


class Test_Filestorage(unittest.TestCase):
    '''test for filestorage
    '''
    def test_file_path(self):
        '''test if file_path is a string
        '''
        fs = FileStorage()
        assert isinstance(fs._FileStorage__file_path, str)

    def test_objects(self):
        '''test if test_objects is a string
        '''
        fs = FileStorage()
        assert isinstance(fs._FileStorage__objects, dict)

    def test_all(self):
        '''test if all returns the correct objects
        '''
        fs = FileStorage()
        self.assertEqual(fs.all(), fs._FileStorage__objects)
