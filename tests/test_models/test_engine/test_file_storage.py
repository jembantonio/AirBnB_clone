#!/usr/bin/python3
''' file_storage class unittest module
'''

import unittest
from models.engine.file_storage import FileStorage


class Test_Filestorage(unittest.TestCase):

    def test_file_path(self):
        fs = FileStorage()
        assert isinstance(fs._FileStorage__file_path, str)

    def test_objects(self):
        fs = FileStorage()
        assert isinstance(fs._FileStorage__objects, dict)

    def test_all(self):
        fs = FileStorage()
        self.assertEqual(fs.all(), fs._FileStorage__objects)
