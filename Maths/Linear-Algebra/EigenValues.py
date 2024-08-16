import numpy as np

A = np.array([[-1,4],[2,-2]])

lambdas, V = np.linalg.eig(A)

print(V)
print(lambdas)

#extrect clmns
v = V[:,0]
print(v)

lambduh = lambdas[0]
print(lambduh)


#both are same...
Av = np.dot(A,v)
print(Av)

print(lambduh*v)
#hence proved that Av = λv