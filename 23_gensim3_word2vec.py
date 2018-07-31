# Word embedding models are a popular tool these days and gensim has an 
# implementation of the popular word2vec model
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


# the word2vec model wants tokenized sentences, so we will break our documents
# apart in a slightly different way
refinedSentences = []
for text in sherlockTexts:
    sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]
    for sent in sentences:
        refined = [lemmatizer.lemmatize(word) for word in sent if word.isalnum() and word not in stopwords]
        refinedSentences.append(refined)

# Create the model
word2vecModel = gensim.models.Word2Vec(refinedSentences)

# After training you can get the vectors for individual words:
word2vecModel.wv['sherlock']

# You can check similar words:
closetohim = word2vecModel.wv.most_similar("him")
print(f"{closetohim} is similar to 'him'")

# You can also preform math on vectors
new = word2vecModel.wv.most_similar(positive=['woman','gentleman'],negative=['man'])
print(f"Woman plus gentleman minus man is {new}" )