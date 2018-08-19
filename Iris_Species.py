# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:01:12 2018
@author: jitpa
"""

# I got this csv dataset from Kaggle
# https://www.kaggle.com/uciml/iris
# Used Spyder IDE



import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'C:\Users\jitpa\Desktop\CSV files python\Iris.csv')

s = ['SepalLengthCm', 'SepalWidthCm']
p = ['PetalLengthCm', 'PetalWidthCm']
setoS = df.loc[0:49, s]
versS = df.loc[50:99, s]
virgS = df.loc[100:149, s]

setoP = df.loc[0:49, p]
versP = df.loc[50:99, p]
virgP = df.loc[100:149, p]

plt.figure(1)
plt.ylabel('Sepal Length (Cm)')
plt.xlabel('Sepal Width (Cm)')
plt.title('Iris Sepal')
plt.scatter(setoS[s[0]], setoS[s[1]], color='red')
plt.scatter(versS[s[0]], versS[s[1]], color='green')
plt.scatter(virgS[s[0]], virgS[s[1]], color='blue')
plt.style.use('ggplot')
plt.legend()

plt.figure(2)
plt.ylabel('Petal Length (Cm)')
plt.xlabel('Petal Width (Cm)')
plt.title('Iris Petal')
plt.scatter(setoP[p[0]], setoP[p[1]], color='red')
plt.scatter(versP[p[0]], versP[p[1]], color='green')
plt.scatter(virgP[p[0]], virgP[p[1]], color='blue')
plt.style.use('ggplot')
plt.legend()

plt.show()
