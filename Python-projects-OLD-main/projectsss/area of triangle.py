a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# calculate semi perimeter

s = (a + b + c) / 2

area = (s*(s-a)-(s-b)*(s-c)) ** 0.5
print(f"The area is {area}")