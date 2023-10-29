# counting

counts = dict()
list = ["bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom", "sos", "bob", "mom"]
for name in list:
    counts[name] = counts.get(name, 0) + 1
print(counts)