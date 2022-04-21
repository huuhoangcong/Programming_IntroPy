import numpy as np


#KHOI TAO
A = np.ones((3,3)) - np.eye(3)
C = 4*(np.ones((3,3)) - np.eye(3))
D = 7*(np.ones((3,3)) - np.eye(3))

for i in range(2,10):
    B = i*(np.ones((3,3)) - np.eye(3))
    if i in [2,3]:
        A = np.hstack([A,B])
    elif i in [5,6]:
        C = np.hstack([C,B])
    elif i in [8,9]:
        D = np.hstack([D,B])

A = np.vstack([A,C,D])
print(A,'\n')

#DOI VI TRI 1va9, 3va7
a = np.copy(A)

for i in range(len(a)):
    for j in range(len(a[i])):
        if   a[i,j] == 1:
             a[i,j] = 9
        elif a[i,j] == 9:
             a[i,j] = 1
        elif a[i,j] == 3:
             a[i,j] = 7
        elif a[i,j] == 7:
             a[i,j] == 3

print(a,"\n")

#1,4,7
y = np.hsplit(A,3)
print(y[0],"\n")

#4,5,6
x = np.vsplit(A,3)
print(x[1],"\n")

#3,6
m = np.vstack([np.vsplit(y[2],3)[0],np.vsplit(y[2],3)[1]])
print(m, "\n")

#8,9
n = np.hstack([np.hsplit(x[2],3)[1],np.hsplit(x[2],3)[2]])
print(n, "\n")


for i in [1,4,7]:
    for j in [1,4,7]:
        if j==1:
            A[i,j]+=i+j-1
        elif j==4:
            A[i,j]+=i+j-3
        elif j==7:
            A[i,j]+=i+j-5
print(A)