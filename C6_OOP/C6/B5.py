from matplotlib import pyplot as plt
from math import sqrt



class Polygon:
    def __init__(self, n, points):
        self.n = n
        self.points = points
        self.sides = []
        
        for i in range(len(self.points)):
            d = 0
            if i < len(self.points)-1:
                for j in range(len(self.points[i])):
                    d += (self.points[i+1][j]-self.points[i][j])**2
            elif i == len(self.points)-1:
                for j in range(len(self.points[i])):
                    d += (self.points[0][j]-self.points[i][j])**2
            self.sides.append(sqrt(d))

    def draws(self):
        self.points.append(self.points[0])
        xs, ys = zip(*self.points)
        plt.plot(xs,ys)
        plt.show()
        del self.points[len(self.points)-1]

    def perimeter(self):
        return sum(self.sides)                

# P = [[1,2],[3,5],[2,7]]
# n = Polygon(3,P)
# n.draws()





class Triangle(Polygon):

    def __init__(self, points):
        Polygon.__init__(self, 3, points)

    def area(self):
        p = self.perimeter()/2
        return sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))
    
    def pointInTriangle(self, P):
        t1 = Triangle([self.points[0],self.points[1],P])
        t2 = Triangle([self.points[1],self.points[2],P])
        t3 = Triangle([self.points[2],self.points[0],P])
        delta = self.area() - (t1.area()+t2.area()+t3.area())
        
        return True if abs(delta)<1e-8 else False

    def rightTriangle(self):
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

        return True if abs(m-Cmax**2)<=1e-8 else False
        

P = [[1,2],[1,6],[5,2]]
M = [2,4]
n = Triangle(P)
print(n.pointInTriangle(M))
print(n.rightTriangle())
