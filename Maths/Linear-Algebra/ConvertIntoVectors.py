import numpy as np

def vectorfy(mtrx, clmn):
    return np.array(mtrx)[:, clmn].reshape(-1) 

v = [[1, 3], [2, 6], [1, 6]]  
print(vectorfy(v, 1))  
