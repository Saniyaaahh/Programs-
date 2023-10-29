class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print((f"Id number is {self.idnumber}"))

class emp(person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        person. __init__(self, name, idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print((f"Id number is {self.idnumber}"))
        print(f"post = {self.post}")
        print(f"Salary = {self.salary}")

miran = emp("Syed Miran", 38, 90000, "CEO")
saniya = emp("Yasmin Saniya", 46, 100000, "CFO")
asma = emp("Asma Khan", 40, 45000, "Asst CEO")
aziz = emp("Abdul aziz", 29, 70000, "HR")
jaleel = emp("Abdul jaleel", 35, 30000, "Web Developer")
afham = person("Mohd Afham", 57)

saniya.details()
