import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.optimize import curve_fit

ListArc = [eval(x) for x in input().split(" ")]
ListU = [eval(x) for x in input().split(" ")]

x = np.array(ListArc)
x = np.array(ListU)

def linear_function(x, a, b, c):
    return a * sin (b * x + c)

params, covariance = curve_fit(linear_function, x, y) 
a, b, c = params
fitted_y = linear_function(x, a, b, c)


plt.plot(ListArc, ListU, "rx")
plt.plot(x, fitted_y, color='red', label='Fitted Curve')
plt.xlabel("Arc Length")
plt.ylabel("U")
plt.title("U vs Arc Length")
plt.show()
