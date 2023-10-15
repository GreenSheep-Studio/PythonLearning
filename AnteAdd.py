def main():
    In_Num = input()
    Sum = 0
    n = 0
    for i in In_Num:
        if i > '9' or i < '0':
            print ("err")
            return
        else:
            Sum += int(i) * (10 ** n)
            n += 1
    Sum += int(In_Num)
    Sum = "{:,}".format(Sum)
    print(Sum)
if __name__ == '__main__':
    main()