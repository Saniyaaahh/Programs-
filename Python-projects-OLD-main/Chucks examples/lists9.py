fhand = open("mbox2")
for line in fhand:
    line = line.strip()
    if not line.startswith("from"): continue
    words = line.split()
    print(words[1])