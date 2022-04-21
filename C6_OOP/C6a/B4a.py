from B3a import Quadrangle
from B1a import Point2D

class Rectangle(Quadrangle):

    def __init__(self, P1:Point2D, P3:Point2D):
        self.P1 = P1
        self.P3 = P3
        Quadrangle.__init__(self, self.P1, self.getP2(), self.P3, self.getP4())

    def getP1(self):
        return super().getP1()
    
    def getP2(self):
        P2 = [self.P3.x,self.P1.y]
        return Point2D(P2)

    def getP3(self):
        return super().getP3()

    def getP4(self):
        P4 = [self.P1.x,self.P3.y]
        return Point2D(P4)
    
    def getLens(self):
        return super().getLens()
    
    def getCircum(self):
        return super().getCircum()

    def getArea(self):
        return super().getArea()

    

        


P1 = Point2D([3,4])
P3 = Point2D([5,7])

Q = Rectangle(P1,P3)

print(Q.getP1())