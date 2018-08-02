# We've talked a lot about processing texts, but we haven't dealt much with 
# how to get texts. One of the best ways is via the internet. Many websites
# offer APIs (Application Programming Interfaces) and it is also possible to
# "scrape" others (though you should always be careful about the ethics of 
# this). Any time you are thinking about scraping a page, you should first look
# at its "robots.txt" For example: https://en.wikipedia.org/robots.txt

# First and foremost: be a good citizen!! If you find yourself running requests
# inside a loop, use time.sleep() to slow down the loop!

# In order to get anything off the internet, we must connect to it.
import urllib.request

# Let's put the url we want to access in a variable
url = "https://en.wikipedia.org/wiki/United_States_Attorney_for_the_Southern_District_of_New_York"

# We will use a request object to get the page here
request = urllib.request.urlopen(url)

# We will use the "read" function to get the contents (much like w/ files)
contents = request.read()

# Close the request object
request.close()

# Print the results:
print(contents)