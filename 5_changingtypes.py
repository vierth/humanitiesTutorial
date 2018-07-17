# You can check what type of data a variable is easily:
myNum = "3"
print(myNum, type(myNum))

# You can change one data type into another with 'casting'
# to Integer
myNum = int(myNum)
print(myNum, type(myNum))

# to float
myNum = float(myNum)
print(myNum, type(myNum))

# to string
myNum = str(myNum)
print(myNum, type(myNum))

# You will get an error if you try to cast
# something that can't be cast 
# int("hello"), for example
