# Let's visualize the information from this topic model using the files that
# MALLET produced.
import matplotlib.pyplot as plt
import seaborn as sns

# Let's load in the information. mytopickeys contains info on the topics
topicsFile = open("mytopickeys.txt","r")
topicsInfo = topicsFile.read().split("\n")
topicsFile.close()

topics = {}

for line in topicsInfo:
    if line != "":
        topicInfo = line.split("\t")
        # Get topic number:
        topicNumber = topicInfo[0]
        # Get the topic weight:
        weight = float(topicInfo[1])
        # Get the words and make them into a list. Delete the empty item at the end
        words = topicInfo[2].split(" ")[:-1]
        # Save information
        topics[topicNumber] = (weight, words)

print(topics["0"])

# Let's visualize the weight of each topic as a bar chart:
sns.set() # Let's make it pretty

index = [i for i in range(len(topics))]
# Get the weight of each topic in order
weights = [topics[str(i)][0] for i in range(len(topics))]
# Create some labels:
labels = [f"Topic {i}" for i in range(len(topics))]


sns.barplot(index, weights)
plt.xticks(index,labels,rotation=90)
plt.xlabel("Topic")
plt.ylabel("Weight")
plt.title("Topic Weights")
plt.tight_layout()
plt.show()