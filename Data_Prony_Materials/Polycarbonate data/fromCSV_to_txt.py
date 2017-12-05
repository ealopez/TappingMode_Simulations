# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:56:38 2017

@author: Enrique Alejandro
"""

import numpy as np
import matplotlib.pyplot as plt
from quique import*

a = np.loadtxt('Polycarbonate_Prony.txt', delimiter=',', skiprows=1)

tau = a[:,0]
G = a[:,1]


np.savetxt('PC.txt', array((tau, G)).T, delimiter='\t')