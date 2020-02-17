import unittest

from LinkFetcher import LinkFetcher


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fetcher = LinkFetcher()

    def test_linkCount(self):
        self.assertEqual(14, self.fetcher.linkCount('testLink'))

    def test_getLinks(self):
        sett = {"/wiki/Suomenlinna",
                "/wiki/Plac_Targowy_w_Helsinkach",
                "/wiki/Komisja_Standaryzacji_Nazw_Geograficznych_poza_Granicami_Rzeczypospolitej_Polskiej",
                "/wiki/Helsinki",
                "/wiki/Morze_Ba%C5%82tyckie",
                "/wiki/Suomenlinna",
                "/wiki/Katedra",
                "/wiki/Pa%C5%82ac_Prezydencki_w_Helsinkach",
                "/wiki/Finlandia",
                "/wiki/Szwecja",
                "/wiki/Urz%C4%85d_miejski",
                "/wiki/Wikimedia_Commons",
                "/wiki/Plac_Targowy_w_Helsinkach",
                "/wiki/Ambasada",
                "/wiki/Esplanadi",}
        links = self.fetcher.getLinks('testLink', 1)
        self.assertEqual(sett, links)

if __name__ == '__main__':
    unittest.main()
