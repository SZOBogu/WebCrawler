import operator
import csv

class DataFileGenerator:
    def __init__(self):
        pass

    def generate_article_csvs(self):
        dicQuan = dict()
        dicOccur = dict()
        wordcount = 0
        for i in range(10166):
            with open('Articles/article%i.txt' % i, 'r') as article:
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

        with open('wordFirstOccurance.csv', 'a') as occur:
            for key in dicOccur:
                print(key)

                occur.write(str(key) + ',' + str(dicOccur[key]) + ',\n')

        with open('wordQuantity.csv', 'a') as quantity:
            dicQuan = sorted(dicQuan.items(), key= operator.itemgetter(1))
            print(dicQuan)
            for i in range(len(dicQuan)):
                quantity.write(str(dicQuan[i][0]) + ',' + str(dicQuan[i][1]) + ',\n')
            quantity.close()

    def generate_csv(self, i, word_count):
        sett = set()
        with open('Articles/article%i.txt' % i, 'r') as article:
            reader = csv.reader(article)
            with open('CSV%i.csv' % i, 'a') as file:
                writer = csv.writer(file)
                for list in reader:
                    for word in list:
                        sett.add(word)

                #writer.writerow(word, first, count)

    def megre_csvs(self):
        """
            TODO: sklej csvki
            sprawdz czy dane slowo jest juz w poprzedniej csvce, jesli tak to dodaj count, jak nie to dodaj na koniec pliku, merguj do jednego pliku
        :return:
        """
