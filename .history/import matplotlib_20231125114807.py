import matplotlib.pyplot as plt
import numpy as np
ListU = [eval(x) for x in input().split(" ")]
ListR = [eval(x) for x in input().split(" ")]
ListI = [(i/j)*1000 for i, j in zip(ListU, ListR)]

for i in ListI:
    print(f"{i:.3f}", end=' ')

x = np.array(ListU)
y = np.array(ListI)

z = np.polyfit(x, y, 6)
p = np.poly1d(z)
print('\n\n')
print(p)
yvals = p(x)
plot1 = plt.plot(x,y,'*', label = 'orv')
plot2 = plt.plot(x,yvals,'r', label = 'fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 4)
plt.show()