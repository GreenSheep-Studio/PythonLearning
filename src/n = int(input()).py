# 定义函数YesIs，用于判断字符串中1的个数是否大于等于n
def YesIs(NumStr, n):
    # 定义计数器
    Count = 0
    # 将字符串末尾补0
    NumStr = NumStr + '0'
    # 遍历字符串
    for i in range(len(NumStr)):
        # 如果字符串中为1，计数器加1
        if NumStr[i] == "1":
            Count += 1
            # 如果计数器大于等于n，且计数器大于等于3，返回Yes
            if Count >= n and Count >= 3:
                return "Yes"
        # 如果字符串中为0，计数器重置为0
        else:
            Count = 0
    # 如果遍历完字符串仍未返回Yes，返回No
    return "No"

# 输入n和m
n, m = map(int, input().split())
# 定义一个列表，用于存放结果
ListTrue = []
# 遍历m次，每次输入一个字符串，调用YesIs函数，将结果存入ListTrue列表中
for i in range(m):
    Num = input()
    ListTrue.append(YesIs(Num, n))
# 遍历ListTrue列表，打印每个结果
for x in ListTrue:
    print(x)