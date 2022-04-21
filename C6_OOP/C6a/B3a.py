from math import sqrt
from B1a import Point2D


class Quadrangle(Point2D):

    def __init__(self, P1:Point2D, P2:Point2D, P3:Point2D, P4:Point2D):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.sides = self.getLens()

    def getP1(self):
        return [self.P1.x,self.P1.y]
    
    def getP2(self):
        return [self.P2.x,self.P2.y]

    def getP3(self):
        return [self.P3.x,self.P3.y]

    def getP4(self):
        return [self.P4.x,self.P4.y]

    def printP1234(self):
        return f"P1{self.getP1()}\nP2{self.getP2()}\nP3{self.getP3()}\nP4{self.getP4()}"

    def getLens(self):
        P = [self.P1, self.P2, self.P3, self.P4]
        s = []
        for i in range(len(P)):
            d = 0
            if i < len(P)-1:
                d = (P[i+1].x-P[i].x)**2 + (P[i+1].y-P[i].y)**2
            else:
                d = (P[0].x-P[i].x)**2 + (P[0].y-P[i].y)**2
            
            s.append(sqrt(d))
        
        return s

    def isRect(self):
        ac = (self.P1.x-self.P3.x)**2 + (self.P1.y-self.P3.y)**2
        if self.isParallel()==True & (ac - (self.sides[0]**2+self.sides[1]**2)<1e-6):
            return True
        else:
            return False 
        

    def isSquare(self):
        if self.isRect() == True & self.isLozenge() == True:
            return True
        else:
            return False

    def isLozenge(self):
        if self.isParallel()==True and self.sides[1] == self.sides[2]:
            return True
        else:
            return False

    def isParallel(self):
        if self.sides[0]==self.sides[2] and self.sides[1] == self.sides[3]:
            return True
        else:
            return False

    def getCircum(self):
        return sum(self.sides)

    def getArea(self):
        ac = (self.P1.x-self.P3.x)**2 + (self.P1.y-self.P3.y)**2
        T1 = self.sides[:2]+[sqrt(ac)]
        T2 = self.sides[2:]+[sqrt(ac)]
        p1 = sum(T1)/2
        p2 = sum(T2)/2
        A1 = p1
        A2 = p2
        for i in T1:
            A1*=(p1-i)
        for j in T2:
            A2*=(p2-j)

        return round(sqrt(A1)+sqrt(A2),2)










# P1 = Point2D([3,4])
# P2 = Point2D([6,1])
# P3 = Point2D([9,4])
# P4 = Point2D([6,7])

# Q = Quadrangle(P1,P2,P3,P4)

# print(Q.isLozenge())