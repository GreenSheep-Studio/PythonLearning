import matplotlib.pyplot as plt
import numpy as np
Uh = [7.175,14.61,22.05,29.525,36.825,44.2,51.375,58.75]
Im = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]
Is =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
B = [35.63, 45.47, 62.50, 77.97, 88.75, 91.72, 91.88, 91.88, 92.03, 92.03, 91.88, 91.56, 90.47, 85.94, 74.22, 54.38, 39.84]
Ln = [50,48,46,44,42,40,35,30,25,20,15,10,8,6,4,2,0]
Ln = Ln[::-1]
print(len(B), len(Ln))
'''
plt.scatter(Ln, B, s=None, c='b', marker=None, label='Uh')
y_ticks = np.arange(30,95,5)
plt.yticks(y_ticks)
plt.show()
'''