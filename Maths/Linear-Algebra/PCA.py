from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()

iris.data.shape
iris.get("feature_names")
iris.data[0:6,:]

pca = PCA(n_components=2)
X = pca.fit_transform(iris.data)
X.shape

print(X[0:6,:])
plt.scatter(X[:, 0], X[:, 1])

unique_elements, counts_elements = np.unique(iris.target, return_counts=True)
np.asarray((unique_elements, counts_elements))

# these are 3 ful (flowers)
list(iris.target_names)
_ = plt.scatter(X[:, 0], X[:, 1], c=iris.target)
plt.show()