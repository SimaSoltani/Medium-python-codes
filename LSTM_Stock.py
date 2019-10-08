# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:37:58 2019

@author: Sima

Walking through Support vector regression and LSTM with stock price prediction
From Medium
"""


import keras
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import pandas as pd
import pandas_datareader.data as web
import datetime
import numpy as np
from matplotlib import style

#ignore warnings
import warnings


# get our stock data
style.use('ggplot')

# get 2014-2018 data to train our model
start = datetime.datetime(2014,1,1)
end = datetime.datetime(2018,12,20)
df = web.DataReader("TSLA",'yahoo',start,end)

# get 2019  data to test our model on
start = datetime.datetime(2019,1,1)
end = datetime.date.today()
test_df = web.DataReader("TSLA",'yahoo',start,end)

#sort by date
df = df.sort_values('Date')
test_df = test_df.sort_values('Date')


#fix the date
df.reset_index(inplace=True)
df.set_index("Date",inplace=True)
test_df.reset_index(inplace=True)
test_df.set_index("Date",inplace=True)


# plotting our data
import matplotlib.pyplot as plt

# %matplotlib inline

plt.figure(figsize = (12,6))
plt.plot(df["Adj Close"])
plt.xlabel('Date',fontsize = 15)
plt.ylabel('Adjusted Close Pise',fontsize=15)
plt.show()


# rolling mean :Rolling mean is also called moving average. Moving average helps us smooth out data that has lots of fluctuations and helps us better see the long term trend of the data.
close_px = df['Adj Close']
mavg = close_px.rolling (window=100).mean()

plt.figure(figsize=(12,6))
close_px.plot(label = 'TSLA')
mavg.plot(label='mavg')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()


# converting Data

import matplotlib.dates as mdates

# change the dates into ints for training
dates_df = df.copy()
dates_df = dates_df.reset_index()

# store the original dates for plotting the predictions 
org_dates = dates_df['Date']

#converts to ints
dates_df['Date'] = dates_df['Date'].map(mdates.date2num)


