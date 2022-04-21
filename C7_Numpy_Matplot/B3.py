import numpy as np
from math import sqrt

def f(x):
    return 1/(((2*x-1)**2)*((2*x+1)**2))

def Pi(n):
    x = np.arange(1,n+1,1)
    y = np.sum(f(x))
    pi = sqrt(16*y+8)
    delta = pi*100/np.pi
    
    return f"Pi = {pi}\nDo chinh xac = {delta}"



print(Pi(100))