num1 = float(input("enter number = "))
op = input("enter operator = ")
num2 = float(input("enter number = "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")