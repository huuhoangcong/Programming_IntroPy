def trongTam_TamGiac(A,B,C):
    S = (abs(((B[0]-A[0])*(C[1]-A[1]))-((C[0]-A[0])*(B[1]-A[1]))))/2
    
    if S == 0:
        return "ABC thang hang"
    else:
        x = (A[0]+B[0]+C[0])/3
        y = (A[1]+B[1]+C[1])/3
    
    return [x,y]