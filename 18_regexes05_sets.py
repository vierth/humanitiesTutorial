# You can form character sets with []
# The search will match anything between these brackets
import re

# [abc] matches a, b, or c
result = re.findall(r"[abc]+","Do you run this place?")
print(result)

# [a-e] matches any character a to e

# [a-zA-Z] matches any upper or lowercase alphabetical char

# [0-9] matches zero to nine

# [a-zA-Z0-9] matches alphanumeric characters

# [^a] matches NOT a
result = re.findall(r"[^a]+","Do you run this place?")
print(result)