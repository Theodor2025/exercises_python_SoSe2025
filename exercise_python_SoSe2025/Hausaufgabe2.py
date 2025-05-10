# -*- coding: utf-8 -*-
"""
Created on Sat May 10 14:33:13 2025

@author: s_guerrier22
"""

def buchstaben_ändern(string, buchstabe):
    vokale = "aeiou"
    for neuer_vokal in vokale:
        neuer_text = ""
        for zeichen in string:
            if zeichen.lower() == buchstabe.lower():
                neuer_text += neuer_vokal
            else:
                neuer_text += zeichen
        print(neuer_text)

buchstaben_ändern("banana", "a")
buchstaben_ändern("Wie geht es Ihnen?", "e")

    


