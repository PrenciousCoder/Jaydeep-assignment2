#question 5 section1
from unicodedata import name


class Students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def printall(self):
        print(self.age)
        print(self.name)
        print(self.grade)

s1=Students("Jaydeep",69,"A")
s1.printall()