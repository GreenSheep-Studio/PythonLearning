import matplotlib.pyplot as plt
import numpy as np
ListU = [eval(x) for x in input().split(" ")]
ListR = [eval(x) for x in input().split(" ")]
ListI = [(i/j)*1000 for i, j in zip(ListU, ListR)]

for i in ListI:
    print(f"{i:.3f}", end=' ')

plt.scatter(ListU, ListI, color='red', marker='o')
plt.title('U vs I')
plt.xlabel('U')
plt.ylabel('I')
plt.grid(True)
plt.show()