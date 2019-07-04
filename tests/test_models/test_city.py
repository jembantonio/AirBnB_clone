#!/usr/bin/python3
''' base class unittest module
'''

import unittest
import models
from models.city import City
from datetime import datetime


class Test_City(unittest.TestCase):
    ''' test cases for base class
    '''
    def test_unique_id(self):
        ''' test 1000 instances to look for unique id's
        '''
        for _ in range(1000):
            c0 = City()
            c1 = City()
            self.assertNotEqual(c0, c1)

    def test_char_length_dict(self):
        ''' testing the character length of the id
        '''
        c0 = City()
        test_dict = c0.to_dict()
        self.assertEqual(len(test_dict['id']), 36)

    def test_char_length_update_at(self):
        ''' testing the character length of the updated_at
        '''
        c0 = City()
        test_dict = c0.to_dict()
        self.assertEqual(len(test_dict['updated_at']), 26)

    def test_char_length_created_at(self):
        ''' testing the character length of the created_at
        '''
        c0 = City()
        test_dict = c0.to_dict()
        self.assertEqual(len(test_dict['created_at']), 26)

    def test_bad_kwargs_id(self):
        ''' testing bad kwargs for id
        '''
        test_kwargs = {'id': '1'}
        c0 = City(**test_kwargs)
        self.assertEqual(c0.id, '1')

    def test_bad_kwargs_update(self):
        ''' testing bad kwargs for update_at
        '''
        with self.assertRaises(ValueError,
                               msg="time data '1' does not match format" +
                               "%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'updated_at': '1'}
            City(**test_kwargs)

    def test_bad_kwargs_create(self):
        ''' testing bad kwargs for create_at
        '''
        with self.assertRaises(ValueError, msg="time data '1' does not match" +
                               "format '%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'created_at': '1'}
            City(**test_kwargs)

    def test_uuid_unique(self):
        ''' use a set to test if each uuid is unique
        '''
        for _ in range(100):
            my_list = []
            my_set = set()
            c0 = City()
            my_set.add(c0)
            my_list.append(c0)
        self.assertCountEqual(my_set, my_list)

    def test_new_instance(self):
        self.assertIn(City(), models.storage.all().values())

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_class_datetime(self):
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))

    def test_args_unused(self):
        c0 = City(None)
        self.assertNotIn(None, c0.__dict__.values())
