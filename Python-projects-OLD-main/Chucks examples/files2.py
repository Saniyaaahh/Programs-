# counting lines of any file

fhand = open("mbox")
count = 0
for line in fhand:
    count = count + 1
print("Line Count: ", count)