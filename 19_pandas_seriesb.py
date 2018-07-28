# Panadas series are similar to lists, but have many more functions
import pandas as pd
from pandas import Series
import nltk

# Let's get that wordcount series back
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read()
textfile.close()
words = nltk.word_tokenize(holmesstring)
words = [word.lower() for word in words if word.isalnum()]
wordSeries = Series(words)
wordCounts = wordSeries.value_counts()

# Unlike lists, indexes for series can be words, in addition
# to numbers. Unlike dictionaries, series are ordered

print(wordCounts.index)

# You can get data by index name:
holmesNum = wordCounts["holmes"]
print(f"holmes occurs {holmesNum} times.")

# You can also get it by index number:
theNum = wordCounts[0]
print(f"The most common word occurs {theNum} times")

# You can use get to get a value.
# this returns None if the value doesn't exist
# handy in avoiding errors
print(wordCounts.get("chimp"))

# Series treat data in a very similar way to R (the statistical
# programming language), so it does vector operations on Series.
print(wordCounts*2)
print(wordCounts + wordCounts)
print(wordCounts - wordCounts)