import unittest

from ArticleFetcher import ArticleFetcher


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.articleFetcher = ArticleFetcher()

    def test_checkArticleFilesSize(self):
        self.assertEqual(0, self.articleFetcher.checkArticleFilesSize())
        self.assertEqual(0, self.articleFetcher.checkArticleFilesSize("test/"))

    def test_get_articles(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
