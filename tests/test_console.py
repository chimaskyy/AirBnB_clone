#!/usr/bin/python3
"""
Test for the console interpreter
"""

import re
import unittest
from unittest.mock import patch
from io import StringIO
import console
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import json


class Testconsole(unittest.TestCase):
    """
    Test for the console
    """

    def test_show_no_class_name(self):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show")
            output = mock_stdout.getvalue().strip()

            self.assertEqual(output, "** class name missing **")

    def test_help_show(self):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("help show")
            output = mock_stdout.getvalue().strip()
            expected = """Prints the string representation of an
instance based on the class name and id"""

            self.assertEqual(output, expected)

    def helper_test_show_with_class_name(self, class_name):
        """
        tests show with class name
        """

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show {}".format(class_name))
            output = mock_stdout.getvalue().strip()
            if class_name in FileStorage().Classes():
                expected = """** instance id missing **"""
            else:
                expected = """** class doesn't exist **"""

            self.assertEqual(output, expected)

    def test_show_for_all_classes_with_no_id_no_class(self):
        """
        tests show for all classes without id or invlaid class name
        """

        self.helper_test_show_with_class_name("User")
        self.helper_test_show_with_class_name("BaseModel")
        self.helper_test_show_with_class_name("City")
        self.helper_test_show_with_class_name("Amenity")
        self.helper_test_show_with_class_name("State")
        self.helper_test_show_with_class_name("Place")
        self.helper_test_show_with_class_name("Review")

    def helper_test_show_with_class_name_with_invalid_ID(self, class_name):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd(
                    "show {} wer43-rt45r".format(class_name))
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

    def test_class_with_invalid_id(self):
        """
        test with invalid Id but with correct class
        """
        self.helper_test_show_with_class_name_with_invalid_ID("User")
        self.helper_test_show_with_class_name_with_invalid_ID("BaseModel")
        self.helper_test_show_with_class_name_with_invalid_ID("City")
        self.helper_test_show_with_class_name_with_invalid_ID("Amenity")
        self.helper_test_show_with_class_name_with_invalid_ID("State")
        self.helper_test_show_with_class_name_with_invalid_ID("Place")
        self.helper_test_show_with_class_name_with_invalid_ID("Review")

    def test_show_with_class_name_with_valid_ID(self):
        """
        Test the show command with no class name
        """
        b1 = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show BaseModel {}".format(b1.id))
            output = mock_stdout.getvalue().strip()
            expected = str(b1)

            self.assertEqual(output, expected)

        u1 = User()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show User {}".format(u1.id))
            output = mock_stdout.getvalue().strip()
            expected = str(u1)

            self.assertEqual(output, expected)

        p1 = Place()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Place {}".format(p1.id))
            output = mock_stdout.getvalue().strip()
            expected = str(p1)

            self.assertEqual(output, expected)

        amenity = Amenity()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Amenity {}".format(amenity.id))
            output = mock_stdout.getvalue().strip()
            expected = str(amenity)

            self.assertEqual(output, expected)

        city = City()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show City {}".format(city.id))
            output = mock_stdout.getvalue().strip()
            expected = str(city)

            self.assertEqual(output, expected)

        review = Review()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Review {}".format(review.id))
            output = mock_stdout.getvalue().strip()
            expected = str(review)

            self.assertEqual(output, expected)

        state = State()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show State {}".format(state.id))
            output = mock_stdout.getvalue().strip()
            expected = str(state)

            self.assertEqual(output, expected)

    def test_all_with_no_class_name(self):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                data = json.load(f)
                expected = [str(FileStorage().Classes()
                                [re.search(r'([A-Za-z]+)\.',
                                           k).groups()[0]]
                                (**data[k]))for k in data]
                expected = json.dumps(expected)
                self.assertEqual(output, expected)
        except FileNotFoundError:
            pass

    def helper_test_all_with_class(self, class_name):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("all {}".format(class_name))
            output = mock_stdout.getvalue().strip()

        try:
            with open("file.json", "r", encoding='utf-8') as f:
                data = json.load(f)
                expected = [str(FileStorage().Classes()[class_name]
                                (**data[k]))for k in data if class_name in k]
                expected = json.dumps(expected)
                self.assertEqual(output, expected)
        except FileNotFoundError:
            pass

    def test_all_with_all_classes(self):
        """
        test all with class name provided
        """

        self.helper_test_all_with_class("BaseModel")
        self.helper_test_all_with_class("User")
        self.helper_test_all_with_class("City")
        self.helper_test_all_with_class("State")
        self.helper_test_all_with_class("Place")
        self.helper_test_all_with_class("Review")
        self.helper_test_all_with_class("Amenity")
