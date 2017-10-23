# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:25:44 2017

@author: nhilt
"""

import scipy.misc as sp
import numpy as np
mu = []
xb = [2,4,6,8,10]
for i in xb:
    xi = xb[i]*.2
    mu.append(xi)
prob = []
for i in mu: 
    p =(((mu**(x[i]))/(sp.factorial(x[i])))*np.exp(-mu))/mu
    prob.append(p)