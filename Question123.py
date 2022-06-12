#Question 8 section2
class Subset:
    def __init__(self,arr):
        self.arr=arr
    def display(self):
        length=int(pow(2,len(self.arr)))
        s=set()
        self.arr.sort()
        for i in range(length):
            subset=[]
            for j in range(len(self.arr)):
                if i & (1<<j):
                    subset.append(self.arr[j])
            s.add(tuple(subset))
        print(s)

inst=Subset([4, 5, 6])
inst.display()

