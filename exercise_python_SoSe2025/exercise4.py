# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""

# Variante 1: mit append()
quad_zahl = []

for zahl in range(1, 11):
    if zahl % 2 == 1:  # ungerade
        quad_zahl.append(zahl ** 2)
    else:              # gerade
        quad_zahl.append(zahl)

print("Mit append():", quad_zahl)

# Variante 2: mit Listenabstraktion
quad_zahl = [zahl ** 2 if zahl % 2 == 1 else zahl for zahl in range(1, 11)]

print("Mit Listenabstraktion:", quad_zahl)
