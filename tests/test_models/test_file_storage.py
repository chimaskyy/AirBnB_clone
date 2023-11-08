#!/usr/bin/python3
"""
Tests FileStorage class.
"""

import unittest
from models.engine.file_storage import FileStorage
import json
from models.base_model import BaseModel
from models.user import User
import os


class TestFileStorage(unittest.TestCase):
    """
    Tests FileStorage instances methods and attributes.
    """

    def test_private_attribute(self):
        """
        Tries to access private class attributes
        """

        storage = FileStorage()

        with self.assertRaises(AttributeError):
            storage.__objects
        with self.assertRaises(AttributeError):
            storage.__file_path

    def test_method_new_and_all(self):
        """
        tests class method all.
        """

        model = BaseModel()

        storage = FileStorage()

        storage.new(model)
        self.assertIsInstance(storage.all(), dict)
        self.assertIn(model.__class__.__name__ + '.' + model.id, storage.all())

        self.assertEqual(model.to_dict(), storage.all()["BaseModel."
                                                        + model.id])
        model2 = BaseModel(**{"id": "120859ir6",
                              "name": "instance12",
                              "my_number": 90})
        self.assertNotIn("BaseModel." + model2.id, storage.all())
        storage.new(model2)
        self.assertEqual(model2.to_dict(), storage.all()["BaseModel."
                                                         + model2.id])

    def test_save(self):
        """
        Tests file storage save method.
        """

        store = FileStorage()
        model = BaseModel()
        model_user = User()
        model_user.name = "Pius Aaron"
        model.save()
        with open("file.json", "r", encoding='utf-8') as json_file:
            data = json.load(json_file)

        self.assertTrue(model.to_dict() in data.values())

        model_user.save()
        with open("file.json", "r", encoding='utf-8') as json_file:
            data = json.load(json_file)

        self.assertTrue(model_user.to_dict() in data.values())

    def test_reload(self):
        """
        Test FileStorage reload method.
        """

        store = FileStorage()
        store.reload()

        with open("file.json", "r", encoding='utf-8') as json_file:
            data = json.load(json_file)

        self.maxDiff = None
        self.assertEqual(store.all(), data)

        os.remove("file.json")
        store.reload()
