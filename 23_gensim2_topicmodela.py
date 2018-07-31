# In order to do the topic modelling from python, we will need to use the 
# gensim library. This is NOT installed already, so we will have to do that
# ourselves using the conda package manager. Open your terminal and type
# conda install gensim
# and then hit enter

import gensim, nltk, os

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
stopwords = set()
lemmatizer = nltk.WordNetLemmatizer()
refinedTexts = []
for text in sherlockTexts:
    tokenized = nltk.word_tokenize(text)
    refined = [lemmatizer.lemmatize(word) for word in tokenized if word.isalnum() and word not in stopwords]
    refinedTexts.append(refined)

corpusDictionary = gensim.corpora.Dictionary(refinedTexts)
corpusDictionary.filter_extremes(no_below=5)

processedCorpus = [corpusDictionary.doc2bow(text) for text in refinedTexts] 

# Let's actually run a topic model this time. First let's set how many topics
# we want:
numberOfTopics = 20

# LDA (latent drichlet allocation) is a popular topic modeling algorithm. 
# Many scholars like the MALLET implementation, and gensim has a wrapper for 
# this! You will need java installed on your system and to download MALLET from
# http://mallet.cs.umass.edu/download.php
# Unzip this and place it in the same directory as this code.

# Once you've done this we will need to tell the code where mallet lives
malletPath = os.path.join("mallet-2.0.8","bin","mallet")

# train the model:
ldaModel = gensim.models.wrappers.ldamallet.LdaMallet(malletPath,corpus=processedCorpus,
                            id2word=corpusDictionary,num_topics=numberOfTopics,
                            optimize_interval=50, prefix="my")

corpusLda = ldaModel[processedCorpus]

topics = ldaModel.show_topics(num_topics=20, num_words=5)

for topic in topics:
    print(topic)