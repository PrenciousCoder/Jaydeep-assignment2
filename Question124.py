#Question 10 scetion2
class Student:
    def __init__(self):
        self.admno=input()
        self.sname=input("Enter the student name: ")
        """self.OS_marks=input("Input marks: ")
        self.CA_marks=input("Enter the marks: ")
        self.DBMS_marks=input("Enter the marks: " )"""
    def Enter_Marks(self):
        self.OS_marks=input("Input marks: ")
        self.CA_marks=input("Enter the marks: ")
        self.DBMS_marks=input("Enter the marks: " )
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
inst.calc_total()
inst.Show_percentage(inst.calc_total())
inst.diplay_details(inst.calc_total(),inst.Show_percentage())

    