# You can also provide default values using keyword arguments
# These must come AFTER the positional arguments
def whoseFunction(yourname, myname, interaction="greating"):
    if type == "greating":
        print(f"Hi, {yourname}! My name is {myname}!")
    elif type == "parting":
        print(f"Goodbye, {yourname}. I, {myname}, will miss you.")

# Now give the function both inputs. If you don't provide the 
# keyword arguement, it will use the default value.
whoseFunction("Paul", "Pim")

# This does the same thing:
whoseFunction("Paul", "Pim", interaction="greating")

# This is different:
whoseFunction("Paul", "Pim", interaction="parting")

