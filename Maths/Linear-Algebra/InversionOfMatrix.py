import numpy as np

x = np.array([[4,2], [-5,-3]])
y =  np.array([4,-7])

xinv = np.linalg.inv(x)

w = np.dot(xinv,y)
print(w)

print(np.dot(x,w)) 
# it should give value of y bcz y = wx