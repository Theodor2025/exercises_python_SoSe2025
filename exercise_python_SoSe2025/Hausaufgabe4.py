# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""


import yfinance as yf
import pandas as pd

# Lade Tesla-Daten für 2022
df = yf.download("TSLA", start="2022-01-01", end="2022-12-31")

# Nur Schlusskurs
df = df[['Close']]

# Vorschau und Form
print(df.head())
print(df.shape)  # sollte (250, 1) sein

# Speichern als CSV
df.to_csv("tesla_2022_close.csv")
import matplotlib.pyplot as plt
# Stelle den Schlusskurs (Close) über die Zeit dar
df.plot(title="Tesla Schlusskurs 2022", figsize=(10, 5))
plt.xlabel("Datum")
plt.ylabel("Schlusskurs (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()
