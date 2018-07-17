# We can easily adjust the code from the most common character to the most common word
# by splitting the paragraph into a list of words instead of characters:
myParagraph = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy’s country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties."

# get the "words" in the paragraph by splitting on the spaces:
words = myParagraph.split(" ")

# Note that I've changed the variables to reflect that I am looking at "words" and not "char"
# This is not required, but helps in understanding the code
uniqueWords = set(words)
mostCommonWord = []
mCWFreq = 0
for word in uniqueWords:
    if word != " ":

        # check the frequency inside the "words" list and NOT the myParagraph variable
        # as you will detect partial words (e.g., "these" will count as an instance of "the")
        freq = words.count(word)
        if freq > mCWFreq:
            mCWFreq = freq   
            mostCommonWord = [word]
        elif freq == mCWFreq and word not in mostCommonWord:
            mostCommonWord.append(word)
        
print(f"The most common word(s) is/are {mostCommonWord}, which occur(s) {mCWFreq} time(s)!")