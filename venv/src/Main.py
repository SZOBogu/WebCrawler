from bs4 import BeautifulSoup
import requests
import re
import csv
from Filter import Filter


def get_links(i):
    sett = set()
    with open('links.csv') as file:
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

def get_articles(i):
    with open('Articles/article%i.txt' % i, 'w') as article:
        with open('links1.csv') as file:
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

def generate_csv(i, word_count):
    sett = set()
    with open('Articles/article%i.txt' % i, 'r') as article:
        reader = csv.reader(article)
        with open('CSV%i.csv' % i, 'a') as file:
            writer = csv.writer(file)
            for list in reader:
                for word in list:
                    sett.add(word)
                    """TODO: sprawdz czy set w przypadku nie dodania cos zwraca
                    jesli tak:
                        if none: szukaj slowa i dodaj jeden do counta
                                zapisz pierwsze wystapienie slowa + word_count
                                sprawdz reg expem albo metoda listy ile razy slowo wystepuje
                                zapisz do csvki
                    """

            #writer.writerow(word, first, count)
def megre_csvs():
    """
        TODO: sklej csvki
        sprawdz czy dane slowo jest juz w poprzedniej csvce, jesli tak to dodaj count, jak nie to dodaj na koniec pliku, merguj do jednego pliku
    :return:
    """

def generate_article_csvs():
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
    '''
    with open('occurance.csv', 'a') as occur:
        for key in dicOccur:
            print(key)

            occur.write(str(key) + ',' + str(dicOccur[key]) + ',\n')

    with open('quantity.csv', 'a') as quantity:
        dicQuan = sorted(dicQuan.items(), key=operator.itemgetter(1))
        print(dicQuan)
        for i in range(len(dicQuan)):
            quantity.write(str(dicQuan[i][0]) + ',' + str(dicQuan[i][1]) + ',\n')
        quantity.close()
    '''
def generate_dictionary():
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
def main():
    #TODO: kontrola wielkości plików
    """
    #wez dane z artykulow
    sett = set()
    sett_temp =set()
    num_lines = sum(1 for line in open('links1.csv'))
    for i in range(num_lines):
        get_articles(i)
    """
    '''
    #wez linki i wciep do seta, a z seta do pliku
        sett_temp = get_links(i)
        with open('links1.csv', 'a') as file:
            writer = csv.writer(file, delimiter=' ')
            for link in sett_temp:
                print(link)
                writer.writerow([link])
    #double check unikalnosci
    sett2 = set()
    with open('links.csv') as file:
        reader = csv.reader(file)
        for list in reader:
            for line in list:
                print(line)
                sett2.add(line)
'''
    #generate_article_csvs()
    #generate_dictionary()
    listaO = list()
    listaQ = list()
    with open("occurance.csv") as occur:
        reader = csv.reader(occur)
        for lista in reader:
            for line in lista:
                lines = occur.readlines()
                for linee in lines:
                    linee = linee.split(',')
                    listaO.append(int(linee[1]))
                #print(line[1])

    with open("quantity.csv") as quant:
        reader = csv.reader(quant)
        for lista in reader:
            for line in lista:
                lines = quant.readlines()
                for linee in lines:
                    linee = linee.split(',')
                    listaQ.append(int(linee[1]))
                #print(line[1])
    listaO = listaO[-30:]

    sum = 0
    for i in range(len(listaQ)):
        sum += listaQ[i]
    print(sum)

    print(listaQ)
    for i in range(len(listaQ)):
        listaQ[i] = listaQ[i]/sum

    print(listaQ)

if __name__ == '__main__':
    main()