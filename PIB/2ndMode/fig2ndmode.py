# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 07:04:57 2017

@author: Enrique Alejandro
"""

import matplotlib.pyplot as plt
import pandas as pd

res = pd.read_csv('-160.txt', delimiter='\t')

t = res.iloc[:,0].values
tip = res.iloc[:,1].values
fts = res.iloc[:,2].values
xb = res.iloc[:,3].values

plt.plot(t, xb)