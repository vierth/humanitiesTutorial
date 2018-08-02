# You can load data from a spreadsheet easily
import pandas as pd
from pandas import DataFrame

# Import data
# note this uses the read_csv method
# You can open tsvs and other delimited file types by inputing the actual 
# delimiter as the keyword argument for sep

# This spreadsheet is courtsey of https://www.ncdc.noaa.gov/cdo-web/
# all this data is in the public domain
df = pd.read_csv('weather.csv', sep=",")
print(df)

# You can get the index like this:
print(df.index)

# You can get the columns like this:
print(df.columns)

# Note the lack of paranthesis. These are attributes and not methods

# Get top of the dataframe:
print(df.head()) # df.head(10) will show first 10 rows