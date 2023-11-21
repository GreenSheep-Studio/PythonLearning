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

def main():
    x = 1
    while P(x) <= 1:
        print(f"{x}抽出金概率为：{Posty(x)}", end = "\n")
        x += 1

if __name__ == "__main__":
    main()