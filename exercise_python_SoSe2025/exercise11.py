# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:15:55 2025

@author: s_guerrier22
"""

import numpy as np


zeile = np.arange(1, 11)  

D = np.tile(zeile, (10, 1))


summen = D.sum(axis=1)

mittelwerte = D.mean(axis=0)


print("Array D:\n", D)
print("Zeilensummen:", summen)
print("Spaltenmittelwerte:", mittelwerte)
