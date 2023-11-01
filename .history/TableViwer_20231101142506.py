import matplotlib.pyplot as plt
import numpy as np
Uh = [7.175,14.61,22.05,29.525,36.825,44.2,51.375,58.75]
Im = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]
plt.scatter(Im, Uh, s=None, c='b', marker=None, label='Uh')
y_ticks = np.arange(0, 65, 5)
plt.yticks(y_ticks)
for x,y in zip(Im,Uh):
    plt.text(x,y,x,fontsize=10)
plt.show()