# 从输入中获取性别、腰围和体重
input_str = input().strip()
gender, waist, weight = input_str.split(',')

# 去除性别前后的空格
gender = gender.strip()

# 将腰围和体重转换为浮点数
waist = float(waist)
weight = float(weight)

# 根据性别选择计算体脂率的公式
if gender == '男':
    body_fat_percentage = ((waist * 0.74 - weight * 0.082 + 44.74) / weight) * 10
elif gender == '女':
    body_fat_percentage = ((waist * 0.74 - weight * 0.082 + 34.89) / weight) * 10
else:
    print("性别输入错误")
    exit()

# 输出结果，保留两位小数
print(f"{gender}性，体脂率{body_fat_percentage:.2f}%")
