# If/Else statements allow you to execute a different block of
# code if the first statement fails:

if 30 < 20:
    print("Hey, isn't it weird? 30 is smaller than 20!")
else:
    print("Eh, I guess 30 wasn't smaller than 20.")



# You can add multiple conditions with elif

if 10 > 10:
    a = "10 is larger than 10"
elif 10 == 10:
    a = "10 is equal to 10"
elif 10 < 10:
    a = "10 is smaller than 10"
else:
    a = "everything is meaningless"

print(a)