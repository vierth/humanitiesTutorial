# One of the most important tasks in Natural lanaguage
# processing is tokenization (break texts apart into units
# we can analyze). We can do this with NLTK
import nltk

# First we need something to analyze.

# If you've downloaded the code, you'll notice there is a file 
# called "holmes.txt", which contains The Adventures of 
# Sherlock Holmes by Arthur Conan Doyle.

# Let's open this file:
textfile = open("holmes.txt","r",encoding="utf8")

# Get the text itself (textfile is a file object)
holmesstring = textfile.read() 

# Close the textfile now that we don't need it anymore:
textfile.close()

# First let's look at the top of the file to see what we have
print(holmesstring[:100])

# Get rid of the Gutenburg boilerplate at beginning and end:
startpoint = holmesstring.find('*** START OF THIS PROJECT')
endpoint = holmesstring.find('*** END OF THIS PROJECT')
holmesstring = holmesstring[startpoint:endpoint]

# NLTK comes with tools that help us tokenize the text.

# Sentence tokenization:
sentences = nltk.sent_tokenize(holmesstring)
print(sentences[1000:1010])

# Word tokenization
words = nltk.word_tokenize(holmesstring)
print(words[1000:1010])