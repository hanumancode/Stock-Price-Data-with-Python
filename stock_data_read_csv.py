import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('nflx.csv', parse_dates=True, index_col=0) #dataframe

df['21ma'] = df['Close'].rolling(window=21).mean()

df.dropna(inplace=True) #modifies the dataframe in place

#print(df.head())

#graph with matplotlib with the values from Pandas

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) # 6 rows, 1 column
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['21ma'])
ax2.bar(df.index, df['Volume'])

plt.show()