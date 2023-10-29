# finding the smallest value

smallest = None
print("before")
for value in [4, 5, 56, 85, 74, 76, 79, 71, 78, 51, 52, 57, 45, 48, 49, 21, 23, 25, 3, 26, 24, 27, 2, 28]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("done !")