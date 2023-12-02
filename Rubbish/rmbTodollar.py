def change(money):
    a,b=money.split(' ')
    if a=='$':
        b=int(b)
        c=b*7.18
        print('%d美元=%.2f人民币'%(b,c))
    else:
        b=int(b)
        c=b*0.14
        print('%d人民币=%.2f美元'%(b,c))

x = input()
change(x)