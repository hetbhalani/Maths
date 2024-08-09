import numpy as np

x = np.array([25,2,5])
(25**2 + 2**2 + 5**2)**(1/2) #manual
print(np.linalg.norm(x)) #numpy method