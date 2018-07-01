import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('nflx.csv', parse_dates=True, index_col=0)
print(df.head())