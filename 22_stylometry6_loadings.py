# In order to help with interpretation, it is often useful to plot the 
# component loadings, which will show us how individual words influence where
# documents appear in the plot.
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

federalistnum = [i+1 for i in range(len(papers))]

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

pca = PCA(n_components=2)
myPCA = pca.fit_transform(countMatrix)


uniqueAuthors = ["Hamilton", "Madison", "Jay", "Unknown"]
numberForClass = [i for i in range(len(uniqueAuthors))]
authForClassNumber = dict(zip(uniqueAuthors,numberForClass))
textClass = np.array([authForClassNumber[authorship[str(f)]] for f in federalistnum])
colors = [authorColor[auth] for auth in uniqueAuthors]

# When we plot the information, let's make the dots smaller and make them 
# transparent
for col, classNumber, year in zip(colors, numberForClass, uniqueAuthors):
    plt.scatter(myPCA[textClass==classNumber,0],myPCA[textClass==classNumber,1]
                    ,label=year,c=col, s=2,alpha=.5)

# get the component loadings. Note this comes from the pca object, not the fit
# and transformed object called myPCA:
loadings = pca.components_
# get the vocabulary from the countVectorizer:
vocabulary = countVectorizer.get_feature_names()

# Add them to the plot!
for i, word in enumerate(vocabulary):
    plt.annotate(word,xy=(loadings[0,i],loadings[1,i]))

plt.legend()
plt.show()