# searching through a file with space between 2 lines

fhand = open("mbox")
for line in fhand:
    if line.startswith("hello"):
        print(line)