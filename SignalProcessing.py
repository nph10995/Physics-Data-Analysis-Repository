# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:46:25 2017

@author: nhilt
"""

import os
os.chdir("C:\\Users\\nhilt\Desktop\ ")

import pandas as pd
pergain = pd.read_csv("Percision Rectifier(gain).csv")
gain = pergain["Gain "]
ratio = pergain["Ratio"]
multiplier = pergain["Multiplier"]

#import numpy as np 
import matplotlib.pyplot as plt
plt.plot(gain, ratio, "o", label = "Signal/Noise Ratio")
plt.plot(gain, multiplier, "x", label = "Ratio of Signal/Noise to Original S/N")
plt.xscale("log")
plt.yscale("log")
plt.axis([0,1000,0,1000])
plt.legend(loc="upper right")
plt.xlabel("Gain Setting")
plt.ylabel("Signal-Noise Ratio")
plt.title("Signal Rectifier Changing Gain")