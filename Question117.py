#Question 14 section1
class Rev_string:
    def __init__(self,string):
        self.string=string
    def reverse(self):
        result=""
        for char in self.string:
            result=char+result
        return result

inst=Rev_string(string=input("Enter the string"))
print(inst.reverse())
