#factorial {While loop}

n = int(input('Please enter any number = '))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f'The factorial of {n} is {fact}')