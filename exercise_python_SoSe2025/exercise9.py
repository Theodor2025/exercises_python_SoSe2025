# -*- coding: utf-8 -*-
"""
Created on Sun May 18 17:55:05 2025

@author: s_guerrier22
"""

import numpy as np
a = np.arange(1, 13)
a = a.reshape((3, 2, 2))

print("Anzahl der Dimensionen (ndim):", a.ndim)
print("Form des Arrays (shape):", a.shape)
print("Gesamtzahl der Elemente (size):", a.size)
print("Datentyp der Elemente (dtype):", a.dtype)
