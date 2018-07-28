# Boolean operators can be used on non-numeric variables too

# Are two strings the same?
"a" == "b"
# This is true

# You can also check if two variables are the same object:
a = ["hello"]
b = ["hello"]
# This evaluates to false because the two lists exist at two
# different memory locations and are not the same object
print(a is b)

# This is true, because c refers to the same object as a
c = a
print(a is c)