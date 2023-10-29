d = {'Miran': 55, 'Kate': 85, 'Lamnina': 89}
d.items()
print(d.items())

sorted(d.items())
print(sorted(d.items()))

for (k,v) in sorted(d.items()):
    print(k,v)
