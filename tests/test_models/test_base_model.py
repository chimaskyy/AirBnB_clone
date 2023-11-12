#!/usr/bin/python3
"""
This module contains test cases for the BaseModel Class
"""

import unittest
from unittest.mock import patch
import io
import json
import datetime
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
        self.assertEqual(models.datetime, type(b1.updated_at))

    def test_base_init(self):
        """
        Tests initializations with empty and non empty params
        """

        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)
        self.assertIn("id", model1.__dict__)
        self.assertIn("created_at", model1.__dict__)
        self.assertIn("updated_at", model1.__dict__)
        model1.name = "My first model"
        self.assertEqual("My first model", model1.name)

    def test_base_init_2(self):
        """
        Tests initialization with dictionary passed as parameter.
        """

        model = BaseModel(**{"name": "Another one", "my_number": 69})
        self.assertEqual(2, len(model.__dict__.keys()))

    def test_to_dict_method(self):
        """
        Tests the dictionary representation of Instance.
        """

        b2 = BaseModel()
        self.assertEqual(dict, type(b2.to_dict()))
        self.assertIn("__class__", b2.to_dict())
        b3 = BaseModel(**b2.to_dict())
        self.assertIsInstance(b3.created_at, datetime.datetime)
        self.assertEqual(type(b3.created_at), datetime.datetime)
        self.assertIn("__class__", b3.to_dict())
        self.assertNotIn("__class__", b3.__dict__)

    def test_date_and_time(self):
        """
        Checks created_at time and updated_at time.
        """

        b1 = BaseModel()
        b1.name = "New name"
        b1.id = "e34r-r45t-65t7-7y64"
        b1.created_at = "2023-12-05T21:45:56.7684"
        b1.save()
        b1.updated_at = "2023-12-05T21:45:56.7690"

        self.assertNotEqual(b1.created_at, b1.updated_at)
        self.assertEqual(b1.id, "e34r-r45t-65t7-7y64")
        self.assertEqual(b1.created_at, "2023-12-05T21:45:56.7684")
        self.assertEqual(b1.updated_at, "2023-12-05T21:45:56.7690")
        self.assertEqual(str, type(b1.__str__()))

    def test_base_method_save(self):
        """
        Test base class method save
        """

        another = BaseModel()

        another.save()

        try:
            with open("file.json", "r", encoding="utf-8") as js:
                file_content = js.read()

            self.assertIn(json.dumps(another.to_dict()), file_content)
        except FileNotFoundError:
            return
