#Question8 Section1
class Brackets:
    def __init__(self,string):
        self.brackets=['()', '{}', '[]']
        self.string=string
    def validate(self):
        while any(x in self.string for x in self.brackets):
            for br in self.brackets:
                self.string=self.string.replace(br,'')
        return not self.string
    
inst=Brackets(string=input("Enter the string: "))
print(inst.validate())

