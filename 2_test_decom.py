import unittest
from decom import compress, decompress


class TestRunLengthEncodingFunctions(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress("HELLOOO"), "1H1E2L3O")
        self.assertEqual(compress("BWAAALAAA"), "1B1W3A1L3A")
        self.assertEqual(compress("AAAABBBCCDAA"), "4A3B2C1D2A")
        self.assertEqual(compress(""), "")

    def test_decompress(self):
        self.assertEqual(decompress("1H1E2L3O"), "HELLOOO")
        self.assertEqual(decompress("1B1W3A1L3A"), "BWAAALAAA")
        self.assertEqual(decompress("4A3B2C1D2A"), "AAAABBBCCDAA")
        self.assertEqual(decompress(""), "")


if __name__ == '__main__':
    unittest.main()
