# In order to do the topic modelling from python, we will need to use the 
# gensim library. This is NOT installed already, so we will have to do that
# ourselves using the conda package manager. Open your terminal and type
# conda install gensim
# and then hit enter

import gensim, nltk, os

# Let's load in the sherlock corpus to study it:
ignoreFiles = set([".DS_Store","LICENSE","README.md"])
sherlockTexts = []
sherlockTitles = []
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        if filename not in ignoreFiles:
            with open(os.path.join(root,filename)) as rf:
                sherlockTexts.append(rf.read().lower())
                sherlockTitles.append(filename[:-4].lower())
                
shortenTitle = {"the adventure of the engineer's thumb":"Engineer's Thumb", 
                'the red-headed league':"Red-headed League", 'the man with the twisted lip':"Twisted Lip",
                'a case of identity':"Identity", 'the adventure of the noble bachelor':"Noble Bachelor",
                'the adventure of the beryl coronet': "Beryl Coronet", 'the adventure of the speckled band':"Speckled Band", 
                'the five orange pips':"Orange Pips", 'the adventure of the blue carbuncle':"Blue Carbuncle",
                'the adventure of the copper beeches':"Copper Beeches", 'the boscombe valley mystery':"Boscombe Valley",
                'a scandal in bohemia':"Bohemia"}

shortTitles = [shortenTitle[title] for title in sherlockTitles]

# Let's do a bit of cleaning first to prep our texts for analysis in gensim
lemmatizer = nltk.WordNetLemmatizer()
# Let's also remove stopwords
stopwords = set(nltk.corpus.stopwords.words('english'))
refinedTexts = []
for text in sherlockTexts:
    tokenized = nltk.word_tokenize(text)
    # get rid of punctuation and lemmatize all the words
    refined = [lemmatizer.lemmatize(word) for word in tokenized if word.isalnum() and word not in stopwords]
    refinedTexts.append(refined)

# Gensim is designed to take advantage of quick running algorithms that require
# integers. It has built in functions to help with this:
corpusDictionary = gensim.corpora.Dictionary(refinedTexts)

# We can filter this dictionary in a number of ways, but I won't for the moment
# corpusDictionary.filter_extremes(no_below=5, no_above=.7)

# Gensim uses bag of word vectors for topic modeling. This will transform the 
# corpus into a list of tuples, each representing a word found in the original
# document:
processedCorpus = [corpusDictionary.doc2bow(text) for text in refinedTexts] 

# You can save the processed corpus to file if you want by serializing it
# This is most useful when you are working with a large corpus that you don't
# want to process on the fly
# Save:
# gensim.corpora.Mmcorpus.serialize('mycorpus.mm', processedCorpus)
# Load:
# processedCorpus = gensim.corpora.Mmcorpus('mycorpus.mm')

# Sanity check. Let's look at the processed corpus and try to recover the 
# original words:
vectorWords = []
for item in processedCorpus[0]:
    term = corpusDictionary[item[0]]
    frequency = item[1]
    vectorWords.append((term,frequency))

print(processedCorpus[0][:10])
print(vectorWords[:10])