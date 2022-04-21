import numpy as np
from matplotlib import pyplot as plt


L = 5
u_base = 0
v_base = 2*L
u = np.array([u_base, 0, 0, 0, u_base], dtype = float)
v = np.array([v_base, 0, 0, 0, v_base], dtype = float)
u[1] = -(L*np.cos(np.pi/6))
v[1] = v[0] - L*np.sin(np.pi/6)
u[2] = u[1]
v[2] = v[1] - L
u[3] = u_base
v[3] = v_base - L

for i in [0, 2*np.pi/3, -2*np.pi/3]:
    x = u*np.cos(i) + v*np.sin(i)
    y = v*np.cos(i) - u*np.sin(i)
    x_negative = -x
    y_negative = y
    plt.subplot()
    # plt.plot(x,y)
    plt.fill(x,y, color = '#032B91')
    plt.fill(x_negative, y_negative, color = '#1488DB')
    plt.axis('equal')
plt.text(0, -0.2, 'BK', fontsize = 50, color = '#032B91', ha = 'center')
plt.text(0, -2, 'TP.HCM', fontsize = 20, color = '#1488DB', ha = 'center')


print(u)
plt.show()