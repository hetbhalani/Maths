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

x0 = np.ones(8)

X = np.concatenate((np.matrix(x0).T, np.matrix(x1).T), axis=1)

print(np.dot(np.linalg.pinv(X),y))

# first one is y-intercept of line
# second is slope of line (m)