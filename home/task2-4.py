import math
eps = float(input())
i = 0
sum = 0
pai = 0
per = 0
while 1:
    per = (-1)**i / (2 * i + 1)
    sum += per
    if abs(per) < eps:
        break
    i+=1
print(i)
print(f"{1 / per:.8f}")
print(f"{pai-math.pi:.8f}")
print(f"{math.pi:.8f}")
print(f"{per*4:.8f}")
