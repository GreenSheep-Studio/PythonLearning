import matplotlib.pyplot as plt
import numpy as np
from math import pi

ListIin = [eval(x) for x in input().split(" ")]
ListIout = [eval(x) for x in input().split(" ")]
ListR = [(4 / x * 1000) for x in ListIout]
ListB = [(4 * pi * (10e-7) * 8 * 24000 * x / 1000) for x in ListIin]

plt.plot(ListR, ListB, "ro")
plt.xlabel("R")
plt.ylabel("B")
plt.title("B vs R")
plt.show()
