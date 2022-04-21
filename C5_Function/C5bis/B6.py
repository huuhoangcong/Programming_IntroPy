def dotProduct(a,b): #tich vo huong 2 vecto
    tich = 0
    if len(a) != len(b):
        return "2 vector khong cung size"
    else:
        for i in range(len(a)):
            tich += a[i]*b[i]
        
        return tich


def trucTam_TamGiac(A,B,C):
    S = (abs(((B[0]-A[0])*(C[1]-A[1]))-((C[0]-A[0])*(B[1]-A[1]))))/2
    
    if S == 0:
        return "ABC thang hang"
    else:
        AB = [B[i]-A[i] for i in range(len(B))]
        BC = [C[i]-B[i] for i in range(len(B))]
        AC = [C[i]-A[i] for i in range(len(B))]
        if dotProduct(AB,AC)==0:
            return A
        elif dotProduct(AB,BC)==0:
            return B
        elif dotProduct(BC,AC)==0:
            return C
        else:
            if AC[1]==0:
                x = B[0]
                y = ((-1)*AB[0]*BC[0]/BC[1])+A[1]
            elif BC[1]==0:
                x = A[0]
                y = (AB[0]*AC[0]/AC[1])+B[1]
            else:
                m = BC[0]-BC[1]*(AC[0]/AC[1])
                t = A[0]*BC[0]-B[0]*AC[0]*(BC[1]/AC[1])-BC[1]*(B[1]-A[1])
                x = t/m
                y = ((A[0]-x)*BC[0]/BC[1])+A[1]
            
            return [float(x),float(y)]



A = list(map(float, input("Nhap A(x,y): ").split(',')))
B = list(map(float, input("Nhap B(x,y): ").split(',')))
C = list(map(float, input("Nhap C(x,y): ").split(',')))
a = trucTam_TamGiac(A,B,C)
print(a)