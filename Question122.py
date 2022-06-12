#Question 7 section2
class String:
    def __init__(self):
        self.string=""
    def get_string(self):
        string=input("Enter the string: ")
        print(string)
        return string
    def print_string(self,string):
        final_string=string.upper()

        #print(final_string)
        return final_string

inst=String()
temp=inst.get_string()
inst.print_string(temp)
