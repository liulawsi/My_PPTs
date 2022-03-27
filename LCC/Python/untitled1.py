# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:25:55 2022

@author: User
"""
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib

myfont = matplotlib.font_manager.FontProperties(
            fname='C:\Windows\Fonts\mingliu.ttc')
#import h5py
#import pandas as pd

stockNo = "2330.TW"

#tock_id = stock_list.loc[i, 'STOCK_ID'] + '.TW'
data = yf.Ticker(stockNo)
df = data.history(period="max")