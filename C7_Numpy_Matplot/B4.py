import numpy as np
import matplotlib.pyplot as plt

def createArray(N):
    if N<2:
        return None
    elif N == 2:
        return 1
    elif N%2==0:
        return np.hstack([np.array([int(N/2)]), createArray(int(N/2))])
    else:
        return np.hstack([np.array([3*N+1]), createArray(3*N+1)])



N = int(input("Input N: "))
arr = createArray(N)
print(arr)
print(np.size(arr))

x = []
y = []
for i in range(2,N+1):
    x.append(i)
    y.append(np.size(createArray(i)))

plt.bar(x,y)
plt.xlabel("N")
plt.ylabel("Length of Array")
plt.title("The correlation between N and length of Array")
plt.show()