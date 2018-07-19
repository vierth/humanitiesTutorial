# There is a lot of wasted effort in the last version. We only
# need to run count a single time per character. Let's just
# get a list of the unique character and check each of those:
myParagraph = myParagraph = "Hi, my name is Paul Vierthaler"

# Get the unique characters:
uniqueChars = set(myParagraph)
print("Unique characters: ", uniqueChars)

mostCommonCharacter = []

mCCFreq = 0



# Now iterate through the unique characters instead of the 
# full string
for char in uniqueChars:

    if char != " ":
        freq = myParagraph.count(char)
        if freq > mCCFreq:
            mCCFreq = freq

            
            mostCommonCharacter = [char]

        # Save if freq is equal to the current value and char 
        # not already in the list!
        elif freq == mCCFreq and char not in mostCommonCharacter:
            mostCommonCharacter.append(char)
        

# Print the final results
print(f"The most common character(s) is/are {mostCommonCharacter}, which occur(s) {mCCFreq} time(s)!")
print(f"We got here in {len(uniqueChars)} loops instead of {len(myParagraph)}!")