# same as above using continue function

fhand = open("mbox")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("hello"):
        continue
    print(line)