# Editing lists is pretty easy too:
intList = [1, 2, 3, 4, 5]

# Change item at index 3 (the fourth item)
intList[3] = 10
print(intList)

# Add an item to the end:
intList.append(6)
print(intList)
# remove an item from the end 
intList.pop()
print(intList)

# You can also specify the index to remove:
intList.pop(1)
print(intList)

# You can insert at a specific index:
intList.insert(1,42)
print(intList)

# Lists have some unexpected behaviors that the basic 
# datatypes do not many list methods will modify them in 
# place, meaning they do not need to be reassigned to the
# variable