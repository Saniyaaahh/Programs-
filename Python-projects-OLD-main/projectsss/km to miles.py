# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
x = 0.621371

# calculate miles
miles = kilometers * x

print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))