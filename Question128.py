#Question12 section2



class Triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.number_of_sides=3
    def check_angles(self):
        sum_angles=self.angle1+self.angle2+self.angle3
        if sum_angles==180:return True
        else:return False
    def tri_print(self):
        print(self.number_of_sides)
my_triangle=Triangle(90,30,60)
print(my_triangle.check_angles())
my_triangle.tri_print()


