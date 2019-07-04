#!/usr/bin/python3
''' base class unittest module
'''

import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    '''test for review
    '''
    def test_place_id(self):
        '''test to see if place_id is a string
        '''
        pid = Review()
        assert isinstance(pid.place_id, str)

    def test_user_id(self):
        '''test to see if user_id is a string
        '''
        uid = Review()
        assert isinstance(uid.user_id, str)

    def test_text(self):
        '''test to see if text is a string
        '''
        t = Review()
        assert isinstance(t.text, str)
