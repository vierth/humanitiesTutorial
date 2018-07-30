# In many cases we will want to run our analysis on multiple texts at once.
# We'll get to that in a minute. Sometimes, however, it is useful to break up
# a file into useful components. Let's do this to our holmes.txt file

# Go take a look at it and see if you can figure out how to divide it!

# We'll use regular expressions:
import re, os

rf = open("holmes.txt","r",encoding="utf8")
text = rf.read()
rf.close()
# Cut off the boilerplate at the end
text = text[:text.rfind('End of Project Gutenberg')]

# You'll notice that all of the stories begin with "ADVENTURE" and then a roman
# numeral, followed by the title. Let's use that to break the text apart:
shortStories = re.split(r"ADVENTURE [IVX]+\. ([A-Z\-' ]+)", text)

# Note that I've captured [A-Z\-'\s ]+. This will return the Title of the 
# section as every other item in the list. Let's just save these to individual
# files.

# First, let's make a folder for them if one doesn't already exist:
if not os.path.isdir("corpus"):
    os.mkdir("corpus")


# Delete the first item, which is just preamble
shortStories = shortStories[1:]

# Even items are titles, odd items are stories:
for i in range(0,len(shortStories)-1):
    # Use modulo to check if i is even. If it is, then the item at i in the
    # shortStories list will be a title. The next item will be its text
    if i % 2 == 0:
        filename = shortStories[i]+".txt"
        story = shortStories[i+1]
        wf = open(f"corpus/{filename}","w")
        wf.write(story)
        wf.close()

# Ta-Da!