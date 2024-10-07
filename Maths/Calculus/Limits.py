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

# lim  (x2−1)/(x−1)
# x→1

def my_fun (x_fun):
    y_fun = (x_fun**2 - 1)/(x_fun - 1)
    return y_fun


# print(my_fun(1))
# error

print(my_fun(1.0001)) #2.0000999999993923

print(my_fun(0.999999999)) #2

y = my_fun(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.axvline(x=1, color='purple', linestyle='--')
plt.axhline(y=2, color='purple', linestyle='--')
ax.plot(x,y)

plt.show()