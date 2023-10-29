# using "in"


fhand = open("mbox")
for line in fhand:
    line = line.rstrip()
    if not "syed" in line:
        continue
    print(line)