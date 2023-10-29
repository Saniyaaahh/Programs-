# searching through a file with NO space between 2 lines

fhand = open("mbox")
for line in fhand:
    line = line.rstrip()
    if line.startswith("hello"):
        print(line)