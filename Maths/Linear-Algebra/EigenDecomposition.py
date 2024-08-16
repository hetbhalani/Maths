import matplotlib.pyplot as plt
import numpy as np

v = np.array([3, 1])
# E = np.array([[1,0],[0,-1]])
# ans = np.dot(E,v) #same as v*E

def plot_vectors(vectors, colors):
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0, 0], vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=colors[i])
    plt.xlim(-1, 5)
    plt.ylim(-1, 2)
    plt.show()

plot_vectors([v,ans], ['lightblue','blue'])
