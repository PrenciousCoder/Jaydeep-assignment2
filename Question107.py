class MyString:
    def __init__(self,S):
        self.S=S
    def replaceAll(self,substring1,substring2):
        """for substring1 in range(len(self.S)):
            if self.S[substring1] == substring1:
                self.S[substring1] = substring2
        
        temp="".join(self.S)
        print(temp)

        #return "".join(self.S)"""
        temp=""
        string=self.S
        print(string)
        for i in string:
            if i!=substring1:
                temp+=i
                #print(temp)
            else:

                temp+=substring2
                print(temp)
        print(temp)


        



inst=MyString("Hello World")
inst.replaceAll("lo","icopter")