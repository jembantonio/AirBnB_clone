#!/usr/bin/python3
''' user class unittest module
'''

import unittest
from models.user import User


class Test_User(unittest.TestCase):
    '''test for user
    '''
    def test_email(self):
        '''test if email is a string
        '''
        email = User()
        assert isinstance(email.email, str)

    def test_password(self):
        '''test if password is a string
        '''
        pw = User()
        assert isinstance(pw.password, str)

    def test_first_name(self):
        '''test if first name is a string
        '''
        fn = User()
        assert isinstance(fn.first_name, str)

    def test_last_name(self):
        '''test if last name is a string
        '''
        ln = User()
        assert isinstance(ln.last_name, str)
