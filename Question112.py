#Question6 section1

class Square:
    def __init__(self,length):
        self.length=length
        
    def area(self):
        
        area=self.length*self.length
        return area
    def perimeter(self):
        perimeter=self.length*4
        return perimeter
inst=Square(length=int(input("Enter the edge length: ")))
print(inst.area())
print(inst.perimeter())
