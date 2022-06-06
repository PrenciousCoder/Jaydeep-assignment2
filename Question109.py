class StraightLine:
    def __init__(self,m,c):
        self.m=m
        self.c=c

line1=StraightLine(1,1)
line2=StraightLine(1,4)

def IntersectionCheck(l1:StraightLine,l2:StraightLine):
    if line1.m==line2.m and line1.c!=line2.c:
        return False
    else:
        x=(line1.c-line2.c)/(line2.m-line1.m)
        y=(line1.m*line2.m)+line1.c
    print("("+str(x)+","+str(y)+")")
    

print(IntersectionCheck(line1,line2))


