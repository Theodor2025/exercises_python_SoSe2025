# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 16:21:41 2025

@author: s_guerrier22
"""

import yfinance as yf
import pandas as pd
import numpy as np

# 1) Lade die Tesla-Daten mit Schlusskurs
df = yf.download("TSLA", start="2010-12-31", end="2023-01-01")[['Close']]
df = df.reset_index()  # Damit 'Date' eine Spalte ist
df['Date'] = pd.to_datetime(df['Date'])  # Stelle sicher, dass es ein Datum ist

# 2) Filtere Jahre 2011–2022
df = df[(df['Date'].dt.year >= 2011) & (df['Date'].dt.year <= 2022)]
print(df.shape)  # sollte (3020, 2) sein

# 3) Berechne logarithmische tägliche Renditen
df['ln_Returns'] = np.log(df['Close'] / df['Close'].shift(1))

# 4) Berechne jährliche Durchschnittsrenditen
df['Year'] = df['Date'].dt.year
df_avg = df.groupby('Year')['ln_Returns'].mean()

# 5) Speichere ins Dictionary (auf 3 Dezimalstellen gerundet)
my_dictionary = {year: round(value, 3) for year, value in zip(df_avg.index, df_avg.values)}

# 6) Ausgabe
print(my_dictionary)

from pprint import pprint

pprint(my_dictionary)
