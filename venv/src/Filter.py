import re

class Filter:
    def filter(self, data):
        filteredDataSet = set()

        if isinstance(data, str):
            for links in data:
                temp = links.get('href')
                temp = str(temp)
                if re.match(r'^/wiki/', temp):
                    if re.match(
                            r'^/wiki/(Wikipedia:|Plik:|Wikiprojekt:|#|Szablon:|Specjalna:|Dyskusja:|Portal:|Pomoc:|DOI_|J%C4%99zyk|Kategoria:|http|https|\.orgNone|\.orgnone)',
                                temp):
                        pass
                    else:
                        filteredDataSet.add(temp)

        return filteredDataSet