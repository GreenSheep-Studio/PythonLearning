import matplotlib.pyplot as plt
import numpy as np
ListU = [x for x in eval(input())]
ListR = [x for x in eval(input())]
ListI = [(i/j) for i, j in zip(ListU, ListR)]

for i in ListI:
    print(f"{i:.3f}", end=' ')

plt.scatter(ListU, ListI, color='red', marker='o')

plt.show()