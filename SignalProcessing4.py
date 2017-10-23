# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 01:56:33 2017

@author: nhilt
"""

import os
os.chdir("C:\\Users\\nhilt\Desktop\ ")
import pandas as pd
lockin = pd.read_csv("lockin.csv")
g = lockin["Gain"]
sn = lockin['S-N']

import matplotlib.pyplot as plt
plt.plot(g, sn, 'o', label = "S/N Ratio")
plt.xlabel("Gain Settings")
plt.ylabel("Signal - Noise Ratio")
plt.title("Lock-In - Changing Gain Settings")