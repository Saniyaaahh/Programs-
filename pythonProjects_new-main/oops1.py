'''class dog:
    attr1 = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

roger = dog("roger")
tommy = dog("tommy")

roger.speak()'''

class csd:
    att = "students"

    def __init__(self, name, rollno, genders):
        self.name = name
        self.rollno = rollno
        self.genders = genders

    def intro(self):
        print(f"My name is {self.name}")

    def gender(self):
        print(f"{self.name} is {self.genders}")

    def roll(self):
        print(f"{self.name}'s roll number is {self.rollno}")

asma = csd("Asma khan", 40, "female")
san = csd("Yasmin Saniya", 46, "female")
miran = csd("Syed Miran", 38, "Male")
aziz = csd("Aziz", 29, "male")
sana = csd("Syeda Sana", 54, "female")


asma.intro()
asma.gender()
asma.roll()
san.intro()
san.gender()
miran.intro()
miran.roll()
sana.intro()
sana.gender()
sana.roll()