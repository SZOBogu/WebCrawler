import re
import requests
from bs4 import BeautifulSoup
from Filter import Filter
import csv
from pathlib import Path


class LinkFetcher:
    def __init__(self):
        pass

    def linkCount(self, linksFilePath):

        linksFilePath = Path(linksFilePath)
        linksFilePath.touch(exist_ok=True)

        with open(linksFilePath) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def getLinks(self, linksFilePath, i):
        sett = set()
        setemp = set()
        linksFilePath = Path(linksFilePath)
        linksFilePath.touch(exist_ok=True)

        with open(linksFilePath) as file:
            url = file.read().split('\n')[i]
            source = "https://pl.wikipedia.org/" + url
            data = requests.get(source).text
            soup = BeautifulSoup(data, 'lxml')
            # for line in soup.find_all('p'):
            #     line = line.get_text()
            #     line = re.sub('\W+', ' ', line)
            #     line = line.lower()

            filter = Filter()
            sett = filter.filter(soup.find_all('a'))

            with open(linksFilePath, 'a') as file:
                writer = csv.writer(file, delimiter=' ')
                for link in setemp:
                    print(link)
                    writer.writerow([link])
            return sett
        return sett
