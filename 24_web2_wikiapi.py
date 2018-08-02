# Generally, it is much better to use an API than to directly download a
# website as we did in the last script. These are designed for communication 
# requests from applications.
import urllib.request


# Wikipedia has many differnet ways of accessing its data. Here is the url
# to one of its apis:
# some of this discussion of wikipedia's api comes from Daniel Schiffman's 
# video at https://www.youtube.com/watch?v=RPz75gcHj18
apiURL = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search='

# We can add a searchterm to the end of this run a search!
searchTerm = "pandas"

# we can add them togehter to call the API:
apiCall = apiURL + searchTerm

# Whenever you access a website from a script, it is good to have a way for the
# site to identify you. Put in your own email address here
wikiHeader = {'User-Agent':'Paul'}

# Let's create a request to send that incorperates our header:
wikiRequest = urllib.request.Request(apiCall, headers=wikiHeader)

# Let's make the call now and save the response as a string
request = urllib.request.urlopen(wikiRequest)
responseData = request.read().decode()
request.close()

# The result:
print(responseData)