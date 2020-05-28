import pandas as pd

articleDf = pd.read_csv("CSVFILES/refinedvergeArticles.csv")
print("DATE        ARTICLE TITLE               STOCK SHIFT")
for x in range(0,len(articleDf)):
    articleStr = str(articleDf['article'][x])
    def firstFifteenCharacters(articleString):
        returnStr = ''
        for x in range(17):
            returnStr = returnStr + articleString[x]
        return returnStr + '...'
    print(str(articleDf['date'][x]) + ' ' + firstFifteenCharacters(articleStr) + '       ' + str(articleDf['articleChange'][x]))
