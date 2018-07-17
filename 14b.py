# You can turn strings into lists easily:
myString = "Hello, my name is Paul."

# Turn into list of characters
myList = list(myString)
print(myList)

# Turn into list of words:
myList = myString.split(" ")
print(myList)

# Turn back into string:
newString = " ".join(myList)
print(newString)