# Let's do some quick analysis
import nltk

# Same prep as before
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
startpoint = holmesstring.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
endpoint = holmesstring.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
holmesstring = holmesstring[startpoint:endpoint]
words = nltk.word_tokenize(holmesstring)

# Let's make everything lowercase and get rid of punctuation:
filteredWords = []
for word in words:
    if word.isalnum():
        filteredWords.append(word.lower())

'''
We could do this in a single line too:

filteredWords = [word.lower() for word in words if word.isalnum()]
'''

# We can see these are now all lowercase and no punctuation is
# in the list anymore:
print(filteredWords[:25])

# Let's check the total number of words:
length = len(filteredWords)
print(f"The Adventures of Sherlock Holmes contain {length} words.")

# We can get the number of unique words by using a "set"
uniqueWords = set(filteredWords)
uniqueWordLength = len(uniqueWords)
print(f"Of {length} words, {uniqueWordLength} of them are unique.")

# Let's get the lexical diversity:
lexicalDiversity = uniqueWordLength/length
print(f"It has a lexical diversity of {lexicalDiversity}")