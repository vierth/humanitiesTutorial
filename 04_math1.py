# All of your basic math operators are available in Python

# Addition (mathematical operations will return an integer 
# when all numbers are integers, floats if one number is 
# float)
add = 10 + 10
addf = 10 + 10.0
print(f"Addition (integer result): {add}")
print(f"Addition (float result): {addf}")

# Subtraction
sub = 10 - 5
print(f"Subtraction: {sub}")

# Multiplication
mult = 10 * 3
print(f"Multiply: {mult}")

# Division
# In Python 3, you can get a float back from division:
div = 10/3
print(f"Division (float result): {div}")

# Integer division:
# If you want integer division (returning an integer and 
# dropping remainder, you have to use //)
intdiv = 10//3
print(f"Division (integer): {intdiv}")

# Get the remainder with modulo:
rem = 10 % 3
print(f"Modulo (remainder): {rem}")

# Exponential
exp = 3 ** 2
print(f"Exponent: {exp}")