import numpy as np
x = np.array([[1,2],[3,4],[5,6]])
print(x,x.size,x.shape)

print(x[:,0]) #for columns
print(x[0,:]) #for rows

print(x[0:2, 0:2]) #slice by wanted numbers