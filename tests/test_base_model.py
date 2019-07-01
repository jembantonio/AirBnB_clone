#!/usr/bin/python3
''' base class unittest module
'''

import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    ''' test cases for base class
    '''
    def test_unique_id(self):
        ''' test 1000 instances to look for unique id's
        '''
        for _ in range(1000):
            bm0 = BaseModel()
            bm1 = BaseModel()
            self.assertNotEqual(bm0, bm1)

    def test_char_length_dict(self):
        ''' testing the character length of the id
        '''
        bm0 = BaseModel()
        test_dict = bm0.to_dict()
        self.assertEqual(len(test_dict['id']), 36)

    def test_char_length_update_at(self):
        ''' testing the character length of the updated_at
        '''
        bm0 = BaseModel()
        test_dict = bm0.to_dict()
        self.assertEqual(len(test_dict['updated_at']), 26)

    def test_char_length_created_at(self):
        ''' testing the character length of the created_at
        '''
        bm0 = BaseModel()
        test_dict = bm0.to_dict()
        self.assertEqual(len(test_dict['created_at']), 26)

    def test_bad_kwargs_id(self):
        ''' testing bad kwargs for id
        '''
        test_kwargs = {'id': '1'}
        bm0 = BaseModel(**test_kwargs)
        self.assertEqual(bm0.id, '1')

    def test_bad_kwargs_update(self):
        ''' testing bad kwargs for update_at
        '''
        with self.assertRaises(ValueError, msg="time data '1' does not match format '%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'updated_at': '1'}
            BaseModel(**test_kwargs)

    def test_bad_kwargs_create(self):
        ''' testing bad kwargs for create_at
        '''
        with self.assertRaises(ValueError, msg="time data '1' does not match format '%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'created_at': '1'}
            BaseModel(**test_kwargs)
