import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plb

#x = [1, 2, 3, 4]
#y = [3, 5, 7, 9]
#z = [10, 8, 6, 4]
#x = np.arange(-4, 4, 0.1)
#x = np.linspace(-4, 4, 25)
x = np.linspace(0, 2 * np.pi, 50)
#y = x * x
#y2 = x * x + 2
#y3 = x * x - 2
#y = np.square(x)
#y2 = np.square(x) + 2
#y3 = np.square(x) + 4
y = np.sin(x)
y2 = np.cos(x - np.pi / 2)
plt.grid(True)
plt.xlabel('My X values')
plt.ylabel('My Y values')
plt.title('My first graph')
#plt.axis([0, 5, 2, 11])
plt.plot(x, y, 'b^', linewidth = 3, markersize = 7, label = 'Sin(x)')
plt.plot(x, y2, 'r-', linewidth = 3, markersize = 7, label = 'Cos(x)')
#plt.plot(x, y3, 'g-^', linewidth = 3, markersize = 7, label = 'Green line')
#plt.plot(x, z, 'r:o', linewidth = 3, markersize = 7, label = 'Red line')
plt.legend(loc = 'upper center')
plt.show()
