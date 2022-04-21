from math import sqrt
def vitriHai_DuongTron(C1,C2):
    k1 = C1[2]+C2[2]
    k2 = C1[2]-C2[2] if C1[2]>C2[2] else C2[2]-C1[2]
    d = sqrt((C2[0]-C1[0])**2+(C2[1]+C2[1])**2)
    if d>k2 and d<k1:
        return "Hai duong tron cat nhau"
    elif d == k1:
        return "Hai duong tron tiep xuc ngoai"
    elif d == k2:
        return "Hai duong tron tiep xuc trong"
    elif d > k1:
        return "Hai duong tron o ngoai nhau"
    elif d < k2:
        return "Hai duong tron long nhau"
    else:
        return "Hai duong tron dong tam"