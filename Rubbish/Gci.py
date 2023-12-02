import matplotlib.pyplot as plt
import numpy as np
from math import pi

ListIin = [eval(x) for x in input().split(" ")]
ListIout1 = [eval(x) for x in input().split(" ")]
ListIout2 = [eval(x) for x in input().split(" ")]
ListR1 = [(4 / x * 1000) for x in ListIout1]
ListR2 = [(4 / x * 1000) for x in ListIout2]
ListB = [(4 * pi * (10e-7) * 24000 * x ) for x in ListIin]

plt.plot(ListB, ListR1, "rx-")
plt.plot(ListB, ListR2, "bo-")
plt.xlabel("B")
plt.ylabel("R")
plt.title("R vs B")
plt.show()