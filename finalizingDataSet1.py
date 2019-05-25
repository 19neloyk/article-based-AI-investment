import pandas as pd

stockDf = pd.read_csv("tesla.csv")
articleDf = pd.read_csv("vergeArticles.csv")

print(stockDf['date'][598])
print(articleDf['date'][2])

if (stockDf['date'][598]) == (articleDf['date'][2]):
    print('You Got It Cuh')

def getArticleFluctuation(row):
    Date = row['date']
    for stack in range(0, len(stockDf['date'])):
        if Date == stockDf['date'][stack]:
            return stockDf['percent change'][stack]
    return 0

articleDf['articleChange'] = articleDf.apply(getArticleFluctuation, axis=1)

articleDf.to_csv('refinedvergeArticles.csv')
