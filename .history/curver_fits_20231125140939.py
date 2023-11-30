
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math
# 定义要拟合的函数模型
def linear_function(x, a, b):
    return a + b * x

# 创建一些模拟数据
x_data = np.array([0.5, 1, 1.5, 2, 2.5, 3])
y_data = np.array([0.0583, 0.0524, 0.0452, 0.0429, 0.0402, 0.0373])

# 使用 curve_fit 进行拟合
params, covariance = curve_fit(linear_function, x_data, y_data)

# 拟合参数
a, b = params

# 使用拟合参数生成拟合曲线
fitted_y = linear_function(x_data, a, b)

# 绘制原始数据和拟合曲线
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_data, fitted_y, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Curve Fitting Example')
plt.show()

# 打印拟合得到的参数
print(f"拟合参数 a: {a}")
print(f"拟合参数 b: {b}")