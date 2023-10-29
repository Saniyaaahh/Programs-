meri_list = [24, 25, 28, 29, 31, 39, 35, 37, 12, 19, 45, 73, 91, 54, 75, 96, 10, 20, 99]

result = list(filter(lambda x: (x % 3 == 0), meri_list ))
print("the number 3 is divisible by ", result)