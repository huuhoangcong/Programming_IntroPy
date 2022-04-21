from math import sqrt

def duongPhanGiac(a,b):
    d1 = sqrt(a[0]**2+a[1]**2)
    d2 = sqrt(b[0]**2+b[1]**2)

    if (d1 == 0 and (a[2]!=0 or a[2]==0)) or (d2==0 and (b[2]!=0 or b[2]==0)) :
        return "1 trong 2 duong thang khong ton tai"

    else:
        #PHAN GIAC 1
        p1 = [(d2/d1)*a[i]-b[i] for i in range(len(a))]
        #PHAN GIAC 2
        p2 = [(d2/d1)*a[i]+b[i] for i in range(len(a))]
    
        return f"{p1}\n{p2}"


#NHAP CAC LIST MO TA PHUONG TRINH DUONG THANG
a = list(map(float, input("Nhap duong thang a[x,y,t: la cac he so]: ").split(',')))
b = list(map(float, input("Nhap duong thang b[x,y,t: la cac he so]: ").split(',')))

p = duongPhanGiac(a,b)

print(p)