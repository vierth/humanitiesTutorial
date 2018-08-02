# Filtering DataFrames
# Getting specific information
import pandas as pd
from pandas import DataFrame
df = pd.read_csv('weather.csv', sep=",")

# Drop rows with no temperature data
df = df[df["TMAX"].notnull()] # isnull() is also a thing
df = df[df["TMIN"].notnull()]
print(df)

# Get all observations where temperature is above 28
hot = df[df["TMAX"] > 28]
print(hot)

# Get observations from Rotterdam:
rot = df[df.NAME == "ROTTERDAM, NL"] 
print(rot.describe())
# rot = df[df["NAME"] == "ROTTERDAM, NL"] does the same thing
