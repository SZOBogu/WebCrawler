import csv
import os
import re
import requests
from bs4 import BeautifulSoup


class ArticleFetcher:
    def checkArticleFilesSize(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def get_articles(self, articlePath, linksFile, i):
        with open(articlePath + '%i.txt' % i, 'w') as article:
            with open(linksFile) as file:
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
