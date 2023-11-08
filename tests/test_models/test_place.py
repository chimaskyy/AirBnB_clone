#!/usr/bin/python3
"""
Unit test for Place class.
"""

import unittest
from models.place import Place
from models.user import User

class TestPlaceClass(unittest.TestCase):
    """
    test the Place Class.
    """

    def test_attributes(self):
        """
        test instance attributes
        """

        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes_types(self):
        """
        test class attributes types.
        """

        place = Place()

        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_attributes_setting(self):
        """
        Try setting instance attributes.
        """

        place = Place()
        user = User()

        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)
        self.assertNotEqual(place.user_id, Place.user_id)
        place.name = "Basilica of Santa Maria"
        self.assertEqual(place.name, "Basilica of Santa Maria")
        self.assertNotEqual(place.name, Place.name)
