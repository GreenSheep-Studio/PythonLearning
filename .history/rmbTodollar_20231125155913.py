def change(money):
    list1 = money.split(' ')
    if list1[0]=='$':
        list1[1]=int(list1[1])
        c=list1[1]*7.18
        print('%d美元=%.2f人民币'%(list1[1],c))
    else:
        list1[1]=int(list1[1])
        c=list1[1]*0.14
        print('%d人民币=%.2f美元'%(list1[1],c))

x = input()
change(x)