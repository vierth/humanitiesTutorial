# Let's delve a little further into the Wikipedia api by breaking it apart
import urllib.request, json

# 
baseurl = 'https://en.wikipedia.org/w/api.php?action='

# "action" specifies the type of call you are making. We already used open 
# search. Here, "query" will let us get the contents of a specific page
action = 'query'

# different terms are linked with the ampersand
connector = '&'

# "prop: specifies the properties of the action. there are many possible 
# properties like linkshere, categories, links, etc.
# more info here https://en.wikipedia.org/w/api.php?action=help&modules=query

prop = 'categories'

# we can set the output format. json seems to be the preferred format, but xml
# is another possibility
formatinfo = "json"
# "titles" is how we search for the page to retrieve. We should replace spaces 
# with underscores so the call doesn't get rejected
searchmethod = 'titles='

# We can give the API a title of a Wikipedia page.
searchterm = 'Pandas (software)'
if " " in searchterm:
        searchterm = searchterm.replace(" ","_")

fullCall = f"{baseurl}{action}&prop={prop}&format={formatinfo}&{searchmethod}{searchterm}"
wikiHeader = {'User-Agent':'Paul'}

print("Making the following call:")
print(fullCall)

# Let's make the request and pretty print the results
request = urllib.request.Request(fullCall,headers=wikiHeader) 
with urllib.request.urlopen(request) as page:
    data = page.read().decode()
    jsondata = json.loads(data)
    prettydata = json.dumps(jsondata, indent=4)
    print(prettydata)
