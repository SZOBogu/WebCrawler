import unittest

from Filter import Filter


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = Filter()

    def test_filter(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
