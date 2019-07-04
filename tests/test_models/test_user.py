#!/usr/bin/python3
''' user class unittest module
'''

import unittest
from models.user import User


class Test_User(unittest.TestCase):

        def test_email(self):
            email = User()
            assert isinstance(email.email, str)

        def test_password(self):
            pw = User()
            assert isinstance(pw.password, str)

        def test_first_name(self):
            fn = User()
            assert isinstance(fn.first_name, str)

        def test_last_name(self):
            ln = User()
            assert isinstance(ln.last_name, str)
