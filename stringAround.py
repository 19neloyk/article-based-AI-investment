filterArticlesArray = ["esla", "ESLA", "usk", "USK", "lon","LON" ]


def isIncluded(baseStr, exampleStrArr):
    for x in range(0, len(baseStr) - len(exampleStrArr)+1):
        for y in range(0, len(exampleStrArr)):
            if baseStr[x + y] != exampleStrArr[y]:
                break
            if y == len(exampleStrArr)-1:
                return True
    return False

for element in filterArticlesArray:
    print(isIncluded("Elon Musk Tesla TESLA MUSK ELON", element))

newDict = {'cars':[1]}
newDict['cars'].append(2)
print(newDict)
