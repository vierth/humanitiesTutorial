# Sometimes you will want to look for the literal
# instance of something that is a special character
import re

# you can do this by putting \ before the character:
results = re.findall(r"\[.+\]", "It happened in [1980].")
print(results)

# \. will find a literal period
# \+ find a plus sign
# \* find a star