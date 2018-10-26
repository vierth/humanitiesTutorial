# Pandas is a library designed for data analysis!
# It will make many of the things we want to do much easier

# it is standard to import pandas like this:
import pandas as pd

# let's also import Series
from pandas import Series

# Let's also import nltk
import nltk

# Series are similar to lists, but with many more functions.
# It is easy to turn a list into a Series
numberList = [1, 2, 3, 4, 5, 6, 7, 8]
mySeries = Series(numberList)
print(mySeries)

# Let's do some quick analysis of Sherlock holmes
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
words = nltk.word_tokenize(holmesstring)

# If we turn this list of words into a series, we can easily 
# get word frequencies:
wordSeries = Series(words)
wordCounts = wordSeries.value_counts()
print(wordCounts)

# We can quickly apply a function to all elements of this 
# series:
lowerSeries = wordSeries.str.lower()
wordCounts = lowerSeries.value_counts()
print(wordCounts)
