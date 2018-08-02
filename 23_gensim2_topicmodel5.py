# That last plot looked like nonsense, so let's make it a stacked bar chart
# instead
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

totalTopics = 0
documentTopics = {}
for title,line in zip(shortTitles,dti):
    info = line.split("\t")
    documentTopics[title] = [float(weight) for weight in info[2:]]
    totalTopics = len(info[2:])


docWeightPerTopic = [[] for i in range(totalTopics)]
for title in shortTitles:
    weights = documentTopics[title]
    for i, weight in enumerate(weights):
        docWeightPerTopic[i].append(weight)

index = [i for i in range(len(documentTopics))]
labels = [f"T {i}" for i in range(totalTopics)]

# A stacked bar chart will let us plot each document's topic on a single line,
# but we need to do a bit of math at first. We need to calculate where on the
# y axis each bar should start.
baselines = [np.zeros(len(shortTitles))]
cumulative = np.zeros(len(shortTitles))

for weights in docWeightPerTopic:
    cumulative += np.asarray(weights)
    baselines.append(list(cumulative))

# Remove the last baseline, which should just be all ones
baselines = baselines[:-1]

sns.set()

for docWeights, baseline, label in zip(docWeightPerTopic,baselines,labels):
    plt.bar(index,docWeights,bottom=baseline,label=label)

plt.xticks(index,shortTitles,rotation=45)
plt.xlabel("Document Title")
plt.ylabel("Topic Weight")
plt.title("Topics by Weight")
plt.legend()
plt.tight_layout()
plt.show()