# Getting specific information
import pandas as pd
from pandas import DataFrame
df = pd.read_csv('weather.csv', sep=",")
#df = df.dropna()

# Print first row
print(df[0:1]) # Note that df[0] will not work

# Print first five rows:
print(df[0:5])

# Print the unique values:
print("Here are the unique places:")

# Specify column, unique() returns unique values [:10] returns first ten
print(df['NAME'].unique()[:10]) 