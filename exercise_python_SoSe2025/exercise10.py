# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:09:24 2025

@author: s_guerrier22
"""

import numpy as np

M = np.eye(5, dtype=int)  
M[0:2, 3:5] = 3
M[3:5, 0:2] = 2
print(M)




