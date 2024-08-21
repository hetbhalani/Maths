# Explorartry Data Enalysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("iris.csv")
iris.head()

# print(iris.shape)
# print(iris.columns)

# print(iris["variety"].value_counts())

iris.plot(kind='scatter', x='sepal.length', y='sepal.width')
plt.show()