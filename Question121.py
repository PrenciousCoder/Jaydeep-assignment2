#Question6 section2
class Pair:
    def __init__(self,arr,target):
        self.target=target
        self.arr=arr
    def search(self):
        for num in self.arr:
            for i in range(0,len(self.arr)):
                temp=num+self.arr[i]
                if temp==self.target:
                    return self.arr.index(num),i
                else:
                    return None


inst=Pair([10,20,10,40,50,60,70],50)
print(inst.search())