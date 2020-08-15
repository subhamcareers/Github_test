class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
        return
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

class SO(Employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.incnt=inc
    def getSalary(self):
        return self.salary + self.incnt #Overrides the getsalary method in parent class
e1=Employee("Rajesh", 9000)
print("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SO("Kirti",10000,1990)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))
