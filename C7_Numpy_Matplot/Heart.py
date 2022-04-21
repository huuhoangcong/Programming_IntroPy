import numpy as np
import matplotlib.pyplot as plt


alpha = np.linspace(0, 2*np.pi,100)

x = 16*np.sin(alpha)**3
y = 13*np.cos(alpha) - 5*np.cos(2*alpha) - 2*np.cos(3*alpha) - np.cos(4*alpha)

plt.plot(x, y, color = 'r')
plt.fill(x, y, color = 'r')
plt.axis('equal')
plt.show()