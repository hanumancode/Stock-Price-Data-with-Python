import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2014,1,1)
end = dt.datetime(2015,1,1)

df = web.DataReader('NFLX', 'morningstar', start, end) #dataframe
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)
#print(df.head(100))

df.to_csv('nflx.csv')