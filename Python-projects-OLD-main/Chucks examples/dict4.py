counts = dict()
print("Enter the file name: ")
line = input(" ")


words = line.split()
print("WORDS: ", words)
print("Counting Now.....")

for word in words:
    counts[word] = counts.get(word, 0) + 1
print("COUNTS: ", counts)