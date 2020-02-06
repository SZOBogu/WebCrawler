import csv

class ArticleAnalyzer:
    def generate_dictionary(self):
        wordList = set()
        for i in range(10166):
            with open('Articles/article%i.txt' % i, 'r') as article:
                rdr = csv.reader(article)
                for line in article:
                    line = line.split(' ')
                    for word in line:
                        print(word)
                        wordList.add(word)
            article.close()

        with open('dictionary', 'w') as dic:
            for word in wordList:
                dic.write(word + '\n')
        dic.close()

    def generateFirstOccuranceOfWordCsv(self):
        listaOcc = []
        with open("wordFirstOccurance.csv") as occur:
            reader = csv.reader(occur)
            for lista in reader:
                for line in lista:
                    lines = occur.readlines()
                    for linee in lines:
                        linee = linee.split(',')
                        listaOcc.append(int(linee[1]))
        return listaOcc

    def generateWordCountCsv(self):
        countList = []
        with open("wordQuantity.csv") as quant:
            reader = csv.reader(quant)
            for lista in reader:
                for line in lista:
                    lines = quant.readlines()
                    for linee in lines:
                        linee = linee.split(',')
                        countList.append(int(linee[1]))
                    # print(line[1])
        return countList;