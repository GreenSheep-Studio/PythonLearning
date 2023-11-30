import matplotlib.pyplot as plt
import numpy as np

ListArc = [eval(x) for x in input().split(" ")]
ListU = [eval(x) for x in input().split(" ")]

plt.plot(ListArc, ListU, "rx-")
plt.xlabel("Arc Length")
plt.ylabel("U")
plt.title("U vs Arc Length")
plt.show()
