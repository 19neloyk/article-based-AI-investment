import datetime as dt
import matplotlib as ml
'''the next line is for a backend key that identifies a graphical interface,
not really necessary for other machines unless the error shows up'''
ml.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy

'''the next line is to show the type of graph used'''
style.use('ggplot')

'''
//Began by calling for stock market data into a dataframe format

start = dt.datetime(2016,12,12)
end = dt.datetime(2019,5,11)
df = web.DataReader('TSLA', 'iex', start, end) //Used start and end variables
as constraints of the dataframe rows, imported from iex API, called for Tesla's
stock ticker
df = pd.read_csv('tsla.csv') //reading csv
//About to delete columns that are irrelevant to the data I am looking for
del df['high']
del df['low']
del df['volume']
df['percent change'] = ((df.close - df.open)/df.open)*100 // Adding percent change
column that, for each row, calculates value by finding percentage shift from close
column value to open column value

df.to_csv('tesla.csv') //converting and storing dataframe into a csv file

df = pd.read_csv('tesla.csv') //reading csv for future reference

//This next section is if I do want to include my own ideas of what is good and what is bad
def findChangeQuality(row):
    change = "neutral"
    if row['percent change'] > 0.8:
        change = "positive"
    elif row['percent change'] < -0.8:
        change = 'negative'
    return change
df['change quality'] = df.apply(findChangeQuality, axis=1)
'''

df = pd.read_csv('tesla.csv')
print(df)
