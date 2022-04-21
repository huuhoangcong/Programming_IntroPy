def viTriTuongDoi(P1,P2,A,B):
    pos1 = (P1[0]-A[0])*(B[1]-A[1]) - (P1[1]-A[1])*(B[0]-A[0])
    pos2 = (P2[0]-A[0])*(B[1]-A[1]) - (P2[1]-A[1])*(B[0]-A[0])
    if pos1 == 0:
        return "P1,P2 thuoc AB" if pos2 == 0 else "P1 thuoc AB\nP2 nam ngoai AB"
    elif pos1 != 0:
        return "P1 nam ngoai AB\nP2 thuoc AB" if pos2 == 0 else "P1,P2 thuoc AB"
    elif pos1*pos2 > 0:
        return "P1,P2 nam phia duong cua AB"
    else:
        return "P1,P2 nam khac phia am cua AB"