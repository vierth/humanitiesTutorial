# You'll notice the result we got looked like a bit of a mess. It was a JSON
# (JavaScript Object Notation) object. Fortunately, Python has a library that
# let's us easily turn that into an easy to use Python object
import json, urllib.request
apiURL = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search='
searchTerm = "pandas"
apiCall = apiURL + searchTerm
wikiHeader = {'User-Agent':'Paul'}
wikiRequest = urllib.request.Request(apiCall, headers=wikiHeader)
request = urllib.request.urlopen(wikiRequest)
responseData = request.read().decode()
request.close()

# Turn the results into a python object:
wikiResults = json.loads(responseData)

# The results come in four lists. The search term, a list of titles of pages, 
# the tagline for that page, and a list of urls for the pages. We can use the
# urls to retrieve the contents.
for title, tagline, url in zip(wikiResults[1], wikiResults[2], wikiResults[3]):
    print(f"Page Title: {title}, Tag: {tagline}, URL: {url}")