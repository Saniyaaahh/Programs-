employ_file = open("emplo", "r")
print(employ_file.read())
employ_file.close()

# readable() = gives boolean wheather readable or not
# read() = reads whole file
# readline () = reads one line
# readlines ()[2] = reads based on index number

# using for loop

employ_file = open("emplo", "r")
for emp in employ_file.readlines():
    print(emp)
    employ_file.close()