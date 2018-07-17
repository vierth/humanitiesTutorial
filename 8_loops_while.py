# Loops allow you to execute code over and over again, which is where
# much of the power of programmming lies

# While loops execute as long as the condition is true
# be careful with these, because it is easy to create an infinite loop!
i = 0
while i < 10:
    print(f"{i} is not yet 10.")
    # increment i. if i doesn't change, you will get an infinite loop
    i = i + 1

# it is more common to increment i with i += 1:
i = 0
while i < 10:
    print(f"{i} is not yet 10.")
    # increment i using shorthand
    i += 1