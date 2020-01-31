import re
import requests
from bs4 import BeautifulSoup
from Filter import Filter

class LinkFetcher:
    def file_len(self):
        with open('linksFetched.csv') as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def get_links(self, i):
        sett = set()
        with open('linksForStartup.csv') as file:
                url = file.read().split('\n')[i]
                source = "https://pl.wikipedia.org/" + url
                data = requests.get(source).text
                soup = BeautifulSoup(data, 'lxml')
                for line in soup.find_all('p'):
                    link = line.get_text()
                    link = re.sub('\W+', ' ', link)
                    link = link.lower()

                filter = Filter()
                sett = filter.filter(soup.find_all('a'))
        return sett