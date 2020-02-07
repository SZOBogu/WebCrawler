import csv
from pathlib import Path


class ArticleAnalyzer:
    def generate_dictionary(self, articlesFile, wordListFilePath):
        wordListFilePath = Path(wordListFilePath)
        wordListFilePath.touch(exist_ok=True)

        wordSet = set()
        for i in range(3):
            with open(articlesFile + '%i.txt' % i, 'r') as article:
                for line in article:
                    line = line.split(' ')
                    for word in line:
                        wordSet.add(word)
            article.close()

        wordList = list(wordSet)
        with open(wordListFilePath, 'a+') as wordSetFile:
            writer = csv.writer(wordSetFile, delimiter=' ')
            for word in wordList:
                writer.writerow(word + '\n')
            wordSetFile.close()

    def generateFirstOccurrenceOfWordCsv(self, firstWordOccFilePath):
        firstWordOccFilePath = Path(firstWordOccFilePath)
        firstWordOccFilePath.touch(exist_ok=True)

        listaOcc = []
        with open(firstWordOccFilePath) as occur:
            reader = csv.reader(occur)
            for lista in reader:
                for lines in lista:
                    lines = occur.readlines()
                    for line in lines:
                        line = line.split(',')
                        listaOcc.append(int(line[1]))
        return listaOcc

    def generateWordCountCsv(self, wordCountFilePath):
        wordCountFilePath = Path(wordCountFilePath)
        wordCountFilePath.touch(exist_ok=True)

        countList = []
        with open(wordCountFilePath) as quant:
            reader = csv.reader(quant)
            for lista in reader:
                for lines in lista:
                    lines = quant.readlines()
                    for line in lines:
                        line = line.split(',')
                        countList.append(int(line[1]))
                    # print(line[1])
        return countList