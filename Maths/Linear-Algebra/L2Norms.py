import numpy as np

x = np.array([25,2,5])
(25**2 + 2**2 + 5**2)**(1/2) #manual
print(np.linalg.norm(x)) #numpy method

#L1 norm

y = np.array([25,2,5])
print(np.abs(25) + np.abs(2) + np.abs(5))

# squred L2 norm

z = np.array([25,2,5])
print(25**2 + 2**2 + 5**2)
# np.dot(z,z)

#max norm
a = np.array([25,2,5])
print(np.max([np.abs(25),np.abs(2),np.abs(5)]))