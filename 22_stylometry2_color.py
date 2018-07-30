# Very often it is useful to convey information using color. What if we wanted 
# to color code the leaf labels based on the year in which the story was
# written? This code will do that:
import re, nltk, os
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# First, lets set up some information to use. In what year was each of these 
# stories written?
storyYear = {"Engineer's Thumb":1892,"Red-headed League":1891,"Twisted Lip":1891,
            "Identity":1891,"Noble Bachelor":1892,"Beryl Coronet":1892,
            "Orange Pips":1891,"Blue Carbuncle":1892,"Copper Beeches":1892,
            "Boscombe Valley":1891,"Bohemia":1891, "Speckled Band":1892}

# Let's set some colors for each year:
yearColor = {1891:"magenta",1892:"green"}


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
countVectorizer = TfidfVectorizer(max_features=1000, use_idf=False)
countMatrix = countVectorizer.fit_transform(sherlockTexts)
similarity = euclidean_distances(countMatrix)
linkages = linkage(similarity,'ward')

dendrogram(linkages, labels=shortTitles, orientation="right", leaf_font_size=8,leaf_rotation=45)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tight_layout()

# let's get an axis object so we can manipulate the color of the labels
ax = plt.gca()
# get the labels
labels = ax.get_ymajorticklabels()
# iterate through each label and set its color based on the dictionaries we set
# up earlier
for label in labels:
    label.set_color(yearColor[storyYear[label.get_text()]])

plt.show()