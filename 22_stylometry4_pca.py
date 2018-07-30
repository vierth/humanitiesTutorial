# Principal component analysis is another useful approach to take with 
# stylometric analysis. It uses the same initial data as HCA (matrix of word
# frequencies), but we use linear algebra to get abstracted axes that show us
# where the variance in the data is
# brandonrose.com/clustering has more info on the methods used here
import re, nltk, os
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

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

# We need to make this a dense array
countMatrix = countMatrix.toarray()


# Lets perform PCA on the countMatrix:
pca = PCA(n_components=2)
myPCA = pca.fit_transform(countMatrix)

# To plot this we will need some information (note I do this step by step. This
# is not necessary with only two classes, but handy when you have many more:
# First, let's get the unique items. Here we are coloring the data by year
uniqueYears = [1891,1892]
# We want these classes to be integers starting at zero
numberForClass = [0,1]
# Make a dictionary! This is new sytax for us! It just makes a dictionary where
# the keys are the unique years and the values are found in numberForClass
yearForClassNumber = dict(zip(uniqueYears,numberForClass))

# Let's make a new representation for each document that is just these integers
# and it needs to be a numpy array
textClass = np.array([yearForClassNumber[storyYear[s]] for s in shortTitles])


# Make a list of the colors
colors = [yearColor[year] for year in uniqueYears]

for col, classNumber, year in zip(colors, numberForClass, uniqueYears):
    plt.scatter(myPCA[textClass==classNumber,0],myPCA[textClass==classNumber,1],label=year,c=col)

# Let's add a legend! matplotlib will make this for us based on the data we 
# gave the scatter function.
plt.legend()
plt.show()