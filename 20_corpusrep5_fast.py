# We don't have to calculate this stuff for ourselves.
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
from pandas import Series, DataFrame
import nltk, os

# Create a tokenizer function
def tokenizeText(text):
    words = nltk.word_tokenize(text)
    filtered = [word for word in words if word.isalnum()]
    return filtered

# Create vectorizer object. Include use_idf=False to use frequencies
countVectorizer = TfidfVectorizer(tokenizer=tokenizeText)

# We could create a CountVectorizer() instead if we like

# Load the corpus
sherlockTexts = {}
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        with open(os.path.join(root,filename)) as rf:
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
# Get a list of the stories
shortStories = []
for i, title in enumerate(titles):
    shortStories.append(sherlockTexts[title])

# Get the TFIDF scores
countMatrix = countVectorizer.fit_transform(shortStories)
# Get the vocabulary
vocabulary = countVectorizer.get_feature_names()

# Create a DataFrame to hold this information
countArray = countMatrix.toarray()
dtm = DataFrame(countArray, columns=vocabulary)

bohemia = dtm[0:1].squeeze()

# You'll note the values are different, as sklearn uses a slightly different
# method for its calculations, but the words are in the same order (at least
# when you add 1 to the idf before taking the log)
print(bohemia.sort_values(ascending=False))