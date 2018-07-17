# You will often want to sort these values. While you can't technically
# sort a dictionary while keeping a dictionary, you can save a sorted
# representation:

myParagraph = "In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy’s country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties."
myParagraph = myParagraph.lower()
myParagraph = myParagraph.replace(",", "")
myParagraph = myParagraph.replace(".", "")

words = myParagraph.split(" ")
uniqueWords = set(words)

wordFrequencies = {}
for word in uniqueWords:
    if word != " ":
        freq = words.count(word)
        wordFrequencies[word] = freq

# Sort the keys by their values
sortedWords = sorted(wordFrequencies, key=wordFrequencies.get)
# Reverse sort the keys
revSortedWords = sorted(wordFrequencies, key=wordFrequencies.get, reverse=True)

# Print the sorted list
print(sortedWords)

# Print the top ten words and their values:
for word in revSortedWords[:10]:
    print(f"{word}: {wordFrequencies[word]}")
