total = 0
count = 0
while True:
    inp = input("Enter numbers and Enter 'done' when finished: ")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count = count + 1
avg = total / count

print("Average is ", avg)

# using list

'''numlist = list()
while True:
    inp = input("Enter numbers and Enter 'done' when finished: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)
avg = sum(numlist) / len(numlist)
print("avg is ", avg)'''