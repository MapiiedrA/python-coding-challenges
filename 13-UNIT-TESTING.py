import unittest
from datetime import datetime, date

"""
Unit Testing Exercises
"""

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("The arguments must be integers or floats.")
    return a + b

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)

"""
EXTRA CHALLENGE
* Create a dictionary with the following keys and values:
 * "name": "Your name"
 * "age": "Your age"
 * "birth_date": "Your birth date"
 * "programming_languages": ["List of programming languages"]
 * Create two tests:
 * - A first test that determines all fields exist.
 * - A second test that determines the entered data is correct.
"""

data = {
    "name": "Mauricio Piedra",
    "age": 32,
    "birth_date": datetime.strptime("21/08/1994", "%d/%m/%Y").date(),
    "programming_languages": ["Python"]
}

class TestData(unittest.TestCase):

    def setUp(self):
        self.data = data  #The Object: -this data is used to link the real data of the APP

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_correctness(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

unittest.main()