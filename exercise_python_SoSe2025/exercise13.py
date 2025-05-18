# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:26:16 2025

@author: s_guerrier22
"""

import math

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
log_values = []

for zahl in x:
    log_values.append(math.log10(zahl))

print("Logarithmen mit math:", log_values)

import numpy as np

x = np.array([1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000])
log_values = np.log10(x)

print("Logarithmen mit NumPy:", log_values)
