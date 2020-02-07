import operator
import csv

class DataFileGenerator:
    def generate_article_csvs(self, articlePath, firstWordOccFilePath, wordCountFilePath):
        dicQuan = dict()
        dicOccur = dict()
        wordcount = 0
        for i in range(3):
            with open(articlePath + '%i.txt' % i, 'r') as article:
                art = csv.reader(article)
                for paragraph in art:
                    for line in paragraph:
                        line = line.split(' ')
                        for word in line:
                            wordcount += 1
                            if word in dicQuan and word in dicOccur:
                                #my_dict[key] = my_dict.get(key, 0) + num
                                dicQuan[word] = dicQuan.get(word, 0) + 1
                                #dic[word][1] = dic[word][1] + 1
                            else:
                                dicQuan.update({word: 1})
                                dicOccur.update({word: wordcount})
            article.close()

        with open(firstWordOccFilePath, 'a') as occur:
            for key in dicOccur:
                print(key)
                occur.write(str(key) + ',' + str(dicOccur[key]) + ',\n')

        with open(wordCountFilePath, 'a') as quantity:
            dicQuan = sorted(dicQuan.items(), key= operator.itemgetter(1))
            print(dicQuan)
            for i in range(len(dicQuan)):
                quantity.write(str(dicQuan[i][0]) + ',' + str(dicQuan[i][1]) + ',\n')
            quantity.close()
