import os
from pathlib import Path

import ArticleAnalyzer
import ArticleFetcher
import DataFileGenerator
import LinkFetcher

def init_links():
    linksFilePath = "linksFetched.csv"
    if(os.path.exists(linksFilePath)):
        path = Path(linksFilePath)
        path.touch()
    elif (os.stat(linksFilePath).st_size != 0):
        with open(linksFilePath, 'a') as file:
            file.write("/wiki/Ghana\n/wiki/Niewolnictwo\n\wiki/Australia_i_Oceania\n/wiki/Rwanda\n/wiki/Malediwy\n/wiki/Azerbejd%C5%BCan\n/wiki/Gliwice")
    else:
        pass
def main():
    #TODO: kontrola wielkości plików

    #wez dane z artykulow
    artFetcher = ArticleFetcher.ArticleFetcher()
    linkFetcher = LinkFetcher.LinkFetcher()
    dataFileGen = DataFileGenerator.DataFileGenerator()
    articleAnalyzer = ArticleAnalyzer.ArticleAnalyzer()

    init_links()

    #num_lines = sum(1 for line in open('linksFetched.csv'))
    # num_lines = 3
    # for i in range(num_lines):
    #     linkFetcher.getLinks('linksFetched.csv', i)

    dataFileGen.generate_article_csvs()
    articleAnalyzer.generate_dictionary()

    listaOcc = articleAnalyzer.generateFirstOccuranceOfWordCsv()
    listaQuan = articleAnalyzer.generateWordCountCsv()

    suma = 0
    for i in range(len(listaQuan)):
        suma += listaQuan[i]
    print(suma)

    print(listaQuan)
    for i in range(len(listaQuan)):
        listaQuan[i] = listaQuan[i]/sum

    print(listaQuan)

if __name__ == '__main__':
    main()