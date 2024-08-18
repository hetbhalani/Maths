import numpy as np
import matplotlib.pyplot as plt

x1 = [0, 1, 2, 3, 4, 5, 6, 7.]
y = [1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]

title = 'Clinical Trial'
xlabel = 'Drug dosage (mL)'
ylabel = 'Forgetfulness'

fig, ax = plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
ax.scatter(x1, y)

plt.show()