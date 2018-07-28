# If statemtents are useful when you want to execute code only
# if something is true. Otherwise skip it.

# You use a code block to do this, and code blocks in python
# start with a colon and are determined by indentation (a tab
# character or four spaces marks one level)

# So the indented code will execute IF AND ONLY IF the
# expression evalutes true. Otherwise the interpreter will
# move on to the next unindented line and continue executing
# the program

# This will execute because 10 is less than 20
if 10 < 20:
    print("Exactly!")

# This will not execute because 10 is not greater than 20
if 10 > 20:
    print("What a crazy world!")

# This will always run because it is not inside an if
# statement
print("Here we are!")