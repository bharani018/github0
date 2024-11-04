from numpy import random

x = random.choice([1,2,3,4])
print(x)

arr = [1,3,5,7,9]
p = [0.1, 0.3, 0.4, 0.2, 0]
y = random.choice(arr,p= p , size=10)

print(y)

import numpy as np

#introduction to numpy array

D1 = np.array(23)

D2 = np.array([1, 2, 3, 4])

D3 = np.array([[1,2,3], [4,5,6]])

print(D1)
print(D2)
print(D3)

print(D1.size)
print(D2.size)
print(D3.size)

print(D1.shape)
print(D2.shape)
print(D3.shape)

print(D1.ndim)
print(D2.ndim)
print(D3.ndim)

newar = np.array(random.randint(100, size=10)).reshape(2,5)
print(newar)

ind = newar[1,0]
print(ind)

sli = newar[0, 1:4]
print(sli)

print(newar.dtype)

difData = np.array(['a', 'b', 'c'], dtype='S')
print(difData.dtype)

# COPY AND VIEW
# COPY IS USED WHEN TO CREATE NEW ARRAY WITH SAME VALUES OF PREVIOUS ARRAY, IT HAS DIFFERENT MEMORY LOCATION
# VIEW HAS SAME MEMORY LOCATION OF THE PREVIOUS ARRAY

aray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#Copy
cop = aray.copy()
cop[1] = 92
print(cop)
print(aray)

#View
vie = aray.view()
vie[1] = 92
print(vie)
print(aray)

#iterate in 1D array
for i in aray:
    print(i)

# iterate in 2D array
ar2D = np.array([[1,2,3,4,5],[6,7,8,9,0]])
for i in ar2D:
    for j in i:
        print(j)

# Iterate in 3D array

ar3D = np.array(random.randint(100, size=27)).reshape(3,3,3)
print(ar3D)

for i in ar3D:
    for j in i:
        for k in j:
            print(k)


# JOIN IN NUMPY ARRAY - HERE WE USE CONCATENATE

j1 = np.array([1,2,3,4,5])
j2 = np.arange(6,10)

joined = np.concatenate((j1, j2), axis=0)
print(joined)

# JOIN 2D ARRAY

l1 = np.arange(1,11).reshape(2,5)
l2 = np.arange(11, 21).reshape(2,5)
joined2Dax0 = np.concatenate((l1, l2), axis=0)
joined2Dax1 = np.concatenate((l1, l2), axis=1)

print(joined2Dax0)
print(joined2Dax1)

# SEARCH IN ARRAY - 
print(np.searchsorted(j1, 3,side='right'))

print(np.where(j1 == 2))
print(np.where(j1%2==0))

# FILTER IN ARRAY

fil = [True, False, True, False, True]
filarr = j1[fil]
print(filarr)


newfilter = j1>3
applyfilter = j1[~newfilter]
print(applyfilter)