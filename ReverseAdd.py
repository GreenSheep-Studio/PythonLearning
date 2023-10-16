def ReverseAdd(In_Num):
    Sum = 0
    n = 0
    for i in In_Num:
        if i > '9' or i < '0':
            return "err"
        else:
            Sum += int(i) * (10 ** n)
            n += 1
    Sum += int(In_Num)
    Sum = "{:,}".format(Sum)
    return Sum

def test():
    assert(ReverseAdd("9283746182763") == "12,956,562,656,592")
    assert(ReverseAdd("78991i33") == "err")
    assert(ReverseAdd("9178563") == "12,837,282")
    assert(ReverseAdd("392876 ") == "err")

def main():
    test()
    while 1:
        In_Num = input()
        if In_Num:
            print(ReverseAdd(In_Num))
        else:
            break

print(__name__)
if __name__ == '__main__':
    main()