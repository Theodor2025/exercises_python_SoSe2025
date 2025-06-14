# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:52:50 2025

@author: s_guerrier22
"""

import matplotlib.pyplot as plt

# Parameter
a = 1
r = 0.5
n = 10

s_n = []       # Teilsummen
summe = 0      # Startwert für die Summe

# Schleife Teilsummen
for k in range(n):
    term = a * (r ** k)
    summe += term
    s_n.append(summe)


print("Teilsummen:", s_n)

# Plot Teilsummen
plt.plot(s_n, marker='o')
plt.title("Konvergenz der geometrischen Reihe")
plt.xlabel("Anzahl Terme")
plt.ylabel("Summe")
plt.grid(True)
plt.show()
