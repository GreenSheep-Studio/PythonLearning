import matplotlib.pyplot as plt
import numpy as np
Uh = [7.175,14.61,22.05,29.525,36.825,44.2,51.375,58.75]
Im = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]
Is =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
B = [0.74, 0.89, 1.11, 1.14, 1.30, 1.48, 1.64 ,1.79 ]
plt.scatter(Is, B, s=None, c='b', marker=None, label='Uh')
y_ticks = np.arange(0, 2, 0.2)
plt.yticks(y_ticks)
for x,y in zip(Is,B):
    plt.text(x,y,y,fontsize=10)
plt.show()