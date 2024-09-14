import numpy as np

#Shuffel

var = np.array([1,2,5,3,5,67,76])
np.random.shuffle(var)
print(var)

#Unique

var2 = np.array([1,2,4,6,3,3,3,4,5,7,6])
x = np.unique(var2,return_index = True) # if you want index only then use return_index 
print(x)

#Resize

var3 = np.array([1,2,3,4,5,6])

y = np.resize(var3,(3,2))
print(y)

#Flatten

var3 = np.array([1,2,3,4,5,6])

y = np.resize(var3,(3,2))
print("Flatten:- ",y.flatten(order = 'F'))
print("Ravel:- ",np.ravel(y,order = 'K'))