from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

filterArticlesArray = ["esla", "ESLA", "usk", "USK", "lon","LON" ]
def isIncluded(baseStr, exampleStrArr):
    for x in range(0, len(baseStr) - len(exampleStrArr)+1):
        for y in range(0, len(exampleStrArr)):
            if baseStr[x + y] != exampleStrArr[y]:
                break
            if y == len(exampleStrArr)-1:
                return True
    return False



def search(searchIndex):
#    headers = {
#        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#    }
    articleArray = []
    site = requests.get("https://www.theverge.com/search?order=date&page="+ str(searchIndex) + "&q=tesla")#, headers = headers)
    siteData = site.text.encode('utf-8').decode('ascii', 'ignore')
    soup = BeautifulSoup(siteData, "html.parser")
    #print(soup.text.encode('utf-8').decode('ascii', 'ignore'))
    articles = soup.find_all("h2" , {"class": "c-entry-box--compact__title"})
    k = 0
    arrayOfRelevantIndexes = []
    for article in articles:
        articleTitle = article.text.encode('utf-8').decode('ascii', 'ignore')
        for element in filterArticlesArray:
            if isIncluded(articleTitle, element):
                print(article.text)#.encode('utf-8').decode('ascii', 'ignore')
                articleArray.append(article.text)
                arrayOfRelevantIndexes.append(k)
                print(article.next_sibling)
                break
        print("Index = " + str(k))
        k = k + 1
"""
    k = 0
    for unrefinedDate in soup.find_all("time", {"class": "c-byline__item"}):
        for int in arrayOfRelevantIndexes:
            if int == k:
                unrefinedDate = str(unrefinedDate.text)
                dt = datetime.strptime(unrefinedDate,'       %b %d, %Y      ')
                date = dt.strftime('%m-%d-%Y')
                print(date)
        k = k + 1
        #itemHolder = item.replace
    #for element in range(1,72):
        #site
"""
search(180)
#for element in range(1,41):
#    search(str(element))
