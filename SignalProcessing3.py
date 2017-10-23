# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 01:31:45 2017

@author: nhilt
"""

import os
os.chdir("C:\\Users\\nhilt\Desktop\ ")

import pandas as pd
perq = pd.read_csv("signalrectifierchangingq.csv")
q = perq['Q']
signalnoise = perq["Signal-Noise"]

import matplotlib.pyplot as plt
plt.plot(q, signalnoise, 'v', label = "Signal-Noise Ratio")
plt.xlabel("Q")
plt.ylabel("S/N Ratio")
plt.title("Signal Rectifier changing Q on Bandpass Filter")