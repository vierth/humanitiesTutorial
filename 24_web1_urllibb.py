# Did you notice that that text started with a b? These means it is in bytecode
# and if we want to save it to file, we should change it to a string first
import urllib.request
url = "https://en.wikipedia.org/wiki/United_States_Attorney_for_the_Southern_District_of_New_York"
request = urllib.request.urlopen(url)
contents = request.read()
request.close()

# Decode the results into a string!
htmlstring = contents.decode()

with open("wikiAttorneys.html", "w", encoding="utf8") as wf:
    wf.write(htmlstring)