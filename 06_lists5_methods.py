# Some useful list methods:
intList = [1, 2, 5, 3, 4]

# Get the number of elements in the list:
print(len(intList))

# Get minimum value from list
minimumvalue = min(intList)
print(minimumvalue)

#Get maximum value
maxvalue = max(intList)

# Reverse the list (in place)
intList.reverse()
print(intList)

# Sort the list
intList.sort()
print(intList)

# Sort in reverse order
intList.sort(reverse=True)