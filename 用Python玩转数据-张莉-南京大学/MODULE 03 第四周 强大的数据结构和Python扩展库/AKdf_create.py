# Fillename: AKdf_create.py
# -*- coding: utf-8 -*-
"""
AKdf create
 
@author: Dazhuang
"""
 
# -*- coding: utf-8 -*-
"""
Count days
 
@author: Dazhuang
"""
 
import requests
import re
import json
import pandas as pd
from datetime import date
import time
from pylab import * 
from scipy.cluster.vq import * 
 
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
 
def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = []
    for i in range(len(quotes)):
        x = date.fromtimestamp(quotes[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')   
        list1.append(y)
    quotesdf_ori = pd.DataFrame(quotes, index = list1)
    listtemp = []
    for i in range(len(quotesdf_ori)):
        temp = time.strptime(quotesdf_ori.index[i],"%Y-%m-%d")
        listtemp.append(temp.tm_mon)
    tempdf = quotesdf_ori.copy()
    tempdf['month'] = listtemp
    totalclose = tempdf.groupby('month').close.mean()
    df_totalclose = pd.DataFrame(totalclose)
    df_totalclose['code'] = stock_code
    return df_totalclose
                   
dfAXP_totalclose = create_df('AXP')
dfKO_totalclose = create_df('KO')
AKdf = dfAXP_totalclose.append(dfKO_totalclose)
AKdf['month'] = AKdf.index