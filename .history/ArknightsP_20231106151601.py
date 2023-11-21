import matplotlib.pyplot as plt
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
    ListP = []
    ListX = []
    while P(x) <= 1:
        ListX.append(x)
        ListP.append(f"{PostySum(x):.15f}")
        x += 1
    for i, j in zip(ListX, ListP):
        print(i, j)
    y_ticks = np.arange(0, 1, 0.01)
    plt.xticks(y_ticks)
    plt.scatter(ListX, ListP,s=0.1, c="red")  
    plt.show()
    print(f"{Ecp(x)}")
if __name__ == "__main__":
    main()