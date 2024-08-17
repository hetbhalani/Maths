import matplotlib.pyplot as plt
import numpy as np

v = np.array([3, 1])
# E = np.array([[1,0],[0,-1]])
# ans = np.dot(E,v) #same as v*E

# F = np.array([[-1,0],[0,1]])
# ans = np.dot(v,F) # same as F*v

def plot_vectors(vectors, colors):
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0, 0], vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=colors[i])
    plt.xlim(-5, 5)
    plt.ylim(-1, 2)

# plot_vectors([v,ans], ['lightblue','blue'])

# print(np.matrix(v).T)

a = np.array([1,2])
b = np.array([-3,4])
c = np.array([5,-6])
d = np.array([-6,-5])

# V = np.concatenate((np.matrix(a),
#                    np.matrix(b),
#                    np.matrix(c),
#                    np.matrix(d)),
#                    axis=1)


#jo transpose kariye to row column vice concate thai...

V = np.concatenate((np.matrix(a).T,
                   np.matrix(b).T,
                   np.matrix(c).T,
                   np.matrix(d).T),
                   axis=1)

print(V)

plot_vectors([a, b, c, d,v], ['red', 'green', 'blue', 'yellow','orange'])
plt.xlim(-8, 6)
plt.ylim(-8, 9)
plt.show()
plt.show()