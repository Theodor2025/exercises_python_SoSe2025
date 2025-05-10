# -*- coding: utf-8 -*-
"""
Created on Sat May 10 14:06:28 2025

@author: s_guerrier22
"""

# Berechnung einer geometrischen Reihe in Spyder
a = 1
r = 0.5
s = 0
k = 0

while True:
    term = a * r**k
    s += term
    k += 1
    print(s, end=" ")
    if term < 0.0001:
        break
