# Python contains many useful methods that tell us about the contents
# of our variables. A useful method for strings is "count"
myString = "Hello, how are you today?"

# Count how many "a"s are in the string
aFreq = myString.count("a")
print(aFreq)

# Alternatively, you can search for a variable:
countTerm = "a"
aFreq = myString.count(countTerm)
print(aFreq)