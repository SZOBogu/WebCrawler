import requests
from bs4 import BeautifulSoup
from Filter import Filter
import csv
from pathlib import Path
import os


class LinkFetcher:
    def linkCount(self, linksFilePath):
        linksFilePath = Path(linksFilePath)
        linksFilePath.touch(exist_ok=True)

        with open(linksFilePath) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def getLinks(self, linksFilePath, i):
        sett = set()
        linksFilePath = Path(linksFilePath)
        linksFilePath.touch(exist_ok=True)

        if(os.stat(linksFilePath).st_size != 0):
            with open(linksFilePath) as file:
                url = file.read().split('\n')[i]
                source = "https://pl.wikipedia.org/" + url
                data = requests.get(source).text
                soup = BeautifulSoup(data, 'lxml')

                filter = Filter()
                sett = filter.filter(soup.find_all('a'))

                with open(linksFilePath, 'a') as file:
                    writer = csv.writer(file, delimiter=' ')
                    for link in sett:
                        writer.writerow([link])
                return sett
        else:
            print('file empty')
        return sett