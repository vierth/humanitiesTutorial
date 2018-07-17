# Some operators in regular expressions are greedy.
# This means they will match the longest possible 
# string.
import re

myString = 'arglebargle!'

result = re.search(r'a.+e',myString)
print(result.group())

# If I just want to match argle, then I can use a ? 
# after the + to make this a non-greedy search
result = re.search(r'a.+?e',myString)
print(result.group())
