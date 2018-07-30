# Let's use pandas to calculate term frequency inverse document frequency. This
# is a way of rapidly identifying terms that are important in a specific 
# document, while demphasizing words that appear in all documents

# First lets recreate our document term matrix (which we got at the end of the 
# last piece of code)
import nltk, math, os
import pandas as pd
from pandas import Series, DataFrame

sherlockTexts = {}
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        with open(f"{root}/{filename}") as rf:
            title = filename[:-4]
            title = title.lower()
            shortStory = rf.read()
            sherlockTexts[title] = shortStory

titles  = ['A Scandal in Bohemia','A Case of Identity','The Boscombe Valley Mystery',
           'The Five Orange Pips','The Man with the Twisted Lip','The Adventure of the Blue Carbuncle',
           'The Adventure of the Speckled Band',"The Adventure of the Engineer's Thumb",
           'The Adventure of the Noble Bachelor','The Adventure of the Beryl Coronet',
           'The Adventure of the Copper Beeches']

titles = [title.lower() for title in titles]

shortStoryCounts = []
for i, title in enumerate(titles):
    shortStory = sherlockTexts[title]
    tokenizedStory = nltk.word_tokenize(shortStory)
    tokenizedStory = [word for word in tokenizedStory if word.isalnum()]
    tokenSeries = Series(tokenizedStory)
    shortStoryCounts.append(tokenSeries.value_counts())

df = pd.concat(shortStoryCounts, axis=1, sort=False)
dtm = df.T

# First lets get the term frequencies. These are just the raw terms in the dtm
# divided by the length of the document.
documentLengths = dtm.sum(axis=1) # Add up the word count for all the words!
frequencyDtm = dtm.div(documentLengths, axis='index')
# Replace NaN values with 0 (otherwise the math won't work)
frequencyDtm = frequencyDtm.fillna(0)


# Get a Series which tells you how many Documents have the term
docsWithTerm = dtm.count()

# Get the weight of the term (total number of documents divided by number of
# documents that contain the term).
termWeight = len(dtm)/docsWithTerm

# This is commonly adjusted by taking the log of this value:
inverseDocumentFrequency = termWeight.apply(math.log)
# Any value that is 1 will go to 0. To avoid this happening it is not uncoomon 
# to add 1 to this when calculating
# inverseDocumentFrequency = termWeight.add(1).apply(math.log)

# get the tfidf matrix:
tfidf = frequencyDtm.multiply(inverseDocumentFrequency)

# We can do some cool things with this, but let's look at the top scoring words
# in the first story. Squeeze just turns the 1 row dataframe into a Series
bohemia = tfidf[0:1].squeeze()
print(bohemia.sort_values(ascending=False))