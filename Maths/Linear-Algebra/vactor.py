import numpy as np
x = np.array([25,2,5])

# print(len(x))
# print(x.shape)
# print(type(x))  
# print(x[0]) 

x = x.T
print(x)
# print(len(x))
# print(x.shape)
# print(type(x))  
# print(x[0]) 
# transpose krya pachhi pn there is no chaange...

#but!

y = np.array([[25,2,5]]) # we have to add more than one dimention [[]] jethi krine e more than one dimention ma kaam kri ske
print(y.shape)
y = y.T
print(y.shape)

#zero vactor
z = np.zeros(5)
print(z)