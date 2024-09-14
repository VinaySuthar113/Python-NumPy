import numpy as np

#Shape

var = np.array([[1,4,6,2],[1,4,7,2]])

print(var)
print("")
print(var.shape)

var1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12],ndmin = 10)
print(var1)
print(var1.shape)

#Reshape
x = var1.reshape(3,4)
print(x)
print(x.ndim)

x1 = var1.reshape(2,3,2)
print(x1)
print(x1.ndim)

x2 = x1.reshape(-1)
print(x2)