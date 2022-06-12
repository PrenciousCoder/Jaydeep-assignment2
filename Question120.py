#Question4 section 2
class Sum:
    def __init__(self,n,suma):
        self.n=n
        self.suma=suma
    def validate(self):
        temp=0
        for i in range(0,self.n+1):
            temp=temp+i
            print(temp)
        if self.suma==temp:
            return "Yes"
        else:
            return "No"

inst=Sum(4,10)
print(inst.validate())

