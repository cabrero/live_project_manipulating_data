#!/usr/bin/env python3

import sys

import numpy as np
import pandas as pd

def change_row(row):
    row['Host city'] = row['Host city'].split(',')[0]
    try:
        result = row['Result'].replace(',', ' ').split()
        east, west = [ int(s) for s in result if s.isdigit() ]
        diff = abs(east - west)
    except Exception:
        print(row['Result'])
        east, west, diff = np.NaN, np.NaN, np.NaN
    row['East'] = east
    row['West'] = west
    row['Diff'] = diff
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
df.insert(4, "Diff", 0)
df = df.apply(change_row, axis= 'columns').drop(columns= ["Result", "Host arena", "Game MVP"]).dropna()
print(df)

diff_df = df.groupby('Diff').count().drop(columns= ["East", "West", "Host city"]).rename(columns= {'Year': 'Count'}).sort_values('Diff', ascending= False)
print(diff_df)
