# In many cases, we will want to load a set of texts from file. Let's load
# the files we just saved into the corpus folder
import os

# Let's create an object to contain the corpus:
sherlockTexts = {}


# Use the os.walk function to iterate through all the files in the folder
for root, dirs, files in os.walk("corpus"):
    for filename in files:
        with open(f"{root}/{filename}") as rf:
            title = filename[:-4] # Remove the file extension
            title = title.lower() # Let's make it lower case for readability
            shortStory = rf.read()
            sherlockTexts[title] = shortStory
    
# You can see that we've successfully loaded each of the texts into this dict
for key, value in sherlockTexts.items():
    print(f"Successfully loaded {key}, which is {len(value)} characters long.")