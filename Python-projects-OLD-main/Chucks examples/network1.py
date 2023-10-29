# using urlibb

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("https://www.espncricinfo.com/player/marcus-stoinis-325012")
for line in fhand:
    print(line.decode().strip())