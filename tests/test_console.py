#!/usr/bin/python3
"""
Test for the consol interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import console


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

    def test_show_with_class_name_withno_instance(self):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show User")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Place")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Amenity")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show City")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Review")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show State")
            output = mock_stdout.getvalue().strip()
            expected = """** instance id missing **"""

            self.assertEqual(output, expected)

    def test_show_with_class_name_with_invalid_ID(self):
        """
        Test the show command with no class name
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show BaseModel wer43-rt45r")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show User fhgdjt-hrety")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Place tr5etr-jjef")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Amenity 564fi-hte64")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show City 65gejykgjf")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show Review 7ytr8gdy")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            console.HBNBCommand().onecmd("show State 746tgjeytrew")
            output = mock_stdout.getvalue().strip()
            expected = """** no instance found **"""

            self.assertEqual(output, expected)
