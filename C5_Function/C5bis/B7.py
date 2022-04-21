def dotProduct(a,b): #tich vo huong 2 vecto
    tich = 0
    if len(a) != len(b):
        return "2 vector khong cung size"
    else:
        for i in range(len(a)):
            tich += a[i]*b[i]
        
        return tich


def tamNgoaiTiep(A,B,C):
    #DIEN TICH TAM GIAC
    S = (abs(((B[0]-A[0])*(C[1]-A[1]))-((C[0]-A[0])*(B[1]-A[1]))))/2
    if S == 0:
        return "ABC thang hang"
    
    else:
        #CAC VECTOR
        AB = [B[i]-A[i] for i in range(len(B))]
        BC = [C[i]-B[i] for i in range(len(B))]
        AC = [C[i]-A[i] for i in range(len(B))]

        #KIEM TRA TAM GIAC VUONG
        if dotProduct(AB,AC)==0:
            xO = (B[0]+C[0])/2
            yO = (B[1]+C[1])/2
        elif dotProduct(AB,BC)==0:
            xO = (A[0]+C[0])/2
            yO = (A[1]+C[1])/2
        elif dotProduct(BC,AC)==0:
            xO = (B[0]+A[0])/2
            yO = (B[1]+A[1])/2
        else:
            xO = (A[0]+B[0]+C[0])/3
            yO = (A[1]+B[1]+C[1])/3
        
        return [xO,yO]

A = list(map(float, input("Nhap A(x,y): ").split(',')))
B = list(map(float, input("Nhap B(x,y): ").split(',')))
C = list(map(float, input("Nhap C(x,y): ").split(',')))
a = tamNgoaiTiep(A,B,C)
print(a)