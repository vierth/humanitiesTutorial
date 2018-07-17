# The Natural Language Toolkit Library contains many tools
# that will be useful to us over the course of this class
import nltk


textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
startpoint = holmesstring.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
endpoint = holmesstring.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
holmesstring = holmesstring[startpoint:endpoint]

# Combined sentence and word tokenization:
# first create a dummy list to contain results
sentencesWordsTokens = []

# First break into sentences:
sentences = nltk.sent_tokenize(holmesstring)

# Then break each sentence into words:
for sentence in sentences:
    tokenizedSentence = nltk.word_tokenize(sentence)
    sentencesWordsTokens.append(tokenizedSentence)

print(sentencesWordsTokens[1000])

# We can use list comprehensions to condense this code
# into a single line:
sWT = [nltk.word_tokenize(sentence) for sentence in nltk.sent_tokenize(holmesstring)]
print(sWT[1000])