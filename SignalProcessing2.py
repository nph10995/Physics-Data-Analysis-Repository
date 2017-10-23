# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 01:13:16 2017

@author: nhilt
"""

import os
os.chdir("C:\\Users\\nhilt\Desktop\ ")

import pandas as pd
pertc = pd.read_csv("signalrectifierchangingtc.csv")
tc = pertc["TC"]
ratio = pertc["S/N"]


#import numpy as np 
import matplotlib.pyplot as plt
plt.plot(tc, ratio, "o", label = "Signal/Noise Ratio")
#plt.plot(gain, multiplier, "x", label = "Ratio of Signal/Noise to Original S/N")
plt.xscale("log")
#plt.yscale("log")
#plt.axis([0,1000,0,1000])
plt.legend(loc="lower right")
plt.xlabel("Time Constant Setting")
plt.ylabel("Signal-Noise Ratio")
plt.title("Signal Rectifier Changing Time Constant")