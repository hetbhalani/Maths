import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
y = x**2 + 2*x + 2

# lim sin x/x
# x→0

def sin_fxn(my_x):
    my_y = np.sin(my_x)/my_x
    return my_y

# print(sin_fxn(0))
# error

print(sin_fxn(-0.001)) # 0.9999998333333416

print(sin_fxn(0.0000000001)) # 1

y = sin_fxn(x)

