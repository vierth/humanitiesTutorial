# Dictionaries let you store information with a key, value pair.
# These are useful when the order of information doesn't matter
# create them with curly brackets. Like lists, you can store any
# kind of information in a dictionary, including other dictionaries

# Creating an empty dictionary:
myDictionary = {}
myDictionary = dict()

# Creating a dictionary with values:
ages = {"Paul":34, "Padma":25, "Gorp":155}

# The computer will not remember the order.
print(ages)

# Use the keys to extract information:
gorpAge = ages["Gorp"]
print(gorpAge)

# You can add data to a dictionary easily:
ages["Blobl"] = 20
print(ages)

# You will get a KeyError if you try to get information that doesn't exist
shannonAge = ages["Shannon"]