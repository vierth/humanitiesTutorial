# Note that last time we got a list of with many duplicates!
# Let's only save the character if we are not already tracking
# it!

myParagraph = myParagraph = "Hi, my name is Paul Vierthaler"

mostCommonCharacter = []

mCCFreq = 0


for char in myParagraph:

    if char != " ":
        freq = myParagraph.count(char)
        if freq > mCCFreq:
            mCCFreq = freq

            
            mostCommonCharacter = [char]

        # Save if freq is equal to the current value and char
        # not already in the list!
        elif freq == mCCFreq and char not in mostCommonCharacter:
            mostCommonCharacter.append(char)
        
        # Let's print the values each time to track what is
        # happening:
        print(mostCommonCharacter, mCCFreq)

# Print the final results
print(f"The most common character(s) is/are {mostCommonCharacter}, which occur(s) {mCCFreq} time(s)!")