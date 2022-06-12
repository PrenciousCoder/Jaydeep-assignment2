#Question4 section3
class Robot:
    def __init__(self,UP,DOWN,LEFT,RIGHT):
        self.UP=UP
        self.DOWN=DOWN
        self.LEFT=LEFT
        self.RIGHT=RIGHT
    def position(self):
        countup=countup+self.UP
        countdown=countdown+self.DOWN
        countleft=countleft+self.LEFT
        countright=countright+self.RIGHT
        x=countright-countleft
        y=countup-countdown
        return x,y
    def distance(self,x,y):
        X=x**2
        Y=y**2
        temp=X+Y
        dist=temp**(1/2)
        return dist

inst=Robot(5,3,3,2)

