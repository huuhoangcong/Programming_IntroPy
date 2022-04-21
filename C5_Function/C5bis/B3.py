from math import sqrt
def viTriDiem_DuongTron(P,C):
    d = sqrt((P[0]-C[0])**2+(P[1]-C[1])**2)
    if d == C[2]:
        return "P nam tren C"
    elif d < C[2]:
        return "P nam trong C"
    else:
        return "P nam ngoai C"