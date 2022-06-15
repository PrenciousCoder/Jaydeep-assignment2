class HybridPriorityQueue:
    def __init__(self,K):
        self.K=K
    def add(self,n):
        self.K.append(n)
    def remove(self):
        self.K.remove(self.K[-1])
        return self.K[-1]
    def isEmpty(self):
        if len(self.K)==0:
            return True
        else:
            return False
    def getorderedlist(self):
        temp=[]
        for i in range(len(self.K)):
            temp.append(self.K[-i])
            return temp
