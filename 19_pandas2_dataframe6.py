# Performing calculations
import pandas as pd
from pandas import DataFrame
df = pd.read_csv('weather.csv', sep=",")

# Did you notice that TAVG is NaN? We can fix that
df = df[df["TMAX"].notnull()] 
df = df[df["TMIN"].notnull()]

# Fancy!
df["TAVG"] = df[['TMAX','TMIN']].mean(1)
print(df)