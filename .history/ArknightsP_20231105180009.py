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

def main():
    x = 1
    while P(x) <= 1:
        print(f"{x}内抽出金概率为：{PostySum(x)}, 第{x}发的概率为{P(x).:2f}", end = "\n")
        x += 1

if __name__ == "__main__":
    main()