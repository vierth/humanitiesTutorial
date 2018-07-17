# Errors that are not syntax errors will not be highlighted by
# most plain text editors (like this one)

# An index error
myList = [1,2,3,4,5,6]
print(myList[200])

# A key error
myDict = {"Paul":10, "Shannon": 11}
print(myDict["Roger"])

# A zero division error:
5/0