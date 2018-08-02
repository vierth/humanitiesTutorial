# Let's plot the topic distribution in every document on a single plot! We need
# to reload everything from the last piece of code up to where we started 
# plotting the data.
import os
import matplotlib.pyplot as plt
import seaborn as sns

ignoreFiles = set([".DS_Store","LICENSE","README.md"])
sherlockTitles = []
for root, dirs, files in os.walk("corpus"):
    for fn in files:
        if fn not in ignoreFiles:
            sherlockTitles.append(fn[:-4].lower())

shortenTitle = {"the adventure of the engineer's thumb":"Engineer's Thumb", 
                'the red-headed league':"Red-headed League", 'the man with the twisted lip':"Twisted Lip",
                'a case of identity':"Identity", 'the adventure of the noble bachelor':"Noble Bachelor",
                'the adventure of the beryl coronet': "Beryl Coronet", 'the adventure of the speckled band':"Speckled Band", 
                'the five orange pips':"Orange Pips", 'the adventure of the blue carbuncle':"Blue Carbuncle",
                'the adventure of the copper beeches':"Copper Beeches", 'the boscombe valley mystery':"Boscombe Valley",
                'a scandal in bohemia':"Bohemia"}

shortTitles = [shortenTitle[title] for title in sherlockTitles]

docTopicsFiles = open("mydoctopics.txt","r")
dti = docTopicsFiles.read().split("\n")
docTopicsFiles.close()

# We will need the total number of topics for later
totalTopics = 0
documentTopics = {}
for title,line in zip(shortTitles,dti):
    info = line.split("\t")
    documentTopics[title] = [float(weight) for weight in info[2:]]
    totalTopics = len(info[2:])

# We need to do a bit of data munging. Let's put each document's topic weights
# in a list of lists. Essentially, we need a list for each topic where each 
# item is a document's weight for that topic
docWeightPerTopic = [[] for i in range(totalTopics)]
for title in shortTitles:
    weights = documentTopics[title]
    for i, weight in enumerate(weights):
        docWeightPerTopic[i].append(weight)

# Now, the first item in this list will have the weight for topic one in each 
# of our documents!

# Make the plot!
index = range(len(documentTopics))
labels = [f"T {i}" for i in range(totalTopics)]
plt.stackplot(index,docWeightPerTopic,labels=labels)
plt.xticks(index,shortTitles,rotation=90)
plt.legend()
plt.tight_layout()
plt.show()