
# COMMON FUNCTIONS IN NUMPYS

import numpy as np

# CREATION OF ARRAY

a = np.array([1,2,3,4,5])
print(a)

b = np.arange(1,5)
print(b)

c = np.zeros(3, dtype='i')
print(c)

d = np.ones(5, dtype='i')
print(d)

e = np.empty(0)
print(e)

# ARRAY MANIPULATION

# Reshape:

n1 = np.arange(1,11).reshape(2,5) #creates 2D array
print(n1)

n2 = np.arange(1,13).reshape(3,2,2) # create 3D array
print(n2)

# Transpose of array

t1 = np.transpose(n1)
print(t1)

t2 = n1.transpose()
print(t2)

# Flattern

f1 = n2.flatten()
print(f1)

# STATISTICAL FUNCTION and MATHEMATICAL FUNCION

# square, squrare root, absolute, mean, median, min, max, variance, standard Deviation

