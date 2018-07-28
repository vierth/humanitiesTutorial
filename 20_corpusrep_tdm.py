# Let's use pandas to calculate the frequencies of all words in a corpus. Here
# we will create term-document matrices representing the Adventures of Sherlock
# Holmes
import nltk, math
import pandas as pd
from pandas import Series, DataFrame

# Load the text
rf = open('holmes.txt', 'r')
contents = rf.read()
rf.close()

contents = contents[contents.find('ADVENTURE I'): contents.rfind('End of Project Gutenberg\'s')]
contents = contents.lower()

# Titles of the short stories. 
titles  = ['A Scandal in Bohemia','A Case of Identity','The Boscombe Valley Mystery',
           'The Five Orange Pips','The Man with the Twisted Lip','The Adventure of the Blue Carbuncle',
           'The Adventure of the Speckled Band',"The Adventure of the Engineer's Thumb",
           'The Adventure of the Noble Bachelor','The Adventure of the Beryl Coronet',
           'The Adventure of the Copper Beeches']

# Make them lowercase to find the boundaries between texts
titles = [title.lower() for title in titles]

# Divide the contents into the individual stories. This is simple to do. Simply
# Find where the story starts (by searching for the title). It ends where the 
# next story begins. In the case of the last title, we can just go to the end
# of the document.
shortStoryCounts = []
for i, title in enumerate(titles):
    title = title.lower()

    if i < len(titles) - 1:
        shortStory = contents[contents.find(title):contents.find(titles[i + 1])]
    else:
        shortStory = contents[contents.find(title):]
    
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