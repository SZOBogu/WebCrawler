import csv
import os
import re
import requests
from bs4 import BeautifulSoup


class ArticleFetcher:
    def checkArticleFilesSize(self):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk('Articles'):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def get_articles(self, i):
        with open('Articles/article%i.txt' % i, 'w') as article:
            with open('linksFetched.csv') as file:
                url = file.read().split('\n')[i]
                source = "https://pl.wikipedia.org/" + url
                data = requests.get(source).text
                soup = BeautifulSoup(data, 'lxml')
                writer = csv.writer(article)
                for line in soup.find_all('p'):
                    link = line.get_text()
                    link = re.sub('\W+', ' ', link)
                    link = link.strip('"')
                    link = link.lower()
                    print(link)
                    writer.writerow([link])
