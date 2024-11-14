class Person :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

class Student (Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.hslcyear = year

x = Student('Poonam','Kalita',2027)
x.printname()
print(x.hslcyear)