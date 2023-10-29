# prompt for file name counting lines

files = input("Enter your file name: ")
fhand = open(files)
count = 0
for line in fhand:
        count = count + 1
print("there were", count, "subject lines in", files)


files = input("Enter your file name: ")
fhand = open(files)
count = 0
for line in fhand:
    if line.startswith("hello"):
        count = count + 1
print("there were", count, "subject lines in", files)


