from math import sqrt

def tamNoiTiep(A,B,C):
    #DIEN TICH TAM GIAC
    S = (abs(((B[0]-A[0])*(C[1]-A[1]))-((C[0]-A[0])*(B[1]-A[1]))))/2
    if S == 0:
        return "ABC thang hang"
    else:
        #CAC VECTOR
        AB = [B[i]-A[i] for i in range(len(B))]
        BC = [C[i]-B[i] for i in range(len(B))]
        AC = [C[i]-A[i] for i in range(len(B))]

        #DO DAI CAC CANH
        ab = sqrt(AB[0]**2 + AB[1]**2)
        bc = sqrt(BC[0]**2 + BC[1]**2)
        ac = sqrt(AC[0]**2 + AC[1]**2)

        d = ab+bc+ac

        # TOA DO TAM NOI TIEP
        I = [(bc*A[i]+ac*B[i]+ab*C[i])/d for i in range(len(A))]

        return I
    
A = list(map(float, input("Nhap A(x,y): ").split(',')))
B = list(map(float, input("Nhap B(x,y): ").split(',')))
C = list(map(float, input("Nhap C(x,y): ").split(',')))
a = tamNoiTiep(A,B,C)
print(a)