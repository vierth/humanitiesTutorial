# DataFrames extend Series into two dimensions
# You can think of them sort of like spreadsheets
# With rows and columns of data

# You can see a quick intro at 
# https://pandas.pydata.org/pandas-docs/stable/10min.html
import pandas as pd
import numpy as np
from pandas import DataFrame

# Create a dataframe full of random numbers
df = DataFrame(np.random.randn(10, 5), columns = ["A", "B", "C", "D", "E"])
print(df)

# You'll notice that each column is essentially a Series:
print("Here is a column from the DataFrame:")
print(df["A"])