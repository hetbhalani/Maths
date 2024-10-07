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

