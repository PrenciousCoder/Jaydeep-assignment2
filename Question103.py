from unicodedata import name

from numpy import roll


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def PrintStudent(self):
        print(self.name)
        print(self.roll)
    def testprint(self):
        print("This is test print")


s5=Student("hello",5)
s4=Student("Devansh",4)
s3=Student("jaydeep",3)
s2=Student("python",2)
s1=Student("world",1)
#s1.testprint()
s1.PrintStudent()
s2.PrintStudent()
s3.PrintStudent()
s4.PrintStudent()
s5.PrintStudent()

