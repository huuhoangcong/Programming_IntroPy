
class Polynominal:

    def __init__(self, P):
        self.P = P

    def __add__(self,P1):
        if len(P1) != len(self.P):
            return "Hai da thuc khong cung bac"
        else:
            for i in range(len(P1)):
                P1[i] += self.P[i]
            
            return P1

    def __sub__(self,P1):
        S = []
        if len(P1) != len(self.P):
            return "Hai da thuc khong cung bac"
        else:
            for i in range(len(P1)):
                S.append(P1[i] - self.P[i])
            
            return Polynominal(S)

    def __mul__(self,a):
        Q = [i*a for i in self.P]
        return Polynominal(Q)

    def __truediv__(self,a):
        T = [i/a for i in self.P]
        return Polynominal(T)

    def daoHam(self,n):
        D = self.P[:len(self.P)-n]
        for i in range(n):
            for j in range(len(D)):
                D[j] = D[j]*(len(self.P)-i-j-1)
        
        return Polynominal(D)

    def __str__(self):
        l = len(self.P)
        dathuc = ""
        for i in range(l):
            if self.P[l-i-1]==0:
                continue
            else:
                if i == 0:
                    dathuc += str(self.P[l-1])
                else:
                    if i == 1:
                        if self.P[l-2] == 1:
                            dathuc += f" + x"
                        elif self.P[l-2] == -1:
                            dathuc += f" - x"
                        else:
                            dathuc += f" + {self.P[l-2]}*x" if self.P[l-2] > 0 else f" - {abs(self.P[l-2])}*x"
                    else:
                        if self.P[l-i-1] == 1:
                            dathuc += f" + x^{i}"
                        elif self.P[l-i-1] == -1:
                            dathuc += f" - x^{i}"
                        else:
                            dathuc += f" + {self.P[l-i-1]}*x^{i}" if self.P[l-i-1] > 0 else f" - {abs(self.P[l-i-1])}*x^{i}"

        return dathuc
                                  
    def tichPhan(self,x1,x2):
        h = (x2-x1)/10000
        S = 0
        for i in range(0,10000):
            x = x1 + h*i
            y = 0
            for j in range(len(self.P)):
                y += self.P[j] * (x**(len(self.P)-j-1))
            
            S += h*y
        
        return S

    
                

P1 = Polynominal([2,3,1])
P2 = Polynominal([1,0,-3,4,2])
print(P2.daoHam(2))
print(P2)
print(P1.tichPhan(2,3))

print(P1/2)