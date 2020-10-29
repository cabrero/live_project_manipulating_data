#!/usr/bin/env python3

import sys

import numpy as np
import pandas as pd

def change_row(row):
    row['Host city'] = row['Host city'].split(',')[0]
    try:
        result = row['Result'].replace(',', ' ').split()
        east, west = [ int(s) for s in result if s.isdigit() ]
    except Exception:
        print(row['Result'])
        east, west = np.NaN, np.NaN
    row['East'] = east
    row['West'] = west
    return row

tables = pd.read_html("https://en.wikipedia.org/wiki/NBA_All-Star_Game")
header = pd.Index(['Year', 'Result', 'Host arena', 'Host city', 'Game MVP'])
df = None
for table in tables:
    if table.columns.equals(header):
        df = table
        break
if df is None:
    print("Couldn't find results table")
    sys.exit(1)

    
df.insert(2, "East", 0)
df.insert(3, "West", 0)
df = df.apply(change_row, axis= 'columns').drop(columns= ["Result", "Host arena", "Game MVP"]).dropna()

print(df)
