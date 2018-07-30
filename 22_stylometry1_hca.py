# We now have all the pieces we need to start doing stylometry! Let's import 
# the libraries we will need:
# brandonrose.com/clustering has a good walkthrough on document clustering 
# Go check it out!
import re, nltk, os
from pandas import DataFrame
import numpy as np

# The components for analysis:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

# The components for viz
import matplotlib.pyplot as plt

# Let's load the texts in from the corpus folder we created earlier.
# Let's add a set that contains files we want to ignore (useful if there is a
# license file, a readme, or some metafile you want to ignore)
ignoreFiles = set([".DS_Store","LICENSE","README.md"])

# The vectorizor object wants a list of texts, so we will prepare one for it
sherlockTexts = []
sherlockTitles = []
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        if filename not in ignoreFiles:
            with open(os.path.join(root,filename)) as rf:
                sherlockTexts.append(rf.read().lower())
                sherlockTitles.append(filename[:-4].lower())
                
# We will use the titles as labels, but let's make them shorter
shortenTitle = {"the adventure of the engineer's thumb":"Engineer's Thumb", 
                'the red-headed league':"Red-headed League", 'the man with the twisted lip':"Twisted Lip",
                'a case of identity':"Identity", 'the adventure of the noble bachelor':"Nobel Bachelor",
                'the adventure of the beryl coronet': "Beryl Coronet", 'the adventure of the speckled band':"Speckled Band", 
                'the five orange pips':"Orange Pips", 'the adventure of the blue carbuncle':"Blue Carbuncle",
                'the adventure of the copper beeches':"Copper Beeches", 'the boscombe valley mystery':"Boscombe Valley",
                'a scandal in bohemia':"Bohemia"}

shortTitles = [shortenTitle[title] for title in sherlockTitles]

# Get the frequencies of the 1000 most common ngrams in the corpus
countVectorizer = TfidfVectorizer(max_features=1000, use_idf=False)
countMatrix = countVectorizer.fit_transform(sherlockTexts)

# We can measure the distances between all of these documents using a variety
# of metrics. We will talk about the assumptions these distance metrics make (
# and why some might be better than others) in class.
similarity = euclidean_distances(countMatrix)

# We can group these documents together based on which ones are closest 
# together using Hierarchical Cluster Analysis. Here we use the "Ward" 
# algorithm
linkages = linkage(similarity,'ward')

# Here we will use scipy's dendogram function (which we imported) to plot this:
dendrogram(linkages, labels=shortTitles, orientation="right", leaf_font_size=8,leaf_rotation=45)

# We'll adjust the plot a bit to make it better
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# This will prevent the labels from going off the figure
plt.tight_layout()
plt.show()