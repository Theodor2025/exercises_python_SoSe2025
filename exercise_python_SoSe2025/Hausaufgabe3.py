# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:30:11 2025

@author: s_guerrier22
"""

def buchstaben_häufigkeit(text):
    text = text.lower()
    haeufigkeit = {}
    for buchstabe in text:
        if buchstabe.isalpha():
            if buchstabe in haeufigkeit:
                haeufigkeit[buchstabe] += 1
            else:
                haeufigkeit[buchstabe] = 1
    return dict(sorted(haeufigkeit.items()))

print(buchstaben_häufigkeit("Hi, du!"))
