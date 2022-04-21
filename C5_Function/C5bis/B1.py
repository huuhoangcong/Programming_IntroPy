def viTriTuongDoi(P,A,B):
    pos = (P[0]-A[0])*(B[1]-A[1]) - (P[1]-A[1])*(B[0]-A[0])
    if pos == 0:
        return "P thuoc duong thang AB"
    elif pos > 0:
        return "P nam phia duoi cua AB"
    else:
        return "P nam phia tren cua AB"

P=[3,4]
A=[1,3]
B=[5,0]

print(viTriTuongDoi(P,A,B))