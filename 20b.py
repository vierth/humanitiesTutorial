# for loops are less dangerous than while loops.

# Print up to (but not including) 10
for i in range(10):
    print(f"1: {i} is not yet 10")

# you can also specify a starting place
for i in range(2, 10):
    print(f"2: {i} is not yet 10, but started at 2")

# here you can change i in the loop, but it will not affect how i increments
for i in range(10):
    print(f"3: {i} is not yet 10")
    i += 10
    print(f"added 10 and now have {i}")