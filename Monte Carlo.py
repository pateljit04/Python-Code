#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import i,n,j
from sympy import *
import plotly.express as px


# In[2]:


prod=list(range(25,51))


# In[3]:


Eq((i-n)*1000 - 2000*i-30000+4000*n,j)


# In[4]:


sim = []
for i in prod:
    k = -1000*i + 3000*(np.round(np.random.uniform(25,i,50))) - 30000
    sim.append(k)


# In[5]:


df1 = pd.DataFrame(sim).T


# In[6]:


df1.columns = list(range(25,51))


# In[7]:


fig = px.imshow(df1)
fig.show()


# In[8]:


df2 = df1.T


# In[11]:


df2['sum'] = df2.sum(axis=1)
df2['id'] = df2.index


# In[12]:


df2


# In[14]:


fig1 = px.bar(df2,x='id',y='sum',title='total sum of simulations')
fig1.show()


# In[ ]:




