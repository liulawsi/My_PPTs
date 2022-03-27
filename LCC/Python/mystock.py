# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:25:03 2022

@author: User
"""

#import pandas as pd

myFont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')

stockNo = "2330.TW"

data = yf.Ticker(stockNo)
my_df = data.history(period="max")

stock = Stocker(stockNo, my_df)
stock.plot_stock()
#my_df['Close'].plot(title="台積電 stock price")

#plt.title("台積電", fontproperties=myFont, fontsize = 20)
#plt.plot(my_df['Close'], 'r-')
#plt.show()

#yf.download('2330.TW',start='2016-01-01',end='2021-01-01')
#df = yf.download(stockNo, start=start_date)
#df = df.reset_index()
