# double split

line = "i am awesome Miran yes no yes no"
words = line.split()
yes = words[2]
no = yes.split("e")
print(no)