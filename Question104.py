from pickle import MARK
from unicodedata import name

from numpy import roll


class Student:
    def __init__(self,name:str,roll:int,marks:int):
        self.name=name
        self.roll=roll
        self.marks=marks
        
    def PrintStudnet(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
        

s1=Student("Devansh",1,marks=int(input("Enter the marks: ")))
s2=Student("jaydeep",2,marks=int(input("Enter the marks: ")))
s3=Student("karan",3,marks=int(input("Enter the marks: ")))
s4=Student("jim",4,marks=int(input("Enter the marks: ")))
s5=Student("john",5,marks=int(input("Enter the marks: ")))

s1.PrintStudnet()
s2.PrintStudnet()
s3.PrintStudnet()
s4.PrintStudnet()
s5.PrintStudnet()
