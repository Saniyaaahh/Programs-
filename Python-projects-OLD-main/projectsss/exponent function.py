def raise_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result
print(raise_power(3,3))