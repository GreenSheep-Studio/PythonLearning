import matplotlib as plt
import numpy as np
def P(x):
    if x <= 50:
        return 0.02
    elif x > 50:
        return 0.02 + ((x - 50) * 0.02)
def Posty(x):
    PostyNum = 1
    for i in range(1, x):
        PostyNum = PostyNum * (1- P(i))
    return PostyNum * P(x)
def PostySum(x):
    Sum = 0
    for i in range(1, x + 1):
        Sum += Posty(i)
    return Sum
def Ecp(x):
    Sum = 0
    for i in range(1, x + 1):
        Sum = Sum + (Posty(i) * i)
    return Sum
def main():
    x = 1
    List = []
    while P(x) <= 1:
        List.append(f"{PostySum(x):.15f}")
        x += 1   
    print(f"{Ecp(x)}")
    print(List)
if __name__ == "__main__":
    main()