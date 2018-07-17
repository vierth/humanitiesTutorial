# Regular expressions are extremely useful.
# They let us search for patterns in a text
# We can use them in Python with the re library
import re

# Regular expressions can be used like normal 
# search strings:
myString = 'hello, how are you?'
result = re.match('hello',myString)
print(result)