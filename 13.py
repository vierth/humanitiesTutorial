# Lists always stay in the same order, so you can get information out
# very easily. List indexes act very similar to string indexs
intList = [1, 2, 3, 4, 5]

# Get the first item
print(intList[0])

# Get the last item
print(intList[-1])

# Alternatively:
print(intList[len(intList) - 1])

# Get the 2nd to 4th items
print(intList[1:5])

# Instead of find, lists have "index"
print(intList.index(2))