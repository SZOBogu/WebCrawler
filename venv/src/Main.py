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
    linksFile = "linksFetched.csv"
    articlesFiles = "Articles/article"
    wordCountFilePath = "wordQuantity.csv"
    firstWordOccFilePath = "wordFirstOccurrence.csv"
    wordListFile = 'wordList.csv'

    artFetcher = ArticleFetcher.ArticleFetcher()
    linkFetcher = LinkFetcher.LinkFetcher()
    dataFileGen = DataFileGenerator.DataFileGenerator()
    articleAnalyzer = ArticleAnalyzer.ArticleAnalyzer()

    init_links()
    articlesSize = input("Enter your minimal article files size (in bytes): ")

    num_lines = linkFetcher.linkCount(linksFile)

    if(artFetcher.checkArticleFilesSize() > articlesSize):
        if(num_lines > 10000):
            #num_lines = 3
            for i in range(num_lines):
                linkFetcher.getLinks('linksFetched.csv', i)

            dataFileGen.generate_article_csvs(articlesFiles, firstWordOccFilePath, wordCountFilePath)
            articleAnalyzer.generate_dictionary(articlesFiles, wordListFile)

            listaOcc = articleAnalyzer.generateFirstOccurrenceOfWordCsv(firstWordOccFilePath)
            listaQuan = articleAnalyzer.generateWordCountCsv(wordCountFilePath)

            suma = 0
            for i in range(len(listaQuan)):
                suma += listaQuan[i]
            print(suma)

            print(listaQuan)
            for i in range(len(listaQuan)):
                listaQuan[i] = listaQuan[i]/sum

            print(listaQuan)
        else:
            for i in range(num_lines, linkFetcher.linkCount(linksFile)):
                linkFetcher.getLinks(linksFile, i)
                num_lines = linkFetcher.linkCount(linksFile)


if __name__ == '__main__':
    main()