# -*- coding: utf-8 -*-
"""
Created on Sat May 10 14:18:21 2025

@author: s_guerrier22
"""

def buchstaben_zählen(text):
    anzahl = 0
    for zeichen in text:
        if zeichen.isalpha():
            anzahl += 1
    return anzahl
buchstaben_zählen("Hallo, Berlin!")
print(buchstaben_zählen("Hallo, Berlin!"))
