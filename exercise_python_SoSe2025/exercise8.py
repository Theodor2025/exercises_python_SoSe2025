# -*- coding: utf-8 -*-
"""
Created on Sat May 10 14:21:15 2025

@author: s_guerrier22
"""

def vokon_zählen(text):
    vokale = "aeiou"
    anzahl_vokale = 0
    anzahl_konsonanten = 0

    for zeichen in text.lower(): 
        if zeichen.isalpha():    
            if zeichen in vokale:
                anzahl_vokale += 1
            else:
                anzahl_konsonanten += 1
    print(f"Es gibt {anzahl_vokale} Vokale und {anzahl_konsonanten} Konsonanten.")

vokon_zählen("HI,&%/ BerliN!!")
