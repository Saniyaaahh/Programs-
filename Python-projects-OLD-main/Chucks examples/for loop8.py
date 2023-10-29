# using a boolean

found = False
print("before", found)
for value in [4, 8, 9, 6, 25, 41, 36, 22, 23, 14, 45, 69]:
    if value == 23:
        found = True
    print(found, value)
print("done")