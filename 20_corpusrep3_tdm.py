# Let's use pandas to calculate the frequencies of all words in a corpus. Here
# we will create term-document matrices representing the Adventures of Sherlock
# Holmes
import nltk, math, os
import pandas as pd
from pandas import Series, DataFrame


# Let's load the files!
sherlockTexts = {}
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        with open(f"{root}/{filename}") as rf:
            title = filename[:-4] # Remove the file extension
            title = title.lower() # Let's make it lower case for readability
            shortStory = rf.read()
            sherlockTexts[title] = shortStory


# Titles of the short stories. I'm only using this so the order of our results
# will stay consistent when we do other analyses
titles  = ['A Scandal in Bohemia','A Case of Identity','The Boscombe Valley Mystery',
           'The Five Orange Pips','The Man with the Twisted Lip','The Adventure of the Blue Carbuncle',
           'The Adventure of the Speckled Band',"The Adventure of the Engineer's Thumb",
           'The Adventure of the Noble Bachelor','The Adventure of the Beryl Coronet',
           'The Adventure of the Copper Beeches']

# Make them lowercase to match the sherlock dictionary
titles = [title.lower() for title in titles]

# Get the word count for each item in the corpus. We could have done this when 
# we opened the files, too.
shortStoryCounts = []
for i, title in enumerate(titles):
    shortStory = sherlockTexts[title]
    
    # Tokenize into words
    tokenizedStory = nltk.word_tokenize(shortStory)
    # Filter out punctuation
    tokenizedStory = [word for word in tokenizedStory if word.isalnum()]
    
    # Turn into a series
    tokenSeries = Series(tokenizedStory)

    # Get the counts of each word
    shortStoryCounts.append(tokenSeries.value_counts())

# Concatenate these counts into a DataFrame.
df = pd.concat(shortStoryCounts, axis=1, sort=False)

# We now have what is known as a Term-Document Matrix (terms are rows, 
# documents are columns) We'll do fun stuff with this in later lessons
print(df)

# We can turn this into a Document-Term Matrix (documents are rows, terms are 
# columns) by transposing it
dtm = df.T