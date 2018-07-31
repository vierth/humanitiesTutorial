# Let's visualize the topic distribution in a single document
import os
import matplotlib.pyplot as plt
import seaborn as sns


# Let's get the document names from the corpus folder really quickly and then
# shorten them:
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

documentTopics = {}
for title,line in zip(shortTitles,dti):
    info = line.split("\t")
    # We don't need the first two numbers, so we can eliminate them
    documentTopics[title] = [float(weight) for weight in info[2:]]

print(documentTopics["Twisted Lip"])

# Let's plot the weights for The man with the Twisted Lip!
weights = documentTopics['Twisted Lip']
index = [i for i in range(len(weights))]

sns.set()
sns.barplot(index, weights)
plt.xlabel("Topic")
plt.ylabel("Weight")
plt.title("Topic Weight in Twisted Lip")
plt.tight_layout()
plt.show()