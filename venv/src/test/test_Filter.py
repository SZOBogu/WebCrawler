import unittest

import requests
from bs4 import BeautifulSoup

from Filter import Filter

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filter = Filter()
        data = requests.get("https://pl.wikipedia.org/wiki/Suomenlinna").text
        self.soup = BeautifulSoup(data, 'lxml')

    def test_filter(self):
        resultSet = set({'/wiki/Cmentarzysko_z_epoki_br%C4%85zu_w_Sammallahdenm%C3%A4ki',
 '/wiki/Finlandia',
 '/wiki/Helsinki',
 '/wiki/Komitet_%C5%9Awiatowego_Dziedzictwa#Lista_sesji_Komitetu_Światowego_Dziedzictwa',
 '/wiki/Kvarken_P%C3%B3%C5%82nocny',
 '/wiki/Lista_%C5%9Bwiatowego_dziedzictwa_UNESCO',
 '/wiki/Lista_%C5%9Bwiatowego_dziedzictwa_UNESCO#Kryteria',
 '/wiki/Lista_%C5%9Bwiatowego_dziedzictwa_UNESCO#Obiekty_UNESCO_według_regionów',
 '/wiki/Pa%C5%84stwo',
 '/wiki/Pet%C3%A4j%C3%A4vesi',
 '/wiki/Po%C5%82udnik_Struvego',
 '/wiki/Rauma_(miasto)#Zabytkowa_dzielnica_Raumy_(Vanha_Rauma)',
 '/wiki/Rynek_w_Helsinkach',
 '/wiki/Suomenlinna',
 '/wiki/Twierdza',
 '/wiki/UNESCO',
 '/wiki/Verla',
 '/wiki/Vesikko',
 '/wiki/Ziemia'})
        self.assertEqual(resultSet, self.filter.filter(self.soup.find_all('a')))

if __name__ == '__main__':
    unittest.main()
