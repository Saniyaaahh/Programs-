import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("https://www.espncricinfo.com/player/marcus-stoinis-325012")

counts = dict()
for line in fhand:
    words = line.decode().split
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)