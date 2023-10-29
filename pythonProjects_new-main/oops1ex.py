class csd:
    att = "students"

    def __init__(self, name, rollnumber, gender, address, promo):
        self.name = name
        self.rollnumber = rollnumber
        self.gender = gender
        self.address = address
        self.promo = promo

    def intro(self):
        print(f"Myself is {self.name} with roll number {self.rollnumber} and {self.gender}. I stay in {self.address} and i had been {self.promo} this year")

asma = csd("Asma khan", 40, "female", "Tolichowki", "passed")
aziz = csd("Abdul Aziz", 29, "male", "Falaknuma", "passed")
miran = csd("Syed Miran", 38, "male", "Tolichowki", "passed")
san = csd("Yasmin Saniya", 46, "female", "Langer Houze", "passed")
muqeeth = csd("Syed Muqeeth", 11, "male", "Al Hasnath colony", "passed")

miran.intro()
asma.intro()
san.intro()
aziz.intro()
muqeeth.intro()

