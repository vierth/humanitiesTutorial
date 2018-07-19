# NLTK comes with a Text object that has many useful methods 
# that facilitate many common tasks
import nltk

# Same prep as before
textfile = open("holmes.txt","r",encoding="utf8")
holmesstring = textfile.read() 
textfile.close()
startpoint = holmesstring.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
endpoint = holmesstring.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
holmesstring = holmesstring[startpoint:endpoint]

# To create an NLTK Text object, we need to break the string 
# into a list of words:
words = nltk.word_tokenize(holmesstring)

# now we just give the nltk.Text() function this list:
holmestext = nltk.Text(words)
# We can see this creates a text object
print(holmestext)

# Now we can create concordances:
holmestext.concordance("Holmes")

# You can also specify how many words and instances are 
# displayed:
# holmestext.concordance("Holmes",width=79,lines=25)