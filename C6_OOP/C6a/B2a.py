from B1a import Point2D
from math import sqrt


class Triangle(Point2D):

    def __init__(self, P1:Point2D, P2:Point2D , P3:Point2D):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.sides = self.getLens()

    def printP123(self):
        return f"P1({self.P1.x},{self.P1.y})\nP2({self.P2.x},{self.P2.y})\nP3({self.P3.x},{self.P3.y})"

    def getLens(self):
        P = [self.P1, self.P2, self.P3]
        s = []
        for i in range(len(P)):
            d = 0
            for j in range(len(self.P1)):
                if i < len(P)-1:
                    d += (P[i+1][j] - P[i][j])**2
                elif i == len(P)-1:
                    d += (P[0][j]-P[i][j])**2
            s.append(sqrt(d))

        return s

    def isEquTri(self):
        if abs(self.sides[0]-self.sides[1])<1e-6 and abs(self.sides[1]-self.sides[2])<1e-6:
            return True
        else:
            return False

    def isIsoTri(self):
        if abs(self.sides[0]-self.sides[1])<1e-6 or abs(self.sides[1]-self.sides[2])<1e-6 or abs(self.sides[2]-self.sides[0])<1e-6:
            return True
        else:
            return False

    def isRigAngTri(self):
        C = self.sides[::]
        Cmax = C[0]
        pos = 0
        for i in range(len(self.sides)):
            if Cmax<self.sides[i]:
                Cmax = self.sides[i]
                pos = i
        del C[pos]
        m = 0
        for i in C:
            m += i**2

        return True if abs(m-Cmax**2)<=1e-6 else False

    def isInside(self, P:Point2D):
        T1 = Triangle(self.P1, self.P2, P)
        T2 = Triangle(self.P2, self.P3, P)
        T3 = Triangle(self.P1, self.P3, P)

        if T1.getArea()+T2.getArea()+T3.getArea() <= self.getArea():
            return True
        else:
            return False

    def getCircum(self):
        return sum(self.sides)
    
    def getArea(self):
        p = self.getCircum()
        
        return sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))

    def getCenter(self):
        G = [(self.P1[i]+self.P2[i]+self.P3[i])/3 for i in range(self.P1)]
        
        return Point2D(G)


P1 = [2,5]
P2 = [2,1]
P3 = [8,1]

T = Triangle(P1,P2,P3)

print(T.getLens())