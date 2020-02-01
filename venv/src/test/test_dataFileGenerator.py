import unittest

from DataFileGenerator import DataFileGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = DataFileGenerator()

    def test_generate_article_csvs(self):
        self.assertEqual(True, False)

    def test_generate_csv(self):
        self.assertEqual(True, False)

    def test_megre_csvs(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
