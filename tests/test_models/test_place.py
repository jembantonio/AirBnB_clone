#!/usr/bin/python3
''' base class unittest module
'''

import unittest
import models
from models.place import Place
from datetime import datetime


class Test_Place(unittest.TestCase):
    ''' test cases for base class
    '''
    def test_unique_id(self):
        ''' test 1000 instances to look for unique id's
        '''
        for _ in range(1000):
            p0 = Place()
            p1 = Place()
            self.assertNotEqual(p0, p1)

    def test_char_length_dict(self):
        ''' testing the character length of the id
        '''
        p0 = Place()
        test_dict = p0.to_dict()
        self.assertEqual(len(test_dict['id']), 36)

    def test_char_length_update_at(self):
        ''' testing the character length of the updated_at
        '''
        p0 = Place()
        test_dict = p0.to_dict()
        self.assertEqual(len(test_dict['updated_at']), 26)

    def test_char_length_created_at(self):
        ''' testing the character length of the created_at
        '''
        p0 = Place()
        test_dict = p0.to_dict()
        self.assertEqual(len(test_dict['created_at']), 26)

    def test_bad_kwargs_id(self):
        ''' testing bad kwargs for id
        '''
        test_kwargs = {'id': '1'}
        p0 = Place(**test_kwargs)
        self.assertEqual(p0.id, '1')

    def test_bad_kwargs_update(self):
        ''' testing bad kwargs for update_at
        '''
        with self.assertRaises(ValueError,
                               msg="time data '1' does not match format" +
                               "%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'updated_at': '1'}
            Place(**test_kwargs)

    def test_bad_kwargs_create(self):
        ''' testing bad kwargs for create_at
        '''
        with self.assertRaises(ValueError, msg="time data '1' does not match" +
                               "format '%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'created_at': '1'}
            Place(**test_kwargs)

    def test_uuid_unique(self):
        ''' use a set to test if each uuid is unique
        '''
        for _ in range(100):
            my_list = []
            my_set = set()
            p0 = Place()
            my_set.add(p0)
            my_list.append(p0)
        self.assertCountEqual(my_set, my_list)

    def test_new_instance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_id_type(self):
        self.assertEqual(str, type(Place().id))

    def test_class_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

    def test_args_unused(self):
        p0 = Place(None)
        self.assertNotIn(None, p0.__dict__.values())

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        p0 = Place()
        self.assertIn("id", p0.to_dict())
        self.assertIn("created_at", p0.to_dict())
        self.assertIn("updated_at", p0.to_dict())
        self.assertIn("__class__", p0.to_dict())
