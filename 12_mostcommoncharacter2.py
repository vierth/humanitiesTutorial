# It isn't so interesting that " " is the most common character. Let's ignore the spaces!
myParagraph = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy’s country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties."
mostCommonCharacter = ""
mCCFreq = 0

for char in myParagraph:

    # ignore spaces! This is the only change!
    if char != " ":
        freq = myParagraph.count(char)
        if freq > mCCFreq:
            mCCFreq = freq
            mostCommonCharacter = char

print(f"The most common character is {mostCommonCharacter}, which occurs {mCCFreq} times!")