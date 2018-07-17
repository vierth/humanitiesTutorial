# reading and writing to files is an important task in Python 
# that helps us use the results our scripts produce

# Write to file
# BUT BE CAREFUL!
# This will create a new file if none exists
# but it will ERASE the file if it does exist!!
# Also, always close file objects!
writefile = open("newfile.txt","w",encoding="utf8")
writefile.write("Writing to file!")
writefile.close()

# Alternatively, you can use a context manager, which will 
# close the object for you. This the more "pythonic" way
with open("newfile.txt", "w", encoding = "utf8") as writefile:
    writefile.write("Writing to file!")

# Reading from file uses the "r" flag instead of the "w"
readfile = open("newfile.txt","r",encoding="utf8")
# the read method turns the contents into a string object
contents = readfile.read()
readfile.close()
print(contents)

# You can add data to a file with the append "a" flag:
afile = open("newfile.txt","a",encoding="utf8")
afile.write("Writing more to file!")
afile.close()