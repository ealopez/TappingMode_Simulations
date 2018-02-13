# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 11:15:24 2018

@author: Enrique Alejandro

Plotting polyisobutylene Prony series coefficients
and printing a file with coeffcients containing header
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
coef = pd.read_csv('PIB.txt', delimiter ='\t', header = None)

coef.rename(columns={0:'Relaxation time, s', 1:'Modulus, Pa'}, inplace=True)

coef.set_index('Relaxation time, s', inplace=True)
coef.reset_index(inplace=True)

fo1 = 46.0e3
fo3 = 17.6*fo1
tau_min = 1.0/fo3/10.0
tau_max = 1.0/fo1*10.0

coef2 = coef[ (coef['Relaxation time, s']>tau_min) & (coef['Relaxation time, s']<tau_max)]


x = np.array(coef['Relaxation time, s'])
y =np.array(coef['Modulus, Pa'])
x2= np.array(coef2['Relaxation time, s'])
y2 =np.array(coef2['Modulus, Pa'])
plt.plot(x, y, 'o', label = 'Total Prony Coefficients')
plt.plot(x2, y2, 'r--', lw=3,  label ='Region of interest')
plt.title('Prony Coefficients for Polyisobutylene', fontsize = 15)
plt.xlabel('Relaxation time, s', fontsize = 15)
plt.ylabel('Modulus, Pa', fontsize = 15)
plt.xscale('log')
plt.yscale('log')
plt.legend(loc=3)
plt.savefig('PronyCoefficientsPIB.png', bbox_inches='tight')
 
print(coef.head())

coef.to_csv('Polyisobutylene_coefficients.txt', sep='\t')

