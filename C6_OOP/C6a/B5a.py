from B1a import Point2D
from B3a import Quadrangle


class Square(Quadrangle):

    def __init__(self, P1:Point2D, L):
        self.P1 = P1
        self.L = L
        Quadrangle.__init__(self, P1, self.getP2(), self.getP3(), self.getP4())

    def getP1(self):
        return super().getP1()

    def getP2(self):
        P2 = [self.P1.x+self.L, self.P1.y]
        return Point2D(P2)
    
    def getP3(self):
        P3 = [self.getP2().x, self.P1.y+self.L]
        return Point2D(P3)

    def getP4(self):
        P4 = [self.P1.x, self.P1.y+self.L]
        return Point2D(P4)

    def getCircum(self):
        return super().getCircum()

    def getArea(self):
        return super().getArea()



P1 = Point2D([-8,6])
L = 2
S = Square(P1, L)

print(S.getCircum())