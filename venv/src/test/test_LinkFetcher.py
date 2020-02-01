import unittest

from LinkFetcher import LinkFetcher


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fetcher = LinkFetcher()

    def test_linkCount(self):
        self.assertEqual(3, self.fetcher.linkCount('testLink'))

    def test_getLinks(self):
        sett = {'na jeziorze', 'wielka burza', 'jezus ze mna w lodzi jest'}
        self.assertEqual(sett, self.fetcher.getLinks('testLink', 1))

if __name__ == '__main__':
    unittest.main()
