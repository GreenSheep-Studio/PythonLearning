list = []
for i in range(100, 1000):
    one = i % 10
    ten = (i // 10) % 10
    hud = i // 100
    sum = one**3 + ten**3 + hud**3
    if i == sum:
        list.append(i) 
print(','.join(str(i) for i in list))