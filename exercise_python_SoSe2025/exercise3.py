
"""
Created on Fri Apr 25 16:39:18 2025

@author: s_guerrier22
"""

def steigung_funktion(punkte):
    x1, y1, x2, y2 = punkte

    if x2 - x1 == 0:
        return "Die Steigung ist nicht definiert."

    steigung = (y2 - y1) / (x2 - x1)
    return steigung


# Testaufruf:
print(steigung_funktion([4, 4, 8, 4]))  # Erwartet: 0.0
days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

print(days[-1:])
print(days[:-1])
print(days[10])  # Dieser gibt eine Fehlermeldung
