# You can get all the keys in a dictionary:
ages = {"Paul":34, "Padma":25, "Gorp":155}
print(ages.keys())

# You can iterate through a dictionary in several ways:
# Just the keys
for key in ages.keys():
    print(key, ages[key])

# Just the values
for value in ages.values():
    print(f"value: {value}")

# Both the keys and the values
for key, value in ages.items():
    print(key, value)

