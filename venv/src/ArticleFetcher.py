import csv
import os
import re
import requests
from bs4 import BeautifulSoup


class ArticleFetcher:
    def checkArticleFilesSize(self, path="Articles/"):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def get_article(self, linksFile, articlesFile, i):
        with open(articlesFile + '%i.txt' % i, 'w') as article:
            with open(linksFile) as file:
                url = file.read().split('\n')[i]
                source = "https://pl.wikipedia.org/" + url
                data = requests.get(source).text    #tekst htmla
                soup = BeautifulSoup(data, 'lxml')  #tekst htmla z metodami bs4
                writer = csv.writer(article)
                for line in soup.find_all('p'):
                    line = line.get_text()
                    line = re.sub('\W+', ' ', line)
                    line = line.strip('"')
                    line = line.lower()
                    print(line)
                    writer.writerow([line])