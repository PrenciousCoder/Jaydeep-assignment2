#Question 7 scetion1

class Roman:
    def __init__(self,num):
        self.num=num
    def convert(self):

        m = ["", "M", "MM", "MMM","MMMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
        
        thousand=m[self.num//1000]
        hundreds=c[(self.num%1000)//100]
        tens=x[(self.num)//10]
        ones=i[self.num%10]

        result=(thousand+hundreds+tens+ones)
        return result
    
inst=Roman(num=int(input("Enter the number: ")))
print(inst.convert())