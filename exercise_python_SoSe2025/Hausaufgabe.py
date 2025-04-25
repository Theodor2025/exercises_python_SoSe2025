# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 16:55:11 2025

@author: s_guerrier22
"""

def spar_funktion(AK, SR, i, lz):
    kapital_entwicklung = []
    kapital = AK
    
    for jahr in range(lz):
        kapital *= (1 + i)       # Zinsen aufs Kapital
        kapital += SR            # neue Einzahlung am Ende des Jahres
        kapital_entwicklung.append(round(kapital, 2))  # auf 2 Nachkommastellen runden

    return kapital_entwicklung
ergebnis = spar_funktion(AK=10000, SR=1000, i=0.01, lz=10)
print(ergebnis)
