def HuXing1(x):
    if x <= 230:
        return x * 0.4983
    elif x >= 231 and x <= 420:
        return x * 0.5483
    elif x >= 421:
        return x * 0.7983
    
def HuXing2(x):
    return x * 0.5330

name, Type, x = input().split(",")
x = eval(x)
if Type == "01":
    Price = HuXing1(x)
    TypeName = "居民用户"
elif Type == "02":
    Price = HuXing2(x)
    TypeName = "总表用户"
print(f"{name}，{TypeName}，本月总电费为：{Price:.2f}元。")