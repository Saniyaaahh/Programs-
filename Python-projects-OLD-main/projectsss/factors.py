def factors(x):
    print("the factors of ", x,"are: ")
    for i in range(1, 1 + x):
        if x % i == 0:
            print(i)

num = 532

factors(num)