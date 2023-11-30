import matplotlib.pyplot as plt
import numpy as np
#x轴采用对数坐标
x=[1e-11,1e-9,1e-7,1e-6,1e-5]
y=[1,2,3,4,5]
plt.semilogx(x,y,linewidth =1.5, color='green', linestyle='dotted',label='test',alpha=0.7,marker='o')
plt.legend()
plt.show()
