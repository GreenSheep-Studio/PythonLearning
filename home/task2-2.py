list = input().split(",")
a = 0
b = 0
n = 0
sum = 0
alt = 0
for num in list:
    if float(num) > 0 :
        a += 1
    elif float(num) < 0 :
        b += 1
    sum += float(num)
    n += 1
alt = sum / n
print(f"{a:.0f},{b:.0f}")
print(f"{alt:.2f}")