#Question 10 scetion2
class Student:
    def __init__(self):
        self.admno=input("Enter: ")
        self.sname=input("Enter the student name: ")
        """self.OS_marks=input("Input marks: ")
        self.CA_marks=input("Enter the marks: ")
        self.DBMS_marks=input("Enter the marks: " )"""
    def Enter_Marks(self):
        self.OS_marks=int(input("Input marks: "))
        self.CA_marks=int(input("Enter the marks: "))
        self.DBMS_marks=int(input("Enter the marks: " ))
    def calc_total(self):
        total_marks=self.OS_marks+self.CA_marks+self.DBMS_marks
        return int(total_marks)
    def Show_percentage(self,t_marks):
        percentage=(t_marks/300)*100
        return int(percentage)
    def diplay_details(self,t_marks,percent):
        print(t_marks)
        print(percent)
inst=Student()
inst.Enter_Marks()
var_marks=inst.calc_total()
print(var_marks)
#inst.calc_total()
print(inst.Show_percentage(int(var_marks)))
var_percentage=inst.Show_percentage(int(var_marks))
inst.diplay_details(var_marks,var_percentage)

    