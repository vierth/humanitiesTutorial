# We can improve this code. What if there are two characters that occur
# the same number of times? We would certainly want to know this:

myParagraph = "Hi, my name is Paul Vierthaler"
# Create a variable to store the most common character. Only this time, use a list:
mostCommonCharacter = []

mCCFreq = 0


for char in myParagraph:

    if char != " ":
        freq = myParagraph.count(char)
        if freq > mCCFreq:
            mCCFreq = freq

            # Note that now we are saving the character inside a list!
            mostCommonCharacter = [char]

        # If freq is equal to the current value then save the other character too!
        elif freq == mCCFreq:
            mostCommonCharacter.append(char)
        
        # Let's print the values each time to track what is happening:
        print(mostCommonCharacter, mCCFreq)

# Print the final results
print(f"The most common character(s) is/are {mostCommonCharacter}, which occur(s) {mCCFreq} time(s)!")