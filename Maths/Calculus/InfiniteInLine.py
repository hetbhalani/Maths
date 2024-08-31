import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10000) # start, finish, n points

# y=x^2+2x+2 :
y = x**2 + 2*x + 2

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-5, 10)
plt.ylim(-10, 80)
plt.axvline(x=5, color='purple', linestyle='--')
plt.axhline(y=37, color='purple', linestyle='--')
_ = ax.plot(x,y)

plt.show()