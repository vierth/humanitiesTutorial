# if/elif/else statements are one of our first opportunities 
# to encounter a bug where the code will run but gives us a
# bad answer. 

# the interpreter will exit the block as soon as ANYTHING 
# evaluates true. beware this situation:
a = 10

if a > 1:
    b = "a is closest to 1"
elif a > 5:
    b = "a is closest to 5"
elif a > 6:
    b = "a is closest to 6"
elif a > 8:
    b = "a is closest to 8"
else:
    b = "not sure what you are looking for"

print(b)