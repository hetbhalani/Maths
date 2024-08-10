import numpy as np

x = np.array([[2,25], [3,35], [4,45]])
# print(x*2)

# print(x+2)

# print(x*2+2)

print(x.sum())
print(x.sum(axis=0))
print(x.sum(axis=1))