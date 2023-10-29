# using try/except methods

files = input("Enter your file name: ")
try:
    fhand = open(files)
except:
    print("file cannot be opened")
    quit()
fhand = open(files)
count = 0
for line in fhand:
    if line.startswith("hello"):
        count = count + 1
print("there were", count, "subject lines in", files)
