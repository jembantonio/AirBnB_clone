#!/usr/bin/python3
''' base class unittest module
'''

import unittest
import models
from models.state import State
from datetime import datetime


class Test_State(unittest.TestCase):
    ''' test cases for base class
    '''
    def test_unique_id(self):
        ''' test 1000 instances to look for unique id's
        '''
        for _ in range(1000):
            s0 = State()
            s1 = State()
            self.assertNotEqual(s0, s1)

    def test_char_length_dict(self):
        ''' testing the character length of the id
        '''
        s0 = State()
        test_dict = s0.to_dict()
        self.assertEqual(len(test_dict['id']), 36)

    def test_char_length_update_at(self):
        ''' testing the character length of the updated_at
        '''
        s0 = State()
        test_dict = s0.to_dict()
        self.assertEqual(len(test_dict['updated_at']), 26)

    def test_char_length_created_at(self):
        ''' testing the character length of the created_at
        '''
        s0 = State()
        test_dict = s0.to_dict()
        self.assertEqual(len(test_dict['created_at']), 26)

    def test_bad_kwargs_id(self):
        ''' testing bad kwargs for id
        '''
        test_kwargs = {'id': '1'}
        s0 = State(**test_kwargs)
        self.assertEqual(s0.id, '1')

    def test_bad_kwargs_update(self):
        ''' testing bad kwargs for update_at
        '''
        with self.assertRaises(ValueError,
                               msg="time data '1' does not match format" +
                               "%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'updated_at': '1'}
            State(**test_kwargs)

    def test_bad_kwargs_create(self):
        ''' testing bad kwargs for create_at
        '''
        with self.assertRaises(ValueError, msg="time data '1' does not match" +
                               "format '%Y-%m-%dT%H:%M:%S.%f'"):
            test_kwargs = {'created_at': '1'}
            State(**test_kwargs)

    def test_uuid_unique(self):
        ''' use a set to test if each uuid is unique
        '''
        for _ in range(100):
            my_list = []
            my_set = set()
            s0 = State()
            my_set.add(s0)
            my_list.append(s0)
        self.assertCountEqual(my_set, my_list)

    def test_new_instance(self):
        self.assertIn(State(), models.storage.all().values())

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_class_datetime(self):
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_args_unused(self):
        s0 = State(None)
        self.assertNotIn(None, s0.__dict__.values())

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        s0 = State()
        self.assertIn("id", s0.to_dict())
        self.assertIn("created_at", s0.to_dict())
        self.assertIn("updated_at", s0.to_dict())
        self.assertIn("__class__", s0.to_dict())
