import unittest
from mysolution import mysolution


class TestMySolutionFunction(unittest.TestCase):
    def test_example1(self):
        input_str = "abacabadabacaba"
        result = mysolution(input_str)
        self.assertEqual(result, 'd')

    def test_example2(self):
        input_str = "programming"
        result = mysolution(input_str)
        self.assertEqual(result, 'p')

    def test_no_unique_character(self):
        input_str = "hello"
        result = mysolution(input_str)
        self.assertEqual(result, 'h')

    def test_empty_string(self):
        input_str = ""
        result = mysolution(input_str)
        self.assertEqual(result, '_')

    def test_all_unique_characters(self):
        input_str = "abcdef"
        result = mysolution(input_str)
        self.assertEqual(result, 'a')


if __name__ == '__main__':
    unittest.main()
