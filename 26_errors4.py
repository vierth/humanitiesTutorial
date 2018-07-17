# Python lets you handle these errors with try/except:
myDict = {"Paul":10, "Shannon": 11}

# Try to execute this code
try:
    person = myDict["Peter"]
# If there is an error, do this instead
except KeyError:
    print("Person not in dictionary")