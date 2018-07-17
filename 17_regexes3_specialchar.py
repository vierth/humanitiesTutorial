# Regexes are useful because we can find patterns
# of text using certain special characters
import re

# \d 
# matches a number
# Note that re.match() only finds something at the beginning of
# the string, so we will use search instead
result = re.search(r'\d', "It is the year 2018.")
print(result)

# \D
# matches not a number
result = re.search(r'\D', "It is the year 2018.")
print(result)

# \s
# matches whitespace
result = re.search(r'\s', "It is the year 2018.")
print(result)

# \S
# matches NOT whitespace
result = re.search(r'\S', "It is the year 2018.")
print(result)

# There are other whitespace special characters:
# \t matches a tab, \n matches a new line

# \w
# matches letters and numbers
result = re.search(r'\w', "It is the year 2018.")
print(result)

# \W
# matches NOT letters and numbers
result = re.search('r\W', "It is the year 2018.")
print(result)

# .
# matches anything except a new line
result = re.search(r'.', "It is the year 2018.")
print(result)

# \b
# matches a word boundary (so we won't find the ship in "friendship"):
result = re.search(r"\bship","Will we find friendship or an ocean ship?")
print(result)

# ?
# make optional:
result = re.search(r"humou?r","Americans spell it humor.")
print(result)

# +
# Used in conjunction with something else, matches one or more
# instance of something:
result = re.search(r'\d', "It is the year 2018.")
print(result)

# *
# Used in conjunction with something else, matches zero or more
# instance of something:
result = re.search(r'\d*', "It is the year 2018.")
print(result)