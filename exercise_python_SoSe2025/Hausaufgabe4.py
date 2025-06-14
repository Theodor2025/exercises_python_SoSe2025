# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""


import yfinance as yf
import pandas as pd

# Tesla-Daten 2022
df = yf.download("TSLA", start="2022-01-01", end="2022-12-31")

# Schlusskurs
df = df[['Close']]

# Vorschau
print(df.head())
print(df.shape)  # sollte (250, 1) sein

# Speichern
df.to_csv("tesla_2022_close.csv")
import matplotlib.pyplot as plt
# Stellt Schlusskursüber die Zeit dar
df.plot(title="Tesla Schlusskurs 2022", figsize=(10, 5))
plt.xlabel("Datum")
plt.ylabel("Schlusskurs (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()
