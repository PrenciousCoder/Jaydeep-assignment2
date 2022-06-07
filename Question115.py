#Question 10 scetion1
pi=22/7
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        
        ar=pi*(self.radius*self.radius)
        return ar
    def circumference(self):
        circum=2*pi*self.radius
        return circum

inst=Circle(49)
print(inst.area())
print(inst.circumference())