# 从输入中获取腰围和体重
waist, weight = map(float, input().split())
##上面这行代吗是输入部分，输入多段数字，然后用map函数映射的方法把他们存入waist和weight中
##当然 也可以使用：
'''
waist, weight = input().split()
waist = float(waist)
weight = float(weight)
'''

# 计算体脂率
body_fat_percentage = ((waist * 0.74 - weight * 0.082 + 44.74) / weight) * 10

# 输出结果，保留两位小数
print(f"体脂率={body_fat_percentage:.2f}%")
##使用f-string格式化输出 语法： print(f"AAAA{x}BBBB{y:.2f}")
##比如啊，我们在一起 Day天了 先让 Day = 352
##我要输出“我和我最爱的宝宝在一起352天啦”
##就可以写print(f"我和我最爱的宝宝在一起{Day}天啦")
##把文字打上去，用{}把变量括起来
##其中啊里面的.2f是保留小数的意思{body_fat_percentage:.2f}
##就是 body_fat_percentage这个数一会儿输出是暴力两位小数
##如果.3f就是3位小数的意思啦
