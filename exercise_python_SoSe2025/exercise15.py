# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:11:41 2025

@author: s_guerrier22
"""
import pandas as pd

index = ["Berlin", "Madrid", "Rom"]

bevölkerung = pd.Series([3.6, 3.3, 2.8], index=index)
fläche = pd.Series([892, 604, 1285], index=index)
land = pd.Series(["Deutschland", "Spanien", "Italien"], index=index)
sprache = pd.Series(["deutsch", "spanisch", None], index=index)

df = pd.DataFrame({
    "Bevölkerung": bevölkerung,
    "Fläche": fläche,
    "Land": land,
    "Sprache": sprache
})

print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.isnull())
print(df.isnull().sum())

# Aufgabe 2
df["Sprache"].fillna("italienisch", inplace=True)

# Aufgabe 3
new_data = pd.DataFrame({
    "Bevölkerung": [8.5],
    "Fläche": [784],
    "Land": ["USA"],
    "Sprache": ["englisch"]
}, index=["New York"])

df = pd.concat([df, new_data])

# Aufgabe 4
df["EU"] = df["Land"].isin(["Deutschland", "Spanien", "Italien"])

# Aufgabe 5
import numpy as np
df["Region"] = np.where(df["EU"], "Europa", "Americas")

# Ergebnis 
print(df)


