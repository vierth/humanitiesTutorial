# Pandas is a library designed for data analysis!
# It will make many of the things we want to do much easier

# it is standard to import pandas like this:
import pandas as pd

# let's also import Series and DataFrames
from pandas import Series, DataFrame

# Let's also import nltk
import nltk

# Series are similar to lists, but with many more functions.
# It is easy to turn a list into a Series
numberList = [1, 2, 3, 4, 5, 6, 7, 8]
mySeries = Series(numberList)
print(mySeries)