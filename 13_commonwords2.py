# Let's clean the paragraph up a bit. We don't want to 
# consider "It" and "it" two different words, so let's make
# everything lowercase
myParagraph = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy’s country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties."

myParagraph = myParagraph.lower()

# Let's also delete the punctuation, so "London." and "London"
# aren't two different words. (there are better ways to do 
# this that we will see later)
myParagraph = myParagraph.replace(",", "")
myParagraph = myParagraph.replace(".", "")

# Otherwise, the code is the same:
words = myParagraph.split(" ")
uniqueWords = set(words)
mostCommonWord = []
mCWFreq = 0
for word in uniqueWords:
    if word != " ":
        freq = words.count(word)
        if freq > mCWFreq:
            mCWFreq = freq
            mostCommonWord = [word]
        elif freq == mCWFreq and word not in mostCommonWord:
            mostCommonWord.append(word)
        
# Print the final results
print(f"The most common word(s) is/are {mostCommonWord}, which occur(s) {mCWFreq} time(s)!")