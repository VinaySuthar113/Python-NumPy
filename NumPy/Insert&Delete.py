import numpy as np

#Insert

var = np.array([1,2,3,4])
v = np.insert(var,(2,4),6.5) #(array_name,position,value)
print(var)
print(v)

var1 = np.array([[1,2,3],[4,5,6]])
v1 = np.insert(var1,2,[20,21,22],axis = 0) #(array_name,position,value,axis)
v2 = np.insert(var1,2,[20,21],axis = 1)
print(var1)
print(v1)
print(v2)

#Append

x = np.array([1,2,3,4])
x = np.append(x,6.5)
print(x)

y = np.array([[1,2,3],[4,5,6]])
y = np.append(y,[[45,44,43]],axis = 0)
print(y)

#Delete
x = np.delete(x,2)
print(x)
