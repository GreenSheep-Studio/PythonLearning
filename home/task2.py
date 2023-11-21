# 从输入中获取风速
wind_speed = float(input())

# 根据风速划分风力级别
if wind_speed < 8.0:
    wind_level = "4级及以下"
elif 8.0 <= wind_speed < 10.8:
    wind_level = "5级"
elif 10.8 <= wind_speed < 13.9:
    wind_level = "6级"
elif 13.9 <= wind_speed < 17.2:
    wind_level = "7级"
elif 17.2 <= wind_speed < 20.8:
    wind_level = "8级"
elif 20.8 <= wind_speed < 24.5:
    wind_level = "9级"
elif 24.5 <= wind_speed < 28.5:
    wind_level = "10级"
elif 28.5 <= wind_speed < 32.7:
    wind_level = "11级"
else:
    wind_level = "12级及以上"

# 输出风力级别
print(f"风力:{wind_level}")
