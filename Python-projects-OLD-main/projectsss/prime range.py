lower = int(input("Enter the first number in a interval = "))
upper = int(input("Enter the last number in a interval = "))

print(f"The prime numbers from {lower} tp {upper} are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)