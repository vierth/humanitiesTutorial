# In many cases, we will want to use functions to perform some
# task and then return a value that we can save to a variable:
def add(num1, num2):
    result = num1 + num2
    # use the return keyword to do this
    return result

# We can include code in the return line if we like:
def add(num1, num2):
    return num1 + num2

print(add(10,10))