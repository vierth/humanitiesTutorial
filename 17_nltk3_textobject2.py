# Text objects come with a lot of interesting features:
import nltk

# Same prep as before
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
startpoint = holmesstring.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
endpoint = holmesstring.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
holmesstring = holmesstring[startpoint:endpoint]
words = nltk.word_tokenize(holmesstring)
holmestext = nltk.Text(words)

# Find words that appear in a similar context:
# the bigger the corpus, the more meaningful this will be
print("Similar words to apartment")
holmestext.similar("apartment")

# Make a lexical dispersion plot:
# Give this a list of words. To let the code continue, you 
# will have to close the window that opens.
holmestext.dispersion_plot(["murder", "death"])

# Getting collocations:
holmestext.collocations()

# Getting word frequencies (you can also provide 
# a list of words):
frequencies = nltk.FreqDist(holmestext)
print(frequencies['and'])

# You can get most common words, or words that occur once:
print(frequencies.most_common(1))
#print(frequencies.hapaxes())