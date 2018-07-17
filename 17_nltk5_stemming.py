# Let's do some stemming. We'll need to import some extra stuff
import nltk
from nltk.stem.snowball import SnowballStemmer


# Same prep as before
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
startpoint = holmesstring.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
endpoint = holmesstring.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
holmesstring = holmesstring[startpoint:endpoint]
words = nltk.word_tokenize(holmesstring)
filteredWords = [word.lower() for word in words if word.isalnum()]

# You'll notice that the computer considers similar words
# to be different (start is the starts). Often we don't
# want that to be the case. We can stem the words to get 
# their root:

# create a stemmer object for english (other languages)
# are also available
stemmer = SnowballStemmer("english")

# now we give each word to the stemmer:
stemmedWords = []
for word in filteredWords:
    stemmedWords.append(stemmer.stem(word))

print(stemmedWords[:25])

# Some of these won't be actuall words. We can use a 
# lemmatizer to make sure we only get real words
# note that the lemmatizer is quite slow compared to
# the stemmer
lemmafinder = nltk.WordNetLemmatizer()
lemmas = [lemmafinder.lemmatize(word) for word in filteredWords]
print(lemmas[:25])