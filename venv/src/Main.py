import csv

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
    num_lines = sum(1 for line in open('linksFetched.csv'))
    for i in range(num_lines):
        get_articles(i)
    """
    '''
    #wez linki i wciep do seta, a z seta do pliku
        sett_temp = get_links(i)
        with open('linksFetched.csv', 'a') as file:
            writer = csv.writer(file, delimiter=' ')
            for link in sett_temp:
                print(link)
                writer.writerow([link])
    #double check unikalnosci
    sett2 = set()
    with open('linksForStartup.csv') as file:
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
    with open("wordFirstOccurance.csv") as occur:
        reader = csv.reader(occur)
        for lista in reader:
            for line in lista:
                lines = occur.readlines()
                for linee in lines:
                    linee = linee.split(',')
                    listaO.append(int(linee[1]))
                #print(line[1])

    with open("wordQuantity.csv") as quant:
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