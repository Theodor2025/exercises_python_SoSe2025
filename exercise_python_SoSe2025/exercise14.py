# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:27:50 2025

@author: s_guerrier22
"""

import numpy as np

y = np.array([2, 3, 8, 4, 10, 1, 9, 5, 1, 0])
mean_y = np.mean(y)
n = len(y)
std_manual = np.sqrt(np.sum((y - mean_y)**2) / n)

print("Standardabweichung (manuell):", std_manual)


std_numpy = np.std(y)
print("Standardabweichung (np.std):", std_numpy)
