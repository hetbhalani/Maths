#  Cumulative Distribution Function

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()
iris_setosa = iris.loc[iris['variety'] == "Setosa"]
iris_virginica = iris.loc[iris['variety'] == "Virginica"]
iris_versicolor = iris.loc[iris['variety'] == "Versicolor"]

# bins -> means how many data u want in graph
count , edges = np.histogram(iris_setosa['petal.length'], bins=10, density=True)
pdf = count/(sum(count))
print(pdf,edges)


#for CDF

cdf = np.cumsum(pdf) #cumsum etle Cumulative sum
plt.plot(edges[1:],pdf)
plt.plot(edges[1:],cdf)
plt.xlabel('Petal Length')
plt.ylabel('Probability')
plt.grid(True)
plt.show()