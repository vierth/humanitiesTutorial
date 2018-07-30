# Let's apply this to a real-world problem. The Federalist Papers were written
# anonymously by Alexander Hamilton, James Madison, and John Jay. Authorship of
# twelve are disputed (no 49-58, 62-63). We know that most scholars think that
# Madison, or Madison together with Hamilton, wrote these. This recreates a
# simple version of this experiment.
import re, nltk, os
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Open the text. Note that the Project Gutenberg version contains two versions
# of Federalist no 70. For simplicity's sake, I removed one.
rf = open("federalist.txt","r",encoding="utf8")
text = rf.read()
rf.close()
# Remove end boilerplate:
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

# Ascibe a color to each author:
authorColor = {"Hamilton":"magenta","Madison":"green","Jay":"brown","Unknown":"black"}

# Do the analysis
countVectorizer = TfidfVectorizer(max_features=1000, use_idf=False)
countMatrix = countVectorizer.fit_transform(papers)
similarity = euclidean_distances(countMatrix)
linkages = linkage(similarity,'ward')

dendrogram(linkages, labels=federalistnum, orientation="right", leaf_font_size=8)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tight_layout()

ax = plt.gca()
labels = ax.get_ymajorticklabels()
for label in labels:
    label.set_color(authorColor[authorship[label.get_text()]])

plt.show()