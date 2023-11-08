#!/bin/python3
"""
Contains Unit test for User Class.
"""

import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """
    Test User Class attributes and methods.
    """

    def test_attributes(self):
        """
        Tests class attributes and also assigning values to em
        """

        user = User()

        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)
        
        # Tests Values before assignment
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        # Tests Values after assignment
        self.assertNotEqual(user.email, "")
        self.assertNotEqual(user.password, "")
        self.assertNotEqual(user.first_name, "")
        self.assertNotEqual(user.last_name, "")
