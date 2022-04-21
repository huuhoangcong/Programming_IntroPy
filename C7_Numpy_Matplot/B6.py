import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,1,1e-4)

plt.grid('on', color = '#E5E5E5')

plt.plot(x,x, linestyle = '-', )
plt.text(0.4,0.5,r'$y = x$')

plt.plot(x,x**3, linestyle = '--')
plt.text(0.6,0.1,r'$y = x^3$')

plt.plot(x,np.exp(x), linestyle = ':')
plt.text(0.45,1.75,r'$y = e^x$')

plt.plot(x,np.exp(x**3), linestyle = '-.', linewidth = 2)
plt.text(0.8,1.5,r'$y = (e^x)^3$')

plt.legend([r'$y=x$',r'$y=x^3$',r'$y = e^x$',r'$y = (e^x)^3$'])
plt.xlim(0,1)
plt.show()