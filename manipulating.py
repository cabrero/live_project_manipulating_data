#!/usr/bin/env python3

import sys

import numpy as np
import pandas as pd


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
df = df.dropna()
print(df)
