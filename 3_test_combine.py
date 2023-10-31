import unittest
from combine import generate_combinations_fortest


class TestConvertArrayOfArraysFunction(unittest.TestCase):
    def test_example1(self):
        source = [[1], [2], [3, 4], [5, 6], [7, 8]]
        result = generate_combinations_fortest(source)
        expected_result = [
            [1, 2, 3, 5, 7],
            [1, 2, 3, 5, 8],
            [1, 2, 3, 6, 7],
            [1, 2, 3, 6, 8],
            [1, 2, 4, 5, 7],
            [1, 2, 4, 5, 8],
            [1, 2, 4, 6, 7],
            [1, 2, 4, 6, 8]
        ]
        self.assertEqual(result, expected_result)

    def test_example2(self):
        source = [[1], [2, 3], [4, 5, 6]]
        result = generate_combinations_fortest(source)
        expected_result = [
            [1, 2, 4],
            [1, 2, 5],
            [1, 2, 6],
            [1, 3, 4],
            [1, 3, 5],
            [1, 3, 6]
        ]
        self.assertEqual(result, expected_result)

    def test_empty_input(self):
        source = []
        result = generate_combinations_fortest(source)
        self.assertEqual(result, [[]])

    def test_single_array(self):
        source = [[1, 2, 3]]
        result = generate_combinations_fortest(source)
        expected_result = [[1], [2], [3]]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
