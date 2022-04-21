import numpy as np


A = np.array([[2,-1,4,5]])
B = np.array([[1,2,0,-1]])
C = np.array([[2,-3,-2,5],[1,2,1,6]])
D = np.array([[-4,5,7,-10],[2,-4,3,0]])

E = np.transpose(A).dot(B)
print(E)
F = C.dot(np.transpose(D))
print(np.trace(F))
d = np.linalg.det(F)**2
print(np.trace(E*d))
G = np.transpose(A+B)/(np.transpose(C).dot(D))
print(np.trace(G))
H = E.dot(np.transpose(C))
print(np.trace(H))

K = np.linalg.eig(E)
print(K)
I = np.linalg.eig(F)
print(I)

A1 = np.reshape(A,(2,2))
B1 = np.reshape(B,(2,2))
T = A1.dot(C)+np.transpose(np.transpose(D).dot(B1))
print(T)