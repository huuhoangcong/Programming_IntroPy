from math import sqrt, acos, pi
class VectorCalculus:

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    
    def __add__(self, vec1):
       u = self.x + vec1.x
       v = self.y + vec1.y
       w = self.z + vec1.z
       
       return VectorCalculus(u,v,w)

    def __sub__(self, vec1):
        u = self.x - vec1.x
        v = self.y - vec1.y
        w = self.z - vec1.z
       
        return VectorCalculus(u,v,w)

    def gocGiua2Vector(self, vec1):
        t = self.x*vec1.x + self.y*vec1.y + self.z*vec1.z
        m = self.lengthVector() * vec1.lengthVector()
        return acos(t/m)*180/pi

    def tichCoHuong(self, vec1):
        i = vec1.z*self.y - self.z*vec1.y
        j = vec1.x*self.z - self.x*vec1.z
        k = vec1.y*self.x - self.y*vec1.x
        return VectorCalculus(i,j,k)

    def tichVoHuong(self, vec1):
        return self.x*vec1.x+self.y*vec1.y+self.z*vec1.z


    def lengthVector(self):
        return sqrt(self.x**2+self.y**2+self.z**2)


vec1 = VectorCalculus(1,2,3)
vec2 = VectorCalculus(4,5,6)
print(vec1.tichCoHuong(vec2))