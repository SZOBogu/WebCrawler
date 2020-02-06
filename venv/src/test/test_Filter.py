import unittest

from Filter import Filter

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = Filter()
        self.strToBeFiltered0 = "<a href=\"/wiki/Plik:Klodt_Michail_Petrovich_-_Raskolnikov_and_Marmeladov.jpg\" class=\"image\">"
        self.strToBeFiltered1 = "test"
        self.strToBeFiltered2 = "<a href=\"/wiki/Pomoc:Kontrola_autorytatywna\">"
        self.strToBeFiltered3 = "/wiki/13_Posterunek"
        self.strToBeFiltered4 = "https://pl.wikipedia.org/wiki/Zbrodnia_i_kara"

        self.strToPassThrough0 = "<a href=\"/wiki/Katorga\" title=\"Katorga\">"
        self.strToPassThrough1 = "<a href=\"/wiki/Plik:Klodt_Michail_Petrovich_-_Raskolnikov_and_Marmeladov.jpg\" class=\"image\">"
        self.strToPassThrough2 = "<a href=\"/wiki/Wiesbaden\" title=\"Wiesbaden\">"
        self.strToPassThrough3 = "<a href=\"/wiki/Alkoholizm\" title=\"Alkoholizm\">"
        self.strToPassThrough4 = "<a href=\"/wiki/Syberia\" title=\"Syberia\">"

        self.mixedList0 = [self.strToPassThrough0, self.strToBeFiltered1, self.strToPassThrough2, self.strToPassThrough3, self.strToBeFiltered4]
        self.mixedList1 = [self.strToBeFiltered0, self.strToPassThrough1, self.strToBeFiltered2, self.strToPassThrough3, self.strToBeFiltered4]

        self.listToFail = [self.strToBeFiltered0, self.strToBeFiltered1, self.strToBeFiltered2,
                           self.strToBeFiltered3, self.strToBeFiltered4]
        self.listToPass = [self.strToPassThrough0, self.strToPassThrough1, self.strToPassThrough2,
                           self.strToPassThrough3, self.strToPassThrough4]

    def test_filter(self):
        self.assertEqual(set(), self.filter.filter(self.mixedList0))
        self.assertEqual(set(), self.filter.filter(self.mixedList1))
        self.assertEqual(set(), self.filter.filter(self.listToFail))
        self.assertEqual(set(), self.filter.filter(self.listToPass))

if __name__ == '__main__':
    unittest.main()
