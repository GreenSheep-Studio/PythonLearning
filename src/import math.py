def Pai1(e):
    s=0
    n=1
    sign = 1
    while True:
        s +=1/n*sign
        sign =-sign
        n += 2
        if 1/ n < eps:
            break
    num =4*s
    return num

def Pai2(e): 
    s=0
    n=1
    sign = 1
    while True:
        per = 1/n*sign
        sign =-sign
        n += 2
        if 1/ n < eps:
            break
        s += per
    s += per
    num = 4 * s
    return num

eps = float(input())
num1 = Pai1(eps)
num2 = Pai2(eps)
print("{:.6f}".format(num1))
print("{:.6f}".format(num2))