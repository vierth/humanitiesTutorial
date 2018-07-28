# Pandas DataFrames make simple statistics easy
import pandas as pd
from pandas import DataFrame

# Import data
df = pd.read_csv('weather.csv', sep=",")

# Get basic stats:
print(df.describe())

# Drop missing information
# By default this will drop a row if any information is missing in that row
df = df.dropna()

# df.dropna(axis=1) will drop a column instead of a row
# df.dropna(axis=1, how="all") will drop a column if all values are missing

# Get the maximum values in each column
print("The maximum values:")
print(df.max())
# df.min() and df.mean() behave exactly as you would expect