from math import *

for i in range(0, 95, 5):
    ii = radians(i)
    print('sin({}) = {:.2f}, cos({}) = {:.2f}'.format(i, sin(ii), i, cos(ii)))