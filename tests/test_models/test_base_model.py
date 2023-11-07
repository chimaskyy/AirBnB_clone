#!/usr/bin/python3
"""
This module contains test cases for the BaseModel Class
"""

import unittest
from unittest.mock import patch
import io
import models.base_model as models
from models.base_model import BaseModel


class TestBaseModels(unittest.TestCase):
    """
    Test the BaseModel object instances.
    """

    def test_base_id(self):
        """
        checks the id of base instances
        """

        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))
        self.assertEqual(models.datetime, type(b1.created_at))

    def test_to_dict_method(self):
        """
        Tests the dictionary representation of Instance.
        """

        b2 = BaseModel()
        self.assertEqual(dict, type(b2.to_dict()))

    def test_date_and_time(self):
        """
        Checks created_at time and updated_at time.
        """

        b1 = BaseModel()
        b1.name = "New name"

        self.assertNotEqual(b1.created_at, b1.updated_at)
        self.assertEqual(str, type(b1.__str__()))
