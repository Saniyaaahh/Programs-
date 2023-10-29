class result(object):
    def __init__(self, name, rollno, branch, gender):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.gender = gender

    def intro(self):
        print(f"Name = {self.name}")
        print(f"Roll number = {self.rollno}")
        print(f"Branch = {self.branch}")
        print(f"Gender = {self.gender}")

class sem1(result):
    def __init__(self, env, eitk, m1, ep, pps, ep_lab, pps_lab, egdp_lab, overall1):
        self.env = env
        self.eitk = eitk
        self.m1 = m1
        self.ep = ep
        self.pps = pps
        self.ep_lab = ep_lab
        self.pps_lab = pps_lab
        self.egdp_lab = egdp_lab
        self.overall1 = overall1

    def sem1_results(self):
        print(f"Environmental Science = {self.env}")
        print(f"Indian Tradition and Knowledge = {self.eitk}")
        print(f"Mathematics 1 = {self.m1}")
        print(f"Engineering Physics = {self.ep}")
        print(f"Programming for Problem Solving = {self.pps}")
        print(f"Engineering Physics Lab = {self.ep_lab}")
        print(f"Programming for Problem Solving Lab = {self.pps_lab}")
        print(f"Engg Graphics and Design Practice = {self.egdp_lab}")
        print(f"SGPA Semester 1 = {self.overall1}")
        print("___________________________________________________")
        print()
class sem2(result):
    def __init__(self, epc, ic, m2, ec, bee, bee_lab, ec_lab, ecs_lab, itw_lab,  overall2):
        self.epc = epc
        self.ic = ic
        self.m2 = m2
        self.ec = ec
        self.bee = bee
        self.bee_lab = bee_lab
        self.ec_lab = ec_lab
        self.ecs_lab = ecs_lab
        self.itw_lab = itw_lab
        self.overall2 = overall2

    def sem2_results(self):
        print(f"English for Professional Communication = {self.epc}")
        print(f"Indian Constitution = {self.ic}")
        print(f"Mathematics 2 = {self.m2}")
        print(f"Engineering Chemistry = {self.ec}")
        print(f"Basic Electrical Engineering = {self.bee}")
        print(f"Basic Electrical Engineering Lab = {self.bee_lab}")
        print(f"Engineering Chemistry Lab = {self.ec_lab}")
        print(f"English for Effective Communication Skills Lab = {self.ecs_lab}")
        print(f"Engineering and IT workshop Lab = {self.itw_lab}")
        print(f"SGPA Semester 2 = {self.overall2}")
        print("___________________________________________________")
        print()
class all(result):
    def __init__(self, name, rollno, branch, gender, result_1, cgpa):
        self.result_1 = result_1
        self.cgpa = cgpa

        result. __init__(self, name, rollno, branch, gender)

    def all_details(self):
        print("___________________________________________________")
        print()
        print(f"Name = {self.name}")
        print(f"Roll number = {self.rollno}")
        print(f"Branch = {self.branch}")
        print(f"Gender = {self.gender}")
        print(f"Result = {self.result_1}")
        print(f"CGPA = {self.cgpa}")
        print("___________________________________________________")
        print()



miran_intro = result("Syed Miran Hussain", 160921750038, "CSD", "Male")
miran_sem1 = sem1("Grade C", "Grade C", "Grade D", "Grade D", "Grade S", "Grade A", "Grade S", "Grade S", 8.09)
miran_sem2 = sem2("Grade B", "Grade D", "Grade A", "Grade B", "Grade D", "Grade A", "Grade A", "Grade A", "Grade A", 8.27)
miran_overall = all("Syed Miran Hussain", 160921750038, "CSD", "Male", "Passed", 8.15)

aziz_sem1 = sem1("Grade D", "Grade F", "Grade E", "Grade F", "Grade D", "Grade A", "Grade A", "Grade A", 0.00)
aziz_sem2 = sem2("Grade F", "Grade F", "Grade F", "Grade E", "Grade F", "Grade A", "Grade A", "Grade B", "Grade S", 0.00)
aziz_overall = all("Mohammed Abdul Aziz", 160921750029, "CSD", "Male", "Passed", 0.00)

aziz_overall.all_details()
aziz_sem1.sem1_results()
aziz_sem2.sem2_results()
