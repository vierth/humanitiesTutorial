# If we want to parse the html on a website so we can organize information 
# more effectively, Anaconda includes the Beautiful Soup library
from bs4 import BeautifulSoup

# You load in a page from a urllib call, but I prefer to save html and then
# parse it from my files. Here you can see the file we downloaded earlier:

soup = ""

with open("wikiAttorneys.html","r",encoding="utf8") as rf:
    # lxml just specifies the parser to use. You can leave this off, but I 
    # include it here to supress a warning
    soup = BeautifulSoup(rf.read(),"lxml")

# You can pretty print the file with soup.prettify()

# Let's get all the links:
links = soup.find_all("a")

# Print the text and url for the first link:
linktext = links[2].string
url = links[2].get("href")
print(f"{linktext}: {url}")

# Lets ge some information off of this page. I'll use my knowledge of html to 
# extract the necessary information.
# Find all of the lists on the page:
lists = soup.find_all('ul')

# The third list on the page contains information on all the attorneys general
# get each item from the list
attsgen = lists[2].find_all('li')

# Print out the most recent one (the list item in this list):
print(f"Current Attorney General: {attsgen[-1].text}")