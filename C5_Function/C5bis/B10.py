def cungPhia(A,B,d):
    #HAM VI TRI CUA 2 DIEM A,B so voi duong thang d
    m = d[0]*A[0]+d[1]*A[1]+d[2] #Thay toa do A vao d
    n = d[0]*B[0]+d[1]*B[1]+d[2] #Thay toa do B vao d

    if m*n>0:
        return True
    else:
        return False


def tuGiac(A,B,C,D):
    
    #CAC VECTOR
    AB = [B[i]-A[i] for i in range(len(B))]
    CD = [D[i]-C[i] for i in range(len(C))]
    AD = [D[i]-A[i] for i in range(len(C))]
    BC = [B[i]-C[i] for i in range(len(B))]

    #Phap vector duong thang AB,CD,AD,BC
    n1 = [AB[1],-AB[0]]
    n2 = [CD[1],-CD[0]]
    n3 = [AD[1],-AD[0]]
    n4 = [BC[1],-BC[0]]
    #Duong thang AB, CD, AD,bc
    ab = [n1[0],n1[1],-n1[0]*A[0]-n1[1]*A[1]]
    cd = [n2[0],n2[1],-n2[0]*C[0]-n2[1]*C[1]]
    ad = [n3[0],n3[1],-n3[0]*A[0]-n3[1]*A[1]]
    bc = [n4[0],n4[1],-n4[0]*C[0]-n4[1]*C[1]]

    #Kiem tra C,D co thuoc ab khong neu co thi khong tao thanh tu giac
    if ab[0]*C[0]+ab[1]*C[1]+ab[2] == 0 or ab[0]*D[0]+ab[1]*D[1]+ab[2]==0:
        return "A,B,C,D khong tao thanh tu giac"

    else: # Neu C,D khong thuoc ab
        if cungPhia(C,D,ab) == True: #Khi C,D cung phia ab

            #Kiem tra B,C co thuoc ad khong. neu co thi ko tao tu giac
            if ad[0]*C[0]+ad[1]*C[1]+ad[2] == 0 or ad[0]*B[0]+ad[1]*B[1]+ad[2]==0:
                return "A,B,C,D khong tao thanh tu giac"

            else: #Neu B,C khong thuoc ad                
                if cungPhia(B,C,ad) == True: #khi B, C cung phia ad

                    if cungPhia(A,D,bc) == False: #Kiem tra AD cung phia bc khong
                        return "ABCD la tu giac lom"
                    else:
                        return "ABCD la tu giac loi"
                else:
                    return "ABCD khong phai la tu giac"
        else:
            if cungPhia(A,B,cd) == True:
                return "ABCD la tu giac lom"
            else:
                return "ABCD khong tao thanh tu giac"


#NHAP TOA DO CAC DIEM
A = list(map(float,input("Nhap A(x,y): ").split(',')))
B = list(map(float,input("Nhap B(x,y): ").split(',')))
C = list(map(float,input("Nhap C(x,y): ").split(',')))
D = list(map(float,input("Nhap D(x,y): ").split(',')))

a = tuGiac(A,B,C,D)
print(a)