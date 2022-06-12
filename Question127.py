#Question 14 section2
class String:
    def __init__(self,string):
        self.string=string
    def word(self):
        final_string=[]
        result=""
        vowels='AEIOUaeiou'
        for val in self.string:
            if val in vowels:
                #final_string=self.string.replace(val,(chr(ord(val)+1)))
                final_string.append((chr(ord(val)+1)))
            else:
                final_string.append(val)
        result = ''.join(map(str, final_string))
        return result
inst=String(string=input("Ente rthe string: "))
print(inst.word())