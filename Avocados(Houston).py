# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:22:36 2018

@author: jitpa
"""
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r'C:\Data Science trackrecord\Python\CSV files python\avocado.csv')

df1 = df.loc[df['region'] == 'Houston']

dfconv = df1.loc[df['type'] == 'conventional']

dfconv = dfconv.reset_index(drop=True)

dforg = df1.loc[df['type'] == 'organic']

dforg = dforg.reset_index(drop=True)

plt.xlabel('Date')
plt.ylabel('Average Prices of Avocado')
plt.title('Avocado Price in Houston')
plt.plot(dfconv['Date'], dfconv['AveragePrice'], color='red')
plt.plot(dforg['Date'], dforg['AveragePrice'], color='green')    
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    