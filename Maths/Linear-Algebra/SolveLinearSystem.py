import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-10,10,1000) #strt, finish, no. of points
y1 = 3*x
y2 = 1 + (5*x)/2

fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim([0,3])
ax.set_ylim([0,8])
