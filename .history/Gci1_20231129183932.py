import matplotlib.pyplot as plt
from math import pi
ListI = [eval(x) for x in input().split(" ")]
ListU = [eval(x)*1000 for x in input().split(" ")]

ListB = [(4 * pi * (10e-7) * 24000 * x ) for x in ListI]

plt.plot(ListU, ListB, 'bo')
plt.xlabel('U')
plt.ylabel('B')
plt.title('B vs U')
plt.show()