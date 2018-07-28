# You can replace individual characters with replace:
myString = "Hello, my name is Paul!"

# replace all a's with o's
aomixup = myString.replace("a","o")
print(aomixup)

# You can also replace multiple characters at once:
autooo = myString.replace("au", "oo")
print(autooo)

# By saving the result to the same variable name, you can edit 
# it:
print(myString)
myString = myString.replace("a","o")
print(myString)