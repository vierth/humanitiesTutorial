# If you recall that normal string searching does not
# include a findall method. The re library does:
import re

myString = "In 1954 I found 28 crumpets inside the house at 11 County Road."

# findall just returns the strings
results = re.findall(r'\d',myString)
print(results)

# finditer returns match objects
results = re.finditer(r'\d',myString)
print(results)

# to see the results we need to iterate through the object:
for result in results:
    print(result)