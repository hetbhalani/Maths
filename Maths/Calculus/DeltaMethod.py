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

m = (37-10)/(5-2)
print(m) #9

b = 37 - m*5
print(b)

line_y = m*x +b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(2,10) #point k jena pr aapde slope joto 6
plt.scatter(2.1,10.61, c='orange', zorder=3) # ek bijo point lidho k jena relative aapde slope joye 6
# zorder etle curve ni uper point aave
plt.ylim(-5,150)
plt.plot(x, line_y, c='orange')
ax.plot(x,y)

# plt.show()

#Example

nx1 = -1
ny1 = 1 #func. thi mle

delta_x = 0.000001 #smallllllllllllll

# x2 = x1 + delta_x

nx2 = -0.999999
ny2 = 1.000000000001 #func. thi mle

m1 = (ny2-ny1)/(nx2-nx1)
print(m)

b = ny2-m1*nx2
nline_y = m1*x+b

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.scatter(nx1, ny1)
plt.scatter(nx2, ny2, c='orange', zorder=3)
plt.ylim(-5, 150)
plt.plot(x, nline_y, c='orange', zorder=3)
ax.plot(x,y)

plt.show()