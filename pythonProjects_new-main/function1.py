#(2.)(b) Demonstrate how functions return multiple values with an example?

def cricketer():
    orange_cap = input("Who won orange cap = ")
    purple_cap = input('Who won purple cap = ')
    man_of_match = input("who was man of match = ")
    return orange_cap,purple_cap,man_of_match

orange_cap, purple_cap,man_of_match = cricketer()
print(f'The orange cap and purple cap was won by {orange_cap,purple_cap}')
print(f"man of match was {man_of_match}")