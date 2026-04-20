# Function to test

def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return "Invalid age"
import unittest

class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        self.assertEqual(categorize_by_age(5), "Child")

    def test_adolescent(self):
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self):
        self.assertEqual(categorize_by_age(30), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(70), "Golden age")

    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age")

    def test_boundary_child(self):
        self.assertEqual(categorize_by_age(9), "Child")

    def test_boundary_adolescent(self):
        self.assertEqual(categorize_by_age(10), "Adolescent")

    def test_boundary_adult(self):
        self.assertEqual(categorize_by_age(19), "Adult")

    def test_upper_limit(self):
        self.assertEqual(categorize_by_age(150), "Golden age")

    def test_above_limit(self):
        self.assertEqual(categorize_by_age(151), "Invalid age")

if __name__ == "__main__":
    unittest.main()