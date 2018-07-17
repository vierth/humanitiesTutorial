# and/or allow for more complicated boolean statements:

# and evaluates True if both statements are true
i = 6
if i <10 and i >5:
    print("i is less than ten but greater than 5")

# or evaluates True if one or the other statements evalute true
if i < 5 or i <10:
    print("i is either less than five or less than ten (possibly both)")

# You can also combine these and control order of evaluation with parantheses:
if (i > 5 and i < 10) or i > 100:
    print("i fits the criteria")