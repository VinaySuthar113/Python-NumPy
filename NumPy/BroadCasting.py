import numpy as np

var1 = np.array([1,2,3,4])
print(var1.shape)

var2 = np.array([[1],[2],[3],[4]])
print(var2.shape)

print(var1 + var2)


x = np.array([[1],[2]])
print(x.shape)

y = np.array([[1,2,3],[1,2,3]])
print(y.shape)

print(x * y)