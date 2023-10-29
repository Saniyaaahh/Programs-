# when we see a new name

counts = dict()
names = ["bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "lol", "non"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

