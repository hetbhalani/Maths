import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = x**2 + 2*x + 2

# lim 25/x
# x→∞

def inf_fxn(my_x):
    my_y = 25/my_x
    return my_y

print(inf_fxn(1e3)) #0.025

print(inf_fxn(1e6)) #2.5e-05

y = inf_fxn(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-300, 300)
ax.plot(x, y)

left_x = x[x<0]
right_x = x[x>0]

left_y = inf_fxn(left_x)
right_y = inf_fxn(right_x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-300, 300)
ax.plot(left_x, left_y, c='C0')
ax.plot(right_x, right_y, c='C0')

plt.show()