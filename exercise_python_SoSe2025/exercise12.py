# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:18:30 2025

@author: s_guerrier22
"""

import numpy as np

M = np.array([[3, 1], [2, 4]])
M_inv = np.linalg.inv(M)  # Inverse berechnen

I = M_inv @ M

print("M:\n", M)
print("Inverse von M:\n", M_inv)
print("M_inv @ M =\n", I)

A = np.array([[7, 5, -3],
              [3, -5, 2],
              [5, 3, -7]])

r = np.array([16, -8, 0])


x = np.linalg.inv(A) @ r

x_alt = np.linalg.solve(A, r)

print("Lösung mit Inverse:\n", x)
print("Lösung mit solve():\n", x_alt)
