mylist = ["张红","女","计算机"]
num = input() #输入学号
mylist.append(num)
ymd = eval(input())
mylist.append(list(ymd))
courses = eval(input()) 
mylist.append(list(courses))
x = mylist.pop(1)
print(mylist)
print("{}性别{}、今年{}岁、学号{}、体育{}分".format(mylist[0], x, (2022 - int(mylist[3][0])), mylist[2], mylist[4][2]))
