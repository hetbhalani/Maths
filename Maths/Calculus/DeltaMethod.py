import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-10,10,1000)
y = x**2 + 2*x + 2

def f(my_x):
    my_y = my_x**2 + 2*my_x +2
    return(my_y)

y = f(x)

print(f(2))
# answer is 10 so we have to find slope at 2,10 position
print(f(5))
# ans is 37 

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2,10) #point k jena pr aapde slope joto 6
plt.scatter(5,37, c='orange', zorder=3) # ek bijo point lidho k jena relative aapde slope joye 6
# zorder etle curve ni uper point aave
plt.ylim(-5,150)

ax.plot(x,y)

m = (37-10)/(5-2)
print(m) #9

b = 37 - m*5
print(b)

plt.show()
