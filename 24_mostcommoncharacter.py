# Now we can build a program that actually does something! Let's calculate the most common
# character in this paragraph:
myParagraph = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy’s country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties."

print(myParagraph)

# Create a variable to store the most common character
mostCommonCharacter = ""

# Create a variable to track how often the character occurs
mCCFreq = 0

# Go through each character and count how often it occurs
for char in myParagraph:

    # Remember, we saw the count method earlier!
    freq = myParagraph.count(char)

    # if freq is greater than the current value stored in mCCFreq, it is the most common
    # character seen so far! Save both the frequency and the character
    if freq > mCCFreq:
        mCCFreq = freq
        mostCommonCharacter = char

# Print the results:
print(f"The most common character is {mostCommonCharacter}, which occurs {mCCFreq} times!")