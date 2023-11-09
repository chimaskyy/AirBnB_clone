#!/usr/bin/python3
"""
Unit test for Place class.
"""

import unittest
from models.state import State
from models.user import User


class TestStateClass(unittest.TestCase):
    """
    test the State Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        state = State()

        self.assertEqual(state.name, "")

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        state = State()

        self.assertIsInstance(state.name, str)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        state = State()

        state.name = "Taraba Jalingo"
        self.assertEqual(state.name, "Taraba Jalingo")
        self.assertNotEqual(state.name, State().name)

    def test_to_dict(self):
        """Test to dict"""
        state = State()

        self.assertNotIn("name", state.to_dict())

        state.name = "Ojuelegba"

        self.assertIn("name", state.to_dict())
