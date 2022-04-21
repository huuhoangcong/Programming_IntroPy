def Canbac2(x, e = 1e-5):
    s=1
    while abs(s**2-x)>e:
        s = s+0.5*(x/s-s)
    
    return s

a = Canbac2(9)
print(a)