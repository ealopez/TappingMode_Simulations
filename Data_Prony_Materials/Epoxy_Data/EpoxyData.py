# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:56:38 2017

@author: Enrique Alejandro
Tabulating data of Prony Coefficients for cured Epoxy, taken from:
Simon, Sindee L., Gregory B. Mckenna, and Olivier Sindt. "Modeling the evolution 
of the dynamic mechanical properties of a commercial epoxy during cure after 
gelation." Journal of Applied Polymer Science 76.4 (2000): 495-508. 
"""

import numpy as np
import matplotlib.pyplot as plt
from quique import*

#the list data will store the values of the Prony series in the reference mentioned in the header
data = [ 0.0215, 0.0215, 0.0215, 0.0215, 0.0267, 0.0267, 0.0375, 0.0405, 0.0630, \
0.0630, 0.1054, 0.1160, 0.1160, 0.1653, 0.0561, 0.0561, 0.0199, 0.0119, 0.0055,\
 0.0028, 0.0008, 0.0002, 0.0003, 0.0003]

g = np.asarray(data)
Gg = 891.0e6 #Pa, glassy modulus
Ge = 4.9e6  #Pa, rubbery modulus
G = (Gg-Ge)*g


a = np.zeros(np.size(g))
a[0] = -7.0
for j in range(1,np.size(g)-1):
    a[j] = a[j-1] + 0.5
a[np.size(g)-1] = 5.0
tau = np.zeros(np.size(g))
tau=10.0**(a)

time = log_tw(10**-7, 10**5, 20)
G_t = np.zeros(np.size(time))

for i in range(np.size(time)):
    G_t[i] = Ge + sum(G[:]*exp(-time[i]/tau[:]))

omega = log_tw(2.0*np.pi/time[np.size(time)-1], 2.0*np.pi/time[0], 20)
theta = np.zeros(np.size(omega))

for i in range(np.size(omega)):
    theta[i] = theta_loss_G(omega[i], G, tau, Ge)

#theta = theta_loss_G(omega, G, tau, Ge)

plt.plot(omega/(2.0*np.pi), theta)
#plt.plot(time,G_t)
plt.xscale('log')
#plt.yscale('log')

np.savetxt('Epoxy.txt', array((tau, G)).T, delimiter='\t')
