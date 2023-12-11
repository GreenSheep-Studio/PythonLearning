import matplotlib.pyplot as plt
import numpy as np
from math import pi
ListI = [eval(x) for x in input().split(" ")]
ListU = [eval(x)*1000 for x in input().split(" ")]

ListB = [(4 * pi * (10e-7) * 24000 * x ) for x in ListI]

x = np.array(ListU)
y = np.array(ListB)

z = np.polyfit(x, y, 2)
p = np.poly1d(z)
yval = p(x)

plot2 = plt.plot(x, yval, 'r-')
plot1 = plt.plot(ListU, ListB, 'bo')
plt.xlabel('U')
plt.ylabel('B')
plt.title('B vs U')
plt.show()