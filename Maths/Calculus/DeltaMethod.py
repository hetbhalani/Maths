import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-10,10,1000)
y = x**2 + 2*x + 2

def f(my_x):
    my_y = my_x**2 + 2*my_x +2
    return(my_y)

y = f(x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2,10) #ek point lidho k jena pr aapde slope joto 6
ax.plot(x,y)

print(f(2))
plt.show()
