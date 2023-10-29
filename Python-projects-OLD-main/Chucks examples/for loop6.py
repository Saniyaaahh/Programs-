# finding the average

count = 0
sum = 0
print("before", count, sum)
for value in [4, 50, 65, 20, 35, 12, 85, 74, 95, 91, 21, 22, 25, 745]:
    count += 1
    sum = sum + value
    print(count, sum, value)
print("after", count, sum, sum/count)