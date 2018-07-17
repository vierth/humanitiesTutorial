# The re library has many ways of finding things.
# Match (and other functions) returns a match object
import re

myString = 'hello, how are you?'
# put the pattern in first using a "raw" string
# indicated by an r
result = re.match(r'hello',myString)

# Here are some basic match object methods:

# get the string result
# the utility of this will become clear soon
print(result.group())

# get start, end, and the span
print(result.start())
print(result.end())
print(result.span())