# Let's run the analysis again, but this time with the federalist papers
import re, nltk, os
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

rf = open("federalist.txt","r",encoding="utf8")
text = rf.read()
rf.close()
text = text[:text.rfind("End of the Project Gutenberg")]

# Divide based on the internal divisions ()
papers = re.split(r"FEDERALIST\.? No\.? \d+", text)
papers = papers[1:]
print(len(papers))

federalistnum = [i+1 for i in range(len(papers))]

# Create a dictionary with the authorship information
authorship={}
for i in range(len(papers)):
    fno = i+1
    if fno==10 or fno==14 or (fno>=18 and fno<=20) or (fno>=37 and fno<=48):
        authorship[str(fno)] = "Madison"
    elif (fno>=2 and fno<=5) or fno==64:
        authorship[str(fno)] = "Jay"
    elif (fno>=49 and fno<=58) or fno==62 or fno==63:
        authorship[str(fno)] = "Unknown"
    else:
        authorship[str(fno)] = "Hamilton"


authorColor = {"Hamilton":"magenta","Madison":"green","Jay":"brown","Unknown":"black"}
countVectorizer = TfidfVectorizer(max_features=1000, use_idf=False)
countMatrix = countVectorizer.fit_transform(papers)
countMatrix = countMatrix.toarray()


# Lets perform PCA on the countMatrix:
pca = PCA(n_components=2)
myPCA = pca.fit_transform(countMatrix)

# Now we need the Unique Authors
uniqueAuthors = ["Hamilton", "Madison", "Jay", "Unknown"]
# Let's get a number for each class
numberForClass = [i for i in range(len(uniqueAuthors))]
# Make a dictionary! This is new sytax for us! It just makes a dictionary where
# the keys are the unique years and the values are found in numberForClass
authForClassNumber = dict(zip(uniqueAuthors,numberForClass))

# Let's make a new representation for each document that is just these integers
# and it needs to be a numpy array
textClass = np.array([authForClassNumber[authorship[str(f)]] for f in federalistnum])


# Make a list of the colors
colors = [authorColor[auth] for auth in uniqueAuthors]

for col, classNumber, year in zip(colors, numberForClass, uniqueAuthors):
    plt.scatter(myPCA[textClass==classNumber,0],myPCA[textClass==classNumber,1],label=year,c=col)

# Let's add a legend! matplotlib will make this for us based on the data we 
# gave the scatter function.
plt.legend()
plt.show()