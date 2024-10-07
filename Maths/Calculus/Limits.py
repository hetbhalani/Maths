import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = x**2 + 2*x + 2

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')

plt.xlim(-5, 10)
plt.ylim(-10, 80)

plt.axvline(x=5, color='purple', linestyle='--')
plt.axhline(y=37, color='purple', linestyle='--')
ax.plot(x,y)

plt.show()